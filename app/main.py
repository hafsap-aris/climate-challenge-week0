import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="African Climate Dashboard", layout="wide")


st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    h1 { color: #2e4a31; }
    </style>
    """, unsafe_allow_html=True)

st.title("African Climate Vulnerability Dashboard")
st.subheader("Interactive Analysis for COP32 Position Paper")


@st.cache_data
def load_data():
    df = pd.read_csv("data/master_climate_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Data file not found. Please ensure 'data/master_climate_data.csv' exists.")
    st.stop()


st.sidebar.header("Filter Insights")


countries = st.sidebar.multiselect(
    "Select Countries",
    options=df['Country'].unique(),
    default=df['Country'].unique()
)

# Year range slider
min_year = int(df['YEAR'].min())
max_year = int(df['YEAR'].max())
year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Variable selector dropdown
variable = st.sidebar.selectbox(
    "Select Metric",
    options=['T2M', 'PRECTOTCORR', 'RH2M'],
    index=0
)


filtered_df = df[
    (df['Country'].isin(countries)) & 
    (df['YEAR'] >= year_range[0]) & 
    (df['YEAR'] <= year_range[1])
]


col1, col2 = st.columns(2)

with col1:
    
    st.markdown(f"### {variable} Trend Over Time")
    fig_line = px.line(
        filtered_df, 
        x='date', 
        y=variable, 
        color='Country',
        template="simple_white",
        labels={'date': 'Date', variable: f'{variable} Value'}
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col2:

    st.markdown("### Regional Precipitation Extremes")
    fig_box = px.box(
        filtered_df, 
        x='Country', 
        y='PRECTOTCORR', 
        color='Country',
        points="outliers",
        template="simple_white",
        title="Rainfall Distribution & Variability"
    )
    st.plotly_chart(fig_box, use_container_width=True)

st.divider()
st.markdown("### 📊 Dataset Quick Stats")
st.dataframe(filtered_df.groupby('Country')[['T2M', 'PRECTOTCORR']].mean().style.highlight_max(axis=0, color='#ffcccc'))