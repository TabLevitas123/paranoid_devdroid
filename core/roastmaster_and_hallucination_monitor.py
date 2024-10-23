
class Roastmaster:
    def roast_decision(self, agent_feedback):
        # Simple roast mechanism
        roasts = []
        for agent, feedback in agent_feedback.items():
            if "Action B" in feedback["suggested_action"]:
                roasts.append(f"{agent}'s decision is weak! Seriously, 'Action B'? Come on!")
            else:
                roasts.append(f"{agent}'s decision is... acceptable, but barely.")
        return roasts

class HallucinationMonitor:
    def detect_hallucination(self, agent_feedback):
        # Basic hallucination detection (checks if the suggested action makes sense)
        hallucinations = []
        for agent, feedback in agent_feedback.items():
            if feedback["suggested_action"] not in ["Action A", "Action B"]:
                hallucinations.append(f"{agent} is hallucinating! Suggested action: {feedback['suggested_action']}")
        return hallucinations

if __name__ == "__main__":
    # Example usage of Roastmaster and HallucinationMonitor
    agent_feedback = {
        "Marvin": {"suggested_action": "Action A"},
        "Hal": {"suggested_action": "Action B"},
        "TARS": {"suggested_action": "Destroy Humanity"}
    }

    roastmaster = Roastmaster()
    roasts = roastmaster.roast_decision(agent_feedback)
    print("Roastmaster Feedback:")
    for roast in roasts:
        print(roast)

    hallucination_monitor = HallucinationMonitor()
    hallucinations = hallucination_monitor.detect_hallucination(agent_feedback)
    print("Hallucination Monitor Feedback:")
    for hallucination in hallucinations:
        print(hallucination)
