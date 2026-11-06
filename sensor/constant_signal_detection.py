def constant_signal_detection(df):

    columns = df.columns
    warn = {"status": "no anomalies detected"}
    anomalies = []

    for column in columns:
        index = []
        
        for i, (current_sample, next_sample) in enumerate(
                    zip(df[column], 
                    df[column].iloc[1:])
                    ):
                
                if current_sample == next_sample:
                    index.append(i)

                    if (i+1) == (len(df[column])-1):

                        if len(index) >= 4:
                            anomaly = {
                                "column": column, 
                                "start_row": index[0], 
                                "end_row": i+1, 
                                "value": df[column].iloc[index[0]]}
                            anomalies.append(anomaly)
                            warn = {"status":
                                    "end_row_anomaly",
                                    "anomalies": anomalies}
                            index.clear()
                        else:
                            index.clear()
                            
                if current_sample != next_sample:
                        
                    index.append(i)

                    if len(index) >= 4: 
                            anomaly = {"column": column, 
                                       "start_row": index[0], 
                                       "end_row": i, 
                                       "value": df[column].iloc[index[0]]}
                            anomalies.append(anomaly)
                            warn = {"status": "counter_stuck", 
                                    "anomalies": anomalies}
                            index.clear()

                    else:
                         index.clear()
          
    return warn 