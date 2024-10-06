class Item:
    def __init__(self, name, quantity, price):
        self.name = name
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

    def remove_item(self, item):
        if item in self.item_list:
            self.item_list.remove(item)
            self.total_price -= item.quantity * item.price
        else:
            print("Sản phẩm không tồn tại trong đơn hàng.")

    def update_item(self, item, new_name, new_quantity, new_price):
        if item in self.item_list:
            index = self.item_list.index(item)
            self.total_price -= item.quantity * item.price

            # Giữ nguyên thông tin cũ nếu giá trị mới là 0
            if new_name != "0":
                item.name = new_name
            if new_quantity != 0:
                item.quantity = new_quantity
            if new_price != 0:
                item.price = new_price

            self.item_list[index] = item
            self.total_price += item.quantity * item.price
        else:
            print("Sản phẩm không tồn tại trong đơn hàng.")

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


def display_menu():
    print("\n--- Menu ---")
    print("1. Thêm sản phẩm")
    print("2. Xóa sản phẩm")
    print("3. Sửa sản phẩm")
    print("4. Hiển thị đơn hàng")
    print("5. Tính toán giá")
    print("6. Thoát")


def main():
    order = Order(customer_id="C001")
    while True:
        display_menu()
        choice = input("Chọn chức năng: ")

        if choice == "1":
            name = input("Nhập tên hàng: ")
            quantity = int(input("Nhập số lượng: "))
            price = int(input("Nhập giá: "))
            item = Item(name, quantity, price)
            order.add_item(item)
            print("Đã thêm sản phẩm.")

        elif choice == "2":
            name = input("Nhập tên hàng cần xóa: ")
            quantity = int(input("Nhập số lượng sản phẩm cần xóa: "))
            price = int(input("Nhập giá sản phẩm cần xóa: "))
            item_to_remove = Item(name, quantity, price)
            order.remove_item(item_to_remove)

        elif choice == "3":
            name = input("Nhập tên hàng cần sửa: ")
            quantity = int(input("Nhập số lượng sản phẩm cần sửa: "))
            price = int(input("Nhập giá sản phẩm cần sửa: "))
            item_to_update = Item(name, quantity, price)

            new_name = input("Nhập tên hàng mới (hoặc nhập 0 để giữ nguyên): ")
            new_quantity = int(input("Nhập số lượng mới (hoặc nhập 0 để giữ nguyên): "))
            new_price = int(input("Nhập giá mới (hoặc nhập 0 để giữ nguyên): "))

            order.update_item(item_to_update, new_name, new_quantity, new_price)

        elif choice == "4":
            print("\n--- Đơn hàng ---")
            for item in order.item_list:
                print(f"Tên hàng: {item.name}")
                print(f"Số lượng: {item.quantity}")
                print(f"Giá: {item.price}")
                print("========-----||-----========")
                
            print(f"Tổng tiền: {order.total()}")

        elif choice == "5":
            total_price = order.total()

            bulk_promo = BulkOrderPromo(total_price)
            bulk_discount = bulk_promo.discount()

            loyalty_years = int(input("Nhập số năm trung thành của khách hàng: "))
            loyalty_promo = LoyaltyPromo(total_price, customer_loyalty_years=loyalty_years) 
            loyalty_discount = loyalty_promo.discount()

            final_price = total_price - max(bulk_discount, loyalty_discount)

            print(f"Tổng giá trị đơn hàng: {total_price}")
            print(f"Giảm giá BulkOrderPromo: {bulk_discount}")
            print(f"Giảm giá LoyaltyPromo (với {loyalty_years} năm trung thành): {loyalty_discount}")
            print(f"Tổng giá sau khi áp dụng giảm giá: {final_price}")

        elif choice == "6":
            print("Tạm biệt và hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()
