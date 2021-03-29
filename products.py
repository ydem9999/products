products = []
#Load file
with open('products.csv', 'r') as f:
	for line in f:
		if 'Products,Price' in line:
			continue
		name, price= line.strip().split(',')
		products.append([name, price])
print(products)

#User input
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

#Print all purchase history
for p in products:
	print('Price of', p[0], 'is', p[1])

#Write records
with open('products.csv', 'w') as f:
	f.write('Products,Price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')