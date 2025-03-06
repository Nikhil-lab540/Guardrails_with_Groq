from nemoguardrails import RailsConfig, LLMRails
import config.config  # Ensures custom LLM is registered

# Load the configuration
config = RailsConfig.from_path("./config")
rails = LLMRails(config)

def chatbot():
    print("Chatbot: Hello! How can I assist you with sales today?")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        # Check if the input passes guardrails
        guardrails_response = rails.generate(messages=[{"role": "user", "content": user_input}])

        # If the guardrails reject the query, use the defined rejection response
        if guardrails_response.get("blocked", False):
            print(f"Chatbot: {guardrails_response['content']}")
            continue

        # Generate response using NeMo Guardrails
        response = rails.generate(messages=[{"role": "user", "content": user_input}])
        print(f"Chatbot: {response['content']}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

