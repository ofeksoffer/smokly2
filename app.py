from langchain.chains import load_chain
from langchain.prompts import PromptTemplate
import json

# Load the exported flow configuration
with open("Simple Agent.json", "r") as f:
    flow_config = json.load(f)

# Load the LangChain flow
chain = load_chain(flow_config)

# Run the chatbot locally
def chatbot(message):
    response = chain.run(message)
    return response

# Example interaction
if __name__ == "__main__":
    user_message = input("You: ")
    bot_response = chatbot(user_message)
    print(f"Bot: {bot_response}")
