''' def mcd(n1, n2):
    if n1 > n2:
        small = n2
    else:
        small = n1

    for i in range(1, small+1):
        if((n1 % i == 0) and (n2 % i == 0)):
            calc_mcd = i
    return calc_mcd '''

''' def exponente(n):
    if n % 2 != 0:
        n = n - 1
        print('n', n)
    
    i = 2
    cont = 0
    while i <= n:
        i = 2 * i
        cont = cont + 1
        print(i)
        print(cont)
    
    return cont '''

''' def panprimo(n):
    cont_panprimo = 0
    cont_primo = 1

    cadena = str(n)

    if '0' in cadena and '1' in cadena and '2' in cadena and '3' in cadena and '4' in cadena and '5' in cadena and '6' in cadena and '7' in cadena and '8' in cadena and '9' in cadena:
        cont_panprimo = 1

    num = n % 1000
    for aux in range(2, num):
        if num % aux == 0:
            cont_primo = 0
    
    if cont_panprimo == 1 and cont_primo == 1:
        return True
    else:
        return False '''

''' print(panprimo(10123485769)) '''