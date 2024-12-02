import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm

# Function to plot correlation heatmap
def plot_correlation(df):
    correlation_matrix = df.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f',
                annot_kws={"size": 12}, cbar_kws={'label': 'Correlation Coefficient'})
    plt.title("Correlation Matrix of Pollutants", fontsize=16)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(rotation=0, fontsize=12)
    plt.tight_layout()
    plt.show()

# Function to decompose time series
def plot_time_series_decomposition(df):
    if 'AQI' not in df.columns or df['AQI'].isnull().all():
        print("AQI column is missing or contains only null values.")
        return

    df.set_index('date', inplace=True)
    decomposition = sm.tsa.seasonal_decompose(df['AQI'], model='additive', period=365)
    decomposition.plot()
    plt.suptitle('Time Series Decomposition of AQI', fontsize=16)
    plt.tight_layout()
    plt.show()

# Function to plot animated time series
def plot_animated_time_series(df):
    fig = px.line(df, x='date', y='AQI', animation_frame='date',
                  title="AQI Changes Over Time", 
                  labels={'AQI': 'Air Quality Index'})
    fig.update_layout(
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            buttons=[dict(label="Play", method="animate", args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True)]),
                     dict(label="Pause", method="animate", args=[None, dict(frame=dict(duration=0, redraw=False), mode="immediate")])])
        ]
    )
    fig.show()
