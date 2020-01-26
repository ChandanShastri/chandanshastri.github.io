from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.conf import SparkConf
from pyspark import SparkContext
from pyspark.sql.functions import input_file_name

#sc = SparkContext("local", "test")
#spark  = SparkSession.builder.master("local").enableHiveSupport().getOrCreate()
sc = SparkSession.builder.getOrCreate()
gg = SparkContext(sc)
sql = SQLContext(gg)

df = sql.read.parquet("hdfs://localhost:9000/test/database/")
names = df.select(inputFileName())
names.show()
#names.repartition(1).write.option("header", "true").csv("filename1.csv")