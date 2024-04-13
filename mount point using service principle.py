# Databricks notebook source
dbutils.secrets.list("bwt session")

# COMMAND ----------

application_id=dbutils.secrets.get("bwt session","kv-formulaone-application-id")
directory_id=dbutils.secrets.get("bwt session","kv-bwtformulaone-directory-id")
service_credential=dbutils.secrets.get("bwt session","kv-bwtformulaone-service-credential")

# COMMAND ----------

dbutils.fs.unmount("/mnt/test")

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
       "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
       "fs.azure.account.oauth2.client.id": application_id, 
       "fs.azure.account.oauth2.client.secret": service_credential, 
       "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{directory_id}/oauth2/v2.0/token", 
       "fs.azure.createRemoteFileSystemDuringInitialization": "true"}

dbutils.fs.mount(
source = "abfss://test@formulaonebwts.dfs.core.windows.net/", 
mount_point = "/mnt/test",
extra_configs = configs)

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

display(dbutils.fs.ls("/mnt/test"))