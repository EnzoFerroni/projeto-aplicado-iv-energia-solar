<img src="figuras/mackenzie_logo.jpg" width="25%" align="right"/>

# Análise e Previsão do Crescimento da Energia Solar Distribuída no Brasil

**Projeto Aplicado IV — Ciência de Dados EaD — 2026/02**
Universidade Presbiteriana Mackenzie — Faculdade de Computação e Informática

---

## Equipe

| Integrante (ordem alfabética) | Matrícula |
|---|---|
| Daniel dos Santos da Silva | 10720767 |
| Enzo Ferroni | 10417100 |
| Vinícius de Souza Sabiá | 10721475 |

## Objetivo

Desenvolver um produto analítico de séries temporais capaz de **analisar e prever o crescimento da micro e minigeração distribuída fotovoltaica no Brasil**, a partir de dados públicos oficiais da ANEEL.

Objetivos específicos:

- Organizar os dados de geração distribuída fotovoltaica por data, estado e município.
- Analisar a evolução temporal da potência instalada e do número de empreendimentos solares.
- Identificar estados e municípios com maior crescimento da geração solar distribuída.
- Aplicar modelos de séries temporais para prever tendências futuras.
- Criar visualizações que apoiem a interpretação dos resultados.

## ODS relacionados

<p align="left">
  <img src="figuras/sdg_08.png" width="10%"/>
  <img src="figuras/sdg_09.png" width="10%"/>
  <img src="figuras/sdg_11.png" width="10%"/>
</p>

- **ODS 8** — Trabalho decente e crescimento econômico: movimentação econômica e geração de empregos do setor solar.
- **ODS 11** — Cidades e comunidades sustentáveis: incentivo à geração limpa e descentralizada em áreas urbanas.
- **ODS 9** (complementar) — Indústria, inovação e infraestrutura: modernização da infraestrutura energética.

## Base de dados

| Item | Descrição |
|---|---|
| Fonte principal | ANEEL — Portal de Dados Abertos |
| Base | Relação de empreendimentos de Mini e Micro Geração Distribuída |
| Formato | CSV compactado (ZIP) e Parquet |
| Cobertura | Brasil, estados e municípios |
| Período | Registros a partir de dezembro de 2008 |
| Atualização | Diária |
| Campos úteis | Data de conexão, fonte (solar), potência instalada, UF, município, distribuidora, classe de consumo, modalidade |
| Tratamento previsto | Filtrar fonte solar, agrupar por mês/ano, somar potência instalada por localidade |

- Base principal: https://dadosabertos.aneel.gov.br/pt_BR/dataset/relacao-de-empreendimentos-de-geracao-distribuida
- Fonte complementar (EPE — PDGD): https://dashboard.epe.gov.br/apps/pdgd/

Os arquivos brutos **não são versionados** (ver `data/README.md`); o notebook faz o download direto da fonte oficial.

## Solução proposta

Notebook Python executável e reproduzível cobrindo coleta → pré-processamento → EDA → modelagem → avaliação.
Modelos candidatos para a série mensal de potência instalada: média móvel/baseline sazonal, regressão, **ARIMA/SARIMA**, **Prophet** e modelos baseados em árvores (gradient boosting com features de lag). A escolha final depende da qualidade dos dados após o pré-processamento.

## Estrutura do repositório

```
.
├── README.md                       # apresentação do projeto
├── docs/
│   ├── PA4_Etapa1_Proposta.docx    # documento da Etapa 1
│   └── ETAPA1.md                   # proposta em markdown (contexto, motivação, objetivo, justificativa)
├── notebooks/
│   └── projeto_aplicado_IV_doc.ipynb   # documentação/notebook do projeto (template da disciplina)
├── data/
│   └── README.md                   # instruções de obtenção dos dados (dados brutos não versionados)
├── figuras/                        # imagens usadas na documentação
├── src/                            # scripts auxiliares (etapas seguintes)
└── requirements.txt
```

## Cronograma da disciplina

| Etapa | Entrega | Data |
|---|---|---|
| 1 | Definição do projeto e equipe | 31/08/2026 |
| 2 | Referencial teórico e cronograma | 28/09/2026 |
| 3 | Implementação parcial | 26/10/2026 |
| 4 | Implementação e entrega final | 30/11/2026 |

## Referências

- AGÊNCIA NACIONAL DE ENERGIA ELÉTRICA. *Relação de empreendimentos de Mini e Micro Geração Distribuída*. Portal de Dados Abertos da ANEEL, 2026. Disponível em: https://dadosabertos.aneel.gov.br/pt_BR/dataset/relacao-de-empreendimentos-de-geracao-distribuida. Acesso em: 31 ago. 2026.
- AGÊNCIA NACIONAL DE ENERGIA ELÉTRICA. *Micro e Minigeração Distribuída*. Brasília: ANEEL, 2026. Disponível em: https://www.gov.br/aneel/pt-br/assuntos/geracao-distribuida/. Acesso em: 31 ago. 2026.
- EMPRESA DE PESQUISA ENERGÉTICA. *Painel de Dados de Micro e Minigeração Distribuída (PDGD)*. Rio de Janeiro: EPE, 2026. Disponível em: https://dashboard.epe.gov.br/apps/pdgd/. Acesso em: 31 ago. 2026.
- EMPRESA DE PESQUISA ENERGÉTICA. *Balanço Energético Nacional 2026*. Rio de Janeiro: EPE, 2026. Disponível em: https://dashboard.epe.gov.br/apps/livro-ben/livro/pt/capitulo_1.html. Acesso em: 31 ago. 2026.
- ORGANIZAÇÃO DAS NAÇÕES UNIDAS. *Objetivos de Desenvolvimento Sustentável*. ONU Brasil. Disponível em: https://brasil.un.org/pt-br/sdgs. Acesso em: 31 ago. 2026.
