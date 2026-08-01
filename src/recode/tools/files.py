import os
from smolagents import tool
    
def _resolve_safe_path(filepath:str,workspace:str)->str:
    """ Empeche de lire ou d ecrire en dehors du chemin de travail autorisé"""
    full_path=os.path.abspath(os.path.join(workspace,filepath))
    workspace_abs=os.path.abspath(workspace)
    
    if not full_path.startswith(workspace_abs):
        raise ValueError(f"Accès refusé en dehors du dossier de travail : {filepath}")

    return full_path




@tool
def writing_code(filepath:str,content:str)->str:
    """ Ecris ou remplace entierement le contenu d un fichier
    
    Args:
        filepath: le chemin du fichier (exemple, code.py ici pas dans main.py)
        content: le nouveau contenu complet du fichier
    """
    safe_path=_resolve_safe_path(filepath,workspace=os.getcwd())
    with open(safe_path,"w",encoding="utf-8") as f:
        f.write(content)
    return f"Fichier {filepath} mis a jour (++{len(content)})"
    

@tool
def read_file(filepath:str)->str:
    """ Lis le contenu d un fichier 
    
    Args:
        filepath: le chemin du fichier a lire
    """
    safe_path=_resolve_safe_path(filepath,workspace=os.getcwd())
    with open(safe_path,"r",encoding="utf-8") as f:
        return f.read()
