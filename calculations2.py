TGK = 7.45

tijd = input('hoelang wil je op de vipvr')
tijs2 = 9
VPVR = 0.078

TTPR = (VPVR * tijs2)
TTPR2 = (TGK + TTPR)
print("het verblijf bij de speel kost 7.45 en we willen 45 minuten in het vipVR wat 0.39 per 5 minuten kost" + str(TGK) + "+" + str(tijd) + "*" + str(VPVR) + "=" + str(TTPR) + "plus de verblijf kosten is" + str(TTPR2) )

if TTPR == 44.44:
    print("Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 44.44 euro")