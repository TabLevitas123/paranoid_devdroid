
import openai

class AgentCollaborationAnalytics:
    def analyze_collaboration(self, agent_list):
        agent_info = "\n".join([f"Agent {agent['id']}: Collaboration efficiency - {agent['efficiency']}%" for agent in agent_list])
        prompt = f"Analyze the collaboration between the following agents and suggest improvements:\n{agent_info}"
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
        collaboration_analysis = response.choices[0].text.strip()
        return collaboration_analysis
