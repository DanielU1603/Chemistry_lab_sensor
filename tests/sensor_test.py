
from functions import constant_signal_detection
from functions import visualization 
import pandas as pd 

"""dummy_df = pd.DataFrame(columns="temperature", data=[1, 1, 1, 1, 1])

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
        assert len(check["anomalies"]) == 2"""

# -------------------visualization_function_test
warn_anomalies = [{"column": "temperature", "start_row": 0, "end_row": 5, "value": 29}, {"column": "temperature", "start_row": 15, "end_row": 20, "value": 202}]
warn = {"status": "counter_stuck", "anomalies": warn_anomalies}
anomalies = [{"column": "temperature", "value": 23, "row":6}, {"column": "temperature", "value": 84, "row": 9}]
anomalies_dic = {"status": "anomalies_detected", "anomalies": anomalies}
df = pd.DataFrame({"temperature": [29, 29, 29, 29, 29, 2, 23, 2, 5, 84, 2, 24, 2, 2, 2, 202, 202, 202, 202, 202], "pressure": [15, 20, 18, 17, 102, 14, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]})

visualization(df, warn, anomalies_dic)

anomal_points_dic, normal_points_dic, indexes_dic = visualization(df,warn, anomalies_dic)

print(anomal_points_dic)
print(normal_points_dic)
print(indexes_dic)
#print(warn["anomalies"])
#print(anomalies_dic["anomalies"])

#for anomaly in warn["anomalies"]:
    #print(anomaly["column"])

#for label in df.columns: 
    #print(label)