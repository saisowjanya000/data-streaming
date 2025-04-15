from pyspark.sql.functions import window, count

bronze_df = spark.readStream.table("bronze_table")

agg_df = bronze_df \
    .withWatermark("timestamp", "5 minutes") \
    .groupBy(window(col("timestamp"), "5 minutes")).agg(count("id").alias("event_count"))

agg_df.writeStream.format("delta").option("checkpointLocation", "/mnt/data/checkpoints/transform").table("silver_table")
