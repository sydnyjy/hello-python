import sys

winds = float(sys.argv[1])

if winds >= 220:
    print("Super Typhoon")
elif winds >= 118 or winds == 219.99:
    print("Typhoon")
elif winds >=89 or winds == 117.99:
    print("Severe Tropical Storm")
elif winds >=62 or winds == 88.99:
    print ("Tropical Storm")
else:
    print("Tropical Depression")