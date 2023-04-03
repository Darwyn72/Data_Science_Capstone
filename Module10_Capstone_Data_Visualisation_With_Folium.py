#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Launch Sites Locations Analysis with Folium**
# 

# Estimated time needed: **40** minutes
# 

# The launch success rate may depend on many factors such as payload mass, orbit type, and so on. It may also depend on the location and proximities of a launch site, i.e., the initial position of rocket trajectories. Finding an optimal location for building a launch site certainly involves many factors and hopefully we could discover some of the factors by analyzing the existing launch site locations.
# 

# In the previous exploratory data analysis labs, you have visualized the SpaceX launch dataset using `matplotlib` and `seaborn` and discovered some preliminary correlations between the launch site and success rates. In this lab, you will be performing more interactive visual analytics using `Folium`.
# 

# ## Objectives
# 

# This lab contains the following tasks:
# 
# *   **TASK 1:** Mark all launch sites on a map
# *   **TASK 2:** Mark the success/failed launches for each site on the map
# *   **TASK 3:** Calculate the distances between a launch site to its proximities
# 
# After completed the above tasks, you should be able to find some geographical patterns about launch sites.
# 

# Let's first import required Python packages for this lab:
# 

# In[1]:


get_ipython().system('pip3 install folium')
get_ipython().system('pip3 install wget')


# In[3]:


import folium
import wget
import pandas as pd


# In[4]:


# Import folium MarkerCluster plugin
from folium.plugins import MarkerCluster
# Import folium MousePosition plugin
from folium.plugins import MousePosition
# Import folium DivIcon plugin
from folium.features import DivIcon


# If you need to refresh your memory about folium, you may download and refer to this previous folium lab:
# 

# [Generating Maps with Python](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module\_3/DV0101EN-3-5-1-Generating-Maps-in-Python-py-v2.0.ipynb)
# 

# ## Task 1: Mark all launch sites on a map
# 

# First, let's try to add each site's location on a map using site's latitude and longitude coordinates
# 

# The following dataset with the name `spacex_launch_geo.csv` is an augmented dataset with latitude and longitude added for each site.
# 

# In[5]:


# Download and read the `spacex_launch_geo.csv`
spacex_csv_file = wget.download('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv')
spacex_df=pd.read_csv(spacex_csv_file)


# Now, you can take a look at what are the coordinates for each site.
# 

# In[6]:


# Select relevant sub-columns: `Launch Site`, `Lat(Latitude)`, `Long(Longitude)`, `class`
spacex_df = spacex_df[['Launch Site', 'Lat', 'Long', 'class']]
launch_sites_df = spacex_df.groupby(['Launch Site'], as_index=False).first()
launch_sites_df = launch_sites_df[['Launch Site', 'Lat', 'Long']]
launch_sites_df


# In[7]:


# Check the location of lat long coordinates in the df, for example CCAFS LC-40 to select in code
launch_sites_df.iloc[[0],[1,2]]


# Above coordinates are just plain numbers that can not give you any intuitive insights about where are those launch sites. If you are very good at geography, you can interpret those numbers directly in your mind. If not, that's fine too. Let's visualize those locations by pinning them on a map.
# 

# We first need to create a folium `Map` object, with an initial center location to be NASA Johnson Space Center at Houston, Texas.
# 

# In[129]:


# Start location is NASA Johnson Space Center
nasa_coordinate = [29.559684888503615, -95.0830971930759]
site_map = folium.Map(location=nasa_coordinate, zoom_start=10)


# We could use `folium.Circle` to add a highlighted circle area with a text label on a specific coordinate. For example,
# 

# In[108]:


