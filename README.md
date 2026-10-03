# Sistema de Cadastro de Produtos de TI

Projeto desenvolvido com **Python** e **Django** para praticar os conceitos estudados na linguagem e no framework. O sistema permite gerenciar um catálogo de produtos da área de TI.

## Funcionalidades

- Cadastrar novos produtos
- Visualizar os produtos cadastrados
- Editar produtos existentes
- Excluir produtos

## Tecnologias

- Python 3
- Django
- PostgreSQL
- python-dotenv (variáveis de ambiente)

## Pré-requisitos

Antes de começar, você precisa ter instalado:

- [Python 3](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- Git

## Instalação

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> O arquivo deve incluir `django`, `psycopg2-binary` e `python-dotenv`.

### 4. Crie o banco de dados

Crie o banco no PostgreSQL antes de executar as migrações. Caso contrário, o Django não conseguirá criar as tabelas.

```bash
psql -U postgres
```

```sql
CREATE DATABASE stock_system_db ENCODING 'UTF8';
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto (mesma pasta do `manage.py`) com as credenciais do seu PostgreSQL:

```env
DB_NAME=stock_system_db
DB_USER=meu_usuario
DB_PASSWORD=minha_senha
DB_HOST=localhost
DB_PORT=5432
```

Você pode usar o `.env.example` como base:

```bash
cp .env.example .env
```

### 6. Configure o `settings.py`

Verifique se o `settings.py` lê as variáveis do `.env`:

```python
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}
```

### 7. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

## Executando o projeto

```bash
python manage.py runserver
```

Acesse o sistema em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Estrutura do projeto

```
projeto/
├── manage.py
├── .env              # não versionado
├── .env.example
├── .gitignore
├── requirements.txt
└── ...
```

> Ajuste a estrutura acima conforme as pastas reais do seu projeto.

## Licença

Este projeto foi desenvolvido para fins de estudo.