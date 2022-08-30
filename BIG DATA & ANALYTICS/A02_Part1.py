# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# The knowledge a computer has of Python can be specified in 3 levels:
# (1) Prelude knowledge --> The computer has it by default.
# (2) Borrowed knowledge --> The computer gets this knowledge from 3rd party libraries defined by others
#                            (but imported by us in this program).
# (3) Generated knowledge --> The computer gets this knowledge from the new functions defined by us in this program.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer first processes this PYTHON PROGRAM DEFINITION section of the file.
# On it, our computer enhances its Python knowledge from levels (2) and (3) with the imports and new functions
# defined in the program. However, it still does not execute anything.
#
# --------------------------------------------------------

# ------------------------------------------
# IMPORTS
# ------------------------------------------
import pyspark

# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line):
    # 1. We create the output variable
    res = ()

    # 2. We remove the end of line character
    line = line.replace("\n", "")

    # 3. We split the line by tabulator characters
    params = line.split(";")

    # 4. We assign res
    if (len(params) == 7):
        res = tuple(params)

    # 5. We return res
    return res

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(sc, my_dataset_dir):
  
    # Store the content of the dataset into an RDD
    inputRDD = sc.textFile(my_dataset_dir)
    
    # Process each line of dataset to tuples
    allLinesRDD = inputRDD.map(process_line)
    
    # Filter all lines to retrieve on times where the status = 0 and bikes available = 0
    filterRDD = allLinesRDD.filter(lambda x: x[0] == '0' and  x[5] == '0')
    
    # Mapped each station name with a value of 1 for each row
    mapByKey = filterRDD.map(lambda x: (x[1], 1))
    
    # Combined each keys and their values to get 1 key and value for each station
    combineKeys = mapByKey.reduceByKey(lambda x, y: x + y)
    
    # Sorted by the number of run outs decreasing
    sortByValue = combineKeys.sortBy(lambda x:x[1]  * (-1))
    
    # Returns the entire content of inputRDD into a list
    resVAL = sortByValue.collect()

    # We print by the screen the collection computed in resVAL
    for item in resVAL:
        print(item)

# --------------------------------------------------------
#
# PYTHON PROGRAM EXECUTION
#
# Once our computer has finished processing the PYTHON PROGRAM DEFINITION section its knowledge is set.
# Now its time to apply this knowledge.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer finally processes this PYTHON PROGRAM EXECUTION section, which:
# (i) Specifies the function F to be executed.
# (ii) Define any input parameter such this function F has to be called with.
#
# --------------------------------------------------------
if __name__ == '__main__':
    # 1. We use as many input arguments as needed
    pass

    # 2. Local or Databricks
    local_False_databricks_True = True

    # 3. We set the path to my_dataset
    my_local_path = "/home/nacho/CIT/Tools/MyCode/Spark/"
    my_databricks_path = "/"

    my_dataset_dir = "FileStore/tables/3_Assignment/my_dataset/"

    if local_False_databricks_True == False:
        my_dataset_dir = my_local_path + my_dataset_dir
    else:
        my_dataset_dir = my_databricks_path + my_dataset_dir

    # 4. We configure the Spark Context
    sc = pyspark.SparkContext.getOrCreate()
    sc.setLogLevel('WARN')
    print("\n\n\n")

    # 5. We call to our main function
    my_main(sc, my_dataset_dir)