
from agent_base import Agent, HallucinationMonitor
from roastmaster import Roastmaster
from verification_agent import VerificationAgent
from expert_panel import ExpertPanel, Expert
from communication_protocol import CommunicationProtocol

class Marvin(Agent):
    def __init__(self, name, task, efficiency_level=3):
        super().__init__(name, task)
        self.efficiency_level = efficiency_level
        self.communication_protocol = CommunicationProtocol()

        # Create agents (depending on efficiency level, create more agents)
        self.hallucination_monitor = HallucinationMonitor(name="Hallucination Monitor", task="Monitor for hallucinations")
        self.roastmaster = Roastmaster(name="Roastmaster", task="Roast decisions")
        self.verification_agent = VerificationAgent(name="Fact Checker", task="Verify decisions")
        
        # Expert Panel
        expert1 = Expert(name="Dr. Ada Lovelace", expertise="Mathematics and Computing")
        expert2 = Expert(name="Nikola Tesla", expertise="Electricity and Engineering")
        self.expert_panel = ExpertPanel(name="Expert Panel", task="Solve complex problems", experts=[expert1, expert2])
        
    def decide(self, task):
        # Use all agents to deliberate and make a decision
        
        # Start by monitoring for hallucinations
        hallucination_flag = self.hallucination_monitor.detect_hallucination(task)
        if hallucination_flag:
            self.communication_protocol.send_message(self.hallucination_monitor.name, self.name, "Hallucination detected. Adjust task.")
            return "Task rejected due to hallucination."
        
        # Roast the task for fun
        self.roastmaster.roast_decision(task)
        self.communication_protocol.send_message(self.roastmaster.name, self.name, "Roasted the decision.")
        
        # Verify the task decision
        is_verified = self.verification_agent.verify_decision(task)
        if not is_verified:
            self.communication_protocol.send_message(self.verification_agent.name, self.name, "Task verification failed.")
            return "Task rejected due to failed verification."
        
        # If complex, pass it to the expert panel
        decision = self.expert_panel.deliberate(task)
        self.communication_protocol.send_message(self.expert_panel.name, self.name, f"Expert Panel decision: {decision}")
        
        return f"Final decision: {decision}"

# Example usage
if __name__ == "__main__":
    marvin = Marvin(name="Marvin", task="Orchestrate Agent Swarm")
    
    # Simulate a task
    user_task = "Optimize AI model for better performance"
    final_decision = marvin.decide(user_task)
    
    print(final_decision)
    marvin.communication_protocol.display_message_log()
