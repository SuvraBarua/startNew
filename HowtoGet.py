import urllib.request
import urllib.error
import json
from collections import defaultdict
from datetime import datetime

url1 = "https://raw.githubusercontent.com/SuvraBarua/MathGames/17c07ade7f5488d7253f3527ca2649e51476b3dc/textfile.txt"
url2 = "https://raw.githubusercontent.com/SuvraBarua/MathGames/17c07ade7f5488d7253f3527ca2649e51477b3dc/textfile.txt"
url3 = "https://raw.githubusercontent.com/SuvraBarua/MathGames/refs/heads/main/sales_data.json"

record_count = 0
total_quantity = 0
total_sales = 0
product_sales = defaultdict(int)
product_revenue = defaultdict(float)
date_sales = defaultdict(float)

try:
    with urllib.request.urlopen(url3) as response:
        print("status code:", response.status)
        print('headers:', response.headers["Content-Type"])

        raw_data = response.read()
        texts = raw_data.decode("utf-8")

        sales_data = json.loads(texts)    

        print(f"Loaded {len(sales_data)} records from 'sales_data.json'.")

        for row in sales_data:
            product = row['product']
            quantity = int(row['quantity'])
            price = float(row['price'])
            date = row['date']

            record_count += 1
            total_quantity += quantity

            revenue = quantity * price

            total_sales += revenue

            #generate sales report by product
            if product in product_sales:
                product_sales[product] += quantity
            else:
                product_sales[product] = quantity

            #genrate revenue for each product
            if product in product_revenue:
                product_revenue[product] += revenue
            else:
                product_revenue[product] = revenue

            #generate sales report by date
            if date in date_sales:
                date_sales[date] += revenue
            else:
                date_sales[date] = revenue

            # Process the data as needed
            print(f"Product: {product}, Quantity: {quantity}, Price: {price}, Date: {date}")
        

except urllib.error.URLError as e:
    print("Error fetching URL:", e)
except urllib.error.HTTPError as e:
    print("HTTP error occurred:", e)
except Exception as e:
    print("An unexpected error occurred:", e)

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