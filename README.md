
# Culver's Locations Clustering Project Overview

This project applies K-Means clustering to analyze the geographic distribution of Culver’s restaurant locations across the continental United States. By grouping locations into clusters, we can identify regional concentrations and gain insights into market density and potential expansion areas.   <br>   
Dataset Description: A CSV file containing Culver’s restaurant locations, with columns Longitude and Latitude.

## Preprocessing:
 - Removed entries outside the continental U.S. by filtering longitudes > -130 and latitudes > 22.
 - Dropped any missing coordinate values.


## Resulting Data:
 - Approximately N locations (after filtering) across 26 states.  
 - Clustering: Used sklearn.cluster.KMeans with n_clusters=10 to partition the locations into 10 clusters.  

## Visualization:
 - Loaded U.S. state boundaries from a public GeoJSON file.
 - Plotted the state lines as a background on a dark-style Matplotlib figure.
 - Overlayed the clustered Culver’s locations, color-coded by cluster label.
 - Marked cluster centroids with red X markers.  <br> <br>

   

### Market Density Insights:
Denser clusters around Chicago suburbs, Detroit, and all of Wisconsin highlight regions with high Culver’s concentration, which could inform marketing strategies or resource allocation.
Cluster Centers: The red X markers show central points for each cluster. These centroids can suggest potential hub locations for distribution or service centers.  <br>


![culvers123](https://github.com/user-attachments/assets/0c33559d-071d-4e84-bd33-9b4f502caf9a)
