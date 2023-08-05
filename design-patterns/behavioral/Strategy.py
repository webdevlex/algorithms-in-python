class DiscountStrategy:
    def calculate_discount(self, price):
        pass


class NoDiscount(DiscountStrategy):
    def calculate_discount(self, price):
        return 0


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def calculate_discount(self, price):
        return price * self.percentage / 100


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def calculate_discount(self, price):
        return min(self.amount, price)


class ShoppingCart:
    def __init__(self, discount_strategy):
        self.items = []
        self.discount_strategy = discount_strategy

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total_price = sum(item.price for item in self.items)
        discount = self.discount_strategy.calculate_discount(total_price)
        return total_price - discount


# Client code
item1 = Item("Widget", 100)
item2 = Item("Gadget", 200)

percentage_discount = PercentageDiscount(10)
fixed_amount_discount = FixedAmountDiscount(50)

cart_with_percentage_discount = ShoppingCart(percentage_discount)
cart_with_percentage_discount.add_item(item1)
cart_with_percentage_discount.add_item(item2)
print(
    "Total with percentage discount:", cart_with_percentage_discount.calculate_total()
)

cart_with_fixed_amount_discount = ShoppingCart(fixed_amount_discount)
cart_with_fixed_amount_discount.add_item(item1)
cart_with_fixed_amount_discount.add_item(item2)
print(
    "Total with fixed amount discount:",
    cart_with_fixed_amount_discount.calculate_total(),
)
