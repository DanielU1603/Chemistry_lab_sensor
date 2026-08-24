
from functions import constant_signal_detection
import pandas as pd

df = pd.DataFrame({"temperature": [23, 23, 23, 23, 23, 54, 54, 54, 54, 54]})

anomaly = constant_signal_detection(df)
print(anomaly)

        