class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house cannot be built!"

def check_material(amount_of_material, limit_material):
    if amount_of_material > limit_material:
        return "Enough material"
    else:
        raise BuildingError(amount_of_material)

material = 123
check_material(material, limit_material=300)