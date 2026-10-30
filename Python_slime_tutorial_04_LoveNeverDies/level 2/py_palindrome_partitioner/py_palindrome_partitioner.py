"""
SUBJECT
-------
Dada una cadena s, encuentre el numero minimo de cortes necesarios para
particionarla de modo que cada subcadena resultante sea un palindromo.

Un corte divide la cadena entre dos caracteres. Con c cortes, la cadena
se divide en c + 1 subcadenas. Queremos el minimo c tal que todas las
partes sean palindromos.

Restricciones:
- Cadena vacia o de longitud 1 -> 0 cortes.
- Si toda la cadena ya es un palindromo -> 0 cortes.
- Peor caso (todos distintos): len(s) - 1 cortes.

Firma:
    def palindrome_partitioner(s: str) -> int:

Ejemplos:
    palindrome_partitioner("aab") -> 1   ("aa" | "b")
    palindrome_partitioner("aba") -> 0
    palindrome_partitioner("abc") -> 2   ("a" | "b" | "c")
"""

def palindrome_partitioner(s: str) -> int:
    n = len(s)
    cuts = list(range(n))

    for end in range(n):
        for start in range(end + 1):
            if s[start:end + 1] == s[start:end + 1][::-1]:
                cuts[end] = min(cuts[end], 0 if start == 0 else cuts[start - 1] + 1)

    return cuts[-1] if s else 0

""" def main():
    print(palindrome_partitioner("aab"))
    print(palindrome_partitioner("aba"))
    print(palindrome_partitioner("abc"))
    print(palindrome_partitioner(""))
    print(palindrome_partitioner("a"))


if __name__ == "__main__":
    main() """
