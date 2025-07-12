import pandas as pd
from pathlib import  Path

BASE_DIR=Path(__file__).parent.parent
DATA_DIR=BASE_DIR / "data/houseprice.csv"


data=pd.read_csv(DATA_DIR)

print(data)
