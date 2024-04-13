# Databricks notebook source
# MAGIC %md
# MAGIC Access ADLS From Databricks using SAS (Shared access signature)
# MAGIC

# COMMAND ----------

sas_token=r"sp=rl&st=2024-04-01T05:34:26Z&se=2024-04-02T13:34:26Z&spr=https&sv=2022-11-02&sr=c&sig=ZAV1kuGLstPGQ88A9xZ0WohUl4cc1GTkgLdC9VhS%2BYQ%3D"

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.formulaonebwts.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.formulaonebwts.dfs.core.windows.net", "org.apache.hadoop.fs. azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.formulaonebwts.dfs.core.windows.net", f"{sas_token}")

# COMMAND ----------

dbutils.fs.ls("abfss://test@formulaonebwts.dfs.core.windows.net/input_data/")