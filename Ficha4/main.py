def alineaa():
    for i in range (1,6): #para cada i no range 1-6
        for j in range (1,4): #para cada j no range 1-4
            if ( i % j) == 1: # se o i dividido inteiro por j der 1 de resto
                print (i + j) # soma i + j

def alineab():
    i= 20
    while i> 5: # enquanto i maior que 5
        print ( 4 * i ) # mostra 4* o valor de i atual
        i = i -2 # retira 2 ao valor atual
        #print 20*4 18*4 16*4 14*4 12*4 ... 6*4

def alineac():
    for i in range(1): # pa cada i no range 0-1    possivel 0,1
        for j in range(3, 5): # pa cada j no range 3-5   possivel 3,4,5
            for k in range(5, 1, -2): #pa cada k no range 5-1 que incrementa -2
                if (i + j) % 2 == 0: #se i+j for divisivel por 2  possivel 3+1 0+4 1+5
                    print(i, j, k) # mostra o i, j e k  3,1,5  0,4,3

def alinea2():
    soma = 0
    for i in range(20,0,-2):
        soma += 1
    print('Soma = ', soma)

def alinea3(tup):
    res = ()
    for i in range (len(tup)):
        if tup[i]%2 == 0:
            res += (tup[i]) # n funfa ??
    print (res)


def alinea4(tup):
    res = ( )
    for i in range (len(tup)):
        res = res + (tup[i],tup[i],)
    print (res)

def alinea5(tup):
    count = 0
    for i in range (len(tup)):
        if i+1 < len(tup) and tup[i] == tup[i+1]:
            count += 1
    print (count)


#a = (1,2,2,3,4,5,6,7,8,9,9,0)
a = (1,2,3)
if __name__ == '__main__':
    #alineaa()
    #alineab()
    #alineac()
    #alinea2()
    #alinea3(a)
    alinea4(a)
    #alinea5(a)