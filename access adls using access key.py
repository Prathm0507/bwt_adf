# Databricks notebook source
# MAGIC %md
# MAGIC Access ADLS From Databricks using access key
# MAGIC

# COMMAND ----------

access_key=dbutils.secrets.get("bwt session","kv-formulaone-access-key")

# COMMAND ----------

spark.conf.set("fs.azure.account.key.formulaonebwts.dfs.core.windows.net",access_key)

# COMMAND ----------

display(dbutils.fs.ls("abfss://test@formulaonebwts.dfs.core.windows.net/input_data/"))

# COMMAND ----------

df=spark.read.csv ("abfss://test@formulaonebwts.dfs.core.windows.net/input_data/customer table.csv",header=True)
df.display()

# COMMAND ----------



# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.help("listscopes")

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list("bwt session")

# COMMAND ----------

dbutils.secrets.get("bwt session","kv-formulaone-access-key")