import pandas as pd

#This function reads the file and transforms it to DataFrame type
#The module load_file is separeted from the rest of the program to allow modifications in the file extension
#without compromise the rest of the architecture. 
#This disattach the module from the rest of the program and makes mantainance easier
def load_csv(file):
    df = pd.read_csv(file)
    return df


def data_validation(dataframe):
   columns_found = set([column_name.lower() for column_name in df.columns])
   expected_columns = {"pressure", "temperature", "co2", "time"}
   missing_columns = expected_columns - columns_found

   if len(missing_columns) > 0:  
       error = {"error_type": "missing_columns", "missing_columns": list(missing_columns)}
       return error
    return dataframe

#detects missing value

for k in df:
   for v in df[k]:
       if pd.isna(v): 
           error = {"error_type":"missing_value"; "column":k; "row": v.index()}
           return error

data_types = {"temperature": "float", "presure": "float", "co": "float", "time": "date"}

#detects data type_error
for k in df:
    for i,v in enumerate(df[k]):
        if type(v) != data_type[k]:
            error = {"error_type": "data_type", "column": k, "expected_type": data_type[k], "type_found": data_type(v)}
            return error


#missing_value
#data_validation() access every column and the first error is detected in the order of columns. Not chronological. 
#this fits with the structure of error.

error = {"error_type": "missing_value", "column": "", "row": ""}  

#data_type

error = {"error_type":"invalid_type"; "column": "", "row": "", "input_type":"", "expected_type":""}

def integrity_check(): 

    integrity_report = {"integrity_check": "hash_modified", "original_hash": "", "current_hash": ""}