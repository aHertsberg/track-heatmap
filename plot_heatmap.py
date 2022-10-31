import glob

import gpxpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

plt.figure(dpi=800)
# Using resolution='i' for faster runtime. Dealing with the mapping is food for 
# thought, because it's really wasteful to draw the full earth just to look at 
# a 30 km radius.
m = Basemap(llcrnrlon=24.65 ,llcrnrlat=60.125, urcrnrlon=25.1, urcrnrlat=60.3, projection='merc', resolution='i')
m.drawcoastlines(linewidth=0.01)
m.fillcontinents(color='#202020',lake_color='w')

# Read tracks from dir containing all tracks desired to be plotted
track_files = glob.glob("tracks/*.GPX")
tracks = []
for f in track_files:
    with open(f, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)
        for track in gpx.tracks:
            t = []
            for segment in track.segments:
                for point in segment.points:
                    t.append((point.latitude, point.longitude))
            tracks.append(t)
                
for track in tracks:
    y, x = zip(*track)
    cs = m.plot(x, y, c='aqua', linewidth=0.1, latlon=True)

plt.savefig('running.png')
