import datetime
import matplotlib.pyplot as plt
import pysolar

lat, lon = 12.94519, 77.554416 #Banglore
timezone= datetime.timezone(datetime.timedelta(hours=5, minutes=30))

start= datetime.datetime(2023,2,24,tzinfo=timezone)

#Raditaion Calculation for everyhour

nhr=24*90

dates,altitudes_deg,radiations= list(),list(),list()

for ihr in range(nhr):
    date=start+datetime.timedelta(hours=ihr)
    altitude_deg = pysolar.solar.get_altitude(lat,lon,date)
    if altitude_deg<=0:
        radiation=0
    else:
        radiation=pysolar.radiation.get_radiation_direct(date,altitude_deg)
    dates.append(date)
    altitudes_deg.append(altitude_deg)
    radiations.append(radiation)

days=[ihr/24 for ihr in range(nhr)]
fig,axis=plt.subplots(nrows=2,ncols=1,sharex=True)
axis[0].plot(days,altitudes_deg)
axis[0].set_title('Solar Altitude, degrees')
axis[1].plot(days,radiations)
axis[1].set_title('Solar Radiation')
axis[1].set_xlabel('Days since ' + start.strftime('%Y/%m/%d %H:%M IST'))
plt.show()


