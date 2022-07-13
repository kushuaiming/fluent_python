for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'E1 Nino'.encode(codec), sep='\t')