"""
Grimorio Metrics: Feedback Collector
"""

class GrimorioMetrics:
    def __init__(self):
        self.feedback_log = []

    def collect_feedback(self, user_id, query, response, rating=None, comments=None):
        entry = {
            'user_id': user_id,
            'query': query,
            'response': response,
            'rating': rating,
            'comments': comments
        }
        self.feedback_log.append(entry)
        return True
