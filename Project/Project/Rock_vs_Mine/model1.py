import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv("C:/Users/adars/Desktop/Project/Rock_vs_Mine/dataset/sonar_data.csv",header=None)

data.groupby(60).mean()
x = data.drop(60,axis=1)
y = data[60]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x,y)

joblib.dump(knn,'r_vs_m_model')
knn1 = KNeighborsClassifier(n_neighbors=3)
knn1.fit(x_train,y_train)
y_pred2 = knn1.predict(x_test)
acc = accuracy_score(y_test,y_pred2)
print()
print("Model Created With Accuracy : ",int(acc*100),"%\n")
