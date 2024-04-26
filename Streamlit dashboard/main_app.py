import streamlit as st
import pandas as pd 
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt 
import altair as alt
import requests
from bs4 import BeautifulSoup
from forecast_model import Preprocessor, PricePredictor


st.set_page_config(page_title = "Real-Time Data Dashboard", layout = "wide")
st.sidebar.header('Dashboard `version 1`')

df = pd.read_csv("D:\SETA\ENERGY\streamlit\data\ISEM_scraped_historical_data_raw.csv")
df["Time Start (WET)"] = pd.to_datetime(df["Time Start (WET)"])


# Price Metric + bar chart
latest = df.iloc[-1]
prev = df.iloc[-2]
time = latest["Time Start (WET)"]
st.title(f"ENERGY DASHBOARD :red[{time}]")
col1_1, col1_2= st.columns(2)
current_price = latest["DA Prices-IRELAND (IE) [EUR/MWh]"]
price_delta = current_price - prev["DA Prices-IRELAND (IE) [EUR/MWh]"]

col1_1_1, col1_1_2, temp = col1_1.columns((2, 1.5, 1))
col1_1_1.metric("Electricity Price: ", f"{current_price} EUR/MWh", f"{price_delta}")

last_10_price = np.array(df[-10:]["DA Prices-IRELAND (IE) [EUR/MWh]"].values)
chart_data = pd.DataFrame()
chart_data["a"] = range(10)
chart_data["b"] = last_10_price
c = (
    alt.Chart(chart_data)
    .mark_bar()
    .encode(x=alt.X("a", axis=None), y=alt.Y("b", axis=None))).properties(
    width=150,
    height=100
    )
col1_1_2.altair_chart(c)

# Demand Metric + bar chart
col1_2_1, col1_2_2, temp = col1_2.columns((1.5, 1.5, 2))
current_demand = latest["DEMAND SUMMARY-ACTUAL TOTAL LOAD [MW]"]
demand_delta = current_demand - prev["DEMAND SUMMARY-ACTUAL TOTAL LOAD [MW]"]
col1_2_1.metric("Demand: ", f"{current_demand} MW", demand_delta)
last_10_demand = np.array(df[-10:]["DEMAND SUMMARY-ACTUAL TOTAL LOAD [MW]"].values)
chart_data = pd.DataFrame()
chart_data["a"] = range(10)
chart_data["b"] = last_10_demand
c = (
    alt.Chart(chart_data)
    .mark_bar()
    .encode(x=alt.X("a", axis=None), y=alt.Y("b", axis=None))).properties(
    width=150,
    height=100
    )
col1_2_2.altair_chart(c)

st.header("Price analysis")
col2_1, col2_2 = st.columns(2)
latest_48h = df.iloc[-48:]
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=latest_48h["Time Start (WET)"], y=latest_48h["DA Prices-IRELAND (IE) [EUR/MWh]"], name='Price [EUR/MWh]',
                        line=dict(color='blue', width=4)))
fig1.update_layout(title_text="Last 24h Electricity price", xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False), yaxis_title="EUR/MWh")
col2_1.plotly_chart(fig1)
col2_2.subheader("Related news (From the Independent.ie)")
keyword = col2_2.text_input("Search key: ")
def crawl_independent(keyword = 'ireland energy'):
    url = 'https://www.independent.ie/search'
    params = {
        'keyword': keyword,
    }
    response = requests.get(url, params=params).content
    soup = BeautifulSoup(response, 'html.parser')
    time = [i.text for i in soup.find_all("time")]
    links = [i["data-vr-contentbox-url"] for i in soup.find_all("a", {"data-testid": "article-teaser"})]
    article = [i.text for i in soup.find_all("h6")]
    topic = [i.text for i in soup.find_all("span", {"class": "indo-17abbc75_root indo-17abbc75_caption1 indo-ea190c2_secondary indo-bcee7b1d_displayinlineblock indo-d382f4d9_marginright2"})]
    return (time, links, article, topic)
if keyword:
    time, links, article, topic = crawl_independent(keyword)
else: 
    time, links, article, topic = crawl_independent()
for i in range(5):
    col2_2.write(f":blue[{time[i]}] |:green[\[{topic[i]}\]] {article[i]} [Link]({links[i]})")
st.header("Supply and demand analysis")
# Generation summary pie chart
col3_1, col3_2 = st.columns(2)
gen_columns = df.columns[df.columns.str.contains("Realtime Generation Summary-(?!.*(?:FORECAST|ACTUAL))")]
latest_gen = latest[gen_columns]
latest_gen = latest_gen[latest_gen > 0]
labels = latest_gen.index.str.extract("Realtime Generation Summary-(.*?)\s+\[MW\]")[0].values
values = latest_gen.values

fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=values), 1, 1)
fig.update_traces(hole=.4, hoverinfo="label+percent")

fig.update_layout(
    title_text="Generation summary",
    annotations=[dict(text='Total generated', x=0.5, y=0.5, font_size=15, showarrow=False), dict(text=f'{latest["GENERATION > Generation Forecast-ACTUAL GENERATION [MW]"]}' + " MW", x=0.5, y=0.43, font_size=15, showarrow=False)])

col3_2.plotly_chart(fig)
latest_48h_gen = latest_48h["GENERATION > Generation Forecast-ACTUAL GENERATION [MW]"]
latest_48h_demand = latest_48h["DEMAND SUMMARY-ACTUAL TOTAL LOAD [MW]"]

# Last 24h Supply and demand line chart
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=latest_48h["Time Start (WET)"], y=latest_48h_gen, name='Generation',
                        line=dict(color='blue', width=4)))
fig2.add_trace(go.Scatter(x=latest_48h["Time Start (WET)"], y=latest_48h_demand, name='Demand',
                        line=dict(color='red', width=4)))
fig2.update_layout(title_text="Last 24h Supply and Demand", xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False), yaxis_title="EUR/MWh")
col3_1.plotly_chart(fig2)

