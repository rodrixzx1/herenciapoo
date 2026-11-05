from clases.paqueteria import Envio, Envio_express, EnvioSobre

def main():
    envio = Envio("Hugo", 10)
    sobre = EnvioSobre("Paco")
    express = Envio_express("Luis", 20)

    print(envio.resumen())
    print(sobre.resumen())
    print(express.resumen())

if __name__ == "__main__":
    main()