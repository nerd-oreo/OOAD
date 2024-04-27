from enum import Enum

class Builder(Enum):
    FENDER, GIBSON, MARTIN, YAMAHA, TAYLOR, ANY = range(1, 7)
    
    def __str__(self):
        match(self):
            case self.FENDER: return 'fender'
            case self.GIBSON: return 'gibson'
            case self.MARTIN: return 'martin'
            case self.YAMAHA: return 'yamaha'
            case self.TAYLOR: return 'taylor'
            case self.ANY: return 'any'