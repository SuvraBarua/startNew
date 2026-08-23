import csv

total_sales = 0
product_sales = {}
product_revenue = {}
date_sales = {}
record_count = 0
total_quantity = 0

with open('salesreport.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:

        product = row['product']
        quantity = int(row['quantity'])
        price = float(row['price'])
        record_count += 1
        total_quantity += quantity

        #for generating sales report by date
        date = row['date']

        #generate revenue for each product
        revenue = quantity * price

        #Calculate total sales
        total_sales += quantity * price

        #Generate sales report by product
        if product in product_sales:
            product_sales[product] += quantity
        else:
            product_sales[product] = quantity

        #for generating revenue
        if product in product_revenue:
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue

        #Generate sales report by date
        if date in date_sales:
            date_sales[date] += revenue
        else:
            date_sales[date] = revenue

print('--------------------------------------')
print(f"Total Sales: ${total_sales:.2f}")
print('--------------------------------------')

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

# Find the most profitable product
most_profitable_product = max(product_revenue, key=product_revenue.get)

#prints the most profitable product
print('--------------------------------------')
print(f"Most Profitable Product: {most_profitable_product} with revenue of ${product_revenue[most_profitable_product]:.2f}")
print('--------------------------------------')

#generates sales report by date
print('--------------------------------------')
print("Sales Report by Date:")
for date, sales in date_sales.items():
    print(f"{date}: ${sales:.2f}")
print('--------------------------------------')

print('--------------------------------------')
print(f"Customer Count: {record_count}")
print('--------------------------------------')

print('--------------------------------------')
print(f"Total Units Sold: {total_quantity}")
print('--------------------------------------')