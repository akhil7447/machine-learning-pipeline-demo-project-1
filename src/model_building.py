import numpy as np

import pandas as pd 

import pickle

import os 

from sklearn.ensemble import GradientBoostingClassifier

import yaml

params = yaml.safe_load(open('params.yaml'))['model_building']

# fetch the data from data/processed 

train_data = pd.read_csv('./data/features/train_bow.csv')

X_train = train_data.iloc[:,0:-1].values
y_train = train_data.iloc[:,-1].values


# define & train the gradiant boosting model 

clf = GradientBoostingClassifier(n_estimators=params['n_estimators'], learning_rate=params['learning_rate'])

clf.fit(X_train, y_train)

#save 

pickle.dump(clf, open('model.pkl','wb'))