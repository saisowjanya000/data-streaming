# 🔄 Real-Time Data Streaming with Databricks (Python)

This project demonstrates a scalable real-time data streaming pipeline built on **Azure Databricks** using **Apache Spark Structured Streaming** with **Python (PySpark)**. It ingests data from a streaming source, applies transformations, performs aggregations, and writes the results to a data sink for real-time analytics.


## 📦 Project Structure

```text
data-streaming/
<<<<<<< HEAD
│
=======
>>>>>>> ee9b8e1 (add config and notebook files)
├── notebooks/
│   ├── data_ingestion.py
│   ├── transformations.py
│   └── output_writer.py
├── configs/
│   └── config.json
├── requirements.txt
├── README.md
└── LICENSE
```


## 🚀 **Features**
- Ingest data from Kafka / Auto Loader / Azure Event Hubs  
- Parse and transform JSON or CSV data streams  
- Deduplicate and apply watermarking  
- Perform windowed aggregations  
- Write to Delta Lake / Azure Data Lake Storage (ADLS) / BigQuery  
- Monitor streaming queries in real-time  

---

## 🔧 Technologies Used

- **Databricks (Runtime: DBR 13+)**
- **Apache Spark Structured Streaming**
- **Python (PySpark)**
- **Delta Lake**
- **Kafka / Event Hubs / Auto Loader**
- **Azure Data Lake Storage / BigQuery / PostgreSQL**
- **Databricks Jobs & Triggers**

---

## 🧪 Setup Instructions

### 1. Clone the repository


bash
git clone https://github.com/saisowjanya000/data-streaming.git
cd data-streaming


### 2. Install requirements (for local dev or Databricks CLI)
bash
pip install -r requirements.txt

### 3. Import Notebooks into Databricks
Use the Databricks UI or CLI to import notebooks under /notebooks.


### 4. Set up Secrets and Configs

Store sensitive credentials (e.g., Kafka keys, storage access keys) using Databricks Secrets.
Edit configs/streaming_config.json to match your streaming environment


# ▶️ How to Run
  - 1. Open streaming_ingestion.py notebook in Databricks
  - 2. Configure paths and secrets (via widgets or JSON config)
  - 3. Start the stream using spark.readStream and trigger transformations
  - 4. Monitor query progress using streamingQuery.lastProgress

# 🛡️ Best Practices
  - Use checkpointing to ensure exactly-once semantics
  - Apply watermarking to handle late-arriving data
  - Use Auto Loader for schema evolution support
  - Monitor streaming query metrics in Spark UI


