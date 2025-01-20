import os
import streamlit as stl
from PIL import Image

stl.set_page_config(page_title='Home', page_icon='🎲')

dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(dir_path,'logo.png')
#image_path = './logo.png'
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