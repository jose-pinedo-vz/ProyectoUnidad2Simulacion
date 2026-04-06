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

        self.CuadradosMedios = ctk.CTkButton(self.VentanaP, text="Cuadrados medios",
                                             command=lambda: self.caudrados_medios())
        self.CuadradosMedios.pack(pady=20, padx=20)

        self.CongruencialM = ctk.CTkButton(self.VentanaP, text="Congruencial mixto",
                                           command=lambda: self.Mixto())
        self.CongruencialM.pack(pady=20, padx=20)

        self.CongruencialMul = ctk.CTkButton(self.VentanaP, text="Congruencial multiplicativo",
                                             command=lambda: self.multiplicativo())
        self.CongruencialMul.pack(pady=20, padx=20)

        self.LineasDeEspera = ctk.CTkButton(self.VentanaP, text="Lineas de espra",
                                            command=lambda: self.Esperas())
        self.LineasDeEspera.pack(pady=20, padx=20)

        self.TeoriaIn = ctk.CTkButton(self.VentanaP, text="Teoria de inventarios")
        self.TeoriaIn.pack(pady=20, padx=20)
                                  

        self.VentanaP.mainloop()


    def limpiar_pantalla_grande(self) -> None:
        """
        Descripcion:
            esta madre limpia los elementos del centro del frame
        """
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

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

        self.ventana_genera.grid_columnconfigure(1, weight=1) 
        self.ventana_genera.grid_rowconfigure(0, weight=1)

        self.frame_menu = ctk.CTkFrame(self.ventana_genera, width=200, corner_radius=0)
        self.frame_menu.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.frame_menu.grid_propagate(False) 

        #Botones del menu:

        labelXd = ctk.CTkLabel(self.frame_menu, text="Evaluar con: ").pack(padx=10, pady=10)

        self.corridas = ctk.CTkButton(self.frame_menu, text="Corridas arriba y abajo")
        self.corridas.pack(pady=20, padx=20)

        self.corridasPromedio = ctk.CTkButton(self.frame_menu, text="Corridas arriba y abajo del promedio")
        self.corridasPromedio.pack(pady=20, padx=20)

        self.Distancia = ctk.CTkButton(self.frame_menu, text="Distancia")
        self.Distancia.pack(pady=20, padx=20)

        self.Poker = ctk.CTkButton(self.frame_menu, text="Poker")
        self.Poker.pack(pady=20, padx=20)

        self.Kolmogorov = ctk.CTkButton(self.frame_menu, text="Kolmogorov")
        self.Kolmogorov.pack(pady=20, padx=20)

        self.Frecuencail = ctk.CTkButton(self.frame_menu, text="Frecuencail")
        self.Frecuencail.pack(pady=20, padx=20)

        self.Series = ctk.CTkButton(self.frame_menu, text="Series")
        self.Series.pack(pady=20, padx=20)




        self.frame_contenido = ctk.CTkFrame(self.ventana_genera, fg_color="gray20")
        self.frame_contenido.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    def caudrados_medios(self):
        self.FrameDeLosGeneradores()
        self.limpiar_pantalla_grande()

        lb_central = ctk.CTkLabel(self.frame_contenido, text="Cuadrados medios",
                                  font=("Arial", 18))
        lb_central.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

    def Mixto(self):
        self.FrameDeLosGeneradores()
        self.limpiar_pantalla_grande()

        lb_central = ctk.CTkLabel(self.frame_contenido, text="Congruencial mixto",
                                  font=("Arial", 18))
        lb_central.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

    def multiplicativo(self):
        self.FrameDeLosGeneradores()
        self.limpiar_pantalla_grande()

        lb_central = ctk.CTkLabel(self.frame_contenido, text="Congruencial multiplicativo",
                                  font=("Arial", 18))
        lb_central.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

    def Esperas(self):
        import LIneasUI 

        LIneasUI.ventana()
        





if __name__ == "__main__":
    obj = InterfazPrincipal()