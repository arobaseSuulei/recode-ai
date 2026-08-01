import os
from dotenv import load_dotenv
from smolagents import CodeAgent,OpenAIServerModel
from recode.tools import read_file,writing_code
from recode.tools.memory import remember


load_dotenv()

OPENAI_API_TOKEN=os.environ.get("OPENAI_API_TOKEN")

def create_agent():
  
    model = OpenAIServerModel(
    model_id="gpt-4o-mini",
    api_key=OPENAI_API_TOKEN,
    )

    agent = CodeAgent(
    tools=[read_file,writing_code,remember],
    model=model,
    instructions="Quand on te demande de modifier du code, utilise TOUJOURS l'outil "
                 "writing_code pour sauvegarder le résultat sur disque. Ne te contente "
                 "jamais de donner le code en texte dans ta réponse finale. UTILISE toujours read_file pour connaitre le contenu d un fichier avant d ecrire dedans"
    )

    return agent