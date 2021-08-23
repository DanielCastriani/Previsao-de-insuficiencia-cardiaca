import numpy as np
from sklearn.metrics import confusion_matrix

import seaborn as sns
import matplotlib.pyplot as plt


def plot_conf_matrix(y_test: np.array, y_pred: np.array, path: str = None):
    conf_matrix = confusion_matrix(y_test, y_pred)

    plt.figure()
    sns.heatmap(conf_matrix, annot=True)

    if path:
        plt.savefig(path)

    plt.show()
