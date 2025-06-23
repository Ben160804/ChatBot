
from groq import Groq
from config import GROQ_API_KEY


DEFAULT_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
DEFAULT_TEMPERATURE = 0.8


groq_client = Groq(api_key=GROQ_API_KEY)

def get_groq_response(user_input: str, system_prompt: str, model: str = DEFAULT_MODEL, temperature: float = DEFAULT_TEMPERATURE) -> str:
    """
    Send a chat completion request to Groq and return the assistant's reply.

    Parameters:
    - user_input: The user's message.
    - system_prompt: The system-level instruction for the assistant.
    - model:       The model to use (default from configuration).
    - temperature: Sampling temperature for creativity.

    Returns:
    - The assistant's response as a stripped string.
    """
   
    payload = [
        {"role": "system", "content": system_prompt.strip()},
        {"role": "user",   "content": user_input.strip()}
    ]

    try:
        response = groq_client.chat.completions.create(
            model=model,
            messages=payload,
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except Exception as err:
        return f"Sorry, I'm experiencing technical issues right now. ({err})"