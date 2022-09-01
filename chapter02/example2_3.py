symbols = '$¢£¥€¤'
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(repr(beyond_ascii))
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(repr(beyond_ascii))
