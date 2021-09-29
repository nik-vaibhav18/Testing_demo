import os
import pandas as pd
import numpy as np
import joblib
import logging


def prepare_data(df):
  logging.info("preparing the data by segregating dependent and independent variables")
  X = df.drop("y", axis=1)

  y = df["y"]

  return X, y

def save_model(model,filename):
  model_dir = "models"
  os.makedirs(model_dir, exist_ok=True)  # ONLY CREATE IF MODEL_DIR DOES NOT EXISTS
  filepath = os.path.join(model_dir, filename)  # model/filename
  joblib.dump(model, filepath)