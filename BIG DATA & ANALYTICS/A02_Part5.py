# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(my_input_stream, my_output_stream, my_mapper_input_parameters):
    # 1. We unpack my_mapper_input_parameters
    pass
 
    # 2. This will store results in format [Wikipedia_English, Olympic Games, 211] in a 2D array
    array = []
    
    # 3. We traverse the lines of the file
    for line in my_input_stream:
        # Split line into columns 
        columns = process_line(line)
        
        # Extract data from columns
        wikimedia_project = columns[0]
        webpage_name = columns[1]
        language = columns[2]
        num_views = columns[3]
        
        # Create new name for wiki type and language
        new_type = wikimedia_project + "_" + language
        
        # Append to the array in form of [Wikipedia_English, Olympic Games, 211]
        array.append([new_type, webpage_name, num_views])
        
      # 4. We traverse the index's of the array
      for row in array:
          my_str = row[0] + "\t" + "(" + row[1] + "," + str(row[2]) + ")" + "\n"
          my_output_stream.write(my_str)
        
      
# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    # 1. We unpack my_mapper_input_parameters
    pass
  
    # 2. Dictionary to the most views per project and language type
    dictionary = dict()
    
    # 3. We traverse the lines of the file
    for line in my_input_stream:
        # Extracting the columns from the line
        (key, value) = get_key_value(line)
        
        # Since the value holds two variables seperated by a comma, split them
        webpage_name, num_views = value.split(",")
        
        # ** If the key is not in the dictionary **
        if key not in dictionary:
            # Add key with values to dictionary
            dictionary[key] = [webpage_name, num_views]
        
        # ** If key (Wikipedia_English) is in the dictionary **
        elif key in dictionary:
            # Get stored project's num views for that key (Wikipedia_English)
            stored_projects_views = dictionary[key][1]
            
            # If the current itterations num views is greather than whats stored in the dictionary
            if num_views > stored_projects_views:
                # Update dictionary for that key (Wikipedia_English)
                dictionary[key] = [webpage_name, num_views]
            
            
    # 4. For each key, value in the dictionary
    for key, value in dictionary.items():
        # Since the value holds two variables in a list, extract them
        webpage_name = value[0]
        num_views = value[1]
        
        # Create a string with the number of times the station had no bikes at that hour
        my_str = key + "\t" +  "(" + webpage_name + ", " + str(num_views) + ")" + "\n"
        
        # Write result to file
        my_output_stream.write(my_str)
    
    
# ------------------------------------------
# FUNCTION my_spark_core_model
# ------------------------------------------
def my_spark_core_model(sc, my_dataset_dir):
    # Store the content of the dataset into an RDD
    inputRDD = sc.textFile(my_dataset_dir)
    
    # Process each line of dataset to tuples
    allLinesRDD = inputRDD.map(process_line)
    
    # Mapped each dayOfWeek_hour value (Saturday_15) with 1
    mapByKey = filterRDD.map(lambda x: (x[0] + "_" + x[2], x[1],x[3]))
    
    # Map it to key, value so that web page name and views are in a list
    listRDD = mapByKey.map(lambda x: (x[0], list(x[1:])))

    # Reduce while checking for the largest project_language biggest projects page views
    resultRDD = listRDD.reduceByKey(lambda x, y: x if x[1] > y[1] else y)
    
    # Collect results
    resVAL = resultRDD.collect()
    
    # Print Results
    for item in resVAL:
        print(item)
        
# ------------------------------------------
# FUNCTION my_spark_streaming_model
# ------------------------------------------
def my_spark_streaming_model(ssc, monitoring_dir):
    # Operation C1: textFileStream
    inputDStream = ssc.textFileStream(monitoring_dir)
    
    # Processing line
    allLinesRDD = inputDStream.map(process_line)
    
    # Mapped each dayOfWeek_hour value (Saturday_15) with 1
    mapByKey = filterRDD.map(lambda x: (x[0] + "_" + x[2], x[1],x[3]))
    
    # Map it to key, value so that web page name and views are in a list
    listRDD = mapByKey.map(lambda x: (x[0], list(x[1:])))
    
    # Reduce while checking for the largest project_language biggest projects page views
    resultRDD = listRDD.reduceByKey(lambda x, y: x if x[1] > y[1] else y)
    
    # UpdateStateByKey, to get the newest results
    solutionDStream = combineKeys.updateStateByKey(my_state_update)
    
    # Persist
    solutionDStream.persist(pyspark.StorageLevel.MEMORY_AND_DISK)
    
    # Print results
    solutionDStream.pprint()
    