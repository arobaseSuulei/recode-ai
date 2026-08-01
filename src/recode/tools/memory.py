from smolagents import tool
import json,os

MEMORY_FILE="user_memory.json"


@tool
def remember(key:str,value:str)->str:
    """Enregistre une information sur l utilisateur, tu t en servira pour le connaitre
    
    Args:
        key:le nom de l information
        value:la valeur a retenir
    
    """
    ...
    