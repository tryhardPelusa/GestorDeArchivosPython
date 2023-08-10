import os
from pathlib import Path


def contar_recetas(carpeta):
    total_recetas = 0
    # Separamos la ruta en tres tuplas (la ruta actual, las subcarpetas y los archivos)
    for root, subcarpetas, files in os.walk(carpeta):
        for archivo in files:
            if archivo.endswith(".txt"):
                total_recetas += 1

    return total_recetas


def comprobar_archivo_existe(ruta, archivo):
    for _, _, files in os.walk(ruta):
        for file in files:
            if file == archivo:
                return True
    return False


def elegir_archivo(ruta, subcarpeta):
    ruta_archivo = Path(ruta, subcarpeta)
    comprobar_si_esta_vacia = os.listdir(ruta_archivo)
    if len(comprobar_si_esta_vacia) != 0:
        for _, _, files in os.walk(ruta_archivo):
            for file in files:
                if file.endswith('.txt'):
                    print(file)

        print("-----------------------------")
        archivo = input(': ')
        existe = comprobar_archivo_existe(ruta, archivo)
        if existe:
            return archivo
        else:
            os.system('cls')
            print('Esa receta no existe. Por favor introduce un nombre válido: ')
            elegir_archivo(ruta, subcarpeta)
    else:
        os.system('cls')
        print('Esta carpeta está vacía.')


def comprobar_subcarpeta_existe(ruta, subcarpeta):
    for _, subcarpetas, _ in os.walk(ruta):
        for sub in subcarpetas:
            if sub == subcarpeta:
                return True
    return False


def elegir_subcarpetas(ruta):
    for _, subcarpetas, _ in os.walk(ruta):
        for subcarpeta in subcarpetas:
            print(subcarpeta)

    print("-----------------------------")
    subcarpeta = input(': ')
    existe = comprobar_subcarpeta_existe(ruta, subcarpeta)
    if existe:
        return subcarpeta
    else:
        os.system('cls')
        print('Esa carpeta no existe. Por favor introduce un nombre válido: ')
        elegir_subcarpetas(ruta)


def generar_nombre_receta():
    os.system('cls')
    return input('Escribe un nombre para la receta: ')


def pedir_contenido_receta():
    os.system('cls')
    continua = True
    contenido = ''
    print('Introduce el contenido de la receta.\n'
          'Puede tener varias lineas.\n'
          'Para terminar escribe un 0')
    while continua:
        nueva_linea = input(': ')
        if nueva_linea == '0':
            continua = False
        else:
            contenido += '\n' + nueva_linea
    return contenido


def leer_receta(ruta):
    os.system('cls')
    print('Elige una categoría: ')
    subcarpeta = elegir_subcarpetas(ruta)
    os.system('cls')
    print('Elige una receta: ')
    receta = elegir_archivo(ruta, subcarpeta)
    if receta is not None:
        final = open(Path(ruta, subcarpeta, receta))
        print(final.read())
        final.close()
    input('Pulsa enter para volver al menu. ')
    os.system('cls')



def crear_receta(ruta):
    os.system('cls')
    print('Elige una categoría: ')
    categoria = elegir_subcarpetas(ruta)
    receta = generar_nombre_receta() + '.txt'
    ruta_de_creacion = Path(ruta, categoria, receta)
    archivo = open(ruta_de_creacion, 'w')
    contenido = pedir_contenido_receta()
    archivo.write(contenido)
    print('Receta creada correctamente.')
    input('Pulsa enter para volver al menu. ')
    os.system('cls')
    archivo.close()


def crear_categoria(ruta):
    os.system('cls')
    nueva_carpeta = input('Introduce el nombre de la nueva carpeta: ')
    ruta_completa = os.path.join(ruta, nueva_carpeta)
    try:
        os.mkdir(ruta_completa)
        print(f"Carpeta '{nueva_carpeta}' creada en '{ruta_completa}'.")
    except FileExistsError:
        print(f"La carpeta '{nueva_carpeta}' ya existe en '{ruta_completa}'.")

    input('Pulsa enter para volver al menu. ')
    os.system('cls')


def eliminar_receta(ruta):
    os.system('cls')
    print('Elige una categoría: ')
    subcarpeta = elegir_subcarpetas(ruta)
    os.system('cls')
    print('Elige una receta: ')
    receta = elegir_archivo(ruta, subcarpeta)
    if receta is not None:
        os.remove(Path(ruta, subcarpeta, receta))
        print('Receta eliminada.')
    input('Pulsa enter para volver al menu. ')
    os.system('cls')


def eliminar_categoria(ruta):
    os.system('cls')
    print('Elige una categoría: ')
    subcarpeta = elegir_subcarpetas(ruta)
    carpeta_ha_borrar = Path(ruta, subcarpeta)
    os.rmdir(carpeta_ha_borrar)
    print('Categoría eliminada con éxito.')
    input('Pulsa enter para volver al menu. ')
    os.system('cls')

####################################################################################################################
# -----------------------------------------------------MAIN--------------------------------------------------------#

print('Bienvenido a tu app de recetas. Elige una opción: ')

ruta_base = Path(Path.home(), 'Recetas')
print('Tus recetas se encuentran almacenadas en: ', ruta_base)

total_recetas = contar_recetas(ruta_base)
print(f'Total de recetas encontradas: {total_recetas}')

continuar = True


while continuar:
    print('''
[1] - Leer receta
[2] - Crear receta
[3] - Crear categoría
[4] - Eliminar receta
[5] - Eliminar categoría
[6] - Finalizar programa
-----------------------------''')
    eleccion = input(': ')
    if eleccion == '1':
        leer_receta(ruta_base)
    elif eleccion == '2':
        crear_receta(ruta_base)
    elif eleccion == '3':
        crear_categoria(ruta_base)
    elif eleccion == '4':
        eliminar_receta(ruta_base)
    elif eleccion == '5':
        eliminar_categoria(ruta_base)
    elif eleccion == '6':
        continuar = False
        print('Programa finalizado. Hasta luego :)')
    else:
        print('No has elegido una opción correcta.')
        continue
