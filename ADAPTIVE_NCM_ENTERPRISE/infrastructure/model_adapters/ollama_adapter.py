class OllamaAdapter:
    def __init__(self, model_name: str = "llama3"):
        self.model_name = model_name

    async def generate(self, prompt: str) -> str:
        return f"[Ollama Output for {self.model_name}]: Synthesized response for '{prompt[:30]}...'"
