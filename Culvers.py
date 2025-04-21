import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import geopandas as gpd


# This GeoJSON file outlines US state boundaries and avoids shapefile encoding issues.
us_states = gpd.read_file("https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json")


# raw data from https://www.culvers.com/stories/signature-stories/culvers-locations-by-state
culvers_df = pd.read_csv("culvers_locations.csv")

# Select only the Longitude and Latitude columns and drop any rows with missing values.
culvers = culvers_df[["Longitude", "Latitude"]].dropna().to_numpy()

# Optional filtering: Remove any points that fall outside the continental U.S.
#culvers = culvers[culvers[:, 0] > -130]  # Filter by longitude
#culvers = culvers[culvers[:, 1] > 22]      # Filter by latitude


num_clusters = 10  # Set the number of clusters (this can be adjusted)
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(culvers)

# Retrieve the cluster labels and cluster centers.
labels = kmeans.labels_
centers = kmeans.cluster_centers_



# Plotting Section
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 9))

# Plot the US states GeoJSON boundaries as a background.
us_states.plot(ax=ax, color='none', edgecolor='white')

# Overlay the Culver’s points colored by cluster label (similar to the Walmart example).
ax.scatter(culvers[:, 0], culvers[:, 1], c=labels, cmap='viridis', s=20, alpha=0.6)

# Plot the cluster centers with red 'X' markers.
ax.scatter(centers[:, 0], centers[:, 1], c='red', s=100, marker='X', label='Cluster Centers')

# Set axis limits to focus on the continental United States.
ax.set_xlim(-130, -60)
ax.set_ylim(22, 50)
ax.set_title("K-Means Clustering of Culver's Locations on US States Map")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.legend()

plt.show()
