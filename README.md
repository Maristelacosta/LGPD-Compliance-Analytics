# 🔐 LGPD Compliance Analytics Dashboard

Projeto desenvolvido para monitoramento de indicadores de privacidade, proteção de dados e conformidade com a Lei Geral de Proteção de Dados (LGPD).

O objetivo é transformar dados relacionados à governança, segurança da informação e conformidade regulatória em indicadores estratégicos para apoio à tomada de decisão.

---

## 🎯 Objetivos do Projeto

- Monitorar indicadores de conformidade LGPD.
- Analisar incidentes de segurança.
- Acompanhar solicitações dos titulares de dados.
- Avaliar o nível de maturidade em governança de dados.
- Gerar insights para gestão de riscos e compliance.
- Apoiar auditorias e processos de adequação regulatória.

---

## 📊 Indicadores do Dashboard

O dashboard foi desenvolvido para monitorar métricas relacionadas à privacidade, governança de dados e conformidade com a LGPD.

### 🔐 Indicadores de Conformidade

- Compliance Score Geral
- Nível de Conformidade por Área
- Percentual de Sistemas Adequados
- Percentual de Não Conformidades

### 👥 Indicadores de Dados Pessoais

- Total de Titulares Cadastrados
- Total de Dados Pessoais Tratados
- Quantidade de Dados Sensíveis
- Dados por Setor da Organização
- Dados por Base Legal

### 🚨 Indicadores de Segurança

- Total de Incidentes de Segurança
- Incidentes por Criticidade
- Incidentes por Tipo
- Incidentes por Mês
- Taxa de Resolução de Incidentes

### 📋 Indicadores LGPD

- Solicitações dos Titulares
- Solicitações Concluídas
- Solicitações Pendentes
- Tempo Médio de Atendimento
- Solicitações por Tipo

### 📈 Indicadores Executivos

- Score Geral de Governança
- Principais Riscos Identificados
- Áreas com Maior Exposição
- Tendência de Incidentes
- Resumo Executivo de Conformidade

---

## 🛠️ Tecnologias Utilizadas

## ⚙️ Instalação e Execução

### Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python 3.10 ou superior
- Git
- Power BI Desktop
- Jupyter Notebook ou JupyterLab
- Visual Studio Code (opcional)

---

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/Maristelacosta/LGPD-Compliance-Analytics.git
```

```bash
cd LGPD-Compliance-Analytics
```

---

### 2️⃣ Criar Ambiente Virtual

Windows:

```bash
python -m venv venv
```

Ativar ambiente virtual:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

Caso o arquivo ainda não exista:

```bash
pip install pandas numpy matplotlib seaborn plotly streamlit jupyter
```

---

### 4️⃣ Executar os Notebooks

Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

Abra os arquivos da pasta:

```text
notebooks/
```

e execute as análises.

---

### 5️⃣ Executar a Aplicação Streamlit

Na pasta principal do projeto:

```bash
streamlit run app/app.py
```

A aplicação será disponibilizada em:

```text
http://localhost:8501
```

---

### 6️⃣ Abrir o Dashboard Power BI

Abra o arquivo:

```text
dashboard/LGPD_Compliance.pbix
```

no Power BI Desktop.

---

### 7️⃣ Estrutura dos Dados

Os datasets utilizados encontram-se na pasta:

```text
data/
```

Arquivos:

```text
titulares.csv
incidentes.csv
solicitacoes.csv
sistemas.csv
```

Caso deseje utilizar dados próprios, mantenha a mesma estrutura de colunas para garantir compatibilidade com as análises e dashboards.

---

### ✅ Verificação da Instalação

Se tudo estiver correto, você deverá conseguir:

- Executar os notebooks Python
- Visualizar os gráficos analíticos
- Abrir o dashboard Power BI
- Executar a aplicação Streamlit
- Gerar os indicadores de conformidade LGPD


### 📊 Business Intelligence

- Power BI
- Power Query
- DAX

### 🗄️ Banco de Dados

- SQL
- PostgreSQL
- SQL Server

### 🐍 Linguagens de Programação

- Python
- SQL

### 📚 Bibliotecas Python

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

### 🌐 Desenvolvimento e Visualização

- Streamlit
- GitHub

### 📋 Governança e Compliance

- LGPD
- Governança de Dados
- Compliance
- Gestão de Riscos
- Segurança da Informação

### ⚙️ Ferramentas de Apoio

- Jupyter Notebook
- Visual Studio Code
- Git
- GitHub

---

## 📂 Estrutura do Projeto

```text
LGPD-Compliance-Analytics/
│
├── README.md
│
├── data/
│   ├── titulares.csv
│   ├── incidentes.csv
│   ├── solicitacoes.csv
│   └── sistemas.csv
│
├── notebooks/
│   ├── 01_analise_lgpd.ipynb
│   ├── 02_indicadores.ipynb
│   └── 03_compliance_score.ipynb
│
├── sql/
│   ├── create_tables.sql
│   ├── inserts.sql
│   └── consultas_lgpd.sql
│
├── dashboard/
│   ├── LGPD_Compliance.pbix
│   └── dashboard_documentacao.md
│
├── images/
│   ├── dashboard-geral.png
│   ├── incidentes.png
│   ├── compliance-score.png
│   └── arquitetura-projeto.png
│
├── reports/
│   ├── relatorio_executivo.pdf
│   └── relatorio_conformidade.pdf
│
└── app/
    ├── app.py
    ├── dashboard.py
    ├── compliance.py
    └── utils.py
```

### Descrição das Pastas

| Pasta | Descrição |
|---------|-------------|
| data | Dados utilizados no projeto |
| notebooks | Análises exploratórias e estudos dos indicadores |
| sql | Scripts SQL e consultas analíticas |
| dashboard | Arquivos do Power BI |
| images | Imagens e screenshots dos dashboards |
| reports | Relatórios executivos e documentos |
| app | Aplicação web em Streamlit |

---

## 💡 Principais Insights

A análise dos dados permite identificar padrões relacionados à privacidade, segurança da informação e conformidade regulatória.

### 🔐 Conformidade LGPD

- Identificação das áreas com maior concentração de dados pessoais.
- Monitoramento das bases legais mais utilizadas.
- Avaliação do nível de conformidade por departamento.
- Identificação de oportunidades de melhoria em processos de adequação.

### 🚨 Segurança da Informação

- Mapeamento dos tipos de incidentes mais recorrentes.
- Avaliação da criticidade dos incidentes registrados.
- Monitoramento da evolução dos eventos de segurança.
- Identificação de vulnerabilidades operacionais.

### 👥 Gestão de Dados Pessoais

- Quantificação de dados pessoais e dados sensíveis.
- Distribuição dos dados por área de negócio.
- Identificação de riscos relacionados ao excesso de retenção.
- Avaliação da utilização das bases legais.

### 📋 Direitos dos Titulares

- Volume de solicitações recebidas.
- Tempo médio de atendimento.
- Percentual de solicitações concluídas.
- Identificação de gargalos operacionais.

### 📈 Gestão Executiva

- Monitoramento do Compliance Score.
- Identificação dos principais riscos.
- Avaliação contínua da maturidade em governança.
- Apoio à tomada de decisão baseada em dados.

---

## 📷 Dashboard

O painel apresenta uma visão executiva dos indicadores de privacidade, compliance e segurança da informação.

### Visão Geral

- Compliance Score
- Incidentes de Segurança
- Dados Pessoais por Setor
- Bases Legais Utilizadas
- Solicitações dos Titulares

### Exemplos de Telas

- Dashboard Executivo
- Gestão de Incidentes
- Governança de Dados
- Indicadores de Conformidade
- Análise de Riscos

> As capturas de tela serão adicionadas na evolução do projeto.

---

## 🚀 Próximas Evoluções

As próximas versões do projeto contemplam melhorias voltadas para automação, inteligência analítica, governança de dados e monitoramento contínuo da conformidade.

### 🤖 Inteligência Artificial

- Implementação de geração automática de insights.
- Resumos executivos automatizados com IA.
- Identificação automática de riscos de conformidade.
- Classificação inteligente de incidentes de segurança.
- Recomendações de mitigação de riscos baseadas em dados.

### 📊 Business Intelligence

- Ampliação dos indicadores e KPIs estratégicos.
- Dashboards específicos por área.
- Monitoramento histórico da conformidade.
- Benchmarking entre departamentos.

### 🔒 Segurança da Informação

- Inclusão de indicadores de cibersegurança.
- Monitoramento de vulnerabilidades.
- Métricas de gestão de riscos.
- Dashboards para auditorias e compliance.
- Acompanhamento de incidentes por criticidade.

### ⚖️ Governança e LGPD

- Avaliação automática de conformidade.
- Monitoramento das bases legais.
- Controle de retenção e descarte de dados.
- Mapeamento de dados sensíveis por processo.
- Indicadores de maturidade em governança.

### 🌐 Aplicação Web

- Desenvolvimento de interface em Streamlit.
- Filtros avançados para análise dos indicadores.
- Exportação automática de relatórios.
- Painel executivo em tempo real.

### 📈 Analytics Avançado

- Modelos preditivos para avaliação de riscos.
- Análise de tendências de incidentes.
- Compliance Score preditivo.
- Detecção de anomalias.
- Apoio inteligente à tomada de decisão.

---

## 🎯 Roadmap

### ✅ Versão 1.0

- Estrutura inicial do projeto
- Modelagem dos dados
- Scripts SQL
- Indicadores LGPD
- Dashboard Power BI
- Documentação do projeto

### 🔄 Versão 2.0

- Aplicação Streamlit
- Relatórios automatizados
- Compliance Score avançado
- Visualizações interativas
- Indicadores de governança

### 🚀 Versão 3.0

- Inteligência Artificial aplicada à conformidade
- Predição de riscos
- Geração automática de insights
- Monitoramento em tempo real
- Detecção de anomalias

---

## 🎓 Competências Demonstradas

✅ Business Intelligence

✅ Data Analytics

✅ SQL

✅ Python

✅ Power BI

✅ Compliance

✅ LGPD

✅ Governança de Dados

✅ Gestão de Riscos

✅ Segurança da Informação

✅ Visualização de Dados

✅ Storytelling com Dados

---

## 👩‍💻 Autora

**Maristela Costa**

🎓 Sistemas de Informação

📚 MBA em Business Intelligence, Big Data & Analytics

🔐 MBA em Cibersegurança e Proteção de Dados

💻 Analista de Dados | Business Intelligence | Power BI | SQL | Python

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos, portfólio profissional e demonstração de competências em Business Intelligence, Governança de Dados, LGPD e Segurança da Informação.

---

⭐ **Transformando dados em insights, insights em conhecimento e conhecimento em decisões estratégicas.**
