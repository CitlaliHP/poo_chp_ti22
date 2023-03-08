class Productos:

  def insertarProductos(self,sku:str,nombre:str,unidad:str)-> bool:
    print(f"Insertar: {sku},{nombre},{unidad}")
    return True
    
  def actualizarProducto(self)->bool:
    sku = input("SKU: ")
    nombre = input("Nombre: ")
    unidad = input("Unidad: ")
    print(f"Actualizar: {sku},{nombre},{unidad}")
    return True 

productos  = Productos()
  
sku = input("SKU: ")
nombre = input("Nombre: ")
unidad = input("Unidad: ")
productos.insertarProductos(sku,nombre,unidad)

productos.actualizarProducto()
  