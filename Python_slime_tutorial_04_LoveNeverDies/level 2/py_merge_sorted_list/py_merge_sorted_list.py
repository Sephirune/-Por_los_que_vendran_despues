"""
SUBJECT
-------
Escribe una funcion que fusione multiples listas ordenadas en una sola
lista ordenada de forma eficiente.

La funcion debe:
- Tomar como entrada una lista de listas de enteros ordenadas
- Devolver una unica lista fusionada en orden ascendente
- Conservar todos los elementos duplicados en el resultado final
- Manejar listas vacias y entradas vacias de forma adecuada
- Mantener una eficiencia optima para entradas grandes

RESTRICCIONES DE LA MOULINETTE
-------------------------------
Prohibido: sorted(), .sort(), heapq.merge()

Firma:
    def merge_sorted_lists(lists: list[list[int]]) -> list[int]:

Ejemplos:
    merge_sorted_lists([[1, 3, 5], [2, 4, 6]])          -> [1, 2, 3, 4, 5, 6]
    merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]) -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
    merge_sorted_lists([[5], [1, 3], [2, 4]])           -> [1, 2, 3, 4, 5]
    merge_sorted_lists([[1, 1, 2], [2, 3, 3]])          -> [1, 1, 2, 2, 3, 3]
    merge_sorted_lists([[], [1, 2, 3]])                 -> [1, 2, 3]
    merge_sorted_lists([[]])                            -> []
    merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]])       -> [-5, -3, -1, 0, 2, 4]
    merge_sorted_lists([[10], [10], [10]])              -> [10, 10, 10]
"""


def merge_two(a: list[int], b: list[int]) -> list[int]:
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def merge_sorted_lists_v2(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    # Fusiona las listas de dos en dos hasta que quede una sola
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged.append(merge_two(lists[i], lists[i + 1]))
            else:
                merged.append(lists[i])  # impar: pasa sin pareja
        lists = merged

    return lists[0][:]


""" def main():
    tests = [
        ([[1, 3, 5], [2, 4, 6]], [1, 2, 3, 4, 5, 6]),
        ([[1, 5, 9], [2, 3, 8], [4, 6, 7]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([[5], [1, 3], [2, 4]], [1, 2, 3, 4, 5]),
        ([[1, 1, 2], [2, 3, 3]], [1, 1, 2, 2, 3, 3]),
        ([[], [1, 2, 3]], [1, 2, 3]),
        ([[]], []),
        ([[-5, -1, 0], [-3, 2, 4]], [-5, -3, -1, 0, 2, 4]),
        ([[10], [10], [10]], [10, 10, 10]),
        ([], []),
    ]
    for entrada, esperado in tests:
        r1 = merge_sorted_lists(entrada)
        r2 = merge_sorted_lists_v2(entrada)
        estado = "OK" if r1 == esperado and r2 == esperado else "FALLO"
        print(estado, entrada, "->", r1)


if __name__ == "__main__":
    main() """
