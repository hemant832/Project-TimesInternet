from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression 
import matplotlib.pyplot as plt
import pickle
#bc = datasets.load_breast_cancer()
#X, y = bc.data, bc.target

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
sm=svm.SVC(gamma=.001,C=100,probability=True)
#lr =LogisticRegression()
#sm.fit(X_train,y_train)
Y=[]
vowel=[]
df=pd.read_csv('h.csv')
for i in range(len(df)):
	#n=np.zeros(676)
	a=df['name'][i]
	a=a.lower()
	k=len(a)-1
	v=np.zeros(4)
	if a[k] == 'a' or a[k] == 'e' or a[k] == 'i' or a[k] == 'o' or a[k] == 'u':
			v[0]=1
	else:
			v[0]=0
	v[1]=ord(a[k])
	v[2]=ord(a[k])+ord(a[k-1])
	v[3]=ord(a[k])+ord(a[k-1])+ord(a[k-2])
	vowel.append(v)		
	#lfor j in range(len(a)-1):
	#	m=(ord(a[j])-96)*(ord(a[j+1])-96)
	#	m=m-1
	#	n[m]=1	
	#X.append(n)	
	if df['gender'][i] == 'M':
		Y.append(1)
	else:
		Y.append(0)	
#print(X)
X_train, X_test, y_train, y_test = train_test_split(vowel, Y, test_size=0.2, random_state=1)
sm.fit(X_train,y_train)
#regressor.fit(X,Y)
#print(lr.predict(X_test))
#print(sm.score(X_test,y_test))
with open('model_pickle','wb') as f:
	pickle.dump(sm,f)
#with open('model_pickle','wb') as f:
#	pickle.dump(sm,f)
#with open('model_pickle','rb') as f:
#	hemant=pickle.load(f)
