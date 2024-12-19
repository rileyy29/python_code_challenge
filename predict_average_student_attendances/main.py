from chart import generate_line_chart
from data import mock_data, parse_data
from predict import predict_attendance

def predict():
    data = mock_data()
    df = parse_data(data)
    
    predictions = predict_attendance(df)
    generate_line_chart(df, predictions)

predict()
