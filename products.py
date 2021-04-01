import os# operating system
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if 'Products,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

#User input
def user_input(products):
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
	return products

#Print all purchase history
def print_products(products):
	for p in products:
		print('Price of', p[0], 'is', p[1])

#Write records
def write_file(filename, products):
	with open(filename, 'w') as f:
		f.write('Products,Price\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename):#check file
		print('Yes, file found.')
		products = read_file(filename)
	else:
		print('File not found.')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)



main()