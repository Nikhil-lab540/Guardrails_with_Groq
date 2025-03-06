from groq import Groq
from nemoguardrails import register_action

# Initialize Groq client
client = Groq(api_key="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")  # Replace with your actual API key

@register_action()
def call_groq_llm(prompt: str) -> str:
    """Custom function to call Groq's LLaMA-3.3-70B API"""
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error calling Groq LLM: {str(e)}"
