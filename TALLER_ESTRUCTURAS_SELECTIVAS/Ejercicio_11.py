#Entrada
t=float(input("Ingrese la temperatura: "))
#Casa negra
deporte=""
if(t>85 and t<=100):
    deporte="Natación"
elif(t>=71 and t<=85):
    deporte="Tenis"
elif(t>=33 and t<=70):
    deporte="Golf"
elif(t>11 and t<=32):
    deporte="Esquí"
elif(t>-5 and t<=10):
    deporte="Marcha"
else:
    deporte="😮 Que es esooooooo!"
#Salida
print("El deporte a practicar es:",deporte)
