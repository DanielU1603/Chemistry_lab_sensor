import pandas as pd
import datetime
import hashlib 
from pathlib import Path 
#This function reads the file and transforms it to DataFrame type
#The module load_file is separeted from the rest of the program to allow modifications in the file extension
#without compromise the rest of the architecture. 
#This disattach the module from the rest of the program and makes mantainance easier
def load_csv(file):
    df = pd.read_csv(file)
    return df

data_types = {"temperature": (float, int), "pressure": (float, int), "co2": (float, int), "time": datetime.datetime}

def data_validation(dataframe):
   columns_found = set([column_name.lower() for column_name in df.columns])
   expected_columns = {"pressure", "temperature", "co2", "time"}
   missing_columns = expected_columns - columns_found

   if len(missing_columns) > 0:  
       error = {"error_type": "missing_columns", "missing_columns": list(missing_columns)}
       return error
    return dataframe

#detects missing value
    for column in df:
        for value in df[column]:
            if pd.isna(value): 
                error = {"error_type":"missing_value", "column":column, "row": value.index()}
                return error


#detects data type_error

    for column in df: 
        for index, value in enumerate(df[column]):

             if isinstance(value, data_types[column]):
                continue
             error = {"error_type": "data_type", "column": column, "row": index, "expected_type": data_types[column], "type_found": type(value)}
             return error 
             

#missing_value
#data_validation() access every column and the first error is detected in the order of columns. Not chronological. 
#this fits with the structure of error.

def integrity_check(file_path): 

    p = Path(file_path)
    if p.exists(): 
        with p.open() as f: 
            file_content = f.read()

            hash_object = hashlib.sha256() 
            current_hash = hash_object.update(file_content)
    
    if not(original_hash.exists()):
        integrity_report = {"hash_status": "first_execution", "current_hash":""}

    if current_hash != original_hash:
        integrity_report = {"hash_status": "hash_modified", "original_hash": "", "current_hash": ""}
        
    else: 
        integrity_report = {"hash_status": "hash_match", "original_hash": "", "current_hash": ""}

    return integrity_report 