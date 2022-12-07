import pandas as pd
import numpy as np

df_tlt = pd.read_csv('TLT.csv')
df_voo = pd.read_csv('VOO.csv')

# df_test=pd.read_excel('test.xlsx')
# df_test.to_csv('df_test_output.csv')

df=pd.DataFrame(data={'A':[3,4,'a'],
                      'B':['dafd',3,5]})

df_voo['Volume in thousands']=df_voo['Volume']/1000
df_voo['Open Close Difference']=df_voo['Open']-df_voo['Close']

# A 2002-2020    B 2005-2022
# Inner Join:2005-2020
# Outer Join:2002-2022

df_merge=df_voo.merge(df_tlt, how='inner',
             on='Date',suffixes=('_voo','_tlt'))

df_voo['effective_return']=df_voo['Adj Close']/df_voo['Adj Close'].shift(1)-1
print(df_voo)

df_voo['log_return']=np.log(df_voo['Adj Close']/df_voo['Adj Close'].shift(1))
print(df_voo)

df_voo['cumsum_log_return']=df_voo['log_return'].cumsum()
print(df_voo)
print(df_voo.loc[0,'Adj Close']*np.exp(df_voo.iloc[-1]['cumsum_log_return']))
pass