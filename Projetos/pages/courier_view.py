import os
import streamlit as stl
import pandas as pd
import numpy as np
from PIL import Image

stl.set_page_config(page_title='Courier Overview', page_icon='🚚', layout='wide')
# =========================================================================================
# functions
# =========================================================================================

# ===================
# Data Preprocessing
# ===================

def data_cleaning(df):
    # Limpeza dos dados para melhorar o uso da base de dados
    # Conversão da coluna Delivery_person_Age de string para int
    df['Delivery_person_Age'] = pd.to_numeric(df['Delivery_person_Age'],errors='coerce') # Converte a coluna 'delivery_person_age' para float e coloca 'NaN' para qualquer valor diferente de número
    df.dropna(subset=['Delivery_person_Age'],inplace=True) # Remove as linhas que tiver 'NaN'
    df['Delivery_person_Age'] = df['Delivery_person_Age'].astype('int8') # Transforma o tipo de float para int8
    # print(df['Delivery_person_Age'].dtypes)
    
    # Conversão da coluna Delivery_person_Ratings de string para float
    df['Delivery_person_Ratings'] = pd.to_numeric(df['Delivery_person_Ratings'],errors='coerce') # Converte a coluna 'delivery_person_ratings' para float e coloca 'NaN' para qualquer valor diferente de número
    df.dropna(subset=['Delivery_person_Ratings'],inplace=True) # Remove as linhas que tiver 'NaN'
    df['Delivery_person_Ratings'] = df['Delivery_person_Ratings'].astype('float16') # Transforma o tipo de float para float16
    # print(df['Delivery_person_Ratings'].dtypes)
    
    # Conversão da coluna Order_Date de string para datetime
    df['Order_Date'] = pd.to_datetime(df['Order_Date'],format='%d-%m-%Y')
    # print(type(df['Order_Date'][0]))
    
    # Conversão da coluna multiple_deliveries de string para int
    df['multiple_deliveries'] = pd.to_numeric(df['multiple_deliveries'],errors = 'coerce') # Converte a coluna 'multiple_deliveries' para float e coloca 'NaN' para qualquer valor diferente de número
    df.dropna(subset=['multiple_deliveries'], inplace=True) # Remove as linhas que tiver 'NaN'
    df['multiple_deliveries'] = df['multiple_deliveries'].astype('int8') # Transforma de float para int8
    # print(df['multiple_deliveries'].dtypes)
    
    # Remover NaN das latitudes e longitudes
    df.dropna(subset=['Restaurant_latitude'], inplace=True)
    df.dropna(subset=['Restaurant_longitude'], inplace=True)
    df.dropna(subset=['Delivery_location_latitude'], inplace=True)
    df.dropna(subset=['Delivery_location_longitude'], inplace=True)
    
    # Remover espaços em branco no final das strings de algumas colunas
    df['ID'] = df['ID'].str.strip()
    df['Road_traffic_density'] = df['Road_traffic_density'].str.strip()
    df['Type_of_order'] = df['Type_of_order'].str.strip()
    df['Type_of_vehicle'] = df['Type_of_vehicle'].str.strip()
    df['City'] = df['City'].str.strip()
    df['Festival'] = df['Festival'].str.strip()
    
    # Remover NaN da coluna de City
    df['City'] = df['City'].replace('NaN',np.nan)
    df.dropna(subset=['City'], inplace=True)
    # print(df['City'].unique())
    
    # Remover Nan da coluna Weatherconditions
    df.dropna(subset=['Weatherconditions'],inplace=True)
    
    # Remover NaN da coluna road_traffic_density
    df['Road_traffic_density'] = df['Road_traffic_density'].replace('NaN',np.nan)
    df.dropna(subset=['Road_traffic_density'],inplace=True)
    
    # transformar Time_taken(min) para número
    df['Time_taken(min)'] = df['Time_taken(min)'].apply(lambda x: x.split('(min) ')[1])
    df['Time_taken(min)'] = df['Time_taken(min)'].astype('int8')
    # print(df['ID'])
    return df

# =========================================================================================
# import dataset
# =========================================================================================

