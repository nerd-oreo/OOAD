from inventory import Inventory
from guitar import Guitar
from builder import Builder
from type import Type
from wood import Wood
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
    search_guitar = Guitar('', 0, Builder.FENDER, 'Stratocaster', Type.ELECTRIC, Wood.MAHOGANY, Wood.ALDER)
    guitar = inventory.search(search_guitar)
    
    if guitar != None:
        print(f"You may like this:\n{guitar}")
    else:
        print("Sorry. We have nothing for you.")

if __name__ == '__main__':
    main()