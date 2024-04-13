# Databricks notebook source
# MAGIC %sql
# MAGIC create database  bwtsession

# COMMAND ----------

# MAGIC %sql
# MAGIC describe database bwtsession

# COMMAND ----------

# MAGIC %sql
# MAGIC create database bwtsession_external location '/mnt/databricks_workspace'

# COMMAND ----------

# MAGIC %sql
# MAGIC desc database bwtsession_external