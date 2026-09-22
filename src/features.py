import pandas as pd
POLLUTANTS = ['PM2.5', 'PM10', 'NO2', 'CO', 'O3']

def create_features(data: pd.DataFrame) -> pd.DataFrame:

    x = data.copy().sort_index()
    x['month'] = x.index.month
    x['day_of_week'] = x.index.dayofweek

    x['is_weekend'] = (x['day_of_week'] >= 5).astype(int)
    for lag in [1, 2, 3, 7, 14]:
        x[f'aqi_lag_{lag}'] = x['AQI'].shift(lag)
        x['aqi_3day_mean'] = x['AQI'].shift(1).rolling(3).mean()
        x['aqi_7day_mean'] = x['AQI'].shift(1).rolling(7).mean()
        x['aqi_7day_std'] = x['AQI'].shift(1).rolling(7).std()

    for pollutant in POLLUTANTS:
        x[f'{pollutant}_lag_1'] = x[pollutant].shift(1)
        x['tomorrow_aqi'] = x['AQI'].shift(-1)
        
    return x.dropna()

def aqi_category(aqi: float) -> str:
    if aqi <= 50: return 'Good'
    if aqi <= 100: return 'Satisfactory'
    if aqi <= 200: return 'Moderate'
    if aqi <= 300: return 'Poor'
    if aqi <= 400: return 'Very Poor'
    return 'Severe'