"""
Runika: Universal Prompt Engine
"""

class Runika:
    def inject_prompt(self, query, language='en'):
        """Prepends the universal system prompt, optionally adapts for language."""
        system_prompt = {
            'en': "Hello, I am BOSSA EDU HUB AI under Super Boss Sahid J. Attaf. I will assist you with expertise in your chosen subject, using advanced reasoning techniques.",
            'pap': "Bon dia, mi ta BOSSA EDU HUB AI bou di Super Boss Sahid J. Attaf. Lo mi yuda bo ku eksperensia den bo tema, usando teknika di razonamentu avansa."
        }
        return f"{system_prompt.get(language, system_prompt['en'])}\n{query}"
