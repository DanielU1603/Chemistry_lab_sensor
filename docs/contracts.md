

#load_csv

responsability:
load the dataset, transform it from csv to dataframe and returns the dataframe

input:
csv

output:
dataframe


#data_validation

## responsability: validate if a column exists, validate if a value inside a column exists and  validate if the type of each sample is correct.

### input: dataframe

### output: dataframe

### if fails: returns error {type_error: missing_column}, {type_error: missing_sample} or {type_error: incorrect_value}

#integrity_check

## responsability: calculate hash and calculate with original hash if exist and was saved

## input: dataframe, original_hash.text
## correct output: dataframe and {status: "hash_match", current_hash: "", original_hash: ""}
## if hash are different: {status: "different_hash", original_hash: "", current: "hash"}
## if first execution: {status: "first_execution"}
## don't do: save hashes or print messages for the user


#save_hash()
## responsability: save hash of an individual file on a .txt file
# input: string with a hash
# output: .txt file with different hashes

#load_hash()

## responsability: load a hash previously stored in a .txt file
# input: .txt file with different hashes
# output: string containing the hash of a csv file

#anomaly_detection() 

## responsability: calculate standar deviation from a group of data and compares with individual samples in each columns
## input: a dataframe
## output: {anomaly detected: "", column: "", value: ""} or {no anomalies detected}


#visualization() 

#app.py
## this module decides if save_current hash in first exectution or ask user to update hash if a modification was detected