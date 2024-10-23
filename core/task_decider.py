
class ConsensusEngine:
    def __init__(self):
        self.feedback = {}

    def gather_feedback(self, agent_list):
        # Collect feedback from all agents
        for agent in agent_list:
            feedback = agent.provide_feedback()  # Assuming agents have a feedback method
            self.feedback[agent.name] = feedback
            print(f"Feedback from {agent.name}: {feedback}")
        return self.feedback

    def decide_best_action(self, feedback_list):
        # Simplified decision logic (just chooses based on majority for now)
        action_votes = {}
        for agent, feedback in feedback_list.items():
            action = feedback["suggested_action"]
            if action not in action_votes:
                action_votes[action] = 0
            action_votes[action] += 1

        # Select action with the most votes
        best_action = max(action_votes, key=action_votes.get)
        print(f"Decided best action: {best_action}")
        return best_action

# Extend Agent class to provide feedback for decision-making
class AgentWithFeedback:
    def __init__(self, name, feedback_function):
        self.name = name
        self.feedback_function = feedback_function

    def provide_feedback(self):
        return self.feedback_function()

if __name__ == "__main__":
    # Example usage of ConsensusEngine
    agent1 = AgentWithFeedback("Marvin", lambda: {"suggested_action": "Action A"})
    agent2 = AgentWithFeedback("Hal", lambda: {"suggested_action": "Action B"})
    agent3 = AgentWithFeedback("TARS", lambda: {"suggested_action": "Action A"})

    agent_list = [agent1, agent2, agent3]

    consensus_engine = ConsensusEngine()
    feedback_list = consensus_engine.gather_feedback(agent_list)
    best_action = consensus_engine.decide_best_action(feedback_list)
