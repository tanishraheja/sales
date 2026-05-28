import pandas as pd
df = pd.read_csv('sales.csv',encoding='latin1')
#df=df.isnull().sum()
df.columns =df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df.columns = df.columns.str.replace('-','_')
df['discount_applied']=df['discount'].apply( lambda x: 'no' if x==0 else 'yes')
df['profit_gen']=df['profit'].apply( lambda x: 'no' if x<=0 else 'yes')
print(df.head())
from sqlalchemy import create_engine

engine = create_engine(
    'mysql+mysqlconnector://root:9183@localhost:3306/mydb'
)

df.to_sql(
    'sales',
    con=engine,
    if_exists='replace',
    index=False
)