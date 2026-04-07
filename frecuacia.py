import customtkinter as ctk

def PruebaDeFreeuencais(lista: list) -> bool:
    contante = ""

    lisat2 = lista[:]
    num = 1
    for i in range(2, len(lisat2)):
        if len(lisat2) % i == 0:
            num = i
            break

    contante += (f"Frecuecia esperada {len(lista) / num} \n")
    valor_k = num
    contante += (f"los intervalos son de {1 / num} \n")
    lista_de_intervalos = []
    valor = 0
    while valor <= 1:
        lista_de_intervalos.append(valor)
        valor += 1 / num

    contante += (f"lista de intervalos: {lista_de_intervalos} \n")

    lisat2.sort()

    lista_auxiliar = []
    superLIsta = []

    for i in range(len(lista_de_intervalos) - 1):
        lista_auxiliar = []
        for num in lisat2:
            if num > lista_de_intervalos[i] and num < lista_de_intervalos[i + 1]:
                lista_auxiliar.append(num)
        superLIsta.append(lista_auxiliar)
    contante += f"lista de valores separados: {superLIsta} \n"
    frecuencia_esperada = len(lista) / len(superLIsta) 
    
    acumulador = 0
    for i in range(len(superLIsta)):
        ListaExtraida = superLIsta[i]
        fo = len(ListaExtraida) 
        
        operacion = (fo - frecuencia_esperada) ** 2
        operacion = operacion / frecuencia_esperada
        
        acumulador += operacion

    ventana_dialogo = ctk.CTkInputDialog(
        text=f"Introduce el número de xi considerando un valor de k = {valor_k - 1} :",
        title="Configuración Chi-Cuadrada"
    )

    xi = float(ventana_dialogo.get_input())

    contante += f"Resultado de la formula: {acumulador} "
    if acumulador < xi:
        contante += ("se haceptan los aleatoresos")
    else:
        contante += ("no hace hacepta")

    return contante


class frecuacual:
    def __init__(self, lista):
        ventanita = ctk.CTkToplevel()
        ventanita.geometry("1000x700")
        ventanita.title("Método de Comprobación Frecuencial")

        self.titulo_lista = ctk.CTkLabel(ventanita, text="Lista de Aleatorios:", font=("Arial", 14, "bold"))
        self.titulo_lista.place(relx=0.05, rely=0.05)

        self.txt_lista = ctk.CTkTextbox(ventanita, width=250, height=400, font=("Consolas", 12))
        self.txt_lista.place(relx=0.05, rely=0.1)
        
  
        texto_lista = "\n".join([f"[{i+1}] -> {val}" for i, val in enumerate(lista)])
        self.txt_lista.insert("0.0", texto_lista)
        self.txt_lista.configure(state="disabled") 

        self.titulo_res = ctk.CTkLabel(ventanita, text="Resultados de la Prueba:", font=("Arial", 14, "bold"))
        self.titulo_res.place(relx=0.4, rely=0.35)

        self.txt_resultados = ctk.CTkTextbox(ventanita, width=1600, height=500, font=("Consolas", 13))
        self.txt_resultados.place(relx=0.4, rely=0.4)

        def ejecutar_prueba():
            self.txt_resultados.delete("0.0", "end")
            
            constante = PruebaDeFreeuencais(lista)
            
            self.txt_resultados.insert("0.0", f"{constante}")

        self.boton = ctk.CTkButton(ventanita, text="Ejecutar Prueba Chi-Cuadrada", command=ejecutar_prueba)
        self.boton.place(relx=0.4, rely=0.15)

        ventanita.mainloop()