# Gay el que lo lea
import pandas as pd
import os

archive = pd.read_csv("prototipo.csv")
print("Columnas | filas:", archive.shape)

def limpiar_pantalla():
    os.system("clear")

def listar_paginado(datos: pd.DataFrame, tam_pagina: int=15):
    total= len(datos)
    if total == 0:
        print("\n [!] No hay Datos!")
        return


    pagina = 0
    total_paginas = (total - 1) // tam_pagina + 1

    while True:
            limpiar_pantalla()
            inicio = pagina * tam_pagina
            fin = inicio + tam_pagina
            print(f"=== LISTADO DE REGISTROS (Página {pagina + 1}/{total_paginas} | Total: {total}) ===\n")
            print(datos.iloc[inicio:fin].to_string(index=True))
            print("\n[n] Siguiente | [p] Anterior | [q] Volver al menú")
            opcion = input("> ").strip().lower()

            if opcion == "n" and pagina < total_paginas - 1:
                pagina += 1
            elif opcion == "p" and pagina > 0:
                pagina -= 1
            elif opcion == "q":
                break

def menu():
    while True:
        limpiar_pantalla()
        print("""
            ==== Explorar archivo CSV con PANDAS ====
                            Menu
                1. listar todos los registros .
                2. filtrar por Año (2019-2023).
                3. filtrar por Productos
                4. Resumen por Producto
                0. Salir
            """)
        opcion = input("\nSeleccione opcion: ").strip()
        if opcion == "1":
            listar_paginado(archive)
        elif opcion == "2":
            anio = input("ingresa el año (ej. 2021).").strip()
            if anio.isdigit():
                listar_paginado(archive[archive["Year"] == int(anio)])
        elif opcion == "3":
                    prod = input("Ingresa producto (ej. Product A): ").strip()
                    listar_paginado(archive[archive["Product"].str.lower() == prod.lower()])
        elif opcion == "4":
                    limpiar_pantalla()
                    resumen = archive.groupby("Product").agg(
                        ventas=("Units_Sold", "count"),
                        unidades=("Units_Sold", "sum"),
                        ingresos=("Revenue", "sum"),
                        precio_prom=("Price_per_Unit", "mean"),
                    )
                    print("=== RESUMEN POR PRODUCTO ===\n")
                    print(resumen.round(2))
                    input("\nPresiona Enter para volver...")
        elif opcion == "0":
            break


if __name__ == "__main__":
    menu()
