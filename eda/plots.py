
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.gridspec import GridSpec
from utils.file_utils import create_path_if_not_exists


def create_ax(x: int, y: int, title: str, gs: GridSpec, fig: Figure):
    ax = fig.add_subplot(gs[x, y])
    ax.set_title(title)

    return ax


def feature_distribution(heart_failure: pd.DataFrame, show: bool = True):
    path = create_path_if_not_exists('public/img/plots', file_name='distplot.png')

    fig = plt.figure(figsize=(18, 12), constrained_layout=True)
    gs = GridSpec(2, 4, figure=fig)

    sns.histplot(heart_failure['age'], kde=True,
                 ax=create_ax(0, 0, 'Distribuição de Idade', gs, fig))
    sns.histplot(heart_failure['creatinine_phosphokinase'], kde=True,
                 ax=create_ax(0, 1, 'Enzima CPK (mcg / L)', gs, fig))
    sns.histplot(heart_failure['ejection_fraction'], kde=True,
                 ax=create_ax(0, 2, 'Sangue saindo do coração a cada contração', gs, fig))
    sns.histplot(heart_failure['platelets'], kde=True,
                 ax=create_ax(0, 3, 'Plaquetas', gs, fig))

    sns.histplot(heart_failure['serum_creatinine'], kde=True,
                 ax=create_ax(1, 0, 'Creatinina sérica (mg / dL)', gs, fig))
    sns.histplot(heart_failure['serum_sodium'], kde=True,
                 ax=create_ax(1, 1, 'Sódio sérico (mEq / L)', gs, fig))
    sns.histplot(heart_failure['time'], kde=True,
                 ax=create_ax(1, 2, 'Acompanhamento (dias)', gs, fig))

    plt.savefig(path)

    if show:
        plt.show()


def box_plot_features(heart_failure: pd.DataFrame, show: bool = True):
    path = create_path_if_not_exists('public/img/plots', file_name='boxplot.png')

    fig = plt.figure(figsize=(18, 12), constrained_layout=True)
    gs = GridSpec(2, 4, figure=fig)

    sns.boxplot(y=heart_failure['age'],
                ax=create_ax(0, 0, 'Distribuição de Idade', gs, fig))
    sns.boxplot(y=heart_failure['creatinine_phosphokinase'],
                ax=create_ax(0, 1, 'Enzima CPK (mcg / L)', gs, fig))
    sns.boxplot(y=heart_failure['ejection_fraction'],
                ax=create_ax(0, 2, 'Sangue saindo do coração a cada contração', gs, fig))
    sns.boxplot(y=heart_failure['platelets'],
                ax=create_ax(0, 3, 'Plaquetas no sangue', gs, fig))

    sns.boxplot(y=heart_failure['serum_creatinine'],
                ax=create_ax(1, 0, 'Creatinina sérica (mg / dL)', gs, fig))
    sns.boxplot(y=heart_failure['serum_sodium'],
                ax=create_ax(1, 1, 'Sódio sérico (mEq / L)', gs, fig))
    sns.boxplot(y=heart_failure['time'],
                ax=create_ax(1, 2, 'Acompanhamento (dias)', gs, fig))

    plt.savefig(path)

    if show:
        plt.show()


def scatter_age_x_features(heart_failure: pd.DataFrame, show: bool = True):
    path = create_path_if_not_exists('public/img/plots', file_name='scatter_age.png')

    fig = plt.figure(figsize=(18, 12), constrained_layout=True)
    gs = GridSpec(2, 3, figure=fig)

    sns.scatterplot(x=heart_failure['age'], y=heart_failure['creatinine_phosphokinase'],
                    ax=create_ax(0, 0, 'Idade x Enzima CPK (mcg / L)', gs, fig))
    sns.scatterplot(x=heart_failure['age'], y=heart_failure['ejection_fraction'],
                    ax=create_ax(0, 1, 'Idade x Sangue saindo do coração a cada contração', gs, fig))
    sns.scatterplot(x=heart_failure['age'], y=heart_failure['platelets'],
                    ax=create_ax(0, 2, 'Idade x Plaquetas no sangue', gs, fig))

    sns.scatterplot(x=heart_failure['age'], y=heart_failure['serum_creatinine'],
                    ax=create_ax(1, 0, 'Idade x Creatinina sérica (mg / dL)', gs, fig))
    sns.scatterplot(x=heart_failure['age'], y=heart_failure['serum_sodium'],
                    ax=create_ax(1, 1, 'Idade x Sódio sérico (mEq / L)', gs, fig))
    sns.scatterplot(x=heart_failure['age'], y=heart_failure['time'],
                    ax=create_ax(1, 2, 'Idade x Acompanhamento (dias)', gs, fig))

    plt.savefig(path)

    if show:
        plt.show()


