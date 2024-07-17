
class boligrafo:
    def __init__(self, color: str,grosor_punta: str):
        self.capacidad_tinta_maxima = 100
        self.cantidad_tinta = 80
        self.color = color
        self.grosor_punta = grosor_punta




    def escribir_texto(self, texto: str):
        grosor = 1
        escribio = "No alcanza la tinta"

        if self.grosor_punta == "Grueso":
            grosor = 2

        gasto_tinta = len(texto) * grosor
        if self.cantidad_tinta >= gasto_tinta:
            escribio = texto
            self.cantidad_tinta -= gasto_tinta

        return escribio
    
    def recargar(self, cantidad: int):
        suma_de_tinta = self.cantidad_tinta + cantidad
        if suma_de_tinta > self.capacidad_tinta_maxima:
            self.cantidad_tinta = 100
            sobrante = suma_de_tinta - self.cantidad_tinta  
            carga = f"se cargo la lapicera y sobro {sobrante}"
        else:
            self.cantidad_tinta = suma_de_tinta
            carga = "Lapicera cargada"

        return carga