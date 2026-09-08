def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for i in text:
        if i >= 'a' and i <= 'z':
            result += chr((ord(i) - ord('a') + shift) % 26 + ord('a'))
        elif i >= 'A' and i <= 'Z':
            result += chr((ord(i) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += i
    return result


"""def main():
    print(whisper_cipher("ABC", 2))


if __name__ == "__main__":
    main()"""
