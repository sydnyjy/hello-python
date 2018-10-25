import sys

winds = float(sys.argv[1])


if winds >= 220:
   print ("Super Typhoon")
elif winds >= 118 or winds == 220 :
   print ("Typhoon")
elif winds >= 89 or winds == 117:
    print ("Severe Trpoical Storm")
elif winds >= 62 or winds == 88:
     print ("Trpoical Storm")
else: 
      print ("Trpoical Depression")