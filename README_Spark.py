Using Spark on Azure Hortonworks sandbox to load table to hive from hadoop and query: 

Link about setting up hortonworks sandbox: http://hortonworks.com/blog/hortonworks-sandbox-azure/
Link about using hive on apache spark: http://hortonworks.com/hadoop-tutorial/using-hive-with-orc-from-apache-spark/

# Log into hortonworks sandbox
ssh senkrish@senkrish.cloudapp.net

# Copy the txt file containing the data as comma separated values into the sandbox. From local box
> scp /home/Users/senkrish/Documents/college_data.txt senkrish@senkrish.cloudapp.net:/tmp/data

# Set spark home directory - I already set this in ~/.bashrc file. So no need to do this again. 
>export SPARK_HOME=/usr/hdp/2.3.2.0-2950/spark/

# Change to spark home directory 
> cd $SPARK_HOME

# Now put the csv file from local storage into hadoop file system (hdfs) 
> hadoop fs -put /tmp/data/college_data.txt /tmp/

# You can check if it is present in hadoop now by doing 
> hadoop fs -ls /tmp 

# Lets load the hive table from the /tmp/college_data.txt that we already loaded in hdfs 
> ./bin/spark-submit /home/senkrish/LoadHive.py 

# Now we will run the script to query from this hive table for the input parameters
> ./bin/spark-submit /home/senkrish/RecommendSchool.py --income 100000 --sat_score 1000 --can_afford 30000 --school_type pub
This will print the output along with other logs which indicate how the processing is done in a distributed fashion. 
