# Dados

Os dados brutos **não são versionados** neste repositório (volume elevado e atualização diária na fonte).

## Base principal — ANEEL

Relação de empreendimentos de Mini e Micro Geração Distribuída (Portal de Dados Abertos da ANEEL):

https://dadosabertos.aneel.gov.br/dataset/relacao-de-empreendimentos-de-geracao-distribuida

O notebook `notebooks/projeto_aplicado_IV_doc.ipynb` baixa automaticamente o arquivo Parquet
para `data/raw/` na primeira execução e registra a data do download em `data/raw/data_download.txt`.
Se o Parquet estiver indisponível, ele usa o ZIP com CSV do mesmo conjunto. Para atualizar a base,
apague `data/raw/` e execute o notebook de novo.

Dicionário de dados (PDF, versão 2.3):
https://dadosabertos.aneel.gov.br/dataset/5e0fafd2-21b9-4d5b-b622-40438d40aba2/resource/3fabb9e8-668a-4f94-8f0e-ed9cd2682979/download/dm-geracao-distribuida-relacao-de-empreendimentos.pdf

```
data/
├── raw/          # arquivos originais baixados da ANEEL (ignorados pelo git)
└── processed/    # séries mensais geradas pelo notebook (ignoradas pelo git)
    ├── serie_mensal_brasil.csv   # conexões, potência nova (kW e MW) e acumulada do Brasil
    └── serie_mensal_uf.csv       # as mesmas séries para as 27 UFs
```

## Fonte complementar — EPE

Painel de Dados de Micro e Minigeração Distribuída (PDGD): https://dashboard.epe.gov.br/apps/pdgd/
