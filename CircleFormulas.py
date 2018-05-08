#!/usr/bin/env python3

import math
from sys import argv 

script, selection, radius = argv

radius = float(radius)

def volumeSphere(radius):
    volume = (4.0/3.0) * math.pi * (radius**3)
    return volume

def surfaceAreaSphere(radius):
    surfaceArea = 4 * math.pi * (radius**2)
    return surfaceArea 

def circumferenceSphere(radius):
    circumference = 2 * math.pi * radius
    return circumference

if radius >= 0:
    print('-' * 60)
    if selection == "-v":
        result = volumeSphere(radius)
        print("Volume of sphere: ")
        print("Radius: "+ str(radius)) 
        print("Volume: " + str(result) + " units cubed")
    elif selection == "-sa":
        result = surfaceAreaSphere(radius)
        print("Surface area of sphere: ")
        print("Radius: "+ str(radius)) 
        print("Surface area: " + str(result) + " units squared")
    elif selection == "-c":
        result = circumferenceSphere(radius)
        print("Circumference of sphere: ")
        print("Radius: "+ str(radius)) 
        print("Circumference: " + str(result) + " units")
    else:
        print("\t\t*****-Invalid command-*****")
        print("Available commands:")
        print("\t-v for volume")
        print("\t-sa for surface area")
        print("\t-c for circumference")
    print('-' * 60)
else:
    print("Radius must be greater than or equal to zero.")


