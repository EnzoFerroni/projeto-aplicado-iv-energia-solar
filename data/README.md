# Dados

Os dados brutos **não são versionados** neste repositório (volume elevado e atualização diária na fonte).

## Base principal — ANEEL

Relação de empreendimentos de Mini e Micro Geração Distribuída (Portal de Dados Abertos da ANEEL):

https://dadosabertos.aneel.gov.br/pt_BR/dataset/relacao-de-empreendimentos-de-geracao-distribuida

Baixe o arquivo em CSV/Parquet e salve nesta pasta como `data/raw/`. O notebook em
`notebooks/projeto_aplicado_IV_doc.ipynb` também realiza o download direto da fonte.

```
data/
├── raw/          # arquivos originais baixados da ANEEL (ignorados pelo git)
└── processed/    # séries temporais agregadas geradas pelo notebook (ignoradas pelo git)
```

## Fonte complementar — EPE

Painel de Dados de Micro e Minigeração Distribuída (PDGD): https://dashboard.epe.gov.br/apps/pdgd/
