"""
Maestro de GPT: Central Orchestrator
"""
from runika.engine import Runika
from sentisync_ai.analyzer import SentiSyncAI
from agents.casavisionario import CasaVisionario
from agents.hospitalia import Hospitalia
from agents.estudiamaster import EstudiaMaster

class Maestro:
    def __init__(self):
        self.runika = Runika()
        self.intent_analyzer = SentiSyncAI()
        self.agents = {
            'realestate': CasaVisionario(),
            'hospitality': Hospitalia(),
            'student': EstudiaMaster()
        }

    def handle_query(self, query, language='en'):
        prompt = self.runika.inject_prompt(query, language)
        domain = self.intent_analyzer.analyze(query)
        agent = self.agents.get(domain)
        if agent:
            return agent.answer(prompt)
        else:
            return "[Maestro] Sorry, I could not determine the right agent for your query."
