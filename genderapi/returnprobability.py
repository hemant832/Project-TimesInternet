import pickle
import numpy as np
with open('model_pickle','rb') as f:
	gender_predict=pickle.load(f)
def returnprobability(name):
	c=name
	d=[]
	t=len(c)-1
	b=np.zeros(4)
	if c[t] == 'a' or c[t] == 'e' or c[t] == 'i' or c[t] == 'o' or c[t] == 'u':
			b[0]=1
	else:
			b[0]=0
	b[1]=ord(c[t])
	b[2]=ord(c[t])+ord(c[t-1])
	b[3]=ord(c[t])+ord(c[t-1])+ord(c[t-2])
	d.append(b)
	a=gender_predict.predict_proba(d)[0]
	b=a[0]
	c=a[1]
	pr=max(b,c)
	return(pr)