from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder.appName("WordCountExample").getOrCreate()

# Sample data
data = [
    ("Hello world",),
    ("Hello Airflow",),
    ("Hello PySpark",)
]

# Create DataFrame
df = spark.createDataFrame(data, ["text"])

# Split words and count
from pyspark.sql.functions import explode, split, col

words_df = df.select(explode(split(col("text"), " ")).alias("word"))
word_count = words_df.groupBy("word").count()

# Show result
word_count.show()

# Stop Spark
spark.stop()
