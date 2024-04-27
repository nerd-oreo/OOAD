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
            builder = search_guitar.get_builder()
            if builder is not None and builder != '' and builder == guitar.get_builder():
                continue
            model = search_guitar.get_model()
            if model is not None and model != '' and model == guitar.get_model():
                continue
            guitar_type = search_guitar.get_type()
            if guitar_type is not None and guitar_type != '' and guitar_type == guitar.get_type():
                continue
            back_wood = search_guitar.get_back_wood()
            if back_wood is not None and back_wood != '' and back_wood == guitar.get_back_wood():
                continue
            top_wood = search_guitar.get_top_wood()
            if top_wood is not None and top_wood != '' and top_wood == guitar.get_top_wood():
                continue
            print(guitar)
            return guitar
            # The function never return guitar, which cause the function does not work correctly
        return None