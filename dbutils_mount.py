# Databricks notebook source
# ADLS GEN2 STORAGE ACCCOUNT NAME
storage_accounr_name="practicesessionazur"

#ADLS GEN2 container name
container_name="adf-practice"

#ADLS GEN2 Directory path
Directory_path="databricks_workspace"

#ADLS GEN 2 key
adls_key="k0TXaYt3Yq+tjWtYe9Tp34zgexRsVW2RpMwvxkpd8x2BXb+g495inU2ofuESqRpEsS7b/2EPPvPN+ASt62oVyw=="

#mount point location
mount_point_location="/mnt/databricks_workspace"

#check if the mount point already exist
if not any (mount.mountPoint==mount_point_location for mount in dbutils.fs.mounts()):
    #mount the ADLS GEN2 storage
    dbutils.fs.mount(
        source=f"wasbs://{container_name}@{storage_accounr_name}.blob.core.windows.net/{Directory_path}",
        mount_point=mount_point_location,
        extra_configs={"fs.azure.account.key."+ storage_accounr_name + ".blob.core.windows.net":adls_key} 
        )
    print(f"Mount point '{mount_point_location}'created successfully.")

else:
    print("Mount point '{mount_point_location}' already exists.")


# COMMAND ----------

dbutils.fs.ls("/mnt")

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

display(dbutils.fs.ls("/mnt/databricks_workspace"))

# COMMAND ----------

dbutils.fs.help("unmount")

# COMMAND ----------

dbutils.fs.unmount("/mnt/databricks_workspace")

# COMMAND ----------

dbutils.fs.cp("/mnt/databricks_workspace/abc.txt.txt","/mnt/databricks_workspace/abc.txt.txt")

# COMMAND ----------

display(dbutils.fs.mounts()) 