import joblib
import pandas as pd
import json

encoder_url = 'files/encoder.pkl'
scaler_url = 'files/scaler.pkl'

encoder = joblib.load(encoder_url)
scaler = joblib.load(scaler_url)
categorical = encoder.feature_names_in_

def feature_preprocess(df):
    encoded_df = pd.DataFrame(
        encoder.transform(df[categorical]),
        columns=encoder.get_feature_names_out(categorical)
    )
    df = pd.concat([df.drop(categorical, axis=1), encoded_df], axis=1)

    scaled_df = pd.DataFrame(
        scaler.transform(df),
        columns=df.columns
    )
    return scaled_df

def FeatureEngineering(json_data):
    try:
        data = json.loads(json_data)
        df = pd.DataFrame(data, index=[0])
        df = feature_preprocess(df)
    except:
        df = feature_preprocess(json_data)
    return df

if __name__ == '__main__':
    FeatureEngineering()