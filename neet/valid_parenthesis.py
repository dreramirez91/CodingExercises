def isValid(s: str) -> bool:
    hash = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in s:
        if char in hash.values():
            stack.append(char)
        else:
            try:
                open = stack.pop()
                if open != hash[char]:
                    return False
            except IndexError:
                return False
    return False if stack else True


print(isValid("[([]])"))
