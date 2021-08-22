# Previsão de insuficiência cardíaca

[Dataset - Heart Failure Prediction](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data)

# Como executar

É necessário criar um virtual environment utilizando, e instalar as bibliotecas necessárias para executar o projeto executando os seguintes comandos:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Em seguida, é necessário criar uma pasta data/ na raiz do projeto e adicionar os arquivos do [Dataset](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data)

# Estrutura do projeto


├── data                    # Arquivos que contem os dados
├── database                # Scripts utilizados para carregar os dados
├── ├── sql                 # .sql files
│   ├── import_data.py      # Script de criação do arquivo db.sqlite
│   └── ...
├── utils                   # Módulos de utilidade