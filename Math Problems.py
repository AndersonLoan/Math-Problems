import math
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderson Wayne Loan
# Section: 575
# Assignment: Lab 1.11 Print Math
# Date: 28/08/2020
#

#calculating force
mass = 3
acl = 5.5
force = (mass * acl)

#calculating wavelength
distance = 0.025
angle = math.radians(25)
wavelength = (2*distance) * (math.sin(angle))
x = math.sin(angle)

#calculating left over radon
halflife = 3.8
days = 3
initial = 5
radon = initial * (2 ** (-days / halflife))

#Calculating Pressure 
gasc = 8.314
moles = 5
volume = 0.25
temp = 415
pressure = ((moles * gasc * temp) / volume) / 1000

print("Force is "+ str(force) + " N")
print("Wavelength is " + str(wavelength) + " nm")
print("Radon-222 left is " + str(radon) + " g")
print("Pressure is " + str(pressure) + " kPa")

