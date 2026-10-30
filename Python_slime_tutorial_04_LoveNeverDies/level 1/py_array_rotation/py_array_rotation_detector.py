"""
SUBJECT
-------
Determina si array2 es una rotacion de array1. Una rotacion desplaza
elementos ciclicamente manteniendo el orden relativo.

- Devuelve True si array2 es una rotacion valida de array1
- Devuelve False en caso contrario o si las longitudes difieren
- Maneja arreglos vacios (dos arreglos vacios se consideran rotaciones validas)

RESTRICCIONES DE LA MOULINETTE
-------------------------------
Prohibido: collections.deque.rotate()

Firma:
    def array_rotation_detector(arr1: list, arr2: list) -> bool:

Ejemplos:
    array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]) -> True
    array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]) -> True
    array_rotation_detector([1, 2, 3], [3, 2, 1])             -> False
    array_rotation_detector([1, 2], [1, 2, 3])                -> False
    array_rotation_detector([], [])                           -> True
"""


def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if not arr1:
        return True

    doubled = arr1 + arr1
    n = len(arr1)

    for i in range(n):
        if doubled[i:i + n] == arr2:
            return True
    return False


""" def main():
    print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))  # True
    print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))  # True
    print(array_rotation_detector([1, 2, 3], [3, 2, 1]))              # False
    print(array_rotation_detector([1, 2], [1, 2, 3]))                 # False
    print(array_rotation_detector([], []))                            # True


if __name__ == "__main__":
    main() """
