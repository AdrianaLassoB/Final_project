import pandas as pd
import streamlit as st

#For all the colors in the background I was used Chat gpt
def set_theme():
    # Update the default Streamlit theme
    st.markdown(
        """
        <style>
        .stApp {
            background-color: mintcream; /* Change this to the color you desire */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Call the set_theme function to apply the custom theme
set_theme()

df_nuclear = pd.read_csv("nuclear_explosions.csv")
list_selected =["WEAPON_DEPLOYMENT_LOCATION","WEAPON_SOURCE_COUNTRY"]
comlums_selected = df_nuclear[list_selected]

st.title("Nuclear explosions between 1945 and 1998")
from PIL import Image
img = Image.open("nuclear.jpeg")
st.image(img, width= 500, )
st.write("In this page we are going analize the nuclear bombs data from 1945 to 1998. For it we have three pages which divided the content between year, purpose and magnitude.")
st.write()
st.write()
st.write("As an insight of how the data looks, here are the firts ten rows")
#[PY 1]
def display(df):
    return df.shape, df.head(10)

number_rows, firts_10_rows = display(df_nuclear)
st.write("The data contains",number_rows[0],"rows")
st.write(firts_10_rows)

import pandas as pd
import streamlit as st
import pydeck as pdk
def set_theme():
    # Update the default Streamlit theme
    st.markdown(
        """
        <style>
        .stApp {
            background-color: violet; /* Change this to the color you desire */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Call the set_theme function to apply the custom theme
set_theme()
df_nuclear = pd.read_csv("nuclear_explosions.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)

#[ST2] I was able to change the aligment of the title and the color with the help of chat gpt
title_style = """
    <style>
    .title {
        text-align: center;
        color: aquamarine;
    }
    </style>
"""

# Apply the style for centering the title
st.markdown(title_style, unsafe_allow_html=True)

# Display the centered title
st.markdown("<h1 class='title'>Bombs per country</h1>", unsafe_allow_html=True)

Suma = 0



purpose = []





countries = []

for row in df_nuclear.itertuples():
    if row.WEAPON_SOURCE_COUNTRY not in countries:
        countries.append(row.WEAPON_SOURCE_COUNTRY )




import streamlit as st
import pandas as pd



# Get unique countries
countries = df_nuclear['WEAPON_SOURCE_COUNTRY'].unique()



#[ST4]
selected_country = st.radio("Please select a Country", countries)

#[PY 3]
def calculate_country_percentage( country,df = df_nuclear):
    total_bombs = len(df)
    country_bombs = len(df[df['WEAPON_SOURCE_COUNTRY'] == country])
    percentage = (country_bombs / total_bombs) * 100
    return percentage

st.write("The country", selected_country,"was responsable for", calculate_country_percentage(selected_country),"% of bombs")


#[EXTRA CREDIT] imported plotly with is a package for more complex graphs


#[DA 3] FILTER DATA
selected_country_data = df_nuclear[df_nuclear['WEAPON_SOURCE_COUNTRY'] == selected_country]

# Count occurrences of each purpose for the selected country
purpose_counts = selected_country_data['data_Purpose'].value_counts()


purpose_counts.plot(kind = 'bar')






# Plot the purpose distribution for the selected country with tooltips
Suma = 0
for row in df_nuclear.itertuples():
    if row.WEAPON_SOURCE_COUNTRY == selected_country:  # Convert year to string for comparison
        Suma += 1

st.write("The country," selected_country, "has dropped a total of", Suma," bombs in between 1945 and 1998")

df_selected_country = df_nuclear[df_nuclear['WEAPON_SOURCE_COUNTRY'] == selected_country]





#[VIZ3]
df_selected_country.rename(columns={"Location.Cordinates.Latitude":"lat", "Location.Cordinates.Longitude": "lon"}, inplace= True)
view_state = pdk.ViewState(
latitude = df_selected_country["lat"].mean(),  # The latitude of the view center
longitude = df_selected_country["lon"].mean(),  # The longitude of the view center
# latitude= 20,
# longitude= 20,
zoom = 5,  # View zoom level
pitch = 0)  # Tilt level

# Create a map layer with the given coordinates
layer1 = pdk.Layer(type='ScatterplotLayer',  # layer type
data = df_selected_country,  # data source
get_position = '[lon, lat]',  # coordinates
get_radius = 150000,  # scatter radius
get_color = [100, 250, 30],  # scatter color
pickable = False  # work with tooltip
)

# Can create multiple layers in a map
# For more layer information
# https://deckgl.readthedocs.io/en/latest/layer.html
# Line layer https://pydeck.gl/gallery/line_layer.html
layer2 = pdk.Layer('ScatterplotLayer',
data = df_selected_country,
get_position = '[lon, lat]',
get_radius = 150000,
get_color = [0, 0, 255],
pickable = True
)


# stylish tool tip: https://pydeck.gl/tooltip.html?highlight=tooltip
tooltip = {   "html": "Location: <b>{WEAPON_DEPLOYMENT_LOCATION}</b> Purpose: <b>{data_Purpose}</b>",
    "style": {"backgroundColor": "white", "color": "steelblue"}}


# Create a map based on the view, layers, and tool tip
map = pdk.Deck(
map_style = 'mapbox://styles/mapbox/satellite-streets-v12',  # Go to https://docs.mapbox.com/api/maps/styles/ for more map styles
initial_view_state = view_state,
layers = [layer1, layer2],  # The following layer would be on top of the previous layers
tooltip = tooltip
)

st.pydeck_chart(map)






import matplotlib.pyplot as plt



df_selected_country = df_nuclear[df_nuclear['WEAPON_SOURCE_COUNTRY'] == selected_country]

# Count the occurrences of each purpose for the selected country


#[PY 3] did it with help of chatgpt, at the end I was not able to use the information but it helped to get an idea of how the data was distributed
purposes = ['combat', 'fms', 'me', 'pne', 'sam', 'sse', 'transp', 'we', 'wr']

# Use a list comprehension to count occurrences of each purpose
purpose_counts = {purpose.upper(): sum(1 for row in df_nuclear.itertuples() if getattr(row, 'data_Purpose').lower() == purpose) for purpose in purposes}



df_nuclear['Date_Year'] = pd.to_datetime(df_nuclear['Date_Year'], format='%Y')
bombs_dropped_by_year_country = df_nuclear.groupby(['Date_Year', 'data_Purpose']).size().unstack(fill_value=0)


# Display the line chart [ST3]
st.title("Distribution of the bombs's purposes through out the years")
st.line_chart(bombs_dropped_by_year_country)

# Create a bar plot with custom colors
plt.figure(figsize=(10, 6))

import pandas as pd
import streamlit as st
import pydeck as pdk

def set_theme():
    # Update the default Streamlit theme
    st.markdown(
        """
        <style>
        .stApp {
            background-color: paleturquoise; /* Change this to the color you desire */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
st.title("Magnitude")
# Call the set_theme function to apply the custom theme
set_theme()

df_nuclear = pd.read_csv("nuclear_explosions.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)


st.write("To determin which bombs was the strongest, we analize the Data lower yield and the data upper yield, the higest these two numbers are, the strongest the bombs were")
from PIL import Image
img = Image.open("bombita.jpeg")
st.image(img, width= 500)
max_lower_yield = df_nuclear['Data.Yeild.Lower'].max()
max_upper_yield = df_nuclear['Data.Yeild.Upper'].max()

#[DA4]
df_nuclear['Total_Yield'] = df_nuclear['Data.Yeild.Lower'] + df_nuclear['Data.Yeild.Upper']
#[DA5]
higest = df_nuclear.nlargest(5,'Total_Yield')
st.write("The five strongest bombs were",higest)

#[DA6] Filter data by two conditions

# Filter the DataFrame to show rows where either 'Data.Yeild.Lower' or 'Data.Yeild.Upper' equals the maximum values
max_yield_rows = df_nuclear[(df_nuclear['Data.Yeild.Lower'] == max_lower_yield) | (df_nuclear['Data.Yeild.Upper'] == max_upper_yield)]

st.write("According to these mesuares and our data", max_yield_rows ,"were the strongest bomb in between the years 1045-1998")

max_yield_rows.rename(columns={"Location.Cordinates.Latitude":"lat", "Location.Cordinates.Longitude": "lon"}, inplace= True)
view_state = pdk.ViewState(
latitude = max_yield_rows["lat"].mean(),  # The latitude of the view center
longitude = max_yield_rows["lon"].mean(),  # The longitude of the view center
# latitude= 20,
# longitude= 20,
zoom = 5,  # View zoom level
pitch = 0)  # Tilt level


layer1 = pdk.Layer(type='ScatterplotLayer',  # layer type
data = max_yield_rows,  # data source
get_position = '[lon, lat]',  # coordinates
get_radius = 1500,  # scatter radius
get_color = [100, 250, 30],  # scatter color
pickable = False  # work with tooltip
)


layer2 = pdk.Layer('ScatterplotLayer',
data = max_yield_rows,
get_position = '[lon, lat]',
get_radius = 1500,
get_color = [0, 0, 255],
pickable = True
)


# stylish tool tip: https://pydeck.gl/tooltip.html?highlight=tooltip
tooltip = {   "html": "Location: <b>{WEAPON_DEPLOYMENT_LOCATION}</b>",
    "style": {"backgroundColor": "white", "color": "steelblue"}}


# Create a map based on the view, layers, and tool tip
map = pdk.Deck(
map_style = 'mapbox://styles/mapbox/outdoors-v11',  # Go to https://docs.mapbox.com/api/maps/styles/ for more map styles
initial_view_state = view_state,
layers = [layer1, layer2],  # The following layer would be on top of the previous layers
tooltip = tooltip
)

st.pydeck_chart(map)

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def set_theme():
    # Update the default Streamlit theme
    st.markdown(
        """
        <style>
        .stApp {
            background-color: lightgoldenrodyellow; /* Change this to the color you desire */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# Call the set_theme function to apply the custom theme
set_theme()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Bombs per year")
df_nuclear = pd.read_csv("nuclear_explosions.csv")

#[DA 1]
df_nuclear = df_nuclear.sort_values(by='Data.Magnitude.Surface', ascending= True)





years = []
for row in df_nuclear.itertuples():
    if row.Date_Year not in years:
        years.append(row.Date_Year)

from PIL import Image
img = Image.open("nuclear bombs.jpeg")
st.image(img, width= 500)

#[ST1]
slider_number = st.slider("Please select the year ypu would like to how many bombs were dropped", years[0],years[-1])


from PIL import Image

Suma = 0  # Initialize LOLA outside the loop
for row in df_nuclear.itertuples():
    if row.Date_Year == slider_number:  # Convert year to string for comparison
        Suma += 1


st.write("The amount of bombs dropped in",slider_number,"is",Suma)


df_selected_year = df_nuclear[df_nuclear['Date_Year'] == int(slider_number)]

# Plot distribution of weapon source countries for the selected year
if Suma > 0:
    df_selected_year['WEAPON_SOURCE_COUNTRY'].value_counts().plot(kind='bar',color=["red", "orange", "blue", "green", "yellow"])
    plt.xlabel("Source Countries")
    st.pyplot()




st.title("Bombs Dropped Over Years by Country")
df_nuclear['Date_Year'] = pd.to_datetime(df_nuclear['Date_Year'], format='%Y')


bombs_dropped_by_year_country = df_nuclear.groupby(['Date_Year', 'WEAPON_SOURCE_COUNTRY']).size().unstack(fill_value=0)




#[VIZ1]
# Display the line chart
st.line_chart(bombs_dropped_by_year_country)


