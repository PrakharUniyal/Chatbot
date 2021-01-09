import os
import dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'
DIALOGFLOW_PROJECT_ID = 'chatbot-agent-pbap'
DIALOGFLOW_LANGUAGE_CODE = 'en'

session_client = dialogflow.SessionsClient()

def detect_intent_from_text(text, session_id, language_code='en'):
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def get_reply(query, chat_id):
    response = detect_intent_from_text(query, chat_id)
    return response
