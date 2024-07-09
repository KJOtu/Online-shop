import time
import random

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = float(price)
        self.category = category

class OnlineShop:
    def __init__(self):
        self.products = []

    def load_data(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                id, name, price, category = line.strip().split(', ')
                self.products.append(Product(id, name, float(price), category))
        print(f"Loaded {len(self.products)} products.")

    def insert(self, product):
        self.products.append(product)
        print(f"Inserted product: {product.name}")

    def update(self, id, new_price):
        for product in self.products:
            if product.id == id:
                product.price = new_price
                print(f"Updated product {product.name} price to {new_price}")
                return
        print(f"Product with ID {id} not found.")

    def delete(self, id):
        for i, product in enumerate(self.products):
            if product.id == id:
                del self.products[i]
                print(f"Deleted product: {product.name}")
                return
        print(f"Product with ID {id} not found.")

    def search(self, key, value):
        results = []
        for product in self.products:
            if getattr(product, key.lower()) == value:
                results.append(product)
        return results

    def bubble_sort(self):
        n = len(self.products)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.products[j].price > self.products[j + 1].price:
                    self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]

    def insertion_sort(self):
        for i in range(1, len(self.products)):
            key = self.products[i]
            j = i - 1
            while j >= 0 and key.price < self.products[j].price:
                self.products[j + 1] = self.products[j]
                j -= 1
            self.products[j + 1] = key

    def measure_sort_time(self, sort_method):
        start_time = time.time()
        sort_method()
        end_time = time.time()
        return end_time - start_time

    def analyze_complexity(self):
        # Best case: already sorted
        self.products.sort(key=lambda x: x.price)
        best_case_time = self.measure_sort_time(self.bubble_sort)
        
        # Worst case: reverse sorted
        self.products.sort(key=lambda x: x.price, reverse=True)
        worst_case_time = self.measure_sort_time(self.bubble_sort)
        
        # Average case: random order
        random.shuffle(self.products)
        average_case_time = self.measure_sort_time(self.bubble_sort)
        
        print(f"Best case time: {best_case_time:.6f} seconds")
        print(f"Worst case time: {worst_case_time:.6f} seconds")
        print(f"Average case time: {average_case_time:.6f} seconds")

    def display_products(self, count=5):
        print(f"Displaying first {count} products:")
        for product in self.products[:count]:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

if __name__ == "__main__":
    shop = OnlineShop()
    
    print("Loading product data:")
    shop.load_data("product_data.txt")
    shop.display_products()

    print("Inserting a new product:")
    new_product = Product("99999", "New Item", 199.99, "Electronics")
    shop.insert(new_product)
    shop.display_products()

    print("Updating a product:")
    shop.update("57353", 599.99)
    shop.display_products()

    print("Deleting a product:")
    shop.delete("68097")
    shop.display_products()

    print("Searching for products:")
    results = shop.search("category", "Electronics")
    print(f"Found {len(results)} Electronics products")
    for product in results[:5]:
        print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")

    print("Sorting products:")
    bubble_sort_time = shop.measure_sort_time(shop.bubble_sort)
    print(f"Bubble sort time: {bubble_sort_time:.6f} seconds")
    shop.display_products()

    print("Reshuffling products for insertion sort:")
    random.shuffle(shop.products)
    insertion_sort_time = shop.measure_sort_time(shop.insertion_sort)
    print(f"Insertion sort time: {insertion_sort_time:.6f} seconds")
    shop.display_products()

    print("Complexity Analysis:")
    shop.analyze_complexity()