import pandas as pd
import datetime


# Assume you have a DataFrame
df 

# example of list of date（in Japanese）
date_list = ['2月14日', '2月19日', '2月20日', '3月21日', '3月23日', '3月24日', '3月26日', '3月28日', '3月29日', '4月10日', '4月11日']

# ↑ or
# date_list = df['date].tolist()


date_list_filled = []

for date in date_list:
	#if you want it 2020
	d_str = '2020年' + date
	d_date = datetime.datetime.strptime(d_str, '%Y年%m月%d日')
	date_list_filled.append(d_date)
	
	
# to reindex pandas  DataFrame
value_list = df["value1"].tolist()
idx = pd.date_range('2020-02-14', '2020-04-15')

new_df = pd.DataFrame(value_list, index=date_list_filled)
# or Series ver.
# new_series = pd.Series(value_list, index=date_list_filled)

new_df.reindex(idx, fill_value=0)

