import re
import pandas as pd

def limpieza_canonica(texto: str) -> str:
    """
    Limpieza canónica de texto:
    - Conversión a minúsculas
    - Eliminación de tildes
    - Eliminación de comas
    - Eliminación de espacios duplicados
    """
    if pd.isna(texto):
        return texto
    
    texto = texto.lower()
    
    reemplazos = str.maketrans(
        "áéíóú",
        "aeiou"
    )
    texto = texto.translate(reemplazos)
    texto = texto.translate(str.maketrans("", "", ',\"\'()“”.…#¿?¡!-—⸻@*='))
    texto = re.sub(r"\s+", " ", texto).strip()
    
    return texto