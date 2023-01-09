
import pandas as pd

df = pd.read_csv('PDFMalware2022-shuffled.csv', low_memory=False)

# Let's say we want to split the data in 80:10:10 for train:valid:test dataset
train_size = 0.8
valid_size=0.1

train_index = int(len(df)*train_size)

# First we need to sort the dataset by the desired column 
# df.sort_values(by = 'saledate', ascending=True, inplace=True)

df_train = df[0:train_index]
df_rem = df[train_index:]

valid_index = int(len(df)*valid_size)

df_valid = df[train_index:train_index+valid_index]
df_test = df[train_index+valid_index:]

df_train.to_csv('train.csv',index=False)
df_test.to_csv('test.csv',index=False)
df_valid.to_csv('validate.csv',index=False)


# X_train, y_train = df_train.drop(columns='SalePrice').copy(), df_train['SalePrice'].copy()
# X_valid, y_valid = df_valid.drop(columns='SalePrice').copy(), df_valid['SalePrice'].copy()
# X_test, y_test = df_test.drop(columns='SalePrice').copy(), df_test['SalePrice'].copy()
        
# print(X_train.shape), print(y_train.shape)
# print(X_valid.shape), print(y_valid.shape)
# print(X_test.shape), print(y_test.shape)


# from sklearn.model_selection import train_test_split
# #split the data into train and test set
# train,test = train_test_split(data, test_size=0.30, random_state=0)
# #save the data
# train.to_csv('train.csv',index=False)
# test.to_csv('test.csv',index=False)