from inventory import Inventory
from guitar import Guitar
from __init__ import guitars


def init_inventory():
    inv = Inventory()
    for guitar in guitars:
        serial_number = guitar['serial_number']
        price = guitar['price']
        builder = guitar['builder']
        model = guitar['model']
        guitar_type = guitar['guitar_type']
        back_wood = guitar['back_wood']
        top_wood = guitar['top_wood']
        inv.add_guitar(serial_number, price, builder, model, guitar_type, back_wood, top_wood)
    return inv

def main():
    inventory = init_inventory()
    search_guitar = Guitar('', 0, 'Cord', 'CR100', 'Acoustic', 'Mahogany', 'Spruce')
    guitar = inventory.search(search_guitar)
    
    print(f"You search for: \n{search_guitar}")
    if guitar != None:
        print(f"You may like this {guitar.get_builder()} {guitar.get_type()} {guitar.get_back_wood()} {guitar.get_top_wood()}. Price: ${guitar.get_price()}")
    else:
        print("Sorry. We have nothing for you.")

if __name__ == '__main__':
    main()