from enum import Enum

class EnumTypeData(Enum):
    LOCAL = "local"
    BITMART = "bitmart"

    def valider_type_data(type_data):
        """
        Valide que 'type_data' est un membre valide de l'énumération EnumTypeData.
        Retourne le membre EnumTypeData correspondant ou lève une ValueError.
        """
        if isinstance(type_data, EnumTypeData):
            return type_data
        try:
            # Essayer de convertir une chaîne ou une autre valeur en membre d'énumération
            return EnumTypeData(type_data)
        except ValueError:
            raise ValueError(f"'{type_data}' n'est pas un type de donnée valide. Utilisez 'local' ou 'bitmart'.")
