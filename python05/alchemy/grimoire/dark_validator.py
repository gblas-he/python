from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    text = ingredients.lower()
    if any(item in text for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
