class Product:
    def __init__(self,id,denumire,pret):
        self.__id=id
        self.__denumire=denumire
        self.__pret=pret

    def getid(self):
        return self.__id    

    def getdenumire(self):
        return self.__denumire

    def getpret(self):
        return self.__pret

    def __str__(self):
        return "ID"+str(self.__id)+"Nume"+str(self.__denumire)+"Pret"+str(self.__pret)  

