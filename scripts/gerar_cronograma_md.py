import csv
from datetime import date
rows=list(csv.DictReader(open("docs/cronograma.csv",encoding="utf-8")))

def d(s): dd,mm=s.split("/"); return date(2026,int(mm),int(dd))
nome={"Enzo":"Enzo Ferroni","Daniel":"Daniel dos Santos","Vinícius":"Vinícius Sabiá","Daniel e Vinícius":"Daniel dos Santos e Vinícius Sabiá","Todos":"Todos"}
etapas={"2":("Referencial Teórico e Cronograma","01/09","28/09","Segunda entrega: 28 de setembro"),
        "3":("Implementação Parcial","29/09","26/10","Terceira entrega: 26 de outubro"),
        "4":("Implementação e Entrega Final","27/10","30/11","Quarta e última entrega: 30 de novembro")}
curto={ "1":"Levantamento bibliográfico","2":"Referencial teórico","3":"Checkpoint Etapa 2","4":"Pipeline da solução",
 "5":"Cronograma detalhado","6":"Revisão e publicação","7":"Coleta automática ANEEL","8":"Limpeza e filtro solar",
 "9":"Checkpoint Etapa 3","10":"Séries mensais Brasil e UFs","11":"Conferência com EPE","12":"Análise gráfica",
 "13":"ACF PACF e STL","14":"Tratamento das quebras","15":"Modelo base ETS","16":"Entrega Etapa 3",
 "17":"SARIMAX","18":"Prophet","19":"LightGBM global","20":"Checkpoint Etapa 4","21":"Validação e comparação",
 "22":"Previsões finais","23":"Resultados e conclusão","24":"Slides e vídeo","25":"Revisão final e Colab","26":"Entrega final"}
rows.sort(key=lambda r:(r["etapa"],d(r["inicio"]),d(r["fim"])))
def periodo(r): return r["inicio"] if r["inicio"]==r["fim"] else f'{r["inicio"]} - {r["fim"]}'
def tabelas(nivel):
    out=[]
    for e,(tit,ini,fim,ent) in etapas.items():
        dias=(d(fim)-d(ini)).days+1
        out+= [f'{nivel} ETAPA {e} – {tit} ({dias} dias)',"",f'**{ent}**',"",
               "| **Período** | **Atividades** | **Responsável** |","| --- | --- | --- |"]
        out+= [f'| {periodo(r)} | {r["atividade"]} | {nome[r["responsavel"]]} |' for r in rows if r["etapa"]==e]
        out.append("")
    return out
md=["# Projeto Aplicado IV - Mackenzie (Cronograma Detalhado)","","## Visão Geral","",
"Este cronograma detalha as atividades previstas para o projeto de análise e previsão do crescimento da energia solar distribuída no Brasil. A Etapa 1 foi concluída em 31/08, e as etapas seguintes estão divididas em atividades com datas e responsáveis definidos, indo além do calendário da disciplina.",""]
md+=tabelas("##")
md+=["## Linha do Tempo","","```mermaid","gantt","    title Cronograma do Projeto","    dateFormat  YYYY-MM-DD","    axisFormat  %d/%m"]
for e in etapas:
    md.append(f"    section ETAPA {e}")
    for r in rows:
        if r["etapa"]!=e: continue
        ini=d(r["inicio"]); n=(d(r["fim"])-ini).days+1
        if ini==d(r["fim"]): md.append(f'    {curto[r["id"]]} :milestone, {ini.isoformat()}, 0d')
        else: md.append(f'    {curto[r["id"]]} :{ini.isoformat()}, {n}d')
md+=["```",""]
resp={}
for r in rows:
    for p in r["responsavel"].split(" e "):
        if p!="Todos": resp.setdefault(p,[]).append(r["atividade"])
md+=["## Divisão de Responsabilidades","","| **Membro da Equipe** | **Responsabilidades** |","| --- | --- |"]
for p in ["Daniel","Enzo","Vinícius"]:
    md.append(f'| {nome[p]} | {"<br>".join(resp[p])} |')
md+=["","As atividades marcadas como Todos (levantamento bibliográfico, checkpoints, validação dos modelos, vídeo e entregas) são feitas em conjunto pelo grupo.","",
"## Marcos Importantes","","| **Marco** | **Data Prevista** |","| --- | --- |",
"| Entrega da Etapa 1 (Definição do projeto e equipe) | 31/08/2026 (concluída) |",
"| Checkpoint da Etapa 2 | 14/09/2026 |","| Entrega da Etapa 2 (Referencial Teórico e Cronograma) | 28/09/2026 |",
"| Checkpoint da Etapa 3 | 05/10/2026 |","| Entrega da Etapa 3 (Implementação Parcial) | 26/10/2026 |",
"| Checkpoint da Etapa 4 | 09/11/2026 |","| Entrega Final e Vídeo de Apresentação | 30/11/2026 |","","---",""]
open("Cronograma.md","w",encoding="utf-8").write("\n".join(md))
