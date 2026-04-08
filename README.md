# Pipeline de Dados IoT com Docker e Streamlit 🌡️

Este projeto consiste em um pipeline de dados completo para processamento de leituras de temperatura de dispositivos IoT, utilizando containers Docker para o banco de dados e Streamlit para a visualização.

## 🚀 Tecnologias Utilizadas
* **Python 3.x**: Linguagem principal do projeto.
* **Docker**: Containerização do banco de dados PostgreSQL.
* **PostgreSQL**: Armazenamento relacional dos dados.
* **Pandas**: Manipulação e limpeza dos dados do Kaggle.
* **SQLAlchemy**: ORM para conexão entre Python e Banco de Dados.
* **Streamlit & Plotly**: Criação do dashboard interativo.

## 📂 Estrutura do Projeto
- `/src`: Scripts Python de ingestão, criação de views e dashboard.
- `/data`: Base de dados em CSV.
- `/sql`: Queries de criação das Views SQL.
- `/docs`: Capturas de tela e documentação adicional.

## 🔧 Como Executar o Projeto

1. **Configurar o Banco de Dados (Docker):**
   ```bash
   docker run --name postgres-iot -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres