# Google Earth Engine Getting Started

[Google Earth Engine (GEE)](https://earthengine.google.com) combines a multi-petabyte catalog of satellite imagery and geospatial datasets with planetary-scale analysis capabilities and makes it available for scientists, researchers, and developers to detect changes, map trends, and quantify differences on the Earth's surface through a cloud based platform. Hence offering the capability of running your algorithms and only requiring to export or visualise the output. The archive includes more than 30 years of historical imagery and scientific datasets, updated and expanded daily. 

For an informative background read on GEE and its applications see the following [hyperlink](https://www.sciencedirect.com/science/article/pii/S0034425717302900?via%3Dihub).

The main [GEE guide](https://developers.google.com/earth-engine) covers everything from installation to available functions and usage, for an extensive range of examples see [here](https://github.com/giswqs/earthengine-py-notebooks). Here we will cover the basic important key points that should walk you through it.


###  Installation

Firstly, you should apply for access to use the GEE. follow this [link](https://code.earthengine.google.com/), if you cannot login yet it will tell you what steps you should follow to apply for access. Do this as soon as possible, I got access within a few minutes, however it says it can take a few days potentially. Referencing you are from Imperial and it is for research should get you access. 

If you decide to access GEE using python you can install geemap which will automatically install all its dependencies like earthengine-api, folium and ipyleaflet. This allows for several methods to intereact with Earh Engine data layers. 

**Important note**: A key difference between folium and ipyleaflet is that ipyleaflet is built upon ipywidgets and allows bidirectional communication between the front-end and the backend enabling the use of the map to capture user input, while folium is meant for displaying static data only. Note that Google Colab currently does not support ipyleaflet. Therefore, if you are using geemap with Google Colab, you should use import geemap.eefolium. If you are using geemap with binder or a local Jupyter notebook server, you can use import geemap, which provides more functionalities for capturing user input (e.g., mouse-clicking and moving).

# Installs geemap package
import subprocess

try:
    import geemap
except ImportError:
    print('geemap package not installed. Installing ...')
    subprocess.check_call(["python", '-m', 'pip', 'install', 'geemap'])

# Checks whether this notebook is running on Google Colab
try:
    import google.colab
    import geemap.eefolium as geemap
except:
    import geemap

# Authenticates and initializes Earth Engine
import ee

try: #authentication only required once for a notebook
    ee.Initialize()
except Exception as e:
    ee.Authenticate()
    ee.Initialize()

# test by creating basemap
Map = geemap.Map(center=[40,-100], zoom=4,)
Map

<img src="GEE_Getting_Started/1.png" style="100%;"/>

###  Google Earth Engine Apps

[GEE apps](https://developers.google.com/earth-engine/apps) are a way to share your results for expert and non-expert audiences alike. It is typically done along with a publication as an easy and accesible way for people to access and interact with the results. Following this [link](https://philippgaertner.github.io/2019/04/earth-engine-apps-inventory/) you can find many examples of these apps and try them out. They can be very useful to obtain an idea of what exists and access some fully functioning examples. 

To clone any of the repositories you can acces the [GEE user list](https://earthengine.googlesource.com/users) and find the project and its git clone link. Firstly, however you will require to obtain access to clone these github repositories, this can be done as follows:
- access this [link](https://earthengine.googlesource.com/users)
- click generate password
- sign in, this needs to be an email with GEE access I believe
- instructions to copy paste into the git prompt will be shown

Now you should be able to freely clone any of the github repositories.

###  Google Earth Engine Code Editor

[GEE code editor](https://developers.google.com/earth-engine/playground) is a web-based IDE for the Earth Engine JavaScript API. Code Editor features are designed to make developing complex geospatial workflows fast and easy.

### Google Earth Engine Database
the [GEE database](https://earthengine.google.com) contains a variety of dataset that can be called within your scripts and be processed on the cloud. Before trying to call a dataset it is recommend to first look through the website. 
For each dataset there is also a few lines of code provided showing how to best access it and best colour palettes to be used.

###  General Guidance 

- Using Azure notebook I encountered many problems regarding package versions not agreeing, using Jupyter via the Anaconda environment or google collab gave me zero problems
- GEE has many built-in functions, make sure to look through the linked documentation before attempting to write a function for it
- GEE has a per user [quota](https://developers.google.com/earth-engine/usage ) on concurrent queries. If needed however you can apply for more
