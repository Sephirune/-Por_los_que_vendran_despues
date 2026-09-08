def anagram(s1: str, s2: str) -> bool:
    def clean(s):
        return sorted(s.lower().replace(" ", ""))
    return clean(s1) == clean(s2)


"""def main():
    print(anagram("racecar", "carrace"))
    print(anagram("jar", "jam"))


if __name__ == "__main__":
    main()"""
