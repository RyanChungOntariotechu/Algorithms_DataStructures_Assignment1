#-------------Question 1: Data Management Using Fundamental Structures------#

class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
#Loading Product data
def load_product_data(filename):
    products = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            product = Product(int(data[0]), data[1], float(data[2]), data[3])
            products.append(product)
    return products

#Storing Product Data
def store_product_data(filename, products):
    with open(filename, 'w') as file:
        for product in products:
            file.write(f"{product.product_id},{product.name},{product.price},{product.category}\n")

#------------Question 2: Data Manipulation Operations-----------------#

#Implementing the insert function         
def insert_product(products, new_product):
    products.append(new_product)

#implementing the update product 
def update_product(products, product_id, new_name, new_price, new_category):
    for product in products:
        if product.product_id == product_id:
            product.name = new_name
            product.price = new_price
            product.category = new_category
            break

#Implementing the delete product function      
def delete_product(products, product_id):
    products[:] = [product for product in products if product.product_id != product_id]

#Implementing search product by ID 
def search_product_by_id(products, product_id):
    for product in products:
        if product.product_id == product_id:
            return product
    return None

#Implemeneting search by product name
def search_product_by_name(products, name):
    result = []
    for product in products:
        if name.lower() in product.name.lower():
            result.append(product)
    return result
#-------------------Question 3: Sorting Algorithms----------------#
# Implemeneting of quick sort algortithm 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2].price
    left = [product for product in arr if product.price < pivot]
    middle = [product for product in arr if product.price == pivot]
    right = [product for product in arr if product.price > pivot]
    return quick_sort(left) + middle + quick_sort(right)

#-------------Testing Functions-----------------#

product_data = load_product_data("product_data.txt")

# Inserting a new product function
insert_product(product_data, Product(101, "Testing Insert function", 15.99, "Testing Insert Function"))

# Updating a product function
update_product(product_data, 69260, "Testing Update function", 99.99, "Testing Update Function")

# Deleting a product function
delete_product(product_data, 68097)

# Search by product ID function
result_product = search_product_by_id(product_data, 18086)
if result_product:
    print("Product Has Been Found:", result_product.name)
else:
    print("Product Was Not Found.")

# Search by product name function
results = search_product_by_name(product_data, "shirt")
print("Products found by name:")
for product in results:
    print(product.name)

# Sorting products by price using Quick Sort function
sorted_products = quick_sort(product_data)
print("Sorted Products by Price:")
for product in sorted_products:
    print(product.name, "-", product.price)

# Storing the updated data function
store_product_data("updated_product_data.txt", product_data)

#-------------Question 4: Complexity Analysis--------------#

#Implementation of Complexity Analysis
def analyze_sorting_complexity(data):
    import time
    import random

    def generate_random_products(size):
        return [Product(i, f"Product {i}", random.uniform(1, 1000), "Category") for i in range(1, size + 1)]

    def measure_sorting_time(data):
        start_time = time.time()
        sorted_data = quick_sort(data)
        end_time = time.time()
        return end_time - start_time

    print("Analyzing sorting complexity...\n")
    for size in [5000, 50000, 500000]:
        sorted_data = generate_random_products(size)
        reverse_sorted_data = sorted_data[::-1]

        print(f"Data size: {size}")
        print("Sorted data:")
        print("Best case Scenario:", measure_sorting_time(sorted_data))
        print("Worst case Scenario:", measure_sorting_time(reverse_sorted_data))
        print("Average case Scenario:", measure_sorting_time(sorted_data))  # Same as best case as Quick Sort performs well on average

# Analyzing sorting complexity
analyze_sorting_complexity(product_data)

