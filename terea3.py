from operator import itemgetter

class reserva:
    def __init__(self):
        self.lista = []
    def addReserva(self,horaInit,horaFin):
        horaInitVal=int(horaInit)
        horaFinVal=int(horaFin)
        if(horaInitVal>horaFinVal):
            raise ValueError("Hora de inicio no puede ser mayor a hora final.")
        tupla1 = (horaInitVal,1)
        tupla2 = (horaFinVal,-1)
        self.lista+=[tupla1,tupla2]
    def validar(self):
        temp = sorted(self.lista,key=itemgetter(0,1))#ordena las tuplas por su hora, que es el elemento 0 de las tuplas y luego por la cantidad que es -1 o 1
        count = 0#como el algoritmo de marsulu contamos de 0
        for r in temp:
            count+=r[1]
            if(count>10):#10 es maximo de reservas pedidas en la tarea
                return False
        return True