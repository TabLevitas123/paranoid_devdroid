
import openai

class Roastmaster2_1:
    def detect_flaws_in_reasoning(self, agent_plan):
        prompt = f"Analyze the following agent's plan for logical flaws or inconsistencies: {agent_plan}."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
        flaw_detection = response.choices[0].text.strip()
        return flaw_detection

    def provide_cognitive_critique(self, agent_reasoning):
        prompt = f"Provide a critique of the following agent's reasoning, highlighting areas for improvement: {agent_reasoning}."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
        cognitive_critique = response.choices[0].text.strip()
        return cognitive_critique

    def predict_task_outcome(self, agent_plan):
        prompt = f"Based on the agent's plan, predict the task outcome and identify potential risks or failures: {agent_plan}."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=150)
        outcome_prediction = response.choices[0].text.strip()
        return outcome_prediction

    def provide_humorous_error_commentary(self, agent_reasoning):
        prompt = f"Provide humorous commentary on the following agent's reasoning flaws: {agent_reasoning}."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=150)
        humor_critique = response.choices[0].text.strip()
        return humor_critique

    def real_time_critique_feedback(self, agent_action):
        prompt = f"Provide real-time critique and suggestions for the following agent action: {agent_action}."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=150)
        real_time_feedback = response.choices[0].text.strip()
        return real_time_feedback
