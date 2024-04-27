class Guitar:
    def __init__(self, serial_number, price, builder, model, guitar_type, back_wood, top_wood):
        # Private properties
        self.__serial_number = serial_number    # str
        self.__price = price                    # float
        self.__builder = builder                # str
        self.__model = model                    # str
        self.__type = guitar_type               # str
        self.__back_wood = back_wood            # str
        self.__top_wood = top_wood              # str
        
    def __str__(self):
        return (
            f"Serial Number: \t{self.get_serial_number()}\n"
            f"Price: \t\t${self.get_price()}\n"
            f"Builder: \t{self.get_builder()}\n"
            f"Model: \t\t{self.get_model()}\n"
            f"Type: \t\t{self.get_type()}\n"
            f"Back Wood: \t{self.get_back_wood()}\n"
            f"Top Wood: \t{self.get_top_wood()}\n")
    
    def get_serial_number(self):
        ''' Return guitar serial number '''
        return self.__serial_number
        
    def get_price(self):
        ''' Return guitar price '''
        return self.__price
    
    def set_price(self, price):
        ''' Set guitar new price '''
        self.__price = price
        
    def get_builder(self):
        ''' Return guitar builder '''
        return self.__builder
        
    def get_model(self):
        ''' Return guitar model '''
        return self.__model
        
    def get_type(self):
        ''' Return guitar type '''
        return self.__type
        
    def get_back_wood(self):
        ''' Return back wood '''
        return self.__back_wood
        
    def get_top_wood(self):
        ''' Return top wood '''
        return self.__top_wood