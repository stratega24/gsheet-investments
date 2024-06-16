# importing the following libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_gsheets import GSheetsConnection


# Set the page config
st.set_page_config(page_title='Investments Data',
                   layout='wide',
                   page_icon='📊')

# Connect with the link of google sheet
conn = st.connection("gsheets", type=GSheetsConnection)

# Read Data from google sheet
df = conn.read(worksheet="0", ttl=5)

# Sidebar in streamlit web app
st.sidebar.header("Please Filter Here:")
type = st.sidebar.multiselect(
    "Select the Type:",
    options=df["type"].unique(),
    default=df["type"].unique()
)

currency = st.sidebar.multiselect(
    "Select the Currency:",
    options=df["currency"].unique(),
    default=df["currency"].unique()
)

status = st.sidebar.multiselect(
    "Select the Status:",
    options=df["status"].unique(),
    default=df["status"].unique()
)

df_selection = df.query(
    "type == @type & currency == @currency & status == @status"
)

# Main KPI to be shown in the streamlit web app
st.title(":bar_chart: Sales Data Visualization")
st.markdown("##")

# Display The Calculations in the streamlit web app
total_investment = df_selection['amount'].str.replace(',', '').astype(float)
total_investment_made = round(total_investment.sum(),2)
count_of_investment = len(df_selection["type"])

left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Total Investments Made:")
    st.subheader(f"INR ₹ {total_investment_made:}")


with right_column:
    st.subheader("Total Number of Investments:")
    st.subheader(f"{count_of_investment:}")

st.markdown("---")


with left_column:
    fig_type = px.pie(df_selection, title= "Online vs Digital Download", names = "type", values = "amount", hole=0.5)

    fig_type.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis=(dict(showgrid= False)),
    legend=dict(orientation='h',yanchor='top',xanchor='center',x=0.5),
    margin=dict(l=20, r=20, t=20, b=20)
    )

    st.plotly_chart(fig_type)


with right_column:
    fig_status = px.pie(df_selection, title= "In-Progress vs Completed", names = "status", values = "amount", hole=0.5)

    fig_status.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis=(dict(showgrid= False)),
    legend=dict(orientation='h',yanchor='top',xanchor='center',x=0.5),
    margin=dict(l=20, r=20, t=20, b=20)
    )

    st.plotly_chart(fig_status)

with left_column:
    fig_year = px.pie(df_selection, title= "Financial Year", names = "financial year", values = "amount", hole=0.5)

    fig_year.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis=(dict(showgrid= False)),
    legend=dict(orientation='h',yanchor='top',xanchor='center',x=0.5),
    margin=dict(l=20, r=20, t=20, b=20)
    )

    st.plotly_chart(fig_year)


with right_column:
    fig_currency = px.pie(df_selection, title= "INR vs USD", names = "currency", values = "amount", hole=0.5)

    fig_currency.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis=(dict(showgrid= False)),
    legend=dict(orientation='h',yanchor='top',xanchor='center',x=0.5),
    margin=dict(l=20, r=20, t=20, b=20)
    )

    st.plotly_chart(fig_currency)

# Hide Style CSS
hide_at_style = """
                <style>
                #MainMenu {visibility:hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>   
                """
st.markdown(hide_at_style, unsafe_allow_html= True)




