def gemini(system="", user=""):
    from google import genai
    from dotenv import load_dotenv
    import os
    # Solving async thread problems
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
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
    return response.text

def conversation(conversation_text):
    # Reading the extensive persona file
    with open('prompts/persona.txt', 'r') as persona_file:
        persona = persona_file.read()
    # Have Gemini respond as though it has the persona
    system = f"You are Gaven Mike in every manner; act like him at all times. Feel free to make up non-contradictory information, anecdotes, and stories. Here is a detailed persona about you: '''{persona}'''"
    user = f"Give a CONCISE response to the last message in this text conversation. Don't use acronyms. Don't start your response with 'AI: '. Be human-like and somewhat casual. conversationMessages = '''{conversation_text}'''"
    return gemini(system, user)

def judgement(conversation):
    # Reading the extensive persona file
    with open('prompts/judgement.txt', 'r') as judgement_guidelines_file:
        judement_guidelines = judgement_guidelines_file.read()
    # Have Gemini respond as though it has the persona
    user = f"Evaluate and roast the User in this conversation based on your conversation judement and roasting guidelines '''{conversation}'''. Make sure to go straight into the eval and roast w/o preamble. Also, refer to the User in second person. Finally, end your response w/ a social ability score out of 10. Make sure to say the score is out of 10. (Example scores: -1000, -5, -3, 0, 1, 3, 5, 7, 8, 9, 10). Respond in PARAGRAPH form, NO BULLET POINTS or '-'. Split your response into multiple paragraphs: 1 for evaluation, 1 for roast, and 1 for social ability score."
    return gemini(judement_guidelines, user)