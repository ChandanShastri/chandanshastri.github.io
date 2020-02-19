from pyspark.sql import SparkSession
# from pyspark.sql import SQLContext
# from pyspark.conf import SparkConf
# from pyspark import SparkContext
from pyspark.sql.functions import input_file_name


#conf = SparkConf().setAppName('hello').setMaster('spark://SC-PC.localdomain:7077')
#sc = SparkContext(conf=conf)
#sc = SparkContext("local", "test")
spark  = SparkSession.builder.master("local").enableHiveSupport().getOrCreate()
sql = SQLContext(spark)

df = sql.read.parquet("hdfs://localhost:9000/test/database/")
names = df.select(input_file_name())
names.show()
d=input("WAIT")
#names.repartition(1).write.option("header", "true").csv("filename1.csv")

jdbcDF2 = spark.read.jdbc("jdbc:postgresql:dbserver", "schema.tablename",
          properties={"user": "username", "password": "password"})