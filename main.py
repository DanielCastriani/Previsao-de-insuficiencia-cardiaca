
from eda.summary import summary
from feature_engineering.make_dataset import make_feature_engineering
from database.load_dataset import load_dataset


heart_failure = load_dataset()
heart_failure = make_feature_engineering(heart_failure)
summary(heart_failure)
