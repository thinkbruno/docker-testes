# Imagem oficial Python
FROM python:3.12-slim

# Evita gerar arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório dentro do container
WORKDIR /app

# Copia requirements primeiro (melhora cache)
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Expõe porta
EXPOSE 5000

# Comando para rodar
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]