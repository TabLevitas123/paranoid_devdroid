
class ExpertPanel:
    def __init__(self):
        self.experts = {}

    def add_expert(self, expert_name, expertise):
        self.experts[expert_name] = expertise

    def deliberate(self, question):
        responses = {}
        for expert, expertise in self.experts.items():
            responses[expert] = f"Expert in {expertise} suggests '{question}' should be approached this way."
        return responses

# Example Usage
if __name__ == "__main__":
    panel = ExpertPanel()
    panel.add_expert("Dr. Smith", "AI Ethics")
    panel.add_expert("Prof. Johnson", "Neural Networks")
    deliberation = panel.deliberate("How should we design AI systems?")
    print(deliberation)
