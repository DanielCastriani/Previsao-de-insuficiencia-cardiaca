
from utils.df_utils import value_counts
import pandas as pd
pd.set_option('display.expand_frame_repr', False)


def count_death(heart_failure: pd.DataFrame):
    recovered = len(heart_failure[heart_failure['DEATH_EVENT'] == 0])
    death = len(heart_failure[heart_failure['DEATH_EVENT'] == 1])

    return recovered, death


def summary(heart_failure: pd.DataFrame):
    print("Informações sobre o dataset")
    print(f"Quantidade de observações(linha): {len(heart_failure)}")
    print(f"Quantidade de features (colunas): {len(heart_failure.columns) -1}")
    print(f'Dados faltantes: {heart_failure.isna().sum()}')

    recovered, death = count_death(heart_failure)
    print(f"\nVariável target: DEATH_EVENT")
    print(f'recovered: {recovered}\t\t{recovered/len(heart_failure) * 100}')
    print(f'death: {death}\t\t{death/len(heart_failure) * 100}')

    numeric_cols = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']
    cat_col = list(set(heart_failure.columns.tolist()) - set(numeric_cols))

    print('\nInformações estatisticas')
    print(heart_failure[numeric_cols].describe().T)

    print("\n==========================================================\n")
    for c in cat_col:
        value_counts(heart_failure, column=c)
        print("__________________________________________________________\n")
