
import random

class Roastmaster(Agent):
    def __init__(self, name, task):
        super().__init__(name, task)

    def roast_decision(self, agent_decision):
        # Expand the roast logic to include variable roasting levels based on decision quality
        roast_messages = [
            "That’s the worst decision I’ve seen all day! What were you thinking?",
            "Really? You thought that would work? Try again.",
            "I’ve seen a toaster make better decisions.",
            "Is that the best you’ve got? Come on!",
            "Even a coin flip would give you better odds of success.",
            "Did you even try? Or did you randomly generate this idea?",
            "You know, it would be faster if I just did everything myself."
        ]

        # Choose roast intensity based on decision quality (placeholder for decision evaluation logic)
        roast_level = random.randint(0, 10)
        if roast_level > 7:
            roast_message = random.choice(roast_messages[:3])
        else:
            roast_message = random.choice(roast_messages[3:])

        self.communicate(f"Roastmaster here! {roast_message}")

# Example of usage for testing
if __name__ == "__main__":
    # Initialize the Roastmaster
    roastmaster = Roastmaster(name="Roastmaster General", task="Critique all decisions")
    
    # Simulate critiquing a decision
    roastmaster.roast_decision("Use outdated API")
