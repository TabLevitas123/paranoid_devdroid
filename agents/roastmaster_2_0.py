
import openai

class Roastmaster2_0:
    def personality_driven_response(self, user_input):
        prompt = f"Respond to the following input with a witty, sarcastic, and humorous tone: {user_input}."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=150)
        personality_response = response.choices[0].text.strip()
        return personality_response

    def adjust_tone_dynamically(self, user_input, user_mood):
        prompt = f"Based on the user's mood: {user_mood}, respond to the following input with the appropriate tone: {user_input}."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=150)
        adjusted_tone_response = response.choices[0].text.strip()
        return adjusted_tone_response

    def generate_humor(self, user_input):
        prompt = f"Generate a humorous response to the following input: {user_input}."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=100)
        humor_response = response.choices[0].text.strip()
        return humor_response

    def analyze_sentiment(self, user_input):
        prompt = f"Analyze the sentiment of this input: {user_input}, and return whether the tone is positive, neutral, or negative."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=50)
        sentiment_analysis = response.choices[0].text.strip()
        return sentiment_analysis

    def interactive_game_mode(self, user_input):
        prompt = f"Engage the user in a witty roast battle based on this input: {user_input}. Respond with playful insults."
        response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=150)
        game_response = response.choices[0].text.strip()
        return game_response
