import logging

from rasa_sdk import Action

logger = logging.getLogger(__name__)

class CustomAction(Action):
    def name(self):
        return "custom_action"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get('text')
        if user_message:
            logger.info(f"User message: {user_message}")

        response_text = "Это мой ответ."
        dispatcher.utter_message(text=response_text)
        logger.info(f"Bot response: {response_text}")

        return []