dir_path = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(dir_path,'../datasets','train.csv')
df = pd.read_csv(csv_path)
data_cleaning(df)
# print(df.head())

# =========================================================================================
# sidebar
# =========================================================================================

dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(dir_path,'../logo.png')
image = Image.open(image_path)
# stl.dataframe(df)
stl.sidebar.image(image, width=120)
stl.sidebar.markdown('# Cury Company')
stl.sidebar.markdown('## Fastest Delivery in Town')
stl.sidebar.markdown('***')
stl.sidebar.markdown('## Select a data limit')
date_slider = stl.sidebar.slider(
    'Until which date?',
    value=df['Order_Date'].max().to_pydatetime(),
    min_value=df['Order_Date'].min().to_pydatetime(),
    max_value=df['Order_Date'].max().to_pydatetime(),
    format='DD-MM-YYYY')
traffic_options = stl.sidebar.multiselect(
    'Which traffic condition do you want to select?',
    ['Low','Medium','High','Jam'],
    default='Low'
)
weather_options = stl.sidebar.multiselect(
    'Which weather conditions do you want to select?',
    df['Weatherconditions'].unique()
)
stl.sidebar.markdown('***')
# date filter
selected_lines = df['Order_Date'] <= date_slider
df = df.loc[selected_lines,:]

# road density filter
selected_lines = df['Road_traffic_density'].isin(traffic_options)
df = df.loc[selected_lines,:]

# weather condition filter
selected_lines = df['Weatherconditions'].isin(weather_options)
df = df.loc[selected_lines,:]

# =========================================================================================
# Streamlit layout
# =========================================================================================

stl.header('Marketplace - Delivery View')
tab1, tab2, tab3 = stl.tabs(['Delivery Stats','Delivery Ratings Analysis','Speed Metrics'])

with tab1:
    with stl.container():
        col1, col2, col3, col4 = stl.columns(4)
        with col1:
            youngest_delivery_person = df['Delivery_person_Age'].min()
            col1.metric('Age of the youngest employee', youngest_delivery_person)
        with col2:
            oldest_delivery_person = df['Delivery_person_Age'].max()
            col2.metric('Age of the oldest employee', oldest_delivery_person)
        with col3:
            best_condition = df['Vehicle_condition'].max()
            col3.metric('Best Vehicle Condition', best_condition)
        with col4:
            worst_condition = df['Vehicle_condition'].min()
            col4.metric('Worst Vehicle Condition', worst_condition)
with tab2:
    with stl.container():
        col1, col2 = stl.columns(2)
        with col1:
            stl.subheader('Average Rating by employee')
            avaliacao_media_por_entregador = df.groupby('Delivery_person_ID')['Delivery_person_Ratings'].mean().reset_index()
            avaliacao_media_por_entregador.rename(columns={'Delivery_person_Ratings':'Average_rating'},inplace=True)
            stl.dataframe(avaliacao_media_por_entregador, height=538)
        with col2:
            stl.subheader('Average Rating by traffic density')
            avg_rating_traffic = df.groupby('Road_traffic_density')['Delivery_person_Ratings'].mean().reset_index()
            avg_rating_traffic.rename(columns={'Delivery_person_Ratings':'Average'},inplace=True)
            stl.dataframe(avg_rating_traffic)
            stl.subheader('Average Rating by weather condition')
            avg_rating_weather = df.groupby('Weatherconditions')['Delivery_person_Ratings'].mean().reset_index()
            avg_rating_weather.rename(columns={'Delivery_person_Ratings':'Average'},inplace=True)
            stl.dataframe(avg_rating_weather)
with tab3:
    col1, col2 = stl.columns(2)
    with col1:
        stl.subheader('Ten fastest employees')
        ten_fastest = df.nsmallest(10,'Time_taken(min)')
        selected_columns = ['ID','Delivery_person_ID','Time_taken(min)']
        stl.dataframe(ten_fastest[selected_columns])
    with col2:
        stl.subheader('Ten slowest employees')
        ten_slowest = df.nlargest(10,'Time_taken(min)')
        stl.dataframe(ten_slowest[selected_columns])
















    


