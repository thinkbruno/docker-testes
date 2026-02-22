# Full Stack User Management System

## Sistema de Gerenciamento de Usuários (Full Stack)

Aplicação Full Stack desenvolvida com foco em arquitetura limpa, boas práticas, organização em camadas e containerização com Docker.

Projeto ideal para demonstrar competências em Backend Python, APIs REST, MySQL, Vue.js e Dockerização profissional.

### 🚀 Tech Stack | Tecnologias

#### Backend

- Python 3.12
- Flask
- SQLAlchemy (ORM)
- MySQL 8
- Arquitetura em Camadas (Repository Pattern + Service Layer)
- Validação com Marshmallow
- Hash de senha com bcrypt
- Docker

#### Frontend

- Vue 3
- Vite
- Axios
- Nginx (produção)
- Toast notifications
- Loading state management

#### Infraestrutura

- Docker
- Docker Compose
- Multi-stage build
- Healthcheck (MySQL)
- Reverse Proxy com Nginx
- Ambiente isolado via containers

---

### 🏗 Arquitetura | Architecture

O backend segue princípios de Clean Architecture e Separation of Concerns, dividido em:

```text
app/
 ├── routes/
 ├── services/
 ├── repositories/
 ├── models/
 ├── schemas/
 ├── database/
 └── config.py
```

### Padrões Aplicados | Applied Patterns

- Repository Pattern
- Service Layer Pattern
- Environment-based configuration (.env)
- RESTful API Design
- Clean Code
- Container-first approach

### 📌 Funcionalidades | Features

#### Backend

- Listagem de usuários (GET)
- Criação de usuário (POST)
- Atualização completa (PUT)
- Atualização parcial (PATCH)
- Remoção (DELETE)
- Validação de dados
- Hash seguro de senha (bcrypt)
- Persistência em MySQL
- Banco inicializado via SQL dump

#### Frontend

- Interface responsiva
- Feedback visual com Toasts (sucesso/erro)
- Loading indicator para requisições
- Integração completa com API REST
- Formulário dinâmico (Create / Update)

### 🐳 Como Executar | How to Run

#### Pré-requisitos

- Docker
- Docker Compose

#### Executar o projeto

```Bash
docker compose up --build
```

#### Acessos

Frontend: http://localhost

API (via Nginx reverse proxy): http://localhost/api/users

### 🔐 Variáveis de Ambiente | Environment Variables

Exemplo de configuração:

```Snippet de código
MYSQL_HOST=db
MYSQL_USER=root
MYSQL_PASSWORD=root
MYSQL_DATABASE=bd_testes
FLASK_ENV=development
```

### 🎯 Objetivo do Projeto | Project Purpose

Este projeto demonstra:

- Desenvolvimento de APIs REST com Python
- Estruturação de backend escalável
- Aplicação de padrões de arquitetura
- Integração Frontend + Backend
- Containerização profissional
- Organização voltada para produção
- Conhecimento em MySQL e ORM
- Boas práticas de validação e segurança (hash de senha)

## 👨‍💻 Autor | Author

Bruno Ramos\
Full Stack Software Engineer\
Python \| APIs REST \| Docker \| Cloud \| Arquitetura

LinkedIn: https://www.linkedin.com/in/ramosbruno90/
