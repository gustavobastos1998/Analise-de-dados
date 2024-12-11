import streamlit as stl
import pandas as pd
import numpy as np
import haversine as hs
from PIL import Image

# import dataset
df = pd.read_csv('D:/Estudos/Analise-de-dados/Projetos/datasets/train.csv')
# print(df.head())

# =========================================================================================
# Data Preprocessing
# =========================================================================================

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

# =========================================================================================
# sidebar
# =========================================================================================

image_path = 'D:/Estudos/Analise-de-dados/Projetos/logo.png'
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
city_options = stl.sidebar.multiselect(
    'Which city type do you want to select?',
    df['City'].unique(),
    default='Urban'
)
type_of_order_options = stl.sidebar.multiselect(
    'Which type of order do you want to select?',
    df['Type_of_order'].unique(),
    default='Snack'
)
stl.sidebar.markdown('***')
# date filter
selected_lines = df['Order_Date'] <= date_slider
df = df.loc[selected_lines,:]

# road density filter
selected_lines = df['Road_traffic_density'].isin(traffic_options)
df = df.loc[selected_lines,:]

# city filter
selected_lines = df['City'].isin(city_options)
df = df.loc[selected_lines,:]

# type of order filter
selected_lines = df['Type_of_order'].isin(type_of_order_options)
df = df.loc[selected_lines,:]

# =========================================================================================
# streamlit layout
# =========================================================================================

stl.header('Marketplace - Restaurant View')
tab1, tab2, tab3 = stl.tabs(['Delivery Performance','Delivery Time & Distance','City-Based Performance'])
with tab1:
    stl.markdown('')
    with stl.container():
        stl.markdown('')
        col1, col2 = stl.columns(2)
        with col1:
            qtd_unique_employees = df['Delivery_person_ID'].nunique()
            col1.metric('Number of employees', qtd_unique_employees)
        with col2:
            df_festival_on = df[df['Festival'] == 'Yes']
            average_festival_on = df_festival_on['Time_taken(min)'].mean()
            col2.metric('Average time taken during festival',f'{average_festival_on:.2f}')
with tab2:
    with stl.container():
        stl.subheader('Restaurants and delivery locations latitudes/longitudes and distance between them')
        cols = ['Restaurant_latitude','Restaurant_longitude','Delivery_location_latitude','Delivery_location_longitude']
        df_aux = df[cols]
        df_aux['Distance_between_restaurant_and_delivery(km)'] = df.loc[:,cols].apply( lambda x: hs.haversine((x['Restaurant_latitude'],x['Restaurant_longitude']),(x['Delivery_location_latitude'],x['Delivery_location_longitude'])),axis=1)
        stl.dataframe(df_aux, height=350, width=345)
        stl.markdown('***')
    with stl.container():   
        stl.subheader('Average and standard deviation of the time taken to deliver grouped by city')
        df_aux = df.groupby('City')['Time_taken(min)'].mean().reset_index()
        df_aux.rename(columns={'Time_taken(min)':'average'},inplace=True)
        df_aux['standard_deviation'] = df.groupby('City')['Time_taken(min)'].std().reset_index()['Time_taken(min)']
        stl.dataframe(df_aux)
with tab3:
    with stl.container():
        stl.subheader('Average and standard deviation of the time taken to deliver grouped by city and type of order')
        df_aux = df.groupby(['City','Type_of_order'])['Time_taken(min)'].mean().reset_index()
        df_aux.rename(columns={'Time_taken(min)':'average'},inplace=True)
        df_aux['standard_deviation'] = df.groupby(['City','Type_of_order'])['Time_taken(min)'].std().reset_index()['Time_taken(min)']
        stl.dataframe(df_aux, width=500)
    with stl.container():
        stl.subheader('Average and standard deviation of the time taken to deliver grouped by city and traffic density')
        df_aux = df.groupby(['City','Road_traffic_density'])['Time_taken(min)'].mean().reset_index()
        df_aux.rename(columns={'Time_taken(min)':'average'},inplace=True)
        df_aux['standard_deviation'] = df.groupby(['City','Road_traffic_density'])['Time_taken(min)'].std().reset_index()['Time_taken(min)']
        stl.dataframe(df_aux, width=500)



























