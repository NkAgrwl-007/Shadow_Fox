import pandas as pd
import numpy as np
import plotly.graph_objects as go
from analysis import analyze_pollutants, analyze_seasonal_variations, analyze_geographical_factors
from preprocessing import preprocess_data
from predictive import forecast_aqi
from visualization import plot_correlation, plot_time_series_decomposition


# Function to create an animated time series plot with sliders
def plot_animated_time_series(df):
    # Ensure 'date' is in datetime format and sorted
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)

    # Create a unique list of dates and pollutant types for sliders
    unique_dates = df['date'].dt.date.unique()
    pollutant_types = ['PM2.5', 'PM10', 'NO2', 'SO2', 'O3', 'AQI']  # Adjust based on your dataset

    # Initial frame data
    initial_date = unique_dates[0]
    initial_pollutant = 'AQI'
    initial_data = df[df['date'].dt.date == initial_date]

    # Create a base figure
    fig = go.Figure()

    # Add traces for the initial frame
    fig.add_trace(go.Scatter(
        x=initial_data['longitude'],
        y=initial_data['latitude'],
        mode='markers',
        marker=dict(size=10, color=initial_data[initial_pollutant], colorscale='Viridis', showscale=True),
        name=f"{initial_pollutant} on {initial_date}"
    ))

    # Add frames for each date
    frames = [
        go.Frame(
            data=[
                go.Scatter(
                    x=df[df['date'].dt.date == date]['longitude'],
                    y=df[df['date'].dt.date == date]['latitude'],
                    mode='markers',
                    marker=dict(size=10, color=df[df['date'].dt.date == date][initial_pollutant], colorscale='Viridis')
                )
            ],
            name=str(date)
        )
        for date in unique_dates
    ]
    fig.frames = frames

    # Add horizontal slider for dates
    sliders = [
        dict(
            steps=[
                dict(
                    method='animate',
                    args=[[str(date)], dict(mode='immediate', frame=dict(duration=500, redraw=True), transition=dict(duration=0))],
                    label=str(date)
                )
                for date in unique_dates
            ],
            active=0,
            x=0.1,
            xanchor='left',
            y=0,
            yanchor='top'
        )
    ]

    # Add vertical dropdown for pollutants
    pollutant_dropdown = [
        dict(
            buttons=[
                dict(
                    label=pollutant,
                    method='update',
                    args=[
                        {
                            'marker.color': df[pollutant]
                        },
                        {
                            'title': f"{pollutant} Concentration"
                        }
                    ]
                )
                for pollutant in pollutant_types
            ],
            direction='down',
            showactive=True,
            x=1.15,
            xanchor='right',
            y=0.9,
            yanchor='top'
        )
    ]

    # Update layout with sliders and dropdown
    fig.update_layout(
        title="Animated AQI Time Series with Sliders",
        xaxis=dict(title="Longitude"),
        yaxis=dict(title="Latitude"),
        sliders=sliders,
        updatemenus=pollutant_dropdown
    )

    # Show the plot
    fig.show()


# Main function
def main():
    # Load and preprocess the dataset
    data_path = r'D:\Ml_lab\Air_Quality\delhiaqi.csv'  # Replace with your dataset path
    df = pd.read_csv(data_path)
    df = preprocess_data(df)  # Cleaning and preprocessing

    # Initial exploration
    print("Dataset Info:")
    print(df.info())
    print("\nFirst few rows of the dataset:")
    print(df.head())

    # Exploratory Data Analysis (EDA)
    print("\nPerforming exploratory data analysis...")

    # Key pollutants analysis
    analyze_pollutants(df)

    # Seasonal variations
    analyze_seasonal_variations(df)

    # Geographical and environmental factors
    if 'wind_speed' in df.columns:
        analyze_geographical_factors(df)

    # Correlation Heatmap
    plot_correlation(df)

    # Time Series Decomposition
    plot_time_series_decomposition(df)

    # Animated AQI plot
    plot_animated_time_series(df)

    # Forecasting AQI using Prophet
    forecast_aqi(df)

    print("\nAnalysis complete. Check the generated visualizations.")


# Execute the main function
if __name__ == "__main__":
    main()
