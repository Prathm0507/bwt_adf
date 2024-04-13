# Databricks notebook source
# MAGIC %md
# MAGIC Access ADLS From Databricks using Services Principle
# MAGIC

# COMMAND ----------

application_id="131859f1-802a-4560-b3a9-a74ff6b70ea7"
directory_id="5ffafbb8-4e4a-4712-840e-2504133575f0"
service_credential="HSJ8Q~DanydBcvoSHc61UqXVxYsYRIB2ry8gGcDw"

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.formulaonebwts.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.formulaonebwts.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.formulaonebwts.dfs.core.windows.net", application_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.formulaonebwts.dfs.core.windows.net", service_credential)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.formulaonebwts.dfs.core.windows.net", "https://login.microsoftonline.com/{directory_id}/oauth2/token")

# COMMAND ----------

dbutils.fs.ls("abfss://test@formulaonebwts.dfs.core.windows.net/input_data/")