string = "hello"
print([s for s in dir(str) if "__" not in s])
print(help(str.startswith))  # !
