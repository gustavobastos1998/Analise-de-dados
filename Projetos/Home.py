import streamlit as stl
from PIL import Image

stl.set_page_config(page_title='Home', page_icon='🎲')

image_path = '/mount/src/analise-de-dados/Projetos/logo.png'
image = Image.open(image_path)

stl.sidebar.image(image, width=120)
stl.sidebar.markdown('# Cury Company')
stl.sidebar.markdown('## Fastest Delivery in Town')
stl.sidebar.markdown('***')

stl.write('# Cury Company Growth Dashboard')

stl.markdown("""
Growth Dashboard was built to track the growth metrics of Couriers and Restaurants.
### How to use this Growth Dashboard?
- Company Overview:
    - Management View: General behavior metrics.
    - Tactical View: Weekly growth indicators.
    - Geographical View: Geolocation insights.

- Courier Overview:
    - Monitoring weekly growth indicators.

- Restaurant Overview:
    - Weekly growth indicators for restaurants.
""")