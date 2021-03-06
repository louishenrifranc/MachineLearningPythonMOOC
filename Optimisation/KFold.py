import numpy as np
import pandas as pd
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Meme exemple que Cancer.py
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases'
                 '/breast-cancer-wisconsin/wdbc.data', header=None)

X = df.loc[:, 2:].values
y = df.loc[:, 1].values
lb = LabelEncoder()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Possibilité de pipeliner plusieurs opérations sur les données dans
# une pipeline, 'scl', 'pca' sont
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)

pipe_lr = Pipeline([('scl', StandardScaler()),
                    ('clf', LogisticRegression(penalty='l2', random_state=0))])

# Methode des K fold cross
# Permet de tester notre modèle sur un nombre limité de données, en splittant notre ensemble de données de départ
# en 'cv' fold différents et en utilisant comme donnée de validation, chacu fold a tour de role... donc cv fois
# Implementer dans sklearn
scores = cross_val_score(estimator=pipe_lr, y=y_train, X=X_train, cv=10, n_jobs=1)
print(np.mean(scores), '+-', np.std(scores))
