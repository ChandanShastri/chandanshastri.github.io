from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.conf import SparkConf
from pyspark import SparkContext
from pyspark.sql.functions import input_file_name

#sc = SparkContext("local", "test")
spark  = SparkSession.builder.master("local").enableHiveSupport().getOrCreate()
sql = SQLContext(spark)

df = sql.read.parquet("hdfs://localhost:9000/test/database/")
names = df.select(input_file_name())
names.show()
#names.repartition(1).write.option("header", "true").csv("filename1.csv")