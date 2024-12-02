import plotly.graph_objects as go
import plotly.express as px

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
