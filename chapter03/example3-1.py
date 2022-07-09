DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'Unite States')
]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

print({code: country.upper() for country, code in country_code.items() if code < 66})