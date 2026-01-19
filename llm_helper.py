from openai import OpenAI
import os
from openai import RateLimitError

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(question, chat_history):
    """
    Uses OpenAI as a fallback for general questions.
    Handles quota errors gracefully.
    """
    try:
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant."}
        ]

        # Add recent context
        for msg in chat_history[-5:]:
            messages.append({"role": "user", "content": msg["user"]})
            messages.append({"role": "assistant", "content": msg["agent"]})

        messages.append({"role": "user", "content": question})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.5
        )

        return response.choices[0].message.content.strip()

    except RateLimitError:
        return (
            "LLM service is currently unavailable due to API quota limits. "
            "However, the integration is implemented and can be enabled "
            "by providing a valid API key with available credits."
        )

    except Exception:
        return "LLM service is temporarily unavailable."
