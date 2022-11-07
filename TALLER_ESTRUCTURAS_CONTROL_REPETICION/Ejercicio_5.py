ñ=0
sumatoria=0
for k in range(1,1000):
    if(sumatoria<=1000):
        sumatoria=sumatoria+((k**2)+1)/k
        if(sumatoria<=1000):
            ñ=ñ+1
    else:
        break
assert(ñ==44)
print("Prueba superada😎")
