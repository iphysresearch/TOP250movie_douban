import numpy as np
from sklearn.model_selection import train_test_split

#创建一个数据集X和相应的标签y,X中样本数目为100
X, y = np.arange(200).reshape((100, 2)), range(100)
print(X)
print('=====')
print(y)
#用train_test_split函数划分出训练集和测试集，测试集占比0.33
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33, random_state=42)

#打印出原始样本集、训练集和测试集的数目
print('打印出原始样本集、训练集和测试集的数目')
print("The length of original data X is:", X.shape[0])
print("The length of train Data is:", X_train)
print("The length of test Data is:", X_test)
print("The length of y_train Data is:", y_train)