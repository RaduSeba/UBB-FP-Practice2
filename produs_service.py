from calendar import c
import imp
from domain.entitati import Product
from repository.produs import ProductRepoFile

class ProductService:
    def __init__(self,repo):
        self.__repo=repo

    def add_product(self,id,denumire,pret):
        product=Product(id,denumire,pret)
        self.__repo.store(product)

    def all(self):
       return self.__repo.get_all()        

    def delete_pret(self,string):
        n=self.__repo.delete_by_pret(string)
        return n

    def filtare(self,string,numar):
        f=self.__repo.filtrare(string,numar)
        return f

    def undo(self):
        self.__repo.undo()