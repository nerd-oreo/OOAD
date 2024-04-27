from guitar import Guitar

class Inventory:
    def __init__(self):
        self.__guitar_list = []
        
    def add_guitar(self, serial_number, price, builder, model, guitar_type, back_wood, top_wood):
        guitar = Guitar(serial_number, price, builder, model, guitar_type, back_wood, top_wood)
        self.__guitar_list.append(guitar)
        
    def get_guitar(self, serial_number):
        for guitar in self.__guitar_list:
            if guitar.get_serial_number() == serial_number:
                return guitar 
        return None
    
    def search(self, search_guitar:Guitar):
        for guitar in self.__guitar_list:
            # Ignore serial number since it's unique
            # Ignore price since it's unique
            print(guitar)
            if search_guitar.get_builder() != guitar.get_builder():
                continue
            model = search_guitar.get_model()
            if model is not None and model != '' and model.lower() != guitar.get_model().lower():
                continue
            if search_guitar.get_type() != guitar.get_type():
                continue
            if search_guitar.get_back_wood() != guitar.get_back_wood():
                continue
            if search_guitar.get_top_wood() != guitar.get_top_wood():
                continue
            return guitar
        return None