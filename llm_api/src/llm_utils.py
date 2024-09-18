# src/llm_utils.py
import requests

# Function to interact with the Granite LLM API
def generate_llm_response(prompt):
    try:
        data = {
            "messages": [
                {
                    "content": "You are a helpful assistant.",
                    "role": "system"
                },
                {
                    "content": prompt,
                    "role": "user"
                }
            ]
    }

        # Send a POST request to the local Granite LLM API
        response = requests.post(
            "http://localhost:53777/v1/chat/completions",  # Replace with the actual endpoint of your Granite LLM
            json=data  # Adjust the payload according to your LLM's API
        )
        
        # Raise an error if the request was unsuccessful
        response.raise_for_status()
        
        # Return the generated text (adjust the key as per the LLM's response format)
        return response.json().get("choices")
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        return f"Error communicating with Granite LLM: {e}"