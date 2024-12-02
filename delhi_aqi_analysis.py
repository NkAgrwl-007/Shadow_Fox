import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

# Main function
def main():
    # Load the dataset
    data_path = r'D:\Ml_lab\Air_Quality\delhiaqi.csv'  # Replace with your dataset path
    df = pd.read_csv(data_path)

    # Initial exploration
    print("Dataset Info:")
    print(df.info())
    print("\nFirst few rows of the dataset:")
    print(df.head())

    # Data cleaning
    print("\nCleaning data...")
    df = df.dropna()  # Drop missing values (adjust based on the dataset)
    df['date'] = pd.to_datetime(df['date'])  # Ensure 'date' is in datetime format

    # Exploratory Data Analysis
    print("\nPerforming exploratory data analysis...")

    # Key pollutants analysis
    analyze_pollutants(df)

    # Seasonal variations
    analyze_seasonal_variations(df)

    # Geographical and environmental factors (if applicable)
    if 'wind_speed' in df.columns:
        analyze_geographical_factors(df)

    print("\nAnalysis complete. Check the generated visualizations.")

# Function to analyze key pollutants
def analyze_pollutants(df):
    pollutants = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
    fig = go.Figure()

    for pollutant in pollutants:
        if pollutant in df.columns:
            fig.add_trace(go.Scatter(
                x=df['date'],
                y=df[pollutant],
                mode='lines+markers',
                name=pollutant,
                hovertemplate=f'<b>Date</b>: {{x}}<br><b>{pollutant} (µg/m³)</b>: {{y}}<extra></extra>'
            ))

    fig.update_layout(
        title='Trends of Major Pollutants Over Time',
        xaxis_title='Date',
        yaxis_title='Concentration (µg/m³)',
        legend_title='Pollutants',
        hovermode='x unified'
    )
    fig.show()

# Function to analyze seasonal variations
def analyze_seasonal_variations(df):
    df['month'] = df['date'].dt.month
    season_map = {12: 'Winter', 1: 'Winter', 2: 'Winter',
                  3: 'Spring', 4: 'Spring', 5: 'Spring',
                  6: 'Summer', 7: 'Summer', 8: 'Summer',
                  9: 'Monsoon', 10: 'Autumn', 11: 'Autumn'}
    df['season'] = df['month'].map(season_map)

    fig = px.box(df, x='season', y='AQI', color='season',
                 title='Seasonal Variations in AQI',
                 labels={'AQI': 'Air Quality Index', 'season': 'Season'},
                 category_orders={'season': ['Winter', 'Spring', 'Summer', 'Monsoon', 'Autumn']})
    fig.update_traces(hovertemplate='<b>Season</b>: %{x}<br><b>AQI</b>: %{y}<extra></extra>')
    fig.show()

# Function to analyze geographical and environmental factors
def analyze_geographical_factors(df):
    fig = px.scatter(df, x='wind_speed', y='AQI',
                     title='Impact of Wind Speed on AQI',
                     labels={'wind_speed': 'Wind Speed (km/h)', 'AQI': 'Air Quality Index'},
                     hover_data=['date'])
    fig.update_traces(marker=dict(size=10, opacity=0.6),
                      hovertemplate='<b>Wind Speed</b>: %{x} km/h<br><b>AQI</b>: %{y}<br><b>Date</b>: %{customdata[0]}<extra></extra>')
    fig.show()

# Execute the main function
if __name__ == "__main__":
    main()
