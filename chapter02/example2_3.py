symbols = '!@#$%^&*()'
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 48]

print(repr(beyond_ascii))
