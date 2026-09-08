def inter(s1: str, s2: str) -> str:
    result = ""
    seen = set()
    for i in s1:
        if i in s2 and i not in seen:
            result += i
            seen.add(i)
    return result


def main():
    print(inter("hello", "world"))
    print(inter("banana", "band"))
    print(inter("abcabc", "bc"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))


if __name__ == "__main__":
    main()
