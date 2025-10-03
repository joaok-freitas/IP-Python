#se hr =< 40 s= hr*s se hr>40 s = 40*s + hr-40*s*2

hrs = int(input("Número de horas -> "))
slr = float(input("Salário por hora ->"))
res = 0
if hrs <= 40:
    res = hrs*slr
if hrs >=40:
    res = 40*slr + (hrs-40)*slr*2

print(res,"€")
