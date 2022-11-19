# Eddited by Nolan Kelley

from cmath import sqrt

speed_of_light = 2999792458

def star_travel_time(distanceInLightYears,percent_light_speed):
    
    distanceInMeters = distanceInLightYears * (9460800000000000)
    speedInMetersPerSecond = (speed_of_light * (percent_light_speed/100))
    #print(speedInMetersPerSecond)

    factor = 1/(sqrt(1-(speedInMetersPerSecond**2/speed_of_light**2)))
    #print(factor)

    timeInSeconds = (distanceInMeters/speedInMetersPerSecond)/factor
    #print(timeInSeconds)
    timeInYears = (timeInSeconds/(3.154*(10**7))*10)
    return (timeInYears)

# To call the function, type star_travel_time() in the file, typing the distance in light years and percentage of the speed of light in the parenthases (in that order.)
# E.g. 1) : For a star 4.4 light years away and a ship moving 1/2 the speed of light, type: star_travel_time(4.4,50)

print(star_travel_time(4.4,50))
print(star_travel_time(6.0,50))
print(star_travel_time(640,50))
print(star_travel_time(2500000,50))