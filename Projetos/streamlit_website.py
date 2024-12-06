# libraries
import pandas as pd
import haversine as hs
import numpy as np
import matplotlib.pyplot as plt
import streamlit as stl
from PIL import Image
from streamlit_folium import folium_static
import folium


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

# Remover NaN da coluna road_traffic_density
df['Road_traffic_density'] = df['Road_traffic_density'].replace('NaN',np.nan)
df.dropna(subset=['Road_traffic_density'],inplace=True)

# transformar Time_taken(min) para número
df['Time_taken(min)'] = df['Time_taken(min)'].apply(lambda x: x.split('(min) ')[1])
df['Time_taken(min)'] = df['Time_taken(min)'].astype('int8')
# print(df['ID'])

# =========================================================================================
# Layout streamlit
# =========================================================================================

stl.header('Marketplace')
tab1, tab2, tab3 = stl.tabs(['Management View','Tactical View','Geographic View'])

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
    'Which traffic condition you want to select?',
    ['Low','Medium','High','Jam'],
    default='Low'
)
stl.sidebar.markdown('***')
# date filter
selected_lines = df['Order_Date'] <= date_slider
df = df.loc[selected_lines,:]

# road density filter
selected_lines = df['Road_traffic_density'].isin(traffic_options)
df = df.loc[selected_lines,:]

# =========================================================================================
# management View
# =========================================================================================

with tab1:
    with stl.container():
        stl.markdown('### Orders by day')
        aux = df.groupby('Order_Date')['ID'].count().reset_index()
        fig, ax = plt.subplots(figsize=(15,6))
        ax.set_xlabel('day')
        ax.set_ylabel('ID quantity')
        ax.bar(aux['Order_Date'].values,aux['ID'],color=['purple'])
        fig.patch.set_facecolor('gray')
        ax.set_facecolor('lightblue')
        stl.pyplot(fig,use_container_width=True)
    with stl.container():
        col1, col2 = stl.columns(2)
        with col1:
            stl.markdown('Amount of IDs by city and road traffic density')
            qtd_pedidos_cidade_trafego = df.groupby(['City','Road_traffic_density'])['ID'].count().reset_index()
            unique_cities = qtd_pedidos_cidade_trafego['City'].unique()
            city_color_mapping = {city: i for i, city in enumerate(unique_cities)}
            qtd_pedidos_cidade_trafego['colors'] = qtd_pedidos_cidade_trafego['City'].map(city_color_mapping)
            fig, axes = plt.subplots(figsize=(15,15.48))
            axes.set_xlabel('City')
            axes.set_ylabel('Road traffic density')
            axes.set_title('amount of IDs grouped by city and traffic density')
            axes.scatter(qtd_pedidos_cidade_trafego['City'],qtd_pedidos_cidade_trafego['Road_traffic_density'],s=qtd_pedidos_cidade_trafego['ID'],c=qtd_pedidos_cidade_trafego['colors'])
            fig.patch.set_facecolor('gray')
            stl.pyplot(fig,use_container_width=True)
            
        with col2:
            stl.markdown('Percentage of deliveries by traffic density')
            pedidos_por_tipo_de_trafego = df.groupby('Road_traffic_density')['ID'].count().reset_index()
            soma_total = pedidos_por_tipo_de_trafego.sum()['ID']
            percentual_relativo = pedidos_por_tipo_de_trafego['ID']/soma_total*100
            pedidos_por_tipo_de_trafego['Percentual_relativo'] = percentual_relativo
            fig, axes = plt.subplots(figsize=(6.4,5))
            axes.pie(percentual_relativo, labels=pedidos_por_tipo_de_trafego['Road_traffic_density'],autopct='%1.1f%%')
            fig.patch.set_facecolor('gray')
            stl.pyplot(fig, use_container_width=True)

# =========================================================================================
# tactical view
# =========================================================================================

with tab2:
    with stl.container():
        stl.markdown('### Orders by week')
        df['week_of_year'] = df['Order_Date'].dt.strftime('%U') # cria a coluna 'week_of_year' e o dt.strftime('%U') elenca segunda-feira como o primeiro dia da semana
        pedidos_por_semana = df.groupby('week_of_year')['ID'].count().reset_index()
        fig, axes = plt.subplots(figsize=(6.4,6.75))
        axes.set_xlabel('Week of Year')
        axes.set_ylabel('ID quantity')
        axes.grid()
        axes.plot(pedidos_por_semana['week_of_year'],pedidos_por_semana['ID'],marker='o',markerfacecolor='green',linestyle='-',color='blue')
        fig.patch.set_facecolor('gray')
        stl.pyplot(fig,use_container_width=True)
    with stl.container():
        stl.markdown('### Order share by week')
        df_aux1 = df.groupby('week_of_year')['ID'].count().reset_index()
        df_aux2 = df.groupby('week_of_year')['Delivery_person_ID'].nunique().reset_index()
        df_aux = pd.merge(df_aux1, df_aux2, how='inner', on='week_of_year')
        df_aux['order_by_deliver'] = df_aux['ID']/df_aux['Delivery_person_ID']
        fig, axes = plt.subplots(figsize=(6.4,6.75))
        axes.set_xlabel('week of year')
        axes.set_ylabel('order by deliver')
        axes.grid()
        axes.plot(df_aux['week_of_year'],df_aux['order_by_deliver'],marker='o',markerfacecolor='green',linestyle='-',color='blue')
        fig.patch.set_facecolor('gray')
        stl.pyplot(fig,use_container_width=True)
# =========================================================================================
# geographic view
# =========================================================================================

with tab3:
    stl.markdown('Median points of latitudes and longitudes grouped by city and traffic density.')
    df_aux = df.groupby(['City','Road_traffic_density'])['Delivery_location_latitude'].median().reset_index()
    df_aux['median_longitude'] = df.groupby(['City','Road_traffic_density'])['Delivery_location_longitude'].median().reset_index()['Delivery_location_longitude']
    df_aux.rename(columns={'Delivery_location_latitude':'median_latitude'},inplace=True)
    map = folium.Map()
    for i, location_info in df_aux.iterrows():
        folium.Marker([location_info['median_latitude'],
                     location_info['median_longitude']],
                     popup=location_info[['City','Road_traffic_density']]).add_to(map)
    
    folium_static(map, width=1024, height=600)




















