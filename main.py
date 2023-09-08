import joblib
from features import FeatureEngineering

model = joblib.load('files/model.pkl')

def prediction(value):
    df = FeatureEngineering(value)
    prediction_result = model.predict(df)[0]
    return prediction_result

if __name__ == '__main__':
    prediction()