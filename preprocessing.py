import pandas as pd

def preprocess_data(df):
    # Drop missing values
    df = df.dropna()  
    
    # Convert 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'])
    
    # Add month and season columns
    df['month'] = df['date'].dt.month
    season_map = {12: 'Winter', 1: 'Winter', 2: 'Winter',
                  3: 'Spring', 4: 'Spring', 5: 'Spring',
                  6: 'Summer', 7: 'Summer', 8: 'Summer',
                  9: 'Monsoon', 10: 'Autumn', 11: 'Autumn'}
    df['season'] = df['month'].map(season_map)
    
    return df
