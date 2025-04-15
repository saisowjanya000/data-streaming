silver_df = spark.readStream.table("silver_table")

silver_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start() \
    .awaitTermination()
