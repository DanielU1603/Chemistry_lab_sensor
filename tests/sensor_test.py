
from functions import constant_signal_detection 
import pandas as pd 

dummy_df = pd.DataFrame(columns="temperature", data=[1, 1, 1, 1, 1])

dummy_df_two = pd.DataFrame(columns="temperature", data=[1, 1, 1, 1, 1, 2, 2, 2, 2, 2])

dummy_df_three = pd.DataFrame({"temperature": [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]})

class TestClass:

    def no_anomalies_test(self):
        check = constant_signal_detection(dummy_df)
        assert check["status"] == "no_anomalies_detected"
    
    def end_anomaly_test(self):
        check = constant_signal_detection(dummy_df_two)
        assert check ["status"] == "end_row_anomaly"
        #assert

    def multiple_anomalies_test(self): 
        check = constant_signal_detection(dummy_df_three)
        assert len(check["anomalies"]) == 2
    