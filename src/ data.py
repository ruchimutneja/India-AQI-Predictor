from pathlib import Path
import pandas as pd

COLUMNS = ['AQI', 'PM2.5', 'PM10', 'NO2', 'CO', 'O3']

def load_processed(path='data/processed/hyderabad_aqi.csv'):
    frame = pd.read_csv(Path(path), parse_dates=['Date'], index_col='Date')
    return frame.sort_index()[COLUMNS]