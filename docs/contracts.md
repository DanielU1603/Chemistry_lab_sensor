

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

#stuck_detector_detection()

## responsability: report if the lab sensor is stuck in a value and the same value is repeated on across different samples. This functions covers the edge case where the standard deviation is 0 and the mean is 0.

## input: a dataframe containing the columns with different variables (time, temperature, pressure anc co2 levels)

## anomaly detected output: a dictionary indicating that an anomaly was detected, the value detected, the column and the rows where the value is repeated.
## no anomalies detected output: a dictionary indicating the status of the analysis with a str showing "no anomalies detected" 


#visualization() 

## input: dictionary of anomalies detected, dictionary of stuck detector anomalies and standard deviation of values on each column. 
## output: a pie chart showing the percentage of anomalies per category on the dataframe, a dispersion plot showing the clusters of normal data compared to anomalie values

## output in case of error: 
## 1-There's missing a dictionary
## 2-There's missing a value inside a dictionary
## 3-There's no data to plot

#app.py
## this module decides if save_current hash in first exectution or ask user to update hash if a modification was detected