import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.set_page_config(
     page_title="GOAT Analysis",
     page_icon="🧊",
     layout="centered",
     initial_sidebar_state="auto",
 )
st.title('GOAT Analysis')


fdf = pd.read_csv(r'Cleaned Data\federer_stats_cleaned.csv')
ndf = pd.read_csv(r'Cleaned Data\nadal_stats_cleaned.csv')
ddf = pd.read_csv(r'Cleaned Data\djokovic_stats_cleaned.csv')


fdf.reset_index(inplace=True)
ndf.reset_index(inplace=True)
ddf.reset_index(inplace=True)

fig1 = px.bar(fdf, x="Year", y="Total wins %",
             height=450,width=850, color="Total wins %", text="Total wins %",
             color_continuous_scale=px.colors.sequential.Blues, title="Federer yearly win %", template="seaborn")
fig1.update_traces(texttemplate="%{y:.2f}")
fig1.update_layout(paper_bgcolor="#0F0F11",margin_t=35, margin_b=10, plot_bgcolor="#1C1917")
fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(showgrid=False)

fig2 = px.bar(ndf, x="Year", y="Total wins %",
             height=450,width=850, color="Total wins %", text="Total wins %",
             color_continuous_scale=px.colors.sequential.Blues, title="Nadal yearly win %", template="seaborn")
fig2.update_traces(texttemplate="%{y:.2f}")
fig2.update_layout(paper_bgcolor="#0F0F11",margin_t=35, margin_b=10, plot_bgcolor="#1C1917")
fig2.update_xaxes(showgrid=False)
fig2.update_yaxes(showgrid=False)

fig3 = px.bar(ddf, x="Year", y="Total wins %",
             height=450,width=850, color="Total wins %", text="Total wins %",
             color_continuous_scale=px.colors.sequential.Blues, title="Djokovic yearly win %", template="seaborn")
fig3.update_traces(texttemplate="%{y:.2f}")
fig3.update_layout(paper_bgcolor="#0F0F11",margin_t=35, margin_b=10, plot_bgcolor="#1C1917")
fig3.update_xaxes(showgrid=False)
fig3.update_yaxes(showgrid=False)

fig = st.sidebar.radio(
            "Choose Player",
            ("Federer","Nadal","Djokovic")
)

if fig == "Federer":
    st.plotly_chart(fig1, use_container_width=False)
if fig == "Nadal":
    st.plotly_chart(fig2, use_container_width=False)
if fig == "Djokovic":
    st.plotly_chart(fig3, use_container_width=False)

fdf['Total matches'] = fdf['Total wins'] + fdf['Total loss']
ndf['Total matches'] = ndf['Total wins'] + ndf['Total loss']
ddf['Total matches'] = ddf['Total wins'] + ddf['Total loss']

fed = round(fdf['Total matches'].mean(), ndigits=2)
nad = round(ndf['Total matches'].mean(), ndigits=2)
djo = round(ddf['Total matches'].mean(), ndigits=2)

avg_matches = [fed,nad,djo]
players = ['Federer','Nadal','Djokovic']

fed = round(fdf['Total wins'].mean(), ndigits=2)
nad = round(ndf['Total wins'].mean(), ndigits=2)
djo = round(ddf['Total wins'].mean(), ndigits=2)

avg_wins = [fed,nad,djo]

fed = round(fdf['Total loss'].mean(), ndigits=2)
nad = round(ndf['Total loss'].mean(), ndigits=2)
djo = round(ddf['Total loss'].mean(), ndigits=2)

avg_loss = [fed,nad,djo]

fig = make_subplots(rows=1, cols=3, subplot_titles=("Avg matches played","Avg matches won","Avg matches lost"))
fig.add_trace(go.Bar(x=players, y=avg_matches, name="Avg matches", text=avg_matches, marker_color="#1E36AA"), row=1, col=1)
fig.add_trace(go.Bar(x=players, y=avg_wins, name="Avg wins", text=avg_wins, marker_color="green"), row=1, col=2)
fig.add_trace(go.Bar(x=players, y=avg_loss, name="Avg losses", text=avg_loss, marker_color="#E2193A"), row=1, col=3)
fig.update_layout(title="Analyzing Career Averages", width=850, paper_bgcolor="#0F0F11",margin_r=30, plot_bgcolor="#1C1917", template="seaborn")
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
st.plotly_chart(fig)

fed = fdf['Total wins'].sum() / fdf['Total matches'].sum()
fed = round(fed, ndigits=4)*100
nad = ndf['Total wins'].sum() / ndf['Total matches'].sum()
nad = round(nad, ndigits=4)*100
djo = ddf['Total wins'].sum() / ddf['Total matches'].sum()
djo = round(djo, ndigits=4)*100

Total = [fed,nad,djo]
players = ['Federer','Nadal','Djokovic']

fed = fdf['Clay wins'].sum() / (fdf['Clay wins'].sum() + fdf['Clay loss'].sum())
fed = round(fed, ndigits=4)*100
nad = ndf['Clay wins'].sum() / (ndf['Clay wins'].sum() + ndf['Clay loss'].sum())
nad = round(nad, ndigits=4)*100
djo = ddf['Clay wins'].sum() / (ddf['Clay wins'].sum() + ddf['Clay loss'].sum())
djo = round(djo, ndigits=4)*100

Clay = [fed,nad,djo]

fed = fdf['Hard wins'].sum() / (fdf['Hard wins'].sum() + fdf['Hard loss'].sum())
fed = round(fed, ndigits=4)*100
nad = ndf['Hard wins'].sum() / (ndf['Hard wins'].sum() + ndf['Hard loss'].sum())
nad = round(nad, ndigits=4)*100
djo = ddf['Hard wins'].sum() / (ddf['Hard wins'].sum() + ddf['Hard loss'].sum())
djo = round(djo, ndigits=4)*100

Hard = [fed,nad,djo]

fed = fdf['Grass wins'].sum() / (fdf['Grass wins'].sum() + fdf['Grass loss'].sum())
fed = round(fed, ndigits=4)*100
nad = ndf['Grass wins'].sum() / (ndf['Grass wins'].sum() + ndf['Grass loss'].sum())
nad = round(nad, ndigits=4)*100
djo = ddf['Grass wins'].sum() / (ddf['Grass wins'].sum() + ddf['Grass loss'].sum())
djo = round(djo, ndigits=4)*100

Grass = [fed,nad,djo]

fig = make_subplots(rows=1, cols=4, subplot_titles=("Overall win %","Clay win %","Hard win %","Grass win %"))
fig.add_trace(go.Bar(x=players, y=Total, text=Total, name="Overall",marker_color="#036F04"), row=1, col=1)
fig.add_trace(go.Bar(x=players, y=Clay, text=Clay, name="Clay",marker_color="#E2193A"), row=1, col=2)
fig.add_trace(go.Bar(x=players, y=Hard, text=Hard, name="Hard",marker_color="#1E36AA"), row=1, col=3)
fig.add_trace(go.Bar(x=players, y=Grass, text=Grass, name="Grass",marker_color="green"), row=1, col=4)
fig.update_layout(title="Analyzing Career Percentages", width=850, paper_bgcolor="#0F0F11",margin_r=30, plot_bgcolor="#1C1917", template="seaborn")
fig.update_traces(texttemplate="%{y:.2f}")
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
st.plotly_chart(fig)
