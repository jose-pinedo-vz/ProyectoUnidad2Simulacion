def congruencial(n: int, itera: int) -> str:
    cadena = ""
    lista = []
    V = [3, 11, 13, 14, 21, 23, 24, 27, 53, 59, 64, 69, 77,
     83, 91, 113, 117, 123, 131, 133, 141, 147, 163,
     171, 173, 179, 181, 187, 189, 197]
    
    e = len(str(n))
    cadena += (f"e: {e} - 2e: {2*e} \n")
    a = 0
    a2 = 0
    t = 0 
    objetivo = 10**(e / 2)
    cadena += (f"valor de 10^e / 2 {objetivo} \n ")
    error = 200
    a1 = 0 
    a2 = 0
    a = 0
    valor = 0

    while True:
        error_antes = error
        for num in V:
            a1 = 200 * t + num
            a2 = 200 * t - num

            err1 = abs(objetivo - a1)
            err2 = abs(objetivo - a2)

            a = min(err1, err2)

            if a < error:
                error = a
                valor = a1 if err1 < err2 else a2

        if error == error_antes:
            break
        
        t += 1

    cadena += (f"valor del arreglo mas serca {valor}, con t: {t - 1} \n")

    cadena += (f"semilla: {n} \n")
    n = int(n)
    aleatorio = 0

    for j in range(itera):
        aleatorio = valor * n
        cadena += (f"formula a(n) {n}*{valor} = {aleatorio} ")
        n = ""
        aleatorio = str(aleatorio)
        
        ceros = ""
        for i in range(e*2 - len(aleatorio)):
            ceros += "0"

        aleatorio = ceros + aleatorio
        cadena += (f"aleatirio: {(int(aleatorio[e:]) / 10**e)} \n")
        lista.append(int(aleatorio[e:]) / 10**e)
        n = int(aleatorio[e:])

    return cadena, lista
        





        
