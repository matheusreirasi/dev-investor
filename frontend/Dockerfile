FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y build-essential && apt-get clean

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Cria config do Streamlit
RUN mkdir -p ~/.streamlit && echo "\
[server]\n\
runOnSave = true\n\
headless = true\n\
port = 8501\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]