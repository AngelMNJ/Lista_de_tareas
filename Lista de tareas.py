class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "completada": False})

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True

    def mostrar_tareas(self):
        print("Lista de Tareas:")
        for indice, tarea_info in enumerate(self.tareas):
            estado = "Completada" if tarea_info["completada"] else "Pendiente"
            print(f"{indice + 1}. {tarea_info['tarea']} - {estado}")

def main():
    lista = ListaDeTareas()

    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea = input("Ingrese la tarea: ")
            lista.agregar_tarea(tarea)
            print("Tarea agregada.")

        elif opcion == "2":
            lista.mostrar_tareas()
            indice = int(input("Ingrese el número de tarea completada: ")) - 1
            lista.marcar_completada(indice)
            print("Tarea marcada como completada.")

        elif opcion == "3":
            lista.mostrar_tareas()

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
