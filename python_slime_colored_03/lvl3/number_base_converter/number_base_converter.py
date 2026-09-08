def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"

    try:
        num = int(number, from_base)
    except ValueError:
        return "ERROR"

    if num == 0:
        return "0"

    result = ""

    while num > 0:
        result = digits[num % to_base] + result
        num //= to_base

    return result


"""def main():
    print(number_base_converter("1010", 2, 10))

if __name__ == "__main__":
    main()"""
