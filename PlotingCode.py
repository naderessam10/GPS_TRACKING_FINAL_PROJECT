# import gmplot package
import gmplot
from numpy import loadtxt
  
  
latitude_list = loadtxt("lattiude.txt", comments="#", delimiter=",", unpack=False)
longitude_list = loadtxt("longitude.txt", comments="#", delimiter=",", unpack=False)

# for e in latitude_list:
#     print(e)

# latitude_list = [ 30.3358376, 30.307977, 30.3216419 ]
# longitude_list = [ 77.8701919, 78.048457, 78.0413095 ]
  
gmap3 = gmplot.GoogleMapPlotter(30.290539,
                                31.758783, 13)
  
# scatter method of map object 
# scatter points on the google map
gmap3.scatter( latitude_list, longitude_list, '# FF0000',
                              size = 2, marker = False )
  
# Plot method Draw a line in
# between given coordinates
gmap3.plot(latitude_list, longitude_list, 
           'cornflowerblue', edge_width = 0.1)
  
gmap3.draw( "testFinal.html" )