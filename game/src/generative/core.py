import os

import google.generativeai as genai
from game.src.MoeLogger import MoeLogger
from colorama import Fore, Style

class GenerativeAi:
    def __init__(self, ml,  api_key, model="gemini-1.5-flash", core_memory=""):
        self.api_key = api_key
        self.model = model
        self.history = []
        self.core_memory = core_memory
        self.ml = ml
        try:
            ml.message("Loading Core....")
            if not api_key or api_key == "":
                ml.error("Failed To Load API Key")
                return
            genai.configure(api_key=api_key)
            self.ai_init = genai.GenerativeModel(model,system_instruction=core_memory)
            self.ai = self.ai_init.start_chat(history=self.history)
            ml.message("Core is Ready!...")
        except Exception as e:
            ml.error("Failed To Load the Core")
            ml.error(e)

    def generate_response(self, message):
        # Send the message and get the response
        message_response = self.ai.send_message(message)
        # Assuming message_response is a GenerateContentResponse object
        text = message_response._result.candidates[0].content.parts[0].text
        return text

    def reboot(self, message):
        self.ai.history = message

    def get_chat_history(self):
        return self.ai.history