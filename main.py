from repository.produs import ProductRepoFile
from service.produs_service import ProductService
from ui.consola import Consola

repo_produs=ProductRepoFile("data/products.txt")
srv_product=ProductService(repo_produs)

ui=Consola(srv_product)
ui.show_ui()