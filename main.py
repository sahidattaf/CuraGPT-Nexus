"""
CuraGPT Nexus: Main Entry Point
"""
from maestro.orchestrator import Maestro
from grimorio_metrics.collector import GrimorioMetrics
from loopalquimia.refiner import LoopAlquimia
from dashboard.insight_orb import InsightOrb

# Instantiate core components
maestro = Maestro()
grimo = GrimorioMetrics()
refiner = LoopAlquimia()
dashboard = InsightOrb()

def run_demo():
    # Example queries
    queries = [
        ("How should I price my house in Curaçao competitively?", 'user1'),
        ("How can I improve my restaurant’s reservation process?", 'user2'),
        ("Solve this math problem: 12 + 7 * 2", 'user3')
    ]
    metrics = {}
    for query, user in queries:
        response = maestro.handle_query(query)
        print(f"User: {query}\nAI: {response}\n")
        grimo.collect_feedback(user, query, response, rating=5)
    # Simulate refinement
    print(refiner.refine(grimo.feedback_log))
    # Show dashboard
    metrics['feedback_count'] = len(grimo.feedback_log)
    dashboard.show_metrics(metrics)

if __name__ == "__main__":
    run_demo()
