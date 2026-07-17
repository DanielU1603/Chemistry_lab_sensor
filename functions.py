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

def save_hash(hash):
    with open("hash_file.txt", "w") as f: 
        f = f.write(hash)

def integrity_check(file_path, hash_file="hash_file.txt"): 

    p = Path(file_path)
    if p.exists(): 
        with p.open("rb") as f: 
            digest = hashlib.file_digest(f, "sha256")
            current_hash = digest.hexdigest()
    else: 
        integrity_report = {"error_type": "path file not found", "path": file_path}
        return integrity_report
    
    if hash_file.exists():

        with open(hash_file) as f:
            for original_hash in f:
    

             if current_hash != original_hash:
                integrity_report = {"hash_status": "hash_modified", "original_hash": original_hash, "current_hash": current_hash}
                continue
             else: 
                integrity_report = {"hash_status": "hash_match", "original_hash": original_hash, "current_hash": current_hash}

            return integrity_report 
    
    else: 
        integrity_report = {"hash_status": "first_execution", "current_hash": current_hash}
        save_hash(current_hash)
        return integrity_report
