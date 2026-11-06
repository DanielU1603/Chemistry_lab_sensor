from collections import Counter

import numpy as np
from matplotlib import pyplot as plt


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

def visualization(df, warn, anomalies_dic):

    categories = []
    elements  = []
    sizes = []
    

    indexes_dic = {"temperature": [], "pressure": [], "co2": []}
    anomal_points_dic = {"temperature": [], "pressure": [], "co2": []}
    normal_points_dic = {"temperature": [], "pressure": [], "co2": []}


    for constant_anomaly in warn["anomalies"]: 
        elements.append(constant_anomaly["column"])

    for statistical_anomaly in anomalies_dic["anomalies"]:
        elements.append(statistical_anomaly["column"])

    c = Counter(elements)
    print(f'these are the values inside the counter{c}')
    print(f'these are the counts for parameters: {c["temperature"]}')
    print(categories)

    colors = plt.colormaps['Dark2'].colors
    label_colors = []
    for i, label in enumerate(df.columns):
        
        if c[label] > 0:
            categories.append(label)
            sizes.append(c[label])
            label_colors.append(colors[i])

    plt.pie(
        sizes, 
        labels=categories, 
        colors=colors, 
        autopct="%1.1f%%", 
        shadow=True, 
        startangle=140
        )
    plt.show()


    for column in df.columns:

        for anomaly in warn["anomalies"]:
            if anomaly["column"] == column: 
                for index in range(anomaly["start_row"], anomaly["end_row"]):
                    indexes_dic[column].append(index)


        for anomaly in anomalies_dic["anomalies"]: 
            if anomaly["column"] == column: 
                indexes_dic[column].append(anomaly["row"])
         

        for i, sample in enumerate(df[column]):
 

            if column == "temperature":
                if i in indexes_dic[column]:
                    anomal_points_dic[column].append(sample)
   
                else:
                    normal_points_dic[column].append(sample)

            if column == "pressure":
                if i in indexes_dic[column]: 
                    anomal_points_dic[column].append(sample)
                else: 
                    normal_points_dic[column].append(sample)

            if column == "co2": 
                if i in indexes_dic[column]:
                    anomal_points_dic[column].append(sample)
                else:
                    normal_points_dic[column].append(sample)


    indexes_normal_points_dic = {"temperature": [], "pressure": [], "co2": []}
    indexes_anomal_points_dic = {"temperature": [], "pressure": [], "co2": []}
    
    for column in df.columns:

        
        indexes_normal_points_dic[column].append(
            np.zeros_like(normal_points_dic[column])
            )
        indexes_anomal_points_dic[column].append(
            np.ones_like(anomal_points_dic[column])
            )


    for column in df.columns: 

        plt.scatter(
            indexes_normal_points_dic[column], 
            normal_points_dic[column],
              color='blue', 
              marker='o', 
              label='normal points')
        plt.scatter(
            indexes_anomal_points_dic[column],
              anomal_points_dic[column],
                color='green', 
                marker='o', 
                label='anomal points') 
        
        print(f'this is a column value: {column}')
        plt.title(
            f'1-D scatter plot for normal vs anomal points in {column} variable'
            )
        plt.xticks([0,1], ['normal points', 'anomal points'])
        plt.xlabel('Indexes')
        plt.ylabel(f'{column} values')
        plt.show()
    return anomal_points_dic, normal_points_dic, indexes_dic