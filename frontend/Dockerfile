FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

# Cria config do Streamlit
# RUN mkdir -p ~/.streamlit && echo "\
# [server]\n\
# runOnSave = true\n\
# headless = true\n\
# port = 8501\n\
# enableCORS = false\n\
# " > ~/.streamlit/config.toml

# Criação segura do arquivo de configuração do Streamlit
RUN mkdir -p /root/.streamlit && \
    echo "[server]\n\
headless = true\n\
enableCORS = false\n\
port = 8501\n\
address = \"0.0.0.0\"" > /root/.streamlit/config.toml

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]