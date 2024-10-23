
class Roastmaster(Agent):
    def __init__(self, name, task):
        super().__init__(name, task)

    def roast_decision(self, agent_decision):
        # This method will 'roast' the decision by critiquing it with random harsh feedback
        roast_messages = [
            "That's the worst decision I've seen all day! What were you thinking?",
            "Really? You thought that would work? Try again.",
            "I've seen a toaster make better decisions.",
            "Is that the best you've got? Come on!",
            "Even a coin flip would give you better odds of success."
        ]
        roast_message = random.choice(roast_messages)
        self.communicate(f"Roastmaster here! {roast_message}")

# Example of usage
if __name__ == "__main__":
    # Initialize the Roastmaster
    roastmaster = Roastmaster(name="Roastmaster General", task="Critique all decisions")
    
    # Simulate critiquing a decision
    roastmaster.roast_decision("Use outdated API")
