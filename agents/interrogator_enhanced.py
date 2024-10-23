
import openai

class InterrogatorEnhanced:
    def analyze_context(self, task_description):
        prompt = f"Analyze the context for the following task: {task_description}, and provide a detailed analysis to aid decision-making."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
        context_analysis = response.choices[0].text.strip()
        return context_analysis

    def optimize_query_in_real_time(self, query_description):
        prompt = f"Optimize the following query based on real-time information: {query_description}."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=150)
        optimized_query = response.choices[0].text.strip()
        return optimized_query

    def formulate_strategic_questions(self, task_description):
        prompt = f"Formulate strategic questions for the following task: {task_description}, to gather the most relevant information."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
        strategic_questions = response.choices[0].text.strip()
        return strategic_questions
