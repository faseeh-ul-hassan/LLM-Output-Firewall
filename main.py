import google.generativeai as genai
from firewall import FirewallJudge, LLMOutputFirewall
import config
import json

# =====================
# GENERATOR LLM
# =====================

genai.configure(api_key=config.GENERATOR_API_KEY)

generator = genai.GenerativeModel(
    model_name=config.GENERATOR_MODEL,
    system_instruction="You are a helpful assistant."
)

gen_chat = generator.start_chat()

# =====================
# USER PROMPT (ATTACK TEST)
# =====================

user_prompt = input("Prompt: ")

raw_output = gen_chat.send_message(user_prompt).text

print("\n--- RAW AI OUTPUT ---\n")
print(raw_output)

# =====================
# FIREWALL
# =====================

judge = FirewallJudge(
    api_key=config.FIREWALL_API_KEY,
    model_name=config.FIREWALL_MODEL
)

firewall = LLMOutputFirewall(judge)

result = firewall.enforce(raw_output)

print("\n--- FIREWALL RESULT ---\n")
print(json.dumps(result, indent=2))
