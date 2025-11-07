"""
Reusable OpenAI chat client wrapper.
Reads OPENAI_API_KEy from environment (do NOT hard-code). 
"""



from openai import OpenAI

class OpenAIChatClient:
    def __init__(self, model: str = "gpt-4o-mini"):
        # auto-reads OPENAI_API_KEY form environment
        self._client = OpenAI()
        self._model = model
        
    def complete(self, prompt: str, max_tokens:int | None = 200):
        """_summary_
        
        send a user prompt to chat completions and return text.
        Raises RuntimeError on failure.

        Args:
            prompt (str): _description_
            max_tokens (int | None, optional): _description_. Defaults to 200.
        """
        try:
            resp = self._client.chat.completions.create(
                model = self._model,
                messages = [{"role": "user", "content": prompt}],
                max_tokens = max_tokens or 200, 
            )
            
            
            choices = getattr(resp, "choices", None)
            
            if not choices:
                raise RuntimeError("OpenAI response had no choices.")
            
            # Reading the response text
            text = choices[0].message.content
            
            if not text:
                raise RuntimeError("OpenAI response content was empty.")
            # we have the response and we are returning this.
            return text
        
        # 
        except Exception as ex:
            raise RuntimeError(
                "Failed to get response from OpenAI."
                "Check OPENAI_API_KEY, network, and model access"
            ) from ex
    