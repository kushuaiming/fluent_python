lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205956')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country, _ in traveler_ids:
    print(country)

# unpacking
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

a = 1
b = 2
b, a = a, b
print('a', a, 'b', b)

a, b, *rest = range(5)
print(a, b, rest)