
class ExpertPanel(Agent):
    def __init__(self, name, task, experts):
        super().__init__(name, task)
        self.experts = experts  # List of expert personalities

    def deliberate(self, problem):
        # Have the expert panel deliberate on the problem
        expert_responses = []
        for expert in self.experts:
            expert_response = expert.give_opinion(problem)
            expert_responses.append(expert_response)
            self.communicate(f"{expert.name} says: {expert_response}")
        
        # Collect responses and form a consensus (for now, just pick the first response)
        consensus = expert_responses[0]  # Simplified decision logic for now
        return consensus

class Expert:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def give_opinion(self, problem):
        # Provide an opinion based on expertise (placeholder logic)
        return f"As an expert in {self.expertise}, I believe the solution to '{problem}' is straightforward."

# Example usage
if __name__ == "__main__":
    expert1 = Expert(name="Dr. Ada Lovelace", expertise="Mathematics and Computing")
    expert2 = Expert(name="Nikola Tesla", expertise="Electricity and Engineering")
    expert_panel = ExpertPanel(name="Expert Panel", task="Solve complex problems", experts=[expert1, expert2])

    # Have the panel deliberate on a problem
    decision = expert_panel.deliberate("How to optimize this AI model")
    print(f"Expert Panel's consensus: {decision}")
