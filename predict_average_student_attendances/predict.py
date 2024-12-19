import numpy as np
from sklearn.linear_model import LinearRegression

def predict_attendance(df):
    predictions = {}
    for year_group in df['year_group'].unique():
        year_data = df[df['year_group'] == year_group]
        X = year_data['week'].values.reshape(-1, 1)
        y = year_data['attendance'].values

        model = LinearRegression()
        model.fit(X, y)

        future_weeks = np.array([5, 6]).reshape(-1, 1)
        predicted = model.predict(future_weeks)

        predictions[year_group] = predicted
        print(f"Predicted attendance for Year {year_group}:")
        for week, pred in zip([5, 6], predicted):
            print(f"  Week {week}: {pred:.2f}%")
    return predictions