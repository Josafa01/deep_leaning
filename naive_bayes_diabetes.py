# -*- coding: utf-8 -*-
"""naive_bayes_diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P_mKRsT354RA2C8JiT2Cy8-XMN1l-_xK

#Base de dados retidado do kaggle

https://www.kaggle.com/uciml/pima-indians-diabetes-database

O codigo a seguir foi construito somente para demonstração de conhecimento sem nehum uso profissional.

The following code was created only to demonstrate knowledge without professional use.

El siguiente código fue creado solo para demostrar conocimiento sin uso profesional.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

data.head()

data.shape

data.isnull().values.any()

data

data.info()

data.describe()

sns.countplot(x = 'Outcome', data = data);

data.hist(figsize=(20,12));

sns.pairplot(data, hue = 'Outcome', 
             vars = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']);

sns.heatmap(data.corr(), annot = True);

X = data.iloc[:, 0:8].values

X

y = data.iloc[:, 8].values

y

#https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

#https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15)

#https://scikit-learn.org/stable/modules/naive_bayes.html
#https://www.datacamp.com/community/tutorials/naive-bayes-scikit-learn
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

prev = classifier.predict(X_test)
prev

prev = (prev > 0.5)

prev

from sklearn.metrics import confusion_matrix
y_train_pred = classifier.predict(X_train)
y_train_pred = (y_train_pred > 0.5)
cm = confusion_matrix(y_train, y_train_pred)
sns.heatmap(cm, annot=True);

cm

from sklearn.metrics import classification_report
print(classification_report(y_train_pred, y_train))

cm = confusion_matrix(y_test, prev)
sns.heatmap(cm, annot=True);

from sklearn.metrics import classification_report
print(classification_report(y_test, prev))