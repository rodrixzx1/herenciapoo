from clases.empleados import Empleado, Vendedor, EmpleadoPorHoras

def main():

    empleado = Empleado("Hugo", 2500)
    vendedor = Vendedor("Paco", 2500, 1000)  
    empleado_por_horas = EmpleadoPorHoras("Luis", 20, 100)

    print(empleado.descripcion())
    print(vendedor.descripcion())
    print(empleado_por_horas.descripcion())

if __name__ == "__main__":
    main()