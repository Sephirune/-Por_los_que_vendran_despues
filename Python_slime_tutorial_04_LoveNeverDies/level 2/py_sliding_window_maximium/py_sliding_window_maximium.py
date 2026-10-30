"""
SUBJECT
-------
Dada una lista de enteros nums y un entero k, considere una "ventana" de
tamano k que se desliza de izquierda a derecha, una posicion a la vez.

Para cada posicion de la ventana, encuentre el valor maximo dentro de ella.
Devuelva la lista con todos estos maximos, en orden.

Restricciones:
- 1 <= k <= len(nums) en casos normales.
- Si nums esta vacia o k <= 0, devuelva [].
- El numero de ventanas es: len(nums) - k + 1.

Firma:
    def sliding_window_maximium(nums: list[int], k: int) -> list[int]:

Ejemplos:
    sliding_window_maximium([1, 3, -1, -3, 5, 3, 6, 7], 3) -> [3, 3, 5, 5, 6, 7]
    sliding_window_maximium([4, 2, 12, 11, -5], 2)         -> [4, 12, 12, 11]
    sliding_window_maximium([], 3)                         -> []
"""

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []

    iterations = len(nums) - k + 1

    return [max(nums[i:i + k]) for i in range(iterations)]


""" def main():
    print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(sliding_window_maximum([4, 2, 12, 11, -5], 2))
    print(sliding_window_maximum([], 3))


if __name__ == "__main__":
    main() """
