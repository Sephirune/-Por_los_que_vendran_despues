def bracket_validator(s: str) -> bool:
    stack = []
    valid = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in valid.values():
            stack.append(c)
        elif c in valid:
            if not stack or stack.pop() != valid[c]:
                return False

    return len(stack) == 0
