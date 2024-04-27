from builder import Builder
from type import Type
from wood import Wood

guitars = [
    {
        "serial_number": "EL00001", 
        "price": 1299.99, 
        "builder": Builder.FENDER, 
        "model": "Stratocaster", 
        "guitar_type": Type.ELECTRIC, 
        "back_wood": Wood.MAHOGANY, 
        "top_wood": Wood.ALDER,
    },
    {
        "serial_number": "EL00002", 
        "price": 899.99, 
        "builder": Builder.GIBSON, 
        "model": "Les Paul", 
        "guitar_type": Type.ELECTRIC, 
        "back_wood": Wood.MAHOGANY, 
        "top_wood": Wood.MAPLE,
    },
    {
        "serial_number": "AC00003", 
        "price": 1999.99, 
        "builder": Builder.MARTIN, 
        "model": "OOO-DC Aura", 
        "guitar_type": Type.ACCOUSTIC, 
        "back_wood": Wood.INDIAN_ROSEWOOD, 
        "top_wood": Wood.SITKA_SPRUCE,
    },
    {
        "serial_number": "AC00004", 
        "price": 749.99, 
        "builder": Builder.YAMAHA, 
        "model": "FG800", 
        "guitar_type": Type.ACCOUSTIC, 
        "back_wood": Wood.NATO, 
        "top_wood": Wood.SPRUCE,
    },
    {
        "serial_number": "AC00005", 
        "price": 1599.99, 
        "builder": Builder.TAYLOR, 
        "model": "814ce DLX", 
        "guitar_type": Type.ACCOUSTIC, 
        "back_wood": Wood.INDIAN_ROSEWOOD, 
        "top_wood": Wood.ENGLEMANN_SPRUCE,
    },
 ]