def tempsEnSeconde(temps):
    tempsEnSeconde = temps[0]*24*3600 + temps[1]*3600 + temps[2]*60 + temps[3]
    return tempsEnSeconde

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    temps[1] = (seconde%86400)//3600
    temps[2] = ((seconde%86400)%3600)//60
    temps[3] = (seconde%86400)%3600)%60)
    return temps


temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")