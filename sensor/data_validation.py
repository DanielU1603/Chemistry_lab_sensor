import datetime

import pandas as pd

data_types = {
    "temperature": (float, int), 
    "pressure": (float, int), 
    "co2": (float, int), 
    "time": datetime.datetime
    }

def data_validation(df):
   
   columns_found = {column_name.lower() for column_name in df.columns}
   expected_columns = {"pressure", "temperature", "co2", "time"}
   missing_columns = expected_columns - columns_found
   data_type_errors = {}
   missing_value_errors = {}

   if len(missing_columns) > 0:  
       missing_column_error = {
           "error_type": "missing_columns",
             "missing_columns": list(missing_columns)
             }
       return missing_column_error
   


   for column in df:
        for value in df[column]:
            if pd.isna(value):
                missing_value_error = {"error_type":"missing_value",
                                        "column":column, "row": value.index()}
                missing_value_errors.append(missing_value_error)
                return missing_value_errors




   for column in df: 
        for index, value in enumerate(df[column]):

             if isinstance(value, data_types[column]):
                continue
             data_type_error = {
                 "error_type": 
                "data_type", 
                "column": column, 
                "row": index, 
                "expected_type": data_types[column], 
                "type_found": type(value)}
             data_type_errors.append(data_type_error)
             return data_type_errors
             
   return df 
