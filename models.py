class Customer:
    """Represents a ByteBites customer and their purchase history."""

    def __init__(self, name: str):
        if not name or not name.strip():
            raise ValueError("Customer name cannot be empty.")
        self.name = name.strip()
        self.purchase_history = []

    def get_name(self) -> str:
        return self.name

    def add_purchase(self, item: "Item") -> None:
        if item is None:
            raise ValueError("Purchase item cannot be empty.")
        self.purchase_history.append(item)

    def get_purchase_history(self) -> list["Item"]:
        return self.purchase_history

    def is_verified_customer(self) -> bool:
        return len(self.purchase_history) > 0


class Category:
    """Represents a product category such as Drinks or Desserts."""

    def __init__(self, name: str):
        if not name or not name.strip():
            raise ValueError("Category name cannot be empty.")
        self.name = name.strip()
        self.items = []

    def get_name(self) -> str:
        return self.name

    def add_item(self, item: "Item") -> None:
        if item is None:
            raise ValueError("Item cannot be empty.")
        self.items.append(item)

    def get_items(self) -> list["Item"]:
        return self.items

    def filter_items(self) -> list["Item"]:
        return self.items


class Item:
    """Represents one menu item sold by ByteBites."""

    def __init__(self, name: str, price: float, category: "Category", popularity_rating: float):
        if not name or not name.strip():
            raise ValueError("Item name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if category is None:
            raise ValueError("Category cannot be empty.")
        if popularity_rating < 0:
            raise ValueError("Popularity rating cannot be negative.")

        self.name = name.strip()
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def get_category(self) -> "Category":
        return self.category

    def get_popularity_rating(self) -> float:
        return self.popularity_rating


class Transaction:
    """Represents a single customer transaction containing selected items."""

    def __init__(self):
        self.items = []

    def add_item(self, item: Item) -> None:
        if item is None:
            raise ValueError("Item cannot be empty.")
        self.items.append(item)

    def get_items(self) -> list[Item]:
        return self.items

    def calculate_total(self) -> float:
        total = 0.0
        for item in self.items:
            total += item.get_price()
        return total


# Example scenario
if __name__ == "__main__":
    drinks = Category("Drinks")
    desserts = Category("Desserts")

    soda = Item("Large Soda", 2.50, drinks, 4.7)
    tea = Item("Iced Tea", 2.00, drinks, 4.5)
    cookie = Item("Chocolate Cookie", 3.25, desserts, 4.9)
    cake = Item("Vanilla Cake", 4.75, desserts, 4.8)

    drinks.add_item(soda)
    drinks.add_item(tea)
    desserts.add_item(cookie)
    desserts.add_item(cake)

    # Filtering by category
    drink_menu = drinks.filter_items()
    dessert_menu = desserts.filter_items()

    # Sorting by price (lowest to highest)
    sorted_drinks = sorted(drink_menu, key=lambda item: item.get_price())
    sorted_desserts = sorted(dessert_menu, key=lambda item: item.get_price(), reverse=True)

    # Customer purchase history
    customer = Customer("Jordan")
    customer.add_purchase(soda)
    customer.add_purchase(cookie)

    # Build a transaction
    order = Transaction()
    order.add_item(soda)
    order.add_item(cookie)
    order.add_item(tea)

    print("Customer:", customer.get_name())
    print("Purchase history:", [item.get_name() for item in customer.get_purchase_history()])
    print("Verified customer:", customer.is_verified_customer())

    print("Drinks menu:", [item.get_name() for item in drink_menu])
    print("Desserts menu:", [item.get_name() for item in dessert_menu])

    print("Sorted drinks by price:", [item.get_name() for item in sorted_drinks])
    print("Sorted desserts by price (high to low):", [item.get_name() for item in sorted_desserts])

    print("Order items:", [item.get_name() for item in order.get_items()])
    print("Order total:", order.calculate_total())

