
from model.train_test import train_test_pipeline
from database.load_dataset import load_dataset
from eda.plots import plots
from eda.summary import summary

heart_failure = load_dataset()

summary(heart_failure)
plots(heart_failure)

train_test_pipeline(heart_failure)
