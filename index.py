from sucursales import gestionar_sucursales
from productos import gestionar_productos
from ventas import gestionar_ventas
from proveedores import gestionar_proveedores
from categoria_productos import gestionar_categorias
from clientes import gestionar_clientes
from empleados import gestionar_empleados


def menu_principal():
    while True:
        print("Bienvenido al Sistema de Control de Stock")
        print("1. Gestionar Sucursales")
        print("2. Gestionar Productos")
        print("3. Gestionar Ventas")
        print("4. Gestionar Proveedores")
        print("5. Gestionar Clientes")
        print("6. Gestionar Categorías de Productos")
        print("7. Gestionar empleados")
        print("8. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            gestionar_sucursales()
        elif opcion == "2":
            gestionar_productos()
        elif opcion == "3":
            gestionar_ventas()
        elif opcion == "4":
            gestionar_proveedores()
        elif opcion == "5":
            gestionar_clientes()
        elif opcion == "6":
            gestionar_categorias()            
        elif opcion == "7":
            gestionar_empleados()
        elif opcion == "8":
            print("Gracias por usar el Sistema de Control de Stock.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu_principal()


'''
La última parte del código if __name__ == "__main__": menu_principal() es una convención común en Python que se utiliza para asegurarse de que el código dentro de este bloque solo se ejecute cuando el script es ejecutado directamente, y no cuando es importado como un módulo en otro script.

Vamos a desglosar lo que significa cada parte:

if __name__ == "__main__":

__name__ es una variable especial en Python que se refiere al nombre del módulo actual.
Cuando un archivo Python es ejecutado directamente, Python asigna a __name__ el valor "__main__".
Esto significa que el bloque de código indentado bajo if __name__ == "__main__": será ejecutado solo cuando el script se ejecute directamente desde la línea de comandos o desde otro programa principal.
menu_principal()

menu_principal es una función definida anteriormente en el código.
Al llamar menu_principal() dentro de if __name__ == "__main__":, garantizas que cuando ejecutes este script directamente, se iniciará el menú principal del sistema de control de stock.
Esto permite al usuario interactuar con las opciones del menú y realizar las gestiones correspondientes según la opción seleccionada.
En resumen, la parte if __name__ == "__main__": menu_principal() asegura que el programa comience ejecutando la función menu_principal() solo cuando ejecutes el script directamente, y no cuando lo importes como un módulo en otro programa. Es una práctica recomendada para estructurar y modularizar el código Python de manera efectiva.
'''