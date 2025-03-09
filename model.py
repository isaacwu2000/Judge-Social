def gemini(system="", user=""):
    from google import genai
    from dotenv import load_dotenv
    import os

    # Accessing the API Key in .env
    load_dotenv()
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    # Initialize the client with your API key
    client = genai.Client(api_key=GEMINI_API_KEY)

    # Generate content using the Gemini model
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"System: {system}, User: {user}",
    )

    # Returning the generated text
    print(response.text)
    return response.text

def conversation(conversation_text):
    # Reading the extensive persona file
    with open('persona.txt', 'r') as persona_file:
        persona = persona_file.read()

    # Have Gemini respond as though it has the persona
    system = f"You are Gaven Mike in every manner; act like him at all times. Feel free to make up non-contradictory information, anecdotes, and stories. Here is a detailed persona about you: '''{persona}'''"
    user = f"Give a response to the last message in this text conversation. conversationMessages = '''{conversation_text}'''"
    return gemini(system, user)

async def judgement():
    pass

gemini(system="Hello", user="How are you?")