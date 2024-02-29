from API import Api
from UI import Ui

def main():
    limite_registros = input("Digite el número de registros que desea consultar:")
    nombre_departamento = input("Ingrese el departamento que desea consultar:")
    data_frame = Api.obtener_datos_covid(limite_registros, nombre_departamento.upper())
    Ui.mostrar_datos(data_frame)

if __name__=="__main__":
    main()