import numpy as np


def anomaly_detection(df, sigma): 

    anomalies_dic = {"status": "no anomalies detected"}
    anomalies = []

    for column in df.columns: 
      threshold =  np.std(df[column])*sigma
      avg = np.mean(df[column])

      for i,sample in enumerate(df[column]):
          if abs(sample - avg) > threshold:
        
              anomaly = {"column": column, "value": sample, "row": i}
              anomalies.append(anomaly)
              
    if len(anomalies) > 0:
        anomalies_dic = {
            "status":"anomalies_detected", 
            "anomalies": anomalies}
    
    return anomalies_dic