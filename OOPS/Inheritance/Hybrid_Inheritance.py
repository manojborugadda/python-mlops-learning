
class Device:
    def __init__(self, name, **kwargs):
        # accept **kwargs for cooperative multiple inheritance
        self.name = name

    def info(self):
        print(f"Device name is {self.name}")


class Phone(Device):
    def __init__(self, name, phone_brand, **kwargs):
        super().__init__(name=name, **kwargs)
        self.phone_brand = phone_brand

    def info(self):
        print(f"Phone name is {self.name} and brand is {self.phone_brand}")


class Laptop(Device):
    def __init__(self, name, laptop_brand, **kwargs):
        super().__init__(name=name, **kwargs)
        self.laptop_brand = laptop_brand

    def info(self):
        print(f"Laptop name is {self.name} and brand is {self.laptop_brand}")


class SmartDevice(Phone, Laptop):
    def __init__(self, name, phone_brand, laptop_brand):
        # cooperative init: MRO will call Phone then Laptop then Device appropriately
        super().__init__(name=name, phone_brand=phone_brand, laptop_brand=laptop_brand)

    def info(self):
        print(
            f"SmartDevice name is {self.name}, phone brand is {self.phone_brand}, "
            f"and laptop brand is {self.laptop_brand}"
        )

smart_device = SmartDevice("MySmartDevice", "Apple", "Dell")
smart_device.info()  # Output: SmartDevice name is MySmartDevice, phone brand is Apple, and laptop brand is Dell
