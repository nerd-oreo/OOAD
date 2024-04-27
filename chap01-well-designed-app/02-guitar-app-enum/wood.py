from enum import Enum

class Wood(Enum):
    MAHOGANY, ALDER, MAPLE, INDIAN_ROSEWOOD, SITKA_SPRUCE, NATO, SPRUCE, ENGLEMANN_SPRUCE, ANY = range(1, 10)
    
    def __str__(self):
        match(self):
            case self.MAHOGANY: return 'mahogany'
            case self.ALDER: return 'alder'
            case self.MAPLE: return 'maple'
            case self.INDIAN_ROSEWOOD: return 'indian rosewood'
            case self.SITKA_SPRUCE: return 'sitka spruce'
            case self.NATO: return 'nato'
            case self.SPRUCE: return 'spruce'
            case self.ENGLEMANN_SPRUCE: return 'engelmann spruce'
            case self.ANY: return 'any'