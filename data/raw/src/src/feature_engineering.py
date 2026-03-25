def split_features_target(df):
    X = df.drop("fire_risk", axis=1)
    y = df["fire_risk"]
    return X, y
