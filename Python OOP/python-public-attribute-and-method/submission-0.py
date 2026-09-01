class StoreItem:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price         


chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them
print(f"{chips.name}\n{chips.price}")
