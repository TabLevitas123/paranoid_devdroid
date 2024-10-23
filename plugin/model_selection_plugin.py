
import openai
import requests

class ModelSelectionPlugin:
    def __init__(self, openai_api_key, anthropic_api_key, huggingface_api_key):
        self.openai_api_key = openai_api_key
        self.anthropic_api_key = anthropic_api_key
        self.huggingface_api_key = huggingface_api_key
        openai.api_key = openai_api_key
    
    def list_available_models(self):
        """
        Return a list of available models from OpenAI, Anthropic, Meta, and Hugging Face.
        """
        models = {
            "OpenAI": ["gpt-4", "gpt-3.5-turbo", "davinci", "curie", "babbage", "ada"],
            "Anthropic": ["claude-1", "claude-2", "claude-instant"],
            "Meta": ["OPT-175B", "OPT-30B", "OPT-6.7B", "LLAMA-2-70B", "LLAMA-2-13B"],
            "HuggingFace": self.get_top_huggingface_models()
        }
        return models

    def get_top_huggingface_models(self):
        """
        Retrieve top 20 models from Hugging Face's model hub.
        """
        headers = {"Authorization": f"Bearer {self.huggingface_api_key}"}
        response = requests.get("https://huggingface.co/api/models", headers=headers, params={"sort": "downloads", "limit": 20})
        if response.status_code == 200:
            models = [model["id"] for model in response.json()]
            return models
        else:
            return ["Failed to retrieve models from Hugging Face"]

    def interact_with_model(self, provider, model_name, prompt):
        """
        Interact with a specific model from the selected provider (OpenAI, Anthropic, Meta, or Hugging Face).
        """
        if provider == "OpenAI":
            return self.openai_interaction(model_name, prompt)
        elif provider == "Anthropic":
            return self.anthropic_interaction(model_name, prompt)
        elif provider == "Meta":
            return self.meta_interaction(model_name, prompt)
        elif provider == "HuggingFace":
            return self.huggingface_interaction(model_name, prompt)
        else:
            return "Provider not supported."

    def openai_interaction(self, model_name, prompt):
        """
        Interact with an OpenAI model.
        """
        try:
            response = openai.Completion.create(
                engine=model_name,
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"OpenAI model interaction failed: {e}"

    def anthropic_interaction(self, model_name, prompt):
        """
        Interact with an Anthropic model (using a hypothetical API structure).
        """
        headers = {"Authorization": f"Bearer {self.anthropic_api_key}"}
        data = {"model": model_name, "prompt": prompt}
        response = requests.post(f"https://api.anthropic.com/v1/completions", headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["completion"]
        else:
            return f"Anthropic model interaction failed: {response.status_code}"

    def meta_interaction(self, model_name, prompt):
        """
        Interact with a Meta model (assuming direct interaction).
        """
        return f"Meta model interaction with {model_name} is not yet supported via a public API."

    def huggingface_interaction(self, model_name, prompt):
        """
        Interact with a Hugging Face model.
        """
        headers = {"Authorization": f"Bearer {self.huggingface_api_key}"}
        data = {"inputs": prompt}
        response = requests.post(f"https://api-inference.huggingface.co/models/{model_name}", headers=headers, json=data)
        if response.status_code == 200:
            return response.json()[0]["generated_text"]
        else:
            return f"Hugging Face model interaction failed: {response.status_code}"
