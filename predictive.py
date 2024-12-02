from prophet import Prophet
import plotly.graph_objects as go

def forecast_aqi(df):
    df_prophet = df[['date', 'AQI']].rename(columns={'date': 'ds', 'AQI': 'y'})
    model = Prophet(daily_seasonality=True)
    model.fit(df_prophet)
    future = model.make_future_dataframe(df_prophet, periods=365)
    forecast = model.predict(future)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Predicted AQI'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], fill='tonexty', mode='lines', name='Lower Confidence Interval'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], fill='tonexty', mode='lines', name='Upper Confidence Interval'))
    
    fig.update_layout(title="AQI Forecast with Prophet", xaxis_title="Date", yaxis_title="Predicted AQI")
    fig.show()

