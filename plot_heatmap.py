from mpl_toolkits.basemap import Basemap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Using resolution='i' for faster runtime. Dealing with the mapping is food for 
# thought, because it's really wasteful to draw the full earth just to look at 
# a 30 km radius.
m = Basemap(llcrnrlon=24.65 ,llcrnrlat=60.1, urcrnrlon=25.1, urcrnrlat=60.3, projection='merc', resolution='i')
m.drawcoastlines(linewidth=0.25)
m.fillcontinents(color='#202020',lake_color='w')
m.drawmeridians(np.arange(0,360,0.025))
m.drawparallels(np.arange(-90,90,0.025))
plt.savefig('running.png')
