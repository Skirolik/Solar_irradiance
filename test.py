import numpy as np
import pvlib
import pandas as pd
import matplotlib.pyplot as plt
from pvlib.location import Location
from zoneinfo import ZoneInfo
import matplotlib.dates as mdates

from datetime import datetime

lat, lon = 12.94519, 77.554416

site=Location(12.94519,77.554416,'Asia/Kolkata',920,'Banglore')


times=pd.date_range('2023-3-08 00:00:00','2023-3-08 23:59:00', closed='left', freq='H', tz=site.tz)

# solpos = site.get_solarposition(times)

solpos= pvlib.solarposition.get_solarposition(times,site.latitude,site.longitude,site.altitude,method='pyephem')


irradance= pvlib.irradiance.get_total_irradiance(0, 0, solpos.loc['2023-03-08'].zenith, solpos.loc['2023-03-08'].azimuth, dni, ghi, dhi, dni_extra=None, airmass=None, albedo=0.25, surface_type=None, model='isotropic', model_perez='allsitescomposite1990')

print(solpos)
solpos.head()




# Plots for solar zenith and solar azimuth angles
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle('Solar Position Estimation in ' + site.name + ' 7th MArch')

# plot for solar zenith angle
ax1.plot(solpos.loc['2023-03-08'].zenith)
ax1.set_ylabel('Solar zenith angle (degree)')
ax1.set_xlabel('Time (hour)')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H'))


# plot for solar azimuth angle
ax2.plot(solpos.loc['2023-03-08'].azimuth)
ax2.set_ylabel('Solar azimuth angle (degree)')
ax2.set_xlabel('Time (hour)')
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
plt.grid()


plt.show()