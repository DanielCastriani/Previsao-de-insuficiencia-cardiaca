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


# Dicionário de dados

| Feature                   | Descrição                                                                   | Tipo             |
| ------------------------- | --------------------------------------------------------------------------- | ---------------- |
| age                       | Idade da pessoa                                                             | Float            |
| anaemia                   | Diminuição de glóbulos vermelhos ou hemoglobina                             | Int 0 ou 1       |
| creatinine_phosphokinase  | Nível da enzima CPK no sangue (mcg / L))                                    | Int              |
| diabetes                  | Se o paciente tem diabetes                                                  | Int 0 ou 1       |
| ejection_fraction         | Porcentagem de sangue saindo do coração a cada contração                    | Int              |
| high_blood_pressure       | Indica se paciente tem pressão alta                                         | Int 0 ou 1       |
| platelets                 | Plaquetas no sangue (kiloplatelets/mL)                                      | Float            |
| serum_creatinine          | Nível de creatinina sérica no sangue (mg / dL)                              | Float            |
| serum_sodium              | Nível de sódio sérico no sangue (mEq / L)                                   | Int              |
| sex                       | Mulher ou homem                                                             | Int 0 ou 1       |
| smoking                   | Se paciente fuma ou não                                                     | Int 0 ou 1       |
| time                      | Período de acompanhamento (dias)                                            | Int              |
| DEATH_EVENT               | Se o paciente evoluiu a óbito durante o período de acompanhamento \[TARGET] | Int 0 ou 1       |

