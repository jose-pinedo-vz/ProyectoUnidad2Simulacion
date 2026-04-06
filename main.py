"""
Base sentral de la interfaz, si le mueven que sea con cuidado
"""
import customtkinter as ctk


class InterfazPrincipal:
    def __init__(self):
        self.VentanaP = ctk.CTk()
        self.VentanaP.title("Unidad 2 simulacion")
        
        try: self.VentanaP.state('zoomed')
        except: self.VentanaP.attributes('-zoomed', True)

        self.CuadradosMedios = ctk.CTkButton(self.VentanaP, text="Cuadrados medios")
        self.CuadradosMedios.pack(pady=20, padx=20)

        self.CongruencialM = ctk.CTkButton(self.VentanaP, text="Congruencial mixto")
        self.CongruencialM.pack(pady=20, padx=20)

        self.CongruencialMul = ctk.CTkButton(self.VentanaP, text="Congruencial multiplicativo")
        self.CongruencialMul.pack(pady=20, padx=20)

        self.LineasDeEspera = ctk.CTkButton(self.VentanaP, text="Lineas de espra")
        self.LineasDeEspera.pack(pady=20, padx=20)

        self.TeoriaIn = ctk.CTkButton(self.VentanaP, text="Teoria de inventarios")
        self.TeoriaIn.pack(pady=20, padx=20)
                                  

        self.VentanaP.mainloop()

        def FrameDeLosGeneradores(self) -> None:
            """
            Descripcion: 
            El objetivo de esta funcion es que contengra 2 frames, por un lado los metodos de
            comprogacion y por el otro como tal lo que se nesesita o el metodo de generacion.

            De esta forma no rescribo la funcion de los frames y podemos usar nada mas una ventana
            y limpiamos el frame central y podemos reultilisar el frame de los metodos
            de comprobacion

            return: 
            no retorna nada

            atributos: 
            y no ocupa nada, es independiendte 
            """

            self.ventana_genera = ctk.CTkToplevel()
            self.ventana_genera.title("metodos de genracion")
            
            try: self.ventana_genera.state('zoomed')
            except: self.ventana_genera.attributes('-zoomed', True)



if __name__ == "__main__":
    obj = InterfazPrincipal()