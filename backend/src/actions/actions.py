from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionIntegrationInfo(Action):

    def name(self) -> Text:
        return "action_integration_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Пример ответа ассистента с информацией о проектировании микросервисов
        response = "Микросервисная архитектура - это стиль разработки программного обеспечения, при котором приложения состоят из небольших, независимых сервисов, которые взаимодействуют между собой."

        dispatcher.utter_message(text=response)

        return []
