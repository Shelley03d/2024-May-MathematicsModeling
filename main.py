import pandas as pd

# 读取各园区典型日负荷数据
load_data = pd.read_excel('./data/attachment1.xlsx')
# 读取各园区典型日风光发电数据
solar_wind_data = pd.read_excel('./data/attachment2.xlsx')
# 读取12个月各园区典型日风光发电数据
monthly_solar_wind_data = pd.read_excel('./data/attachment3.xlsx')

