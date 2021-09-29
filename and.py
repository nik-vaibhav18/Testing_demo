from utils.all_utils import prepare_data
from utils.model import Perceptron
import pandas as pd
import logging
import os
import numpy as np

logging_str="[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
logging_dir="logs"
os.makedirs(logging_dir,exist_ok=True)
logging.basicConfig(filename=os.path.join(logging_dir,"running_logs.log"),level=logging.INFO,format=logging_str)

AND = {"x1": [0,0,1,1],
        "x2": [0,1,0,1],
        "y": [0,0,0,1] }

df = pd.DataFrame(AND)
logging.info(df)
X, y = prepare_data(df)
model = Perceptron(eta=0.3, epochs=10)
model.fit(X, y)
_ = model.total_loss()