import pandas as pd
import datetime


# Assume you have a DataFrame
df 



# select df by partial string match
df_target = df[df["target-col"].str.contains("target-string")]



# find duplicated rows from dataframe（if two rows are completely the same, the onlt latter one will be Tru）
df_dup = df[df.duplicated()]

# In Case, you want both rows to be True if twi rows are the same.
df_dup = df[df.duplicated(keep=False)]


# find duplicated rows on specific columns
df_dup = df[df.duplicated(subset=["target-col"])]

