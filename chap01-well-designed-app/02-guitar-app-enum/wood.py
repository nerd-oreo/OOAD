from enum import Enum

class Wood(Enum):
    MAHOGANY, ALDER, MAPLE, INDIAN_ROSEWOOD, SITKA_SPRUCE, NATO, SPRUCE, ENGLEMANN_SPRUCE, ANY = range(1, 10)
    
    def __str__(self):
        match(self):
            case self.MAHOGANY: return 'Mahogany'
            case self.ALDER: return 'Alder'
            case self.MAPLE: return 'Maple'
            case self.INDIAN_ROSEWOOD: return 'Indian Rosewood'
            case self.SITKA_SPRUCE: return 'Sitka Spruce'
            case self.NATO: return 'Nato'
            case self.SPRUCE: return 'Spruce'
            case self.ENGLEMANN_SPRUCE: return 'Engelmann Spruce'
            case self.ANY: return 'Any'