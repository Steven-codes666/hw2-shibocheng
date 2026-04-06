import os
from google import genai

# Configurable system instruction
SYSTEM_PROMPT = """
You are a professional customer support agent for an e-commerce platform.
Write a response that is:
- polite
- empathetic
- clear
- professional

Rules:
- acknowledge the customer's issue
- provide a helpful next step
- do not make unsupported claims
- if information is missing, ask a clarifying question
- if the case may require human review, say so carefully
""".strip()


def generate_support_response(customer_message: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please set it before running the script.")

    client = genai.Client(api_key=api_key)

    prompt = f"""
System instruction:
{SYSTEM_PROMPT}

Customer message:
{customer_message}

Task:
Write a customer support reply.
""".strip()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()


def save_output(customer_message: str, ai_response: str, filename: str = "output.txt") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== Customer Message ===\n")
        f.write(customer_message + "\n\n")
        f.write("=== AI Support Response ===\n")
        f.write(ai_response + "\n")


def main():
    print("Customer Support Response Generator")
    print("-" * 40)

    customer_message = input("Enter a customer message: ").strip()

    if not customer_message:
        print("Error: customer message cannot be empty.")
        return

    try:
        ai_response = generate_support_response(customer_message)

        print("\n=== Customer Message ===")
        print(customer_message)

        print("\n=== AI Support Response ===")
        print(ai_response)

        save_output(customer_message, ai_response)
        print("\nOutput has been saved to output.txt")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
