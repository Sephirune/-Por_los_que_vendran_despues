def string_sculptor(text: str) -> str:
    result = ""
    count = 0

    for i in text:
        if i.isalpha():
            if count % 2 == 0:
                result += i.lower()
            else:
                result += i.upper()
            count += 1
        else:
            result += i
    return result


"""def main():
    print(string_sculptor("hOlA"))

if __name__ == "__main__":
    main()"""
