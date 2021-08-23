

from utils.file_utils import create_path_if_not_exists
from utils.metrics import plot_conf_matrix
import pandas as pd
from feature_engineering.make_dataset import make_feature_engineering
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


def train_test_pipeline(heart_failure: pd.DataFrame):
    heart_failure = make_feature_engineering(heart_failure)

    y = heart_failure['DEATH_EVENT']
    x = heart_failure.drop(columns='DEATH_EVENT')

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

    rfc = RandomForestClassifier()
    rfc.fit(x_train, y_train)

    y_pred = rfc.predict(x_test)

    path = create_path_if_not_exists('public/img/plots', file_name='conf_matrix.png')

    plot_conf_matrix(y_test, y_pred, path)

    print(classification_report(y_test, y_pred))
