"""
SUBJECT
-------
Devuelve una lista que contiene los elementos presentes en cada sublista,
sin duplicados, en orden ascendente. Si la lista de entrada esta vacia, o
si alguna sublista esta vacia, el resultado es una lista vacia. Todas las
sublistas contienen elementos del mismo tipo comparable.

Firma:
    def common_elements(lists: list) -> list:

Ejemplos:
    common_elements([[1, 2, 3], [2, 3, 4], [3, 4, 5]]) -> [3]
    common_elements([[1, 2], [3, 4]])                  -> []
    common_elements([])                                -> []
"""


def common_elements(lists: list) -> list:
    if not lists or any(not sub for sub in lists):
        return []

    common = set(lists[0])
    for sub in lists[1:]:
        common &= set(sub)  # interseccion de conjuntos. es lo mismo que poner common = set(sub) & common

    return sorted(common)


""" def main():
    print(common_elements([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))
    print(common_elements([[1, 2], [3, 4]]))
    print(common_elements([]))


if __name__ == "__main__":
    main() """
