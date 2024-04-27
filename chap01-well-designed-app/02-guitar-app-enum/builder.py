from enum import Enum

class Builder(Enum):
    FENDER, GIBSON, MARTIN, YAMAHA, TAYLOR, ANY = range(1, 7)
    
    def __str__(self):
        match(self):
            case self.FENDER: return 'Fender'
            case self.GIBSON: return 'Gibson'
            case self.MARTIN: return 'Martin'
            case self.YAMAHA: return 'Yamaha'
            case self.TAYLOR: return 'Taylor'
            case self.ANY: return 'Any'