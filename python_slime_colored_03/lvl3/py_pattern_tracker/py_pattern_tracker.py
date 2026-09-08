def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        if text[i].isdigit() and text[i + 1].isdigit():
            if ord(text[i + 1]) - ord(text[i]) == 1:
                count += 1
    return count


"""def main():
    print(pattern_tracker("1a2b3c4"))
    print(pattern_tracker("123"))


if __name__ == "__main__":
    main()"""
