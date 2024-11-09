from datetime import datetime
import glob

import gpxpy
import numpy as np
import plotly.express as px

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
                    name = datetime.strftime(point.time, "%Y-%m-%d")
                    t.append((point.latitude, point.longitude, name))
            tracks.append(t)

lats = []
lons = []
names = []                
c = "#00ffff"
for track in tracks:
    y, x, t = zip(*track)
    lats.extend(y)
    lons.extend(x)
    names.extend(t)
    # cutting the legs
    lats.append(float("nan"))
    lons.append(float("nan"))
    names.append(float("nan"))

map_style="carto-darkmatter"
colors = [c]*len(lats)

fig = px.line_map(
                  lat=lats, 
                  lon=lons, 
                  hover_name=names, 
                  map_style=map_style, 
                 )

fig.update_traces(line_color="cyan")
fig.update_traces(line={'width': 0.2})

fig.write_html('running.html')
