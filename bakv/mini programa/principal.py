from sandwich import Sandwich
from Venta import Venta
from SandwichCarne import SandwichCarne
from SandwichVegetariano import SandwichVegetariano

mi_sandwich = Sandwich("integral", 2000)

venta =  Venta()

vegetariano = SandwichVegetariano("integral", 2000, "tomate, lechuga")
carne = SandwichCarne("centeno", 2500, "cheddar")


#setear variable
instanciarVar = carne.set_precio(3200)
#agregar pedidos

venta.agregar_sandwich(vegetariano)
venta.agregar_sandwich(carne)

venta.mostrar_venta()