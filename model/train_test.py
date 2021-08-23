

import numpy as np
import pandas as pd
from feature_engineering.make_dataset import make_feature_engineering
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from utils.file_utils import create_path_if_not_exists, save_model
from utils.metrics import plot_conf_matrix
from sklearn.model_selection import GridSearchCV


def fit_model(x_train: pd.DataFrame, y_train: pd.Series):
    model = RandomForestClassifier()
    grid_search = GridSearchCV(
        estimator=model,
        param_grid={
            "n_estimators": [100, 150, 250],
            "max_depth": [None, 25, 50],
            "min_samples_split": [2, 4, 8],
            "min_samples_leaf": [1, 2, 8],
            "criterion": ["gini", "entropy"]
        },
        scoring="f1_weighted",
        cv=5,
        n_jobs=-1,
        verbose=2
    )

    grid_search.fit(x_train, y_train)
    print(f"Melhores parametros: {grid_search.best_params_}")
    return grid_search.best_estimator_


def predict(x_test: pd.DataFrame, model):
    return model.predict(x_test)


def train_test_pipeline(heart_failure: pd.DataFrame):
    heart_failure = make_feature_engineering(heart_failure)

    y = heart_failure['DEATH_EVENT']
    x = heart_failure.drop(columns='DEATH_EVENT')

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

    model = fit_model(x_train, y_train)
    y_pred = predict(x_test, model)

    path = create_path_if_not_exists('public/img/plots', file_name='conf_matrix.png')

    plot_conf_matrix(y_test, y_pred, path)

    print(classification_report(y_test, y_pred))

    save_model(model, create_path_if_not_exists('bin', file_name='model.pickle'))
