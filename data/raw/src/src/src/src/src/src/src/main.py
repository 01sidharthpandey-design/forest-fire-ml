from src.preprocessing import load_data, preprocess
from src.feature_engineering import split_features_target
from src.model import train_model
from src.simulation import simulate_fire
from src.evaluation import evaluate_model
from src.utils import print_header

def main():
    print_header()

    df = load_data("data/raw/sample_data.csv")
    df = preprocess(df)

    X, y = split_features_target(df)

    model, X_test, y_test, preds = train_model(X, y)

    evaluate_model(y_test, preds)

    simulate_fire()

if __name__ == "__main__":
    main()
