import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="African Climate Dashboard", layout="wide")

# Custom CSS for the aesthetic you prefer (matte/earthy tones)
st.markdown("""
    <style>
    .main { background-color: #fcfaf8; }
    h1 { color: #3d403a; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; }
    </style>
    """, unsafe_allow_html=True)

st.title("African Climate Vulnerability Dashboard")
st.subheader("Interactive Analysis")

@st.cache_data
def load_data():
    # This is the direct download version of your Google Drive link
    file_id = "1Pah08aJZVFPDe2JMukww1xorbUunTbxi"
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    
    df = pd.read_csv(url)
    
    # Pre-processing
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    return df

try:
    with st.spinner('Fetching climate data from secure storage...'):
        df = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.info("Check that the Google Drive link is set to 'Anyone with the link can view'.")
    st.stop()

st.sidebar.header("Filter Insights")

# Select Countries
countries = st.sidebar.multiselect(
    "Select Countries",
    options=df['Country'].unique(),
    default=df['Country'].unique()[:5] # Defaulting to first 5 to keep initial load fast
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

# Variable selector
variable = st.sidebar.selectbox(
    "Select Metric",
    options=['T2M', 'PRECTOTCORR', 'RH2M'],
    index=0
)

# Filtering logic
filtered_df = df[
    (df['Country'].isin(countries)) & 
    (df['YEAR'] >= year_range[0]) & 
    (df['YEAR'] <= year_range[1])
]

# Visualizations
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"### {variable} Trend Over Time")
    fig_line = px.line(
        filtered_df, 
        x='date' if 'date' in filtered_df.columns else 'YEAR', 
        y=variable, 
        color='Country',
        template="simple_white",
        color_discrete_sequence=px.colors.qualitative.Antique # Organic matte color palette
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
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    st.plotly_chart(fig_box, use_container_width=True)

st.divider()
st.markdown("### 📊 Dataset Quick Stats")
st.dataframe(
    filtered_df.groupby('Country')[['T2M', 'PRECTOTCORR']].mean()
    .style.highlight_max(axis=0, color='#d4e4bc') # Earthy matte highlight
)