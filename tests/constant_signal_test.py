
from functions import constant_signal_detection
import pandas as pd

df = pd.DataFrame({"temperature": [1, 2, 2, 2, 2, 2, 2]})

anomaly = constant_signal_detection(df)
print(anomaly)

                        