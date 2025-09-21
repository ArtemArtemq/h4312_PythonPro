class BuildingErrorForArtem(Exception):
    def __str__(self):
        return f"With so much material the house cannot be build"

def check_material(now_material, min_material):
    if now_material >= min_material:
        print("Enough!")
    else:
        raise BuildingErrorForArtem

user_material = float(input("Enter material: "))
check_material(user_material, 200)