def echo_validator(text: str) -> bool:
    cleaned = ""
    for char in text.lower():
        if char.isalpha():
            cleaned += char
    if cleaned == "":
        return False
    return cleaned == cleaned[::-1]


def main():
    print(echo_validator("racecar"))
    print(echo_validator("race a car"))
    print(echo_validator("Was it a car or a cat I saw"))


if __name__ == "__main__":
    main()
