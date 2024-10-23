
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
        
        # Form consensus based on multiple opinions (placeholder logic)
        if len(expert_responses) > 1:
            consensus = self.form_consensus(expert_responses)
        else:
            consensus = expert_responses[0]
        
        return consensus

    def form_consensus(self, opinions):
        # Simple logic to form a consensus (can be expanded with more complex algorithms)
        return opinions[0]  # Placeholder for now

class Expert:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def give_opinion(self, problem):
        # Provide an opinion based on expertise (can be expanded to simulate deeper expert knowledge)
        return f"As an expert in {self.expertise}, I believe the best approach is to handle: {problem}."
