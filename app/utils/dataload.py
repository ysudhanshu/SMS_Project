"""To upload dummy data
"""

from ..models.models import ChemicalElement, Commodity, ChemicalComposition, User

def load_data():

    element_store = {6: "C", 7: "N", 8: "O", 13: "Al", 26: "FE", 29:"Cu", 999: "Unknown"}
    for key, value in element_store.items():
        element = ChemicalElement(key, value)
        element.save_to_db()

    commodity = Commodity(42, "Plane & Structural", 1234.50, 200.5)
    commodity.save_to_db()

    chem_composition = ChemicalComposition(42, 13, 25)
    chem_composition.save_to_db()

    chem_composition = ChemicalComposition(42, 26, 50)
    chem_composition.save_to_db()

    chem_composition = ChemicalComposition(42, 29, 10)
    chem_composition.save_to_db()

    chem_composition = ChemicalComposition(42, 999, 15)
    chem_composition.save_to_db()

    user = User(1, "dev", "dev@123")
    user.save_to_db()
