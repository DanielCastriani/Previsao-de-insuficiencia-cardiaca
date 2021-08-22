
from utils.file_utils import create_path_if_not_exists
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def feature_distribution(heart_failure: pd.DataFrame):
    path = create_path_if_not_exists('public/img/plots', file_name='distplot.png')

    fig, axes = plt.subplots(ncols=4, nrows=2,  figsize=(18, 12))

    axes[0,0].set_title('Distribuição de Idade')
    axes[0,1].set_title('Enzima CPK (mcg / L)')
    axes[0,2].set_title('Sangue saindo do coração a cada contração')
    axes[0,3].set_title('Plaquetas no sangue')

    axes[1,0].set_title('Creatinina sérica (mg / dL)')
    axes[1,1].set_title('Sódio sérico (mEq / L)')
    axes[1,2].set_title('Acompanhamento (dias)')

    sns.histplot(heart_failure['age'],  kde=True, ax=axes[0, 0])
    sns.histplot(heart_failure['creatinine_phosphokinase'],  kde=True, ax=axes[0, 1])
    sns.histplot(heart_failure['ejection_fraction'],  kde=True, ax=axes[0, 2])
    sns.histplot(heart_failure['platelets'],  kde=True, ax=axes[0, 3])

    sns.histplot(heart_failure['serum_creatinine'],  kde=True, ax=axes[1, 0])
    sns.histplot(heart_failure['serum_sodium'],  kde=True, ax=axes[1, 1])
    sns.histplot(heart_failure['time'],  kde=True, ax=axes[1, 2])

    plt.savefig(path)
    plt.show()


def plots(heart_failure: pd.DataFrame):
    feature_distribution(heart_failure)
