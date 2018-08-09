#dictionaly type

product = {'speaker':200, 'amp':120}
# print(sales['speaker'])
# sales['speaker'] = 300
product['device'] = 500
# print(sales)

#items()
for key, values in product.items():
    print('{0}: {1}'.format(key, values))

#normal for - only key will be shown
for k in product:
    print(k)
    # speaker
    # amp
    # device

# key() - the same result of above
for k in product.keys():
    print(k)

# values()
for k in product.values():
    print(k)
