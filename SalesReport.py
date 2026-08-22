import csv

with open('salesreport.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)

#Generate total sales from the CSV file

total_sales = 0

with open('salesreport.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        quantity = int(row['quantity'])
        price = float(row['price'])

        total_sales += quantity * price

print('--------------------------------------')
print(f"Total Sales: ${total_sales:.2f}")
print('--------------------------------------')

#most sold product

product_sales = {}

with open('salesreport.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row['product']
        quantity = int(row['quantity'])

        if product in product_sales:
            product_sales[product] += quantity
        else:
            product_sales[product] = quantity

# Find the most sold product
most_sold_product = max(product_sales, key=product_sales.get)

print('--------------------------------------')
print(f"Most Sold Product: {most_sold_product} with {product_sales[most_sold_product]} units sold.")
print('--------------------------------------')

#Generate sales report by product

print('--------------------------------------')
print("Sales Report by Product:")  
for product, sales in product_sales.items():
    print(f"{product}: {sales} units sold")
print('--------------------------------------')

#most profitable product

product_revenue = {}

with open('salesreport.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row['product']
        quantity = int(row['quantity'])
        price = float(row['price'])

        revenue = quantity * price

        if product in product_revenue:
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue

# Find the most profitable product
most_profitable_product = max(product_revenue, key=product_revenue.get)

print('--------------------------------------')
print(f"Most Profitable Product: {most_profitable_product} with revenue of ${product_revenue[most_profitable_product]:.2f}")
print('--------------------------------------')

#query sales report by date

date_sales = {}

with open('salesreport.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        date = row['date']
        quantity = int(row['quantity'])
        price = float(row['price'])

        revenue = quantity * price

        if date in date_sales:
            date_sales[date] += revenue
        else:
            date_sales[date] = revenue

print('--------------------------------------')
print("Sales Report by Date:")
for date, sales in date_sales.items():
    print(f"{date}: ${sales:.2f}")
print('--------------------------------------')