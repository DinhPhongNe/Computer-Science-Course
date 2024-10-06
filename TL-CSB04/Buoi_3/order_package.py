
class Item:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

class Order:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.item_list = []
        self.total_price = 0

    def add_item(self, item):
        self.item_list.append(item)
        self.total_price += item.quantity * item.price

    def total(self):
        return self.total_price 


class Promo:
    def __init__(self, price):
        self.price = price

    def discount(self):
        pass


class BulkOrderPromo(Promo):
    def discount(self):
        if self.price > 1000:
            return self.price * 0.10
        return 0


class LoyaltyPromo(Promo):
    def __init__(self, price, customer_loyalty_years):
        super().__init__(price)
        self.customer_loyalty_years = customer_loyalty_years

    def discount(self):
        if self.customer_loyalty_years > 5:
            return self.price * 0.05
        return 0


item1 = Item(10, 100)
item2 = Item(5, 200)

order = Order(customer_id="C001")
order.add_item(item1)
order.add_item(item2)

total_price = order.total()

bulk_promo = BulkOrderPromo(total_price)
bulk_discount = bulk_promo.discount()

loyalty_promo = LoyaltyPromo(total_price, customer_loyalty_years=6)
loyalty_discount = loyalty_promo.discount()

final_price = total_price - max(bulk_discount, loyalty_discount)

print(f"Tổng giá trị đơn hàng: {total_price}")
print(f"Giảm giá BulkOrderPromo: {bulk_discount}")
print(f"Giảm giá LoyaltyPromo: {loyalty_discount}")
print(f"Tổng giá sau khi áp dụng giảm giá: {final_price}")