symbols = '!@#$%^&*()'
print(repr(tuple(ord(symbol) for symbol in symbols)))

import array
print(repr(array.array('I', (ord(symbol) for symbol in symbols))))