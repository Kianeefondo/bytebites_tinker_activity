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

