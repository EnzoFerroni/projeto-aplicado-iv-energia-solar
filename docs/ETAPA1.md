# Etapa 1 — Definição do Projeto e Equipe

**Projeto Aplicado IV — Ciência de Dados EaD — 2026/02**
Universidade Presbiteriana Mackenzie
Entrega: 31/08/2026

## Equipe

- Daniel dos Santos da Silva — RA 10720767
- Enzo Ferroni — RA 10417100
- Vinícius de Souza Sabiá — RA 10721475

## 1. Proposta do projeto

### 1.1 Título

Análise e previsão do crescimento da energia solar distribuída no Brasil.

### 1.2 Contexto

O projeto está inserido na área de Ciência de Dados aplicada ao setor de energia, com foco em séries temporais, análise exploratória e previsão de crescimento. O tema escolhido é a expansão da energia solar fotovoltaica distribuída no Brasil, especialmente em unidades consumidoras conectadas à rede elétrica.

A micro e minigeração distribuída permite que consumidores residenciais, comerciais, rurais e industriais produzam parte da própria energia, principalmente por meio de sistemas solares. Esse tipo de geração tem relação direta com infraestrutura energética, inovação tecnológica, sustentabilidade urbana e desenvolvimento econômico.

O tema se relaciona aos ODS 8 (trabalho decente e crescimento econômico), pela movimentação econômica do setor solar, e ODS 11 (cidades e comunidades sustentáveis), pelo incentivo a cidades mais sustentáveis; de forma complementar, dialoga com o ODS 9, pela modernização da infraestrutura energética.

### 1.3 Motivação

A energia solar distribuída é um tema atual e relevante porque cresce junto com a necessidade de alternativas mais limpas, econômicas e descentralizadas de geração de energia. Mesmo com esse avanço, ainda existem diferenças entre estados e municípios na adoção da tecnologia, o que indica uma lacuna importante para análise.

A motivação do projeto é compreender esse crescimento a partir de dados públicos oficiais. Ao analisar a evolução histórica da capacidade instalada e do número de empreendimentos, o grupo poderá identificar padrões, regiões com maior avanço e locais com menor participação na geração solar.

### 1.4 Objetivo

Desenvolver um produto analítico capaz de analisar e prever o crescimento da energia solar distribuída no Brasil, utilizando dados públicos de micro e minigeração distribuída.

Objetivos específicos:

- Organizar os dados de geração distribuída fotovoltaica por data, estado e município.
- Analisar a evolução temporal da potência instalada e do número de empreendimentos solares.
- Identificar estados e municípios com maior crescimento da geração solar distribuída.
- Aplicar modelos de séries temporais para prever tendências futuras.
- Criar visualizações simples que ajudem na interpretação dos resultados.

### 1.5 Justificativa

A proposta se justifica pela contribuição social e prática do tema. A energia solar distribuída pode reduzir a dependência de fontes tradicionais, apoiar a transição energética, estimular investimentos e ampliar a participação da sociedade na produção de energia limpa.

Do ponto de vista científico e analítico, o projeto permite aplicar técnicas de Ciência de Dados em uma base pública grande, atualizada e relacionada a um problema real. A solução pode ser útil para estudantes, pesquisadores, gestores públicos, empresas do setor e comunidades interessadas em compreender a expansão da energia solar no país.

| Critério | Como o projeto atende |
|---|---|
| Atualidade e importância | Energia solar é um tema atual, ligado à transição energética e ao custo da energia elétrica. |
| Fonte dos dados | Base pública, oficial, nacional e atualizada diariamente pela ANEEL. |
| Solução proposta | Produto analítico viável, com séries temporais, gráficos e modelos de previsão. |
| Contribuição social | Ajuda a entender a expansão de energia limpa e sua relação com cidades sustentáveis. |

## 2. Descrição da base de dados

A principal base selecionada é a **Relação de empreendimentos de Mini e Micro Geração Distribuída**, disponibilizada pela Agência Nacional de Energia Elétrica (ANEEL) no Portal de Dados Abertos. A base registra conexões de unidades consumidoras com geração distribuída, incluindo empreendimentos solares fotovoltaicos.

