import os
from dotenv import load_dotenv
from google import genai

# ----------------------------------------
# Load API Key
# ----------------------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found.")
    exit()

client = genai.Client(api_key=api_key)

# ----------------------------------------
# Function to send prompt to Gemini
# ----------------------------------------
def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Error: {e}"


# ----------------------------------------
# Main Program
# ----------------------------------------
while True:

    print("\n")
    print("=" * 55)
    print("      BASIC LLM APPLICATION")
    print("=" * 55)

    print("1. Question Answering")
    print("2. Text Summarization")
    print("3. Translation")
    print("4. Exit")

    print("-" * 55)

    choice = input("Choose an option (1-4): ")

    # ------------------------------------
    # Question Answering
    # ------------------------------------
    if choice == "1":

        question = input("\nEnter your question:\n> ")

        prompt = f"""
You are an expert AI assistant.

Answer the following question clearly and accurately.

Question:
{question}
"""

        answer = ask_gemini(prompt)

        print("\nGenerated Answer")
        print("-" * 55)
        print(answer)

    # ------------------------------------
    # Summarization
    # ------------------------------------
    elif choice == "2":

        text = input("\nPaste the paragraph to summarize:\n> ")

        prompt = f"""
Summarize the following text in 5 concise bullet points.

Text:
{text}
"""

        answer = ask_gemini(prompt)

        print("\nSummary")
        print("-" * 55)
        print(answer)

    # ------------------------------------
    # Translation
    # ------------------------------------
    elif choice == "3":

        language = input("\nTranslate to which language? ")

        text = input("\nEnter text:\n> ")

        prompt = f"""
Translate the following text into {language}.

Text:
{text}

Only provide the translated text.
"""

        answer = ask_gemini(prompt)

        print("\nTranslated Text")
        print("-" * 55)
        print(answer)

    # ------------------------------------
    # Exit
    # ------------------------------------
    elif choice == "4":

        print("\nThank you for using the Basic LLM Application.")
        break

    else:
        print("\nInvalid choice! Please enter 1-4.")

    input("\nPress Enter to continue...")