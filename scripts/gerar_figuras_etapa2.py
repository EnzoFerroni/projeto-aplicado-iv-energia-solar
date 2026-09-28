import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from datetime import date, timedelta
import matplotlib.dates as mdates

# ---------------- Pipeline ----------------
etapas = [
    ("1. Coleta", "Download do Parquet\nda ANEEL\n(dados abertos)\n→ data/raw", "#1f4e79"),
    ("2. Limpeza", "Filtro da fonte solar,\ntipos e duplicados,\ndatas e potências\ninválidas", "#1f4e79"),
    ("3. Séries mensais", "Agregação por mês\nde conexão, Brasil\ne 27 UFs · conexões,\nkW novo e acumulado", "#2e75b6"),
    ("4. Análise exploratória", "Gráficos, ACF/PACF,\nADF/KPSS, STL, Box-Cox,\ndummy Lei 14.300", "#2e75b6"),
    ("5. Modelagem", "Baselines (naive sazonal,\ndrift) · ETS · SARIMAX\nProphet · LightGBM", "#c00000"),
    ("6. Avaliação", "Origem móvel, horizonte\n12 meses · MAE, RMSE,\nMAPE (MASE de apoio)", "#c00000"),
    ("7. Produto", "Previsões 12–24 meses\ncom intervalos · notebook,\ngráficos e README", "#375623"),
]

fig, ax = plt.subplots(figsize=(16.5, 5.2), dpi=200)
ax.set_xlim(0, 16.5); ax.set_ylim(0, 5.2); ax.axis("off")
w, h, gap = 2.08, 2.3, 0.26
x0, y = 0.25, 1.55
for i, (tit, txt, cor) in enumerate(etapas):
    x = x0 + i * (w + gap)
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc="white", ec=cor, lw=2))
    ax.add_patch(FancyBboxPatch((x, y + h - 0.55), w, 0.55, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc=cor, ec=cor, lw=2))
    ax.text(x + w / 2, y + h - 0.275, tit, ha="center", va="center", color="white", fontsize=8.8, weight="bold")
    ax.text(x + w / 2, y + (h - 0.55) / 2, txt, ha="center", va="center", fontsize=7.6, linespacing=1.45)
    if i < len(etapas) - 1:
        ax.annotate("", xy=(x + w + gap - 0.02, y + h / 2), xytext=(x + w + 0.02, y + h / 2),
                    arrowprops=dict(arrowstyle="-|>", color="#404040", lw=1.6))

# faixas de fase
fases = [(0, 2, "Preparação dos dados", "#1f4e79"), (2, 4, "Caracterização da série", "#2e75b6"),
         (4, 6, "Modelagem e avaliação", "#c00000"), (6, 7, "Entrega", "#375623")]
for a, b, nome, cor in fases:
    xa = x0 + a * (w + gap); xb = x0 + b * (w + gap) - gap
    ax.plot([xa, xb], [1.25, 1.25], color=cor, lw=3, solid_capstyle="round")
    ax.text((xa + xb) / 2, 0.95, nome, ha="center", va="center", fontsize=8.5, color=cor, weight="bold")

# laço de retorno avaliação -> modelagem
xm = x0 + 4 * (w + gap) + w / 2; xa = x0 + 5 * (w + gap) + w / 2
ax.annotate("", xy=(xm, y + h + 0.05), xytext=(xa, y + h + 0.05),
            arrowprops=dict(arrowstyle="-|>", color="#c00000", lw=1.3, connectionstyle="arc3,rad=0.45"))
ax.text((xm + xa) / 2, y + h + 0.62, "ajuste de hiperparâmetros", ha="center", fontsize=7.5, color="#c00000", style="italic")

ax.text(8.25, 0.35, "Tudo executado em um único notebook Python (pandas, pyarrow, statsmodels, prophet, lightgbm) · dados brutos fora do git, séries em data/processed",
        ha="center", fontsize=7.8, color="#404040")
ax.text(0.25, 5.0, "Pipeline da solução", fontsize=13, weight="bold", color="#202020")
plt.savefig("figuras/pipeline_solucao.png", bbox_inches="tight", facecolor="white")
plt.close()

# ---------------- Gantt ----------------
import csv
rows = list(csv.DictReader(open("docs/cronograma.csv", encoding="utf-8")))
def d(s):
    dd, mm = s.split("/"); return date(2026, int(mm), int(dd))
cores = {"2": "#7030a0", "3": "#2e75b6", "4": "#c00000"}
fig, ax = plt.subplots(figsize=(13, 9.5), dpi=200)
n = len(rows)
for i, r in enumerate(rows):
    yy = n - 1 - i
    ini, fim = d(r["inicio"]), d(r["fim"])
    marco = ini == fim
    if marco:
        ax.plot(mdates.date2num(ini) + 0.5, yy, marker="D", color="black", ms=7)
    else:
        ax.barh(yy, (fim - ini).days + 1, left=mdates.date2num(ini), height=0.6, color=cores[r["etapa"]], alpha=0.9)
labels = [f'{r["id"]}. {r["atividade"]}' for r in rows]
ax.set_yticks(range(n)); ax.set_yticklabels(labels[::-1], fontsize=8)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
plt.setp(ax.get_xticklabels(), fontsize=7.5, rotation=45)
ax.grid(axis="x", color="#dddddd"); ax.set_axisbelow(True)
for dl, nome in [("28/09", "Entrega E2"), ("26/10", "Entrega E3"), ("30/11", "Entrega final")]:
    x = mdates.date2num(d(dl)) + 0.5
    ax.axvline(x, color="#404040", ls="--", lw=1)
    ax.text(x - 0.6, n - 0.2, nome, ha="right", fontsize=8, weight="bold")
ax.set_xlim(mdates.date2num(date(2026, 8, 31)), mdates.date2num(date(2026, 12, 2)))
ax.set_ylim(-0.8, n + 0.3)
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
ax.legend(handles=[Patch(color=cores["2"], label="Etapa 2"), Patch(color=cores["3"], label="Etapa 3"),
                   Patch(color=cores["4"], label="Etapa 4"),
                   Line2D([], [], marker="D", color="black", ls="", label="Checkpoint / entrega")],
          loc="lower left", fontsize=8, frameon=False)
ax.set_title("Cronograma do projeto (set. a nov. de 2026)", fontsize=12, weight="bold", loc="left")
plt.tight_layout()
plt.savefig("figuras/cronograma_gantt.png", facecolor="white")
