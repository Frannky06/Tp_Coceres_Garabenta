#Alumnos: Francisco Coceres y Tomas Garabenta
# Un cliente ha solicitado un sistema básico para gestionar las ventas de su quiosco llamado
# Yoda's Snack. El programa debe cumplir con las siguientes funcionalidades:
# 1. Menú principal:
# • Mostrar las siguientes opciones:
# o Agregar producto al inventario.
# o Realizar una venta.
# o Mostrar productos disponibles.
# o Salir del sistema.
# Menu principal
def menu ():
    """
    Funcion del menu principal con un match case segun la opcion deseada que ingresa el usuario.
    """
    while True:
        print("\n----Menu Principal----")
        print("1.--Agregar producto al inventario")
        print("2.--Realizar una venta")
        print("3.--Mostrar productos disponibles")
        print("4.--Salir del sistema")
        opcion = int(input("Seleccione una opción (1-4): "))
        match opcion:
            case 1:
                agregar_producto()
            case 2:
                realizar_venta()
            case 3:
                for elemento in inventario:
                    print (elemento)
            case  4:
                print('Saliendo del menu')
                break
            case _:
                    print("Opcion invalida, selleccionar un numero del 1 al 4")

# 4. Mostrar productos disponibles:
# • Mostrar todos los productos en el inventario, con su nombre, cantidad
# disponible y precio.
inventario = [
    ["Chupetin Sable de luz", 50, 200],
    ["Agua La Fuerza", 35, 3200],
    ["Gomitas Holocubo", 25, 990],
    ["Barrita de Cereal Wookie", 48, 2500],
    ["Galletitas R2D2", 20, 15800],
]


cantidades = [fila[1] for fila in inventario]
print(cantidades)
# 2. Agregar producto al inventario:
# • Permitir al usuario agregar productos al inventario. Cada producto debe tener
# un nombre, una cantidad disponible y un precio unitario.
# • Los productos deben almacenarse en una lista.
# • Ver la estructura del inventario al final de la consigna.
def agregar_producto():
    """
    Se encarga de agregar por nombre, cantidad y precio un nuevo producto y utilizando append lo agregamos al inventario original
    """
    nombre_producto = input("Ingrese el nombre del producto a agregar: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio por unidad del producto: "))
    producto = [nombre_producto, cantidad, precio]
    inventario.append(producto)
    
# 3. Realizar una venta:
# • Mostrar una lista de productos disponibles (nombre, precio y cantidad).
# • El usuario podrá seleccionar un producto y la cantidad que desea comprar.
# • Verificar que haya suficiente stock del producto seleccionado.
# • Restar la cantidad comprada del inventario.
# • Mostrar el total a pagar al cliente por la venta.
# • Si no hay suficiente stock, mostrar un mensaje que indique que no se puede
# realizar la venta.

def realizar_venta():
    """
    Se pide el nombre y unidades del producto deseado para luego buscarlo, comprobar la cantidad de stock y realizar el calculo correspondiente del total a pagar
    """
    producto_a_vender = input("Ingrese el nombre del producto a vender: ").lower()
    cantidad_producto_a_vender = int(input("Ingrese cuantas unidades del producto llevaran: "))
# Variable para comprobar si el producto se encontró
    for producto in inventario:
        if producto [0].lower() == producto_a_vender:
            busca_producto = True
            
            if cantidad_producto_a_vender > producto[1]:
                print("No hay suficiente stock")
                return 

            else:
                producto[1] -= cantidad_producto_a_vender
                valor_final = cantidad_producto_a_vender * producto[2]
                print(f"Venta exitosa!, su total a pagar: {valor_final}")
                return valor_final  
    if not busca_producto:
        print('Producto no encontrado en el inventario. ') 


# 5. Salir del sistema:
# • Finalizar el programa.
# Requisitos técnicos:
# • Deben utilizar funciones para modularizar el código. Cada funcionalidad del
# menú debe estar implementada en una función separada.
# • Implementar bucles y condicionales para manejar el flujo del menú y las
# ventas.
# • Utilizar listas para almacenar los productos del inventario.
# • Los productos deben tener nombre, stock y precio, en ese orden.

menu ()