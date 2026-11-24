# 🔐 LGPD Compliance Analytics Dashboard

Dashboard interativo desenvolvido para monitoramento de indicadores de privacidade, proteção de dados e conformidade com a Lei Geral de Proteção de Dados (LGPD).

O projeto transforma dados relacionados à governança, segurança da informação e compliance em indicadores estratégicos que apoiam a tomada de decisão baseada em dados.

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![LGPD](https://img.shields.io/badge/LGPD-Compliance-green)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black)

---

# 📌 Visão Geral

A Lei Geral de Proteção de Dados (LGPD) exige que organizações implementem controles para proteger dados pessoais, reduzir riscos regulatórios e fortalecer a governança da informação.

Este projeto simula um ambiente corporativo de privacidade e proteção de dados, disponibilizando uma aplicação em Streamlit para monitoramento de:

- Titulares de dados
- Bases legais
- Sistemas corporativos
- Incidentes de segurança
- Solicitações dos titulares
- Indicadores executivos de conformidade

---

# 🏢 Caso de Negócio

Organizações precisam demonstrar conformidade regulatória de forma contínua.

O LGPD Compliance Analytics centraliza indicadores estratégicos relacionados à proteção de dados pessoais, permitindo identificar riscos, monitorar incidentes e acompanhar o desempenho dos programas de adequação à LGPD.

A solução foi construída utilizando conceitos de:

- Governança de Dados
- Business Intelligence
- Data Analytics
- Privacidade
- Segurança da Informação
- Compliance Regulatório

---

# 🏗️ Arquitetura da Solução

```text {preview="false"}
Arquivos CSV
      ↓
Tratamento com Pandas
      ↓
Regras de Negócio LGPD
      ↓
KPIs de Compliance
      ↓
Dashboard Streamlit
      ↓
Tomada de Decisão
```

---

# 🎯 Objetivos do Projeto

- Monitorar indicadores de conformidade LGPD.
- Avaliar sistemas aderentes à LGPD.
- Acompanhar solicitações dos titulares.
- Monitorar incidentes de segurança.
- Identificar riscos de governança.
- Apoiar auditorias internas.
- Gerar insights para tomada de decisão.

---

# 🚀 Funcionalidades Implementadas

## Dashboard Executivo

- KPIs executivos
- Compliance Score
- Indicadores de governança
- Visão consolidada da conformidade

## Gestão de Titulares

- Inventário de titulares
- Visualização por setor
- Visualização por base legal
- Análise de dados pessoais tratados

## Gestão de Incidentes

- Monitoramento de incidentes
- Classificação por criticidade
- Controle de status

## Sistemas Corporativos

- Sistemas conformes
- Sistemas não conformes
- Indicador geral de conformidade

## Direitos dos Titulares

- Solicitações realizadas
- Status de atendimento
- Indicadores operacionais

---

# 📊 Indicadores Disponíveis

## 🔒 Compliance

- Percentual de Conformidade
- Sistemas Conformes
- Sistemas Não Conformes
- Compliance Score

## 👤 Titulares

- Quantidade de Titulares
- Dados por Setor
- Dados por Base Legal

## 🚨 Incidentes

- Total de Incidentes
- Incidentes por Criticidade
- Status dos Incidentes

## 📄 Solicitações

- Total de Solicitações
- Solicitações Pendentes
- Solicitações Concluídas
- Performance Operacional

---

# 📌 KPIs Estratégicos

| KPI | Descrição |
|-------|-----------|
| Compliance Score | Índice geral de aderência à LGPD |
| Sistemas Conformes | Quantidade de sistemas adequados |
| Sistemas Não Conformes | Quantidade de sistemas com riscos |
| Incidentes Críticos | Eventos classificados como alto impacto |
| SLA de Atendimento | Atendimento das solicitações no prazo |
| Taxa de Conformidade | Percentual geral de conformidade |

---

# 📈 Resultados Obtidos

| Indicador | Valor |
|------------|--------|
| Titulares Cadastrados | 6 |
| Incidentes Registrados | 5 |
| Sistemas Monitorados | 5 |
| Solicitações Registradas | 4 |
| Compliance Score | 60% |

Além disso, o painel possibilita:

- Filtros por setor
- Visualização gráfica dos indicadores
- Tabelas interativas
- Monitoramento de conformidade em tempo real

---

# 🔒 Pilares da LGPD Abordados

- Governança de Dados
- Transparência
- Prestação de Contas (Accountability)
- Gestão de Riscos
- Segurança da Informação
- Direitos dos Titulares
- Monitoramento de Incidentes

---

# 🛠️ Tecnologias Utilizadas

## Linguagem

- Python

## Framework

- Streamlit

## Bibliotecas

- Pandas

## Banco de Dados

- SQL

## Versionamento

- Git
- GitHub

## Governança e Compliance

- LGPD
- Governança de Dados
- Compliance
- Gestão de Riscos
- Segurança da Informação

---

# ⚙️ Instalação

## Clonar Repositório

```bash {preview="false"}
git clone https://github.com/Maristelacosta/LGPD-Compliance-Analytics.git
```

```bash {preview="false"}
cd LGPD-Compliance-Analytics
```

## Criar Ambiente Virtual

### Windows

```bash {preview="false"}
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash {preview="false"}
python3 -m venv venv
source venv/bin/activate
```

## Instalar Dependências

```bash {preview="false"}
pip install -r requirements.txt
```

---

# ▶️ Executar Aplicação

```bash {preview="false"}
streamlit run app/dashboard.py
```

A aplicação ficará disponível em:

```text {preview="false"}
http://localhost:8501
```

---

# 📂 Estrutura do Projeto

```text {preview="false"}
LGPD-Compliance-Analytics
│
├── README.md
│
├── app
│   ├── app.py
│   ├── dashboard.py
│   └── dashboard_backup.py
│
├── data
│   ├── titulares.csv
│   ├── incidentes.csv
│   ├── sistemas.csv
│   └── solicitacoes.csv
│
├── sql
│   └── consultas_lgpd.sql
│
└── requirements.txt
```

---

# 📋 Dados Utilizados

## Titulares

- Nome
- Tipo de dado
- Base legal
- Setor

## Incidentes

- Data
- Tipo de incidente
- Criticidade
- Status

## Sistemas

- Nome do sistema
- Status de conformidade

## Solicitações

- Data
- Tipo
- Status

---

# 💡 Principais Insights

## Governança

- Identificação das áreas com maior concentração de dados pessoais
- Avaliação da conformidade dos sistemas corporativos
- Monitoramento das bases legais utilizadas

## Segurança da Informação

- Mapeamento de incidentes
- Avaliação da criticidade
- Acompanhamento de eventos de segurança

## Compliance

- Visão consolidada da conformidade LGPD
- Monitoramento de obrigações regulatórias
- Identificação de oportunidades de melhoria

---

# 🚀 Próximas Evoluções

## Versão 2.0

- Exportação para Excel
- Exportação para PDF
- Novos KPIs
- Dashboard Executivo Avançado
- Compliance Score Automatizado

## Versão 3.0

- Inteligência Artificial
- Geração automática de insights
- Recomendações de mitigação
- Monitoramento em tempo real
- Análise preditiva

---

# 🎯 Diferenciais do Projeto

Este projeto demonstra competências práticas em:

- Business Intelligence
- Data Analytics
- Governança de Dados
- Compliance Regulatório
- Proteção de Dados
- Visualização Executiva
- Desenvolvimento Python
- Storytelling com Dados

---

# 🎓 Competências Demonstradas

✅ Business Intelligence

✅ Data Analytics

✅ Python

✅ Pandas

✅ Streamlit

✅ LGPD

✅ Compliance

✅ Governança de Dados

✅ Gestão de Riscos

✅ Segurança da Informação

✅ Visualização de Dados

✅ Storytelling com Dados

---

# 👩‍💻 Autora

**Maristela Costa**

🎓 Bacharel em Sistemas de Informação

📚 MBA em Business Intelligence, Big Data & Analytics

🔐 MBA em Cibersegurança e Proteção de Dados

💻 Analista de Dados | Power BI | SQL | Python | Business Intelligence

📌 GitHub: github.com/Maristelacosta

📌 LinkedIn: linkedin.com/in/maristela-aparecida-costa

---

# 🏷️ Tags

LGPD • Compliance • Governança de Dados • Data Governance • Business Intelligence • Data Analytics • Python • Pandas • Streamlit • SQL • Segurança da Informação • Gestão de Riscos • Privacy Analytics • Dashboard Executivo

---

# 📄 Licença

Projeto desenvolvido para fins acadêmicos, demonstração de portfólio e aplicação prática de conceitos relacionados a:

- LGPD
- Governança de Dados
- Compliance
- Business Intelligence
- Segurança da Informação
- Analytics
