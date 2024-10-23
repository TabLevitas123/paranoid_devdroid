
class HallucinationDetection:
    def __init__(self):
        self.suspicious_outputs = []

    def monitor_output(self, agent_id, output):
        # Simple heuristic: if the output is gibberish or too repetitive, it's flagged
        if len(output.split()) < 2 or output.count(output.split()[0]) > 5:
            self.suspicious_outputs.append({"agent_id": agent_id, "output": output})
            return f"Agent {agent_id} output flagged for potential hallucination."
        return f"Agent {agent_id} output seems normal."

    def get_flagged_outputs(self):
        return self.suspicious_outputs

# Example Usage
if __name__ == "__main__":
    detector = HallucinationDetection()
    result = detector.monitor_output(1, "This is a normal sentence.")
    print(result)
    result = detector.monitor_output(2, "Gibberish gibberish gibberish gibberish gibberish")
    print(result)
    print(detector.get_flagged_outputs())
