"""
SUBJECT
-------
Escribe una funcion que determine un orden de instalacion de paquetes
valido resolviendo las dependencias. Utiliza el ordenamiento topologico
para asegurar que las dependencias se instalen antes que los paquetes
que las requieren.

La funcion debe:
- Tomar un diccionario donde las claves sean nombres de paquetes y los
  valores sean listas de dependencias.
- Devolver los paquetes en orden de instalacion (las dependencias primero).
- Devolver [] si no existe un orden valido (dependencias circulares o
  auto-dependencias).
- Manejar de forma adecuada las entradas vacias y las cadenas de
  dependencias aisladas.
- Ignorar las referencias a paquetes que no esten presentes como claves
  en el diccionario de entrada.
- Asegurar que un paquete no se pueda instalar hasta que todas sus
  dependencias esten instaladas.

Detalles del algoritmo:
- Ordenamiento topologico tipo Kahn (basado en grados de entrada).
- Salida deterministica: cuando varios paquetes son procesables al mismo
  tiempo, se procesan en orden alfabetico.

Firma:
    def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:

Ejemplos:
    package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []})
        -> ["driver", "database", "app"]
    package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]})
        -> ["A", "B", "C"]
    package_dependency_resolver({})
        -> []
    package_dependency_resolver({"X": ["Y"], "Y": ["X"]})
        -> []
    package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]})
        -> ["api", "web", "backend", "frontend"]
"""


def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    degree = {p: len(set(d) & packages.keys()) for p, d in packages.items()}
    ready = sorted(p for p in packages if degree[p] == 0)
    result = []

    while ready:
        result += ready
        nxt = []
        for p in ready:
            for q, deps in packages.items():
                if p in deps:
                    degree[q] -= 1
                    if degree[q] == 0:
                        nxt.append(q)
        ready = sorted(nxt)

    return result if len(result) == len(packages) else []



""" def main():
    print(package_dependency_resolver(
        {"app": ["database"], "database": ["driver"], "driver": []}
    ))  # ["driver", "database", "app"]

    print(package_dependency_resolver(
        {"A": [], "B": ["A"], "C": ["A", "B"]}
    ))  # ["A", "B", "C"]

    print(package_dependency_resolver({}))  # []

    print(package_dependency_resolver(
        {"X": ["Y"], "Y": ["X"]}
    ))  # []

    print(package_dependency_resolver(
        {"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}
    ))  # ["api", "web", "backend", "frontend"]

    print(package_dependency_resolver(
        {"A": [], "B": ["A", "A"]}
    ))

    # Casos adicionales: auto-dependencia y dependencia faltante ignorada
    print(package_dependency_resolver({"A": ["A"]}))          # []  (auto-dependencia)
    print(package_dependency_resolver({"A": ["ghost"]}))      # ["A"] (ghost no existe, se ignora)


if __name__ == "__main__":
    main() """
