import imp
from itertools import product
from domain.entitati import Product
class ProductRepoFile:
    def __init__(self,filename):
        self.__filename=filename
        self.__undo=[]

    def __load_from_file(self):
        with open(self.__filename,"r") as c:
            produse=[]
            lines=c.readlines()
            for line in lines:
                produs_id,produs_nume,produs_pret=[token.strip() for token in line.split(" ") ]
                p=Product(produs_id,produs_nume,produs_pret)
                produse.append(p)
        c.close()  
        return produse      

    def __save_to_file(self,product_list):
        with open("data/caca.txt","w") as p:
            for produs in product_list:
                produs_string=str(produs.getid())+" "+str(produs.getdenumire())+" "+str(produs.getpret())+"\n"  
                p.write(produs_string)

    def store(self,produs):
        all_product=self.__load_from_file()
        all_product.append(produs)
        self.__save_to_file(all_product) 

    def get_all(self):
        return list(self.__load_from_file())  



    def delete_by_pret(self, str_to_search):
        """
        functia care cauta dupa scop
        rtype:list
        """
        all_produse= self.__load_from_file()
        self.__undo=all_produse[:]
        k=0
        filtered_list = [produs for produs in all_produse if str_to_search in produs.getpret()]
        for produs in filtered_list:
            all_produse.remove(produs)
            k=k+1
        self.__save_to_file(all_produse)
        return k

    def filtrare(self,str_to_search,numar):
        all_produse=self.__load_from_file()
        f=[]
        if not str_to_search:
            for produs in all_produse:
                if int(produs.getpret())<int(numar):
                    f.append(produs)
        elif int(numar)==-1:
            f = [produs for produs in all_produse if str_to_search in produs.getdenumire()]   
        else:        
            filtered_list = [produs for produs in all_produse if str_to_search in produs.getdenumire()]    
            for produs in filtered_list:
                if int(produs.getpret())<int(numar):
                    f.append(produs)
        return f                                          

    def undo(self):
        self.__save_to_file(self.__undo) 