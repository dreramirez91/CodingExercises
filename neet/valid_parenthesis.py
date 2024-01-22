def isValid(s: str) -> bool:
    # Solution 1
    hash = {")": "(", "}": "{", "]": "["}
    stack = []
    for c in s:
        if c in hash.values():
            stack.append(c)
        else:
            try:
                open = stack.pop()
                if open != hash[c]:
                    return False
            except IndexError:
                return False
    return False if stack else True

    # Solution 2
    hash = {")": "(", "}": "{", "]": "["}
    stack = []
    for c in s:
        if c in hash:
            if stack and stack[-1] == hash[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return False if stack else True


print(isValid("[([]])"))