O conjunto possui dados em nível nacional, com identificação por município e unidade federativa. Entre as informações disponíveis estão data de conexão, fonte de geração, potência instalada, distribuidora, classe de consumo, modalidade e localização do empreendimento. Como há datas de conexão, os registros podem ser agrupados por mês ou ano para formar séries temporais.

| Item | Descrição |
|---|---|
| Fonte principal | ANEEL — Portal de Dados Abertos |
| Base | Relação de empreendimentos de Mini e Micro Geração Distribuída |
| Formato | CSV compactado em ZIP e versão em Parquet |
| Cobertura geográfica | Brasil, estados e municípios |
| Período de coleta | Registros a partir de dezembro de 2008 |
| Atualização | Diária, segundo os metadados do portal |
| Dados úteis | Data de conexão, fonte solar, potência instalada, UF, município e distribuidora |
| Tratamento previsto | Filtrar fonte solar, agrupar por mês/ano e somar potência instalada por localidade |

Como fonte complementar, será utilizado o **Painel de Dados de Micro e Minigeração Distribuída (PDGD)** da Empresa de Pesquisa Energética (EPE), que reúne dados históricos, indicadores de capacidade instalada, geração estimada, investimentos e projeções, permitindo comparar os resultados obtidos na base da ANEEL com indicadores consolidados do setor.

## 3. Solução proposta

A solução proposta será um produto analítico executável em Python, em notebook, contendo as etapas de coleta, preparação, análise e previsão dos dados. O produto deverá permitir acompanhar a evolução da energia solar distribuída no Brasil e observar diferenças entre regiões, estados e municípios.

Inicialmente, serão produzidos gráficos de linha para mostrar a evolução temporal da potência instalada e do número de empreendimentos solares. Em seguida, serão calculados indicadores de crescimento por estado e município.

Na etapa de modelagem, poderão ser utilizados métodos estatísticos e de aprendizado de máquina para séries temporais, como média móvel, regressão, ARIMA/SARIMA, Prophet ou modelos baseados em árvores. A escolha final dependerá da qualidade dos dados após o pré-processamento e dos resultados obtidos nos primeiros testes.

A proposta é viável porque os dados são públicos, oficiais, possuem cobertura nacional e podem ser transformados em séries temporais. Além disso, o problema tem aplicação prática, pois pode apoiar a análise de tendências do setor solar e contribuir para discussões sobre energia limpa, infraestrutura e sustentabilidade urbana.

## 4. Referências

AGÊNCIA NACIONAL DE ENERGIA ELÉTRICA. **Relação de empreendimentos de Mini e Micro Geração Distribuída**. Portal de Dados Abertos da ANEEL, 2026. Disponível em: https://dadosabertos.aneel.gov.br/pt_BR/dataset/relacao-de-empreendimentos-de-geracao-distribuida. Acesso em: 31 ago. 2026.

AGÊNCIA NACIONAL DE ENERGIA ELÉTRICA. **Micro e Minigeração Distribuída**. Brasília: ANEEL, 2026. Disponível em: https://www.gov.br/aneel/pt-br/assuntos/geracao-distribuida/. Acesso em: 31 ago. 2026.

EMPRESA DE PESQUISA ENERGÉTICA. **Painel de Dados de Micro e Minigeração Distribuída (PDGD)**. Rio de Janeiro: EPE, 2026. Disponível em: https://dashboard.epe.gov.br/apps/pdgd/. Acesso em: 31 ago. 2026.

EMPRESA DE PESQUISA ENERGÉTICA. **Balanço Energético Nacional 2026**: capítulo 1 — Análise energética e dados agregados. Rio de Janeiro: EPE, 2026. Disponível em: https://dashboard.epe.gov.br/apps/livro-ben/livro/pt/capitulo_1.html. Acesso em: 31 ago. 2026.

ORGANIZAÇÃO DAS NAÇÕES UNIDAS. **Objetivos de Desenvolvimento Sustentável**. Brasília: ONU Brasil. Disponível em: https://brasil.un.org/pt-br/sdgs. Acesso em: 31 ago. 2026.
