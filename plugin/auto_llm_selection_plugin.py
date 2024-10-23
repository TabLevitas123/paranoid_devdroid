
import openai
import requests

class AutoLLMSelectionPlugin:
    def __init__(self, openai_api_key=None, anthropic_api_key=None, huggingface_api_key=None):
        self.api_keys = {
            "OpenAI": openai_api_key,
            "Anthropic": anthropic_api_key,
            "HuggingFace": huggingface_api_key
        }
        openai.api_key = openai_api_key if openai_api_key else None
        self.local_models = self.get_local_models()

    def get_local_models(self):
        """
        Retrieve a list of locally installed models, if available.
        """
        # Assuming local models like GPT-2 or smaller versions of Hugging Face models
        return ["gpt2", "distilgpt2", "bert-base-uncased"]

    def list_available_models(self):
        """
        Return a list of available models (API-based or local).
        """
        models = {
            "OpenAI": ["gpt-4", "gpt-3.5-turbo", "davinci"] if self.api_keys["OpenAI"] else [],
            "Anthropic": ["claude-1", "claude-2"] if self.api_keys["Anthropic"] else [],
            "HuggingFace": self.get_top_huggingface_models() if self.api_keys["HuggingFace"] else [],
            "Local": self.local_models
        }
        return models

    def get_top_huggingface_models(self):
        """
        Retrieve top 20 models from Hugging Face's model hub.
        """
        headers = {"Authorization": f"Bearer {self.api_keys['HuggingFace']}"}
        response = requests.get("https://huggingface.co/api/models", headers=headers, params={"sort": "downloads", "limit": 20})
        if response.status_code == 200:
            models = [model["id"] for model in response.json()]
            return models
        else:
            return ["Failed to retrieve models from Hugging Face"]

    def analyze_task(self, task_description):
        """
        Analyze the task description and categorize it based on the task's needs (e.g., reasoning, text generation).
        """
        if "reasoning" in task_description.lower() or "complex" in task_description.lower():
            return "complex_reasoning"
        elif "summarize" in task_description.lower() or "paraphrase" in task_description.lower():
            return "summarization"
        elif "generate code" in task_description.lower() or "write a script" in task_description.lower():
            return "code_generation"
        else:
            return "general_text_generation"

    def select_best_model(self, task_description):
        """
        Automatically select the best model based on the task analysis and available models.
        """
        task_type = self.analyze_task(task_description)
        available_models = self.list_available_models()

        if task_type == "complex_reasoning" and "OpenAI" in available_models:
            return "OpenAI", "gpt-4"  # Prioritize GPT-4 for complex reasoning
        elif task_type == "code_generation" and "OpenAI" in available_models:
            return "OpenAI", "davinci-codex"  # Use OpenAI Codex for code generation
        elif task_type == "summarization" and "HuggingFace" in available_models:
            return "HuggingFace", available_models["HuggingFace"][0]  # Use top Hugging Face model for summarization
        elif task_type == "general_text_generation" and "Local" in available_models:
            return "Local", available_models["Local"][0]  # Use local models for general text generation if no cloud API available
        else:
            return "No suitable model found", None

    def interact_with_model(self, task_description):
        """
        Execute the task with the best selected model.
        """
        provider, model_name = self.select_best_model(task_description)
        if model_name is None:
            return f"No suitable model found for task: {task_description}"
        
        if provider == "OpenAI":
            return self.openai_interaction(model_name, task_description)
        elif provider == "HuggingFace":
            return self.huggingface_interaction(model_name, task_description)
        elif provider == "Local":
            return f"Using local model: {model_name} for task: {task_description} (Local model interaction not implemented)"
        else:
            return f"Provider {provider} is not supported for interaction."

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

    def huggingface_interaction(self, model_name, prompt):
        """
        Interact with a Hugging Face model.
        """
        headers = {"Authorization": f"Bearer {self.api_keys['HuggingFace']}"}
        data = {"inputs": prompt}
        response = requests.post(f"https://api-inference.huggingface.co/models/{model_name}", headers=headers, json=data)
        if response.status_code == 200:
            return response.json()[0]["generated_text"]
        else:
            return f"Hugging Face model interaction failed: {response.status_code}"
