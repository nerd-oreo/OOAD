from enum import Enum

class Type(Enum):
    ACCOUSTIC, ELECTRIC = range(1,3)
    
    def __str__(self):
        match(self):
            case self.ACCOUSTIC:
                return 'Accoustic'
            case self.ELECTRIC:
                return 'Electric'