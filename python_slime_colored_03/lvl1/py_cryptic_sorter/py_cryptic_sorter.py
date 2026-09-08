def cryptic_sorter(strings: list[str]) -> list[str]:
    def vowel_count(s):
        return sum(1 for c in s if c.lower() in "aeiou")

    return sorted(strings, key=lambda s: (len(s), s.lower(), vowel_count(s)))


def main():
    print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
    print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
    print(cryptic_sorter([]))


if __name__ == "__main__":
    main()