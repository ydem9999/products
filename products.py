products = []
while True:
	name = input('please enter product name:')
	if name == 'q':
		break
	price = input('Please enter product price:')
#	p = []
#	p.append(name)
#	p.append(price)
	products.append([name,price])
print(products)

for p in products:
	print('Price of', p[0], 'is', p[1])


with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')