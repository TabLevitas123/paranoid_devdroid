
class ExpertPanel(Agent):
    def __init__(self, name, task, experts):
        super().__init__(name, task)
        self.experts = experts  # List of expert personalities

    def deliberate(self, problem):
        # Have the expert panel deliberate on the problem and collect responses
        expert_responses = []
        for expert in self.experts:
            expert_response = expert.give_opinion(problem)
            expert_responses.append(expert_response)
            self.communicate(f"{expert.name} says: {expert_response}")
        
        # Form consensus based on expert opinions with majority logic
        consensus = self.form_consensus(expert_responses)
        return consensus

    def form_consensus(self, opinions):
        # Implementing a simple majority consensus logic (can be expanded to more complex logic)
        opinion_count = {}
        for opinion in opinions:
            if opinion in opinion_count:
                opinion_count[opinion] += 1
            else:
                opinion_count[opinion] = 1
        
        # Return the most popular opinion (with majority consensus)
        return max(opinion_count, key=opinion_count.get)

class Expert:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def give_opinion(self, problem):
        # Provide an opinion based on expertise
        return f"As an expert in {self.expertise}, I believe the best approach is to handle: {problem}."
