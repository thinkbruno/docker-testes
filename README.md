# Full Stack User Management System

Projeto Full Stack desenvolvido com foco em arquitetura limpa, boas
práticas e containerização. A aplicação implementa um CRUD completo de
usuários com autenticação básica de senha (hash), organização em camadas
e ambiente 100% Dockerizado.

---

## 🚀 Stack Tecnológica

### Backend

- Python 3.12
- Flask
- SQLAlchemy (ORM)
- MySQL 8
- Arquitetura em camadas (Repository + Service)
- Hash de senha (bcrypt)
- Docker

### Frontend

- Vue 3
- Vite
- Axios
- Nginx (produção)

### Infraestrutura

- Docker
- Docker Compose
- Multi-stage build
- Healthcheck MySQL
- Ambiente isolado

---

## 🏗 Arquitetura

O backend segue padrão organizado em camadas:

app/ ├── routes/ ├── services/ ├── repositories/ ├── models/ ├──
database/ ├── config.py └── **init**.py

### Padrões aplicados:

- Separation of Concerns
- Repository Pattern
- Service Layer
- Environment-based configuration (.env)
- Clean code structure

---

## 📌 Funcionalidades

- Listar usuários
- Criar usuário
- Atualizar usuário (PUT)
- Atualização parcial (PATCH)
- Remover usuário
- Hash seguro de senha
- Banco populado via SQL dump
- Frontend consumindo API REST

---

## 🐳 Como Executar o Projeto

### 1️⃣ Pré-requisitos

- Docker
- Docker Compose

### 2️⃣ Executar

Na raiz do projeto:

docker compose up --build

### 3️⃣ Acessos

Frontend: http://localhost

Backend API: http://localhost:5000/users

---

## 🔐 Variáveis de Ambiente

O projeto utiliza `.env` para configuração.

Exemplo:

MYSQL_HOST=db MYSQL_USER=root MYSQL_PASSWORD=root
MYSQL_DATABASE=bd_testes FLASK_ENV=development

---

## 📦 Banco de Dados

- MySQL 8
- Inicialização via SQL dump
- Estrutura baseada em tabela `user`
- Persistência via volume Docker

---

## 🧪 Endpoints da API

GET /users POST /users PUT /users/`<id>`{=html} PATCH
/users/`<id>`{=html} DELETE /users/`<id>`{=html}

---

## 🎯 Objetivo do Projeto

Este projeto demonstra:

- Capacidade de estruturar backend escalável
- Conhecimento em arquitetura limpa
- Integração frontend-backend
- Containerização profissional
- Organização de código para ambiente produtivo
- Boas práticas de desenvolvimento

---

## 👨‍💻 Autor

Bruno Ramos\
Full Stack Software Engineer\
Python \| APIs REST \| Docker \| Cloud \| Arquitetura

LinkedIn: https://www.linkedin.com/in/ramosbruno90/
