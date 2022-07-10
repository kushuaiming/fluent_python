s = 'cafe'
print(len(s))

b = s.encode('utf8')
print(b)

b'caf\xc3\xa9'
print(len(b))

print(b.decode('utf8'))