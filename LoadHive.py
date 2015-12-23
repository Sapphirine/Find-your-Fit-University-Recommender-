# sc is an existing SparkContext.
from pyspark.sql import HiveContext
from pyspark import SparkContext

sc = SparkContext("local", "Simple App")
sqlContext = HiveContext(sc)


sqlContext.sql("DROP TABLE IF EXISTS src")
sqlContext.sql("DROP TABLE IF EXISTS school_admit_data")
sqlContext.sql("CREATE TABLE IF NOT EXISTS school_admit_data (inst_id INT, inst_name STRING, sat_avg_all INT, adm_rate_all FLOAT, npt41_pub INT, npt42_pub INT, npt43_pub INT, npt44_pub INT, npt45_pub INT, npt41_priv INT, npt42_priv INT, npt43_priv INT, npt44_priv INT, npt45_priv INT, sat_avg_dummy INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ','")
sqlContext.sql("LOAD DATA INPATH '/tmp/college_data.txt' INTO TABLE school_admit_data")

print "Completed loading hive table school_admit_data from hdfs file path : /tmp/college_data.txt"