# Create a blue circle at NASA Johnson Space Center's coordinate with a popup label showing its name
circle = folium.Circle(nasa_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
# Create a blue circle at NASA Johnson Space Center's coordinate with a icon showing its name
marker = folium.map.Marker(
    nasa_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'NASA JSC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)


# Now, let's add a circle for each launch site in data frame `launch_sites`
# 

# *TODO:*  Create and add `folium.Circle` and `folium.Marker` for each launch site on the site map
# 

# An example of folium.Circle:
# 

# `folium.Circle(coordinate, radius=1000, color='#000000', fill=True).add_child(folium.Popup(...))`
# 

# An example of folium.Marker:
# 

# `folium.map.Marker(coordinate, icon=DivIcon(icon_size=(20,20),icon_anchor=(0,0), html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'label', ))`
# 

# In[109]:


# Initial the map
site_map = folium.Map(location=nasa_coordinate, zoom_start=5)
# For each launch site, add a Circle object based on its coordinate (Lat, Long) values. In addition, add Launch site name as a popup label


# Create a yellow circle at Launch Site VAFB SLC-4E coordinate with a popup label showing its namne
circle1 = folium.Circle(launch_sites_df.iloc[[3],[1,2]], radius=1000, color='#FFFF00', fill=True).add_child(folium.Popup('Vandenburg Air Force Base SLC-4E'))
# Create a red circle at Launch Site KSC LC-39A coordinate with a icon showing its name
marker1 = folium.map.Marker(
    launch_sites_df.iloc[[3],[1,2]], 
    icon=DivIcon(
        icon_size=(20,20), 
        icon_anchor=(0,0), 
        html='<div style="font-size: 35; color:#00000;"><b>%s</b></div>' % 'VAFB SLC-4E', 
        )
    )
site_map.add_child(circle1)
site_map.add_child(marker1)

                                                          
# Create a red circle at launch Site CCAFS LC-40 coordinate with a popup label showing its name
circle2 = folium.Circle(launch_sites_df.iloc[[0],[1,2]], radius=200, color='#FF0000', fill=True).add_child(folium.Popup('Cape Canaveral AFS LC-40'))
# Create a red circle at Launch Site CCAFS LC-40 coordinate with a icon showing its name
marker2 = folium.map.Marker(
    launch_sites_df.iloc[[0],[1,2]], 
    icon=DivIcon(
        icon_size=(20,20), 
        icon_anchor=(0,0), 
        html='<div style="font-size: 35; color:#000000;"><b>%s</b></div>' % 'CCAFS LC-40',
        )
    )
site_map.add_child(circle2)
site_map.add_child(marker2)


# Create a lime green circle at launch Site CCAFS SCC-40 coordinate with a popup label showing its name
circle3 = folium.Circle(launch_sites_df.iloc[[1],[1,2]], radius=200, color='#00FF00', fill=True).add_child(folium.Popup('Cape Canaveral AFS SCC-40'))
# Create a lime green circle at Launch Site CCAFS SCC-40 coordinate with a icon showing its name
marker3 = folium.map.Marker(
    launch_sites_df.iloc[[1],[1,2]], 
    icon=DivIcon(
        icon_size=(20,20), 
        icon_anchor=(0,0), 
        html='<div style="font-size: 35; color:#000000;"><b>%s</b></div>' % 'CCAFS SCC-40', 
        )
    )
site_map.add_child(circle3)
site_map.add_child(marker3)


# Create a yellow circle at Launch Site KSC LC-39A coordinate with a popup label showing its namne
circle4 = folium.Circle(launch_sites_df.iloc[[2],[1,2]], radius=1000, color='#FFFF00', fill=True).add_child(folium.Popup('Kennedy Space Center LC-39A'))
# Create a red circle at Launch Site KSC LC-39A coordinate with a icon showing its name
marker4 = folium.map.Marker(
    launch_sites_df.iloc[[2],[1,2]], 
    icon=DivIcon(
        icon_size=(20,20), 
        icon_anchor=(0,0), 
        html='<div style="font-size: 35; color:#00000;"><b>%s</b></div>' % 'KSC LC-39', 
        )
    )
site_map.add_child(circle4)
site_map.add_child(marker4)


# The generated map with marked launch sites should look similar to the following:
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/launch_site_markers.png" />
# </center>
# 

# Now, you can explore the map by zoom-in/out the marked areas
# , and try to answer the following questions:
# 
# 1)  Are all launch sites in proximity to the Equator line?
# 2)  Are all launch sites in very close proximity to the coast?
# 
# Also please try to explain your findings.
# 
# ## 1) No both sites are over 3000 km from the Equator, all though this is relative in comparison to the distance of both sites to the poles. 
# ##     Cape Canavaral is closest, approx 3600 km north of the Equator, Vandenburg is further, approx. 5800 km North. The closer to the Equator, the easier it is 
# ##     to launch heavy payloads into Earth orbit using the spin of the Earth
# 
# ## 2) Both launch sites are very close to the coast, in the case of Cape Canavaral forexample, less than 900 m. 
# 

# # Task 2: Mark the success/failed launches for each site on the map
# 

# Next, let's try to enhance the map by adding the launch outcomes for each site, and see which sites have high success rates.
# Recall that data frame spacex_df has detailed launch records, and the `class` column indicates if this launch was successful or not
# 

# In[61]:


spacex_df.tail(6)


# Next, let's create markers for all launch records.
# If a launch was successful `(class=1)`, then we use a green marker and if a launch was failed, we use a red marker `(class=0)`

# Note that a launch only happens in one of the four launch sites, which means many launch records will have the exact same coordinate. Marker clusters can be a good way to simplify a map containing many markers having the same coordinate.
# 

# Let's first create a `MarkerCluster` object
# 

# In[62]:


marker_cluster = MarkerCluster()


# *TODO:* Create a new column in `launch_sites` dataframe called `marker_color` to store the marker colors based on the `class` value
# 

# In[63]:


# Apply a function to check the value of `class` column
# If class=1, marker_color value will be green
# If class=0, marker_color value will be red


# Function to assign color to launch outcome
def assign_marker_color(launch_outcome):
    if launch_outcome == 1:
        return 'green'
    else:
        return 'red'
    
spacex_df['marker_color'] = spacex_df['class'].apply(assign_marker_color)
#spacex_df.tail(6)


# *TODO:* For each launch result in `spacex_df` data frame, add a `folium.Marker` to `marker_cluster`
# 

# In[64]:


# Add marker_cluster to current launch site_map
site_map.add_child(marker_cluster)

# for each row in spacex_df data frame
# create a Marker object with its coordinate
# and customize the Marker's icon property to indicate if this launch was successed or failed, 
# e.g., icon=folium.Icon(color='white', icon_color=row['marker_color']

# for loop to add markers to the lauch sites and colour by success or not marker colour is Alice Blue
for index, row in spacex_df.iterrows():   
     folium.map.Marker(
                   (row['Lat'], row['Long']), icon=folium.map.Icon(color='lightgray', icon_color=row['marker_color'])).add_to(marker_cluster)

site_map.add_child(marker_cluster)

#show the map 
site_map


# Your updated map may look like the following screenshots:
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/launch_site_marker_cluster.png" />
# </center>
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/launch_site_marker_cluster_zoomed.png" />
# </center>
# 

# From the color-labeled markers in marker clusters, you should be able to easily identify which launch sites have relatively high success rates.
# 

# # TASK 3: Calculate the distances between a launch site to its proximities
# 

# Next, we need to explore and analyze the proximities of launch sites.
# 

# Let's first add a `MousePosition` on the map to get coordinate for a mouse over a point on the map. As such, while you are exploring the map, you can easily find the coordinates of any points of interests (such as railway)
# 

# In[110]:


# Add Mouse Position to get the coordinate (Lat, Long) for a mouse over on the map
formatter = "function(num) {return L.Util.formatNum(num, 5);};"
mouse_position = MousePosition(
    position='topright',
    separator=' Long: ',
    empty_string='NaN',
    lng_first=False,
    num_digits=20,
    prefix='Lat:',
    lat_formatter=formatter,
    lng_formatter=formatter,
)

site_map.add_child(mouse_position)
site_map


# Now zoom in to a launch site and explore its proximity to see if you can easily find any railway, highway, coastline, etc. Move your mouse to these points and mark down their coordinates (shown on the top-left) in order to the distance to the launch site.
# 

# *TODO:* Mark down a point on the closest coastline using MousePosition and calculate the distance between the coastline point and the launch site.
# 

# In[111]:


# find coordinate of the closet coastline point to the CCAFS, VAFB launch sites (taken as centre) to coast
# rail, highways and major urban centres

CCAFS_coast = [28.56176, -80.56781] # Florida coast
VAFB_coast = [34.63554, -120.62521] # California coast

CCAFS_rail = [28.57239, -80.58506] # Florida East Coast rail
VAFB_rail = [34.63617, -120.62383] # Lompoc Inducstrial Lead

CCAFS_road = [28.52979, -80.79011] # Highway US-1
VAFB_road = [34.63617, -120.63617] # Highway CA-1

CCAFS_city = [28.61231, -80.8073] # Titusville
VAFB_city = [34.63886, -120.45796] # Lompoc


# In[118]:


# Due to errors, re-define the launch_sites.df database
# display table
spacex_df = spacex_df[['Launch Site', 'Lat', 'Long', 'class']]
launch_sites_df = spacex_df.groupby(['Launch Site'], as_index=False).first()
launch_sites_df = launch_sites_df[['Launch Site', 'Lat', 'Long']]
launch_sites_df


# In[156]:


# As an example get the values for latitude and Longitude for the closet points to Cape Canavaral CCAFS LC-40
# This is not efficient, really need a 

lat1 = CCAFS_coast[0]
lon1 = CCAFS_coast[1]
lat2 = launch_sites_df.iloc[0,1]
lon2 = launch_sites_df.iloc[0,2]

lat3 = CCAFS_rail[0]
lon3 = CCAFS_rail[1]

lat5 = CCAFS_road[0]
lon5 = CCAFS_road[1]

lat7 = CCAFS_city[0]
lon7 = CCAFS_city[1]

lat9 = VAFB_city[0]
lon9 = VAFB_city[1]
lat10 = launch_sites_df.iloc[3,1]
lon10= launch_sites_df.iloc[3,2]


# You can calculate the distance between two points on the map based on their `Lat` and `Long` values using the following method:
# 

# In[125]:


distance_coastline = calculate_distance(lat1, lon1, lat2, lon2)


# In[126]:


from math import sin, cos, sqrt, atan2, radians

def calculate_distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


# *TODO:* After obtained its coordinate, create a `folium.Marker` to show the distance
# 

# In[140]:


# Create and add a folium.Marker on your selected closest coastline point on the map 
# Display the distance between coastline point and launch site using the icon property 
# example = CCAFS LC-40 (centre) to Florida coastline

coordinates = [lat1, lon1]
distance = distance_coastline
distance_marker = folium.Marker(
   coordinates,  
   icon=DivIcon(
       icon_size=(20,20),
       icon_anchor=(0,0),
       html='<div style="font-size: 18; color:#00000;"><b>%s</b></div>' % "{:10.2f} KM".format(distance)
       )
   )
site_map.add_child(distance_marker)


# *TODO:* Draw a `PolyLine` between a launch site to the selected coastline point
# 

# In[142]:


# Create a `folium.PolyLine` object using the coastline coordinates and launch site coordinate


coordinates =[[lat1, lon1], [lat2, lon2]]
lines=folium.PolyLine(locations=coordinates, weight=5)
site_map.add_child(lines)


# Your updated map with distance line should look like the following screenshot:
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/launch_site_marker_distance.png" />
# </center>
# 

# *TODO:* Similarly, you can draw a line betwee a launch site to its closest city, railway, highway, etc. You need to use `MousePosition` to find the their coordinates on the map first
# 

# A railway map symbol may look like this:
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/railway.png" />
# </center>
# 

# A highway map symbol may look like this:
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/highway.png" />
# </center>
# 

# A city map symbol may look like this:
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/city.png" />
# </center>
# 

# In[144]:


# Create a marker with distance to a closest city, railway, highway, etc.
# Draw a line between the marker (East Florida Railway) to the launch site 

distance_coastline = calculate_distance(lat3, lon3, lat2, lon2)


# In[145]:


from math import sin, cos, sqrt, atan2, radians

def calculate_distance(lat3, lon3, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat3 = radians(lat3)
    lon3 = radians(lon3)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon3
    dlat = lat2 - lat3

    a = sin(dlat / 2)**2 + cos(lat3) * cos(lat3) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


# In[146]:


# Create and add a folium.Marker on your selected closest coastline point on the map 
# Display the distance between coastline point and launch site using the icon property 
# example = CCAFS LC-40 (centre) to railway line Florida East 

coordinates = [lat3, lon3]
distance = distance_coastline
distance_marker = folium.Marker(
   coordinates,  
   icon=DivIcon(
       icon_size=(20,20),
       icon_anchor=(0,0),
       html='<div style="font-size: 18; color:#00000;"><b>%s</b></div>' % "{:10.2f} KM".format(distance)
       )
   )
site_map.add_child(distance_marker)


# In[147]:


# Create a `folium.PolyLine` object using the coastline coordinates and launch site coordinate
# Line from CCAFS LC-40 centre to the Florida East railroad

coordinates =[[lat3, lon3], [lat2, lon2]]
lines=folium.PolyLine(locations=coordinates, weight=5)
site_map.add_child(lines)


# After you plot distance lines to the proximities, you can answer the following questions easily:
# 
# 1)  Are launch sites in close proximity to railways? - Yes, in the case of CCAFS LC-40 the distance is only 1.35 km 
# 2)  Are launch sites in close proximity to highways? - Reasonably close, for example CCAFS LC-40 centre is 21.10 km from the Florida Highway US 1
# 3)  Are launch sites in close proximity to coastline?
# 4)  Do launch sites keep certain distance away from cities?
# 
# Also please try to explain your findings.
# ## 1) Yes, for example CCAFS LC-40 is only 1.35 km from the Florida East Railway 
# 
# ## 2) Reasonably close, for example CCAFS LC-40 is 21.10 km from Florida Highway US-1
# 
# ## 3) Yes, very close, CCAFS LC-40 centre is approx. 900 m from the Florida coastline
# 
# ## 4) Yes, the closest city to CCAFS LC40 is Titusville, at a distance of 23.13 km, however Vandenburg Air Force Base SLC-4E is only 14 km from the launch
# ##     site. Although this site does not launch heavy payloads. Suggests a minimum distance of 10 km from launch site to main towns or habitacion. 

# In[148]:


# Create a marker with distance to a closest city, railway, highway, etc.
# Draw a line between the marker (Florida Highway US1) to the launch site CCAFS LC-40

distance_coastline = calculate_distance(lat5, lon5, lat2, lon2)


# In[149]:


from math import sin, cos, sqrt, atan2, radians

def calculate_distance(lat5, lon5, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat5 = radians(lat5)
    lon5 = radians(lon5)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon5
    dlat = lat2 - lat5

    a = sin(dlat / 2)**2 + cos(lat5) * cos(lat5) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


# In[150]:


# Create and add a folium.Marker on your selected closest coastline point on the map 
# Display the distance between coastline point and launch site using the icon property 
# example = CCAFS LC-40 (centre) to Highway US-1 

coordinates = [lat5, lon5]
distance = distance_coastline
distance_marker = folium.Marker(
   coordinates,  
   icon=DivIcon(
       icon_size=(20,20),
       icon_anchor=(0,0),
       html='<div style="font-size: 18; color:#00000;"><b>%s</b></div>' % "{:10.2f} KM".format(distance)
       )
   )
site_map.add_child(distance_marker)


# In[151]:


# Create a `folium.PolyLine` object using the coastline coordinates and launch site coordinate
# Line from CCAFS LC-40 centre to the Highway US1

coordinates =[[lat5, lon5], [lat2, lon2]]
lines=folium.PolyLine(locations=coordinates, weight=5)
site_map.add_child(lines)


# In[152]:


# Create a marker with distance to a closest city, railway, highway, etc.
# Draw a line between the marker (Titusville) to the launch site CCAFS LC-40

distance_coastline = calculate_distance(lat7, lon7, lat2, lon2)


# In[153]:


def calculate_distance(lat7, lon7, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat7 = radians(lat7)
    lon7 = radians(lon7)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon7
    dlat = lat2 - lat7

    a = sin(dlat / 2)**2 + cos(lat7) * cos(lat7) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


# In[154]:


# Create and add a folium.Marker on your selected closest coastline point on the map 
# Display the distance between coastline point and launch site using the icon property 
# example = CCAFS LC-40 (centre) to Titusville Florida 

coordinates = [lat7, lon7]
distance = distance_coastline
distance_marker = folium.Marker(
   coordinates,  
   icon=DivIcon(
       icon_size=(20,20),
       icon_anchor=(0,0),
       html='<div style="font-size: 18; color:#00000;"><b>%s</b></div>' % "{:10.2f} KM".format(distance)
       )
   )
site_map.add_child(distance_marker)


# In[155]:


# Create a `folium.PolyLine` object using the coastline coordinates and launch site coordinate
# Line from CCAFS LC-40 centre to the townhall in Titusville Florida

coordinates =[[lat7, lon7], [lat2, lon2]]
lines=folium.PolyLine(locations=coordinates, weight=5)
site_map.add_child(lines)


# In[157]:


# Create a marker with distance to a closest city, railway, highway, etc.
# Draw a line between the marker (Lompoc, California) to the launch site VAFB SLC-4E

distance_coastline = calculate_distance(lat9, lon9, lat10, lon10)


# In[158]:


def calculate_distance(lat9, lon9, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat9 = radians(lat9)
    lon9 = radians(lon9)
    lat10 = radians(lat10)
    lon10 = radians(lon10)

    dlon = lon10 - lon9
    dlat = lat10 - lat9

    a = sin(dlat / 2)**2 + cos(lat9) * cos(lat9) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


# In[159]:


# Create and add a folium.Marker on your selected closest coastline point on the map 
# Display the distance between coastline point and launch site using the icon property 
# example = VAFB SLC-4E (centre) to Lompoc city centre California

coordinates = [lat9, lon9]
distance = distance_coastline
distance_marker = folium.Marker(
   coordinates,  
   icon=DivIcon(
       icon_size=(20,20),
       icon_anchor=(0,0),
       html='<div style="font-size: 18; color:#00000;"><b>%s</b></div>' % "{:10.2f} KM".format(distance)
       )
   )
site_map.add_child(distance_marker)


# In[160]:


# Create a `folium.PolyLine` object using the coastline coordinates and launch site coordinate
# Line from VAFB SLC-4E centre to Lompoc California 

coordinates =[[lat9, lon9], [lat10, lon10]]
lines=folium.PolyLine(locations=coordinates, weight=5)
site_map.add_child(lines)


# # Next Steps:
# 
# Now you have discovered many interesting insights related to the launch sites' location using folium, in a very interactive way. Next, you will need to build a dashboard using Ploty Dash on detailed launch records.
# 

# ## Authors
# 

# [Yan Luo](https://www.linkedin.com/in/yan-luo-96288783/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01)
# 

# ### Other Contributors
# 

# Joseph Santarcangelo
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By | Change Description          |
# | ----------------- | ------- | ---------- | --------------------------- |
# | 2021-05-26        | 1.0     | Yan        | Created the initial version |
# 

# Copyright © 2021 IBM Corporation. All rights reserved.
# 
