#Python script to convert Logic Friday generated equations to CUPL syntax

while(True):
    finalEqu = ''
    equ = input()
    finalEqu+=equ.split(' = ')[0]+'='
    products = equ.split(' = ')[1].split(' + ')
    for i in range(len(products)):
        finalEqu+='('
        terms = products[i].split(' ')
        for j in range(len(terms)):
            if len(terms[j])==2:
                finalEqu+='!'
            finalEqu+=terms[j][0]
            if j!=len(terms)-1:
                finalEqu+='&'
        finalEqu+=')'
        if i!=len(products)-1:
            finalEqu+='#'
    print(finalEqu,';')
                
    
