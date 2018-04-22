import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
df_train=pd.read_csv ('G:/kaggle/DriverPrediction/train.csv',
                      nrows=10
                      )
le=LabelEncoder ()

column_name=df_train.columns.values.tolist()
feature_column_name=column_name[2:]
for i in feature_column_name :
    for j in feature_column_name :
        if i!=j:
            new_columns='%s+%s'%(i,j)
            df_train[new_columns]=df_train[i].astype(str)+'_'+df_train[j].astype(str)
            df_train[new_columns]=le.fit_transform(df_train[new_columns].values )


print(df_train.head(1) )