def count_plot_features(heart_failure: pd.DataFrame, show: bool = True):
    path = create_path_if_not_exists('public/img/plots', file_name='count_plot.png')

    fig = plt.figure(figsize=(18, 12), constrained_layout=True)
    gs = GridSpec(2, 3, figure=fig)

    sns.countplot(x=heart_failure['sex'],
                  ax=create_ax(0, 0, 'Sexo', gs, fig))
    sns.countplot(x=heart_failure['smoking'],
                  ax=create_ax(0, 1, 'Fumante', gs, fig))
    sns.countplot(x=heart_failure['anaemia'],
                  ax=create_ax(0, 2, 'Diminuição hemoglobina', gs, fig))

    sns.countplot(x=heart_failure['high_blood_pressure'],
                  ax=create_ax(1, 0, 'Pressão Alta', gs, fig))
    sns.countplot(x=heart_failure['diabetes'],
                  ax=create_ax(1, 1, 'Diabetes', gs, fig))
    sns.countplot(x=heart_failure['DEATH_EVENT'],
                  ax=create_ax(1, 2, 'Óbito', gs, fig))

    plt.savefig(path)

    if show:
        plt.show()


def plot_survival(heart_failure: pd.DataFrame, show: bool = True):
    path = create_path_if_not_exists('public/img/plots', file_name='survival.png')

    fig = plt.figure(figsize=(18, 12), constrained_layout=True)
    gs = GridSpec(2, 3, figure=fig)

    sns.countplot(x=heart_failure['DEATH_EVENT'], hue=heart_failure['sex'],
                  ax=create_ax(0, 0, 'Sobrevivente x Sexo', gs, fig))
    sns.countplot(x=heart_failure['DEATH_EVENT'], hue=heart_failure['smoking'],
                  ax=create_ax(0, 1, 'Sobrevivente x Fumante', gs, fig))
    sns.countplot(x=heart_failure['DEATH_EVENT'], hue=heart_failure['anaemia'],
                  ax=create_ax(0, 2, 'Sobrevivente x Diminuição hemoglobina', gs, fig))

    sns.countplot(x=heart_failure['DEATH_EVENT'], hue=heart_failure['high_blood_pressure'],
                  ax=create_ax(1, 0, 'Sobrevivente x Pressão Alta', gs, fig))
    sns.countplot(x=heart_failure['DEATH_EVENT'], hue=heart_failure['diabetes'],
                  ax=create_ax(1, 1, 'Sobrevivente x Diabetes', gs, fig))

    plt.savefig(path)

    if show:
        plt.show()


def correlation_plot(heart_failure: pd.DataFrame, show: bool = True):
    corr = heart_failure.corr()
    path = create_path_if_not_exists('public/img/plots', file_name='correlation.png')

    plt.figure(figsize=(15, 15))
    sns.heatmap(corr, annot=True)

    plt.savefig(path)

    if show:
        plt.show()


def plots(heart_failure: pd.DataFrame, show: bool = True):
    feature_distribution(heart_failure, show)
    scatter_age_x_features(heart_failure, show)
    box_plot_features(heart_failure, show)
    count_plot_features(heart_failure, show)
    plot_survival(heart_failure, show)
    correlation_plot(heart_failure, show)
