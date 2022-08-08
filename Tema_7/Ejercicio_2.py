import time

H,M=time.strftime('%H'),time.strftime('%M')

if int(H) >= 19:
    print ("Es hora de irse a casa") 
else:
    print ('Quedan '+H+' horas y '+M+' minutos para irnos a casa')