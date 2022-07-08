class Consola:
    def __init__(self,srvProduct):
        self.__srv_product=srvProduct

    def __print_menu(self):
        print("Comenzi disponibile: adauga_produs,delete,filtrare,undo,exit")

    def __show_filtrat(self,lista):
        if len(lista)==0:
            print("Nu exista produse")
        else:
            print("Lista filtrata este:")
            for produs in lista:
                print("ID : ",produs.getid(),"Denumire :",produs.getdenumire(),"Pret : ",produs.getpret())    




    def __add_product(self):
        id=input("ID produs:")
        denumire=input("Denumire produs:")
        pret=input("Pretul produsului:")
        added_product=self.__srv_product.add_product(id,denumire,pret)
        print("Produsul a fost adaugat")

    def __delete(self):
        pret=input("cifra dupa care se face stergerea:")
        deleted_produs=self.__srv_product.delete_pret(pret)
        print("Produsele au fost sterse",deleted_produs)
    
    def __filtrare(self):
        text=input("Textul pe care doriti sa il contina:")
        numar=input("pretul mai mare:")
        l=self.__srv_product.filtare(text,numar)
        self.__show_filtrat(l)

    def __undo(self):
        self.__srv_product.undo()   

    def show_ui(self):
        while True:
            self.__print_menu()
            cmd=input("Comanda este: ")
            cmd=cmd.lower().strip()
            if cmd=="adauga_produs":
                self.__add_product()
            elif cmd=="delete":
                self.__delete()
            elif cmd=="filtrare":
                self.__filtrare()     
            elif cmd=="undo":
                self.__undo()       
            elif cmd=="exit":
                return
            else:
                print("Comanda invalida")                    