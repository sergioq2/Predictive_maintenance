import pandas as pd
from sklearn.metrics import accuracy_score
from main import prediction

def model_validation():
    validation = pd.read_csv('validation.csv')
    X = validation.drop(['Target'], axis=1)
    y = validation['Target']
    y_pred = X.apply(lambda x: prediction(X), axis=1)
    accuracy = accuracy_score(y, y_pred)
    print(accuracy)

if __name__ == '__main__':
    model_validation()