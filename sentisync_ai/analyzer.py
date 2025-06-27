"""
SentiSync-AI: Intent Analyzer
"""

class SentiSyncAI:
    def analyze(self, query):
        """Stub: Classifies query into a domain."""
        # Simple keyword-based stub
        if any(word in query.lower() for word in ['house', 'property', 'real estate', 'home']):
            return 'realestate'
        elif any(word in query.lower() for word in ['hotel', 'restaurant', 'reservation', 'guest']):
            return 'hospitality'
        elif any(word in query.lower() for word in ['student', 'math', 'school', 'tutor', 'education']):
            return 'student'
        else:
            return 'unknown'
