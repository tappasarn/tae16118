from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in meter = 6371000

lat1 = radians(13.7569891624617)
lon1 = radians(100.6189513206482)
lat2 = radians(13.7569991624617)
lon2 = radians(100.6189613206482)

dlon = lon2 - lon1
dlat = lat2 - lat1
#calculation equation
a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = float("6371000") * c

print("Result:", distance," meters")
