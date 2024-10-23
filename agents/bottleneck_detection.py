
import openai

class BottleneckDetection:
    def detect_bottlenecks(self, agent_list):
        agent_info = "\n".join([f"Agent {agent['id']}: Task load - {agent['task_load']}, Progress - {agent['progress']}%" for agent in agent_list])
        prompt = f"Monitor the following agents and predict potential bottlenecks based on their task load and progress:\n{agent_info}"
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
        bottleneck_prediction = response.choices[0].text.strip()
        return bottleneck_prediction
