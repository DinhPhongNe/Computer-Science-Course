class Item:
    def __init__(self, item_id, name, quantity, price, production_date, expiration_date, manufacturer, ingredients):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.production_date = production_date
        self.expiration_date = expiration_date
        self.manufacturer = manufacturer
        self.ingredients = ingredients

class Order:
    def __init__(self, order_id, employee_id, order_date, customer_id):
        self.order_id = order_id
        self.employee_id = employee_id
        self.order_date = order_date
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

    def update_item(self, item, new_name, new_quantity, new_price, new_production_date, new_expiration_date, new_manufacturer, new_ingredients):
        if item in self.item_list:
            index = self.item_list.index(item)
            self.total_price -= item.quantity * item.price

            # Giữ nguyên thông tin cũ nếu giá trị mới là 0 hoặc rỗng
            if new_name != "0":
                item.name = new_name
            if new_quantity != 0:
                item.quantity = new_quantity
            if new_price != 0:
                item.price = new_price
            if new_production_date != "0":
                item.production_date = new_production_date
            if new_expiration_date != "0":
                item.expiration_date = new_expiration_date
            if new_manufacturer != "0":
                item.manufacturer = new_manufacturer
            if new_ingredients != "0":
                item.ingredients = new_ingredients

            self.item_list[index] = item
            self.total_price += item.quantity * item.price
        else:
            print("Sản phẩm không tồn tại trong đơn hàng.")

    def total(self):
        return self.total_price 

    def format_price_in_millions_thousands(self, price):
        units = ["", "ngàn", "triệu", "tỷ", "ngàn tỷ"]
        unit_index = 0

        while price >= 1000:
            price //= 1000
            unit_index += 1

        if unit_index > 0:
            return f"{price} {units[unit_index]} đồng"
        else:
            return f"{price} đồng"
        
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
    order = Order(order_id="O001", employee_id="E001", order_date="2023-10-27", customer_id="C001")
    while True:
        display_menu()
        choice = input("Chọn chức năng: ")

        if choice == "1":
            item_id = input("Nhập mã sản phẩm: ")
            name = input("Nhập tên hàng: ")
            quantity = int(input("Nhập số lượng: "))
            price = int(input("Nhập giá: "))
            production_date = input("Nhập ngày sản xuất (YYYY-MM-DD): ")
            expiration_date = input("Nhập hạn sử dụng (YYYY-MM-DD): ")
            manufacturer = input("Nhập nhà sản xuất: ")
            ingredients = input("Nhập thành phần tạo thành: ")
            item = Item(item_id, name, quantity, price, production_date, expiration_date, manufacturer, ingredients)
            order.add_item(item)
            print("Đã thêm sản phẩm.")

        elif choice == "2":
            name = input("Nhập tên hàng cần xóa: ")
            quantity = int(input("Nhập số lượng sản phẩm cần xóa: "))
            price = int(input("Nhập giá sản phẩm cần xóa: "))
            production_date = input("Nhập ngày sản xuất (YYYY-MM-DD): ")
            expiration_date = input("Nhập hạn sử dụng (YYYY-MM-DD): ")
            manufacturer = input("Nhập nhà sản xuất: ")
            ingredients = input("Nhập thành phần tạo thành: ")
            item_to_remove = Item(None, name, quantity, price, production_date, expiration_date, manufacturer, ingredients)
            order.remove_item(item_to_remove)

        elif choice == "3":
            name = input("Nhập tên hàng cần sửa: ")
            quantity = int(input("Nhập số lượng sản phẩm cần sửa: "))
            price = int(input("Nhập giá sản phẩm cần sửa: "))
            production_date = input("Nhập ngày sản xuất (YYYY-MM-DD): ")
            expiration_date = input("Nhập hạn sử dụng (YYYY-MM-DD): ")
            manufacturer = input("Nhập nhà sản xuất: ")
            ingredients = input("Nhập thành phần tạo thành: ")
            item_to_update = Item(None, name, quantity, price, production_date, expiration_date, manufacturer, ingredients)

            new_name = input("Nhập tên hàng mới (hoặc nhập 0 để giữ nguyên): ")
            new_quantity = int(input("Nhập số lượng mới (hoặc nhập 0 để giữ nguyên): "))
            new_price = int(input("Nhập giá mới (hoặc nhập 0 để giữ nguyên): "))
            new_production_date = input("Nhập ngày sản xuất mới (YYYY-MM-DD) (hoặc nhập 0 để giữ nguyên): ")
            new_expiration_date = input("Nhập hạn sử dụng mới (YYYY-MM-DD) (hoặc nhập 0 để giữ nguyên): ")
            new_manufacturer = input("Nhập nhà sản xuất mới (hoặc nhập 0 để giữ nguyên): ")
            new_ingredients = input("Nhập thành phần tạo thành mới (hoặc nhập 0 để giữ nguyên): ")


            order.update_item(item_to_update, new_name, new_quantity, new_price, new_production_date, new_expiration_date, new_manufacturer, new_ingredients)

        elif choice == "4":
            print("\n--- Đơn hàng ---")
            for item in order.item_list:
                print(f"Mã sản phẩm: {item.item_id}")
                print(f"Tên hàng: {item.name}")
                print(f"Số lượng: {item.quantity}")
                print(f"Giá: {item.price}")
                print(f"Ngày sản xuất: {item.production_date}")
                print(f"Hạn sử dụng: {item.expiration_date}")
                print(f"Nhà sản xuất: {item.manufacturer}")
                print(f"Thành phần tạo thành: {item.ingredients}")
                print("========-----||-----========")
            print(f"Tổng tiền: {order.total()}")
            print(f"Tổng tiền (đọc): {order.format_price_in_millions_thousands(order.total())}")

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
            print(f"Tổng giá sau khi áp dụng giảm giá (đọc): {order.format_price_in_millions_thousands(final_price)}")

        elif choice == "6":
            print("Tạm biệt và hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()