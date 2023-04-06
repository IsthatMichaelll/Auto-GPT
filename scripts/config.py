import os
import openai
from dotenv import load_dotenv
import langchain
# Load environment variables from .env file
load_dotenv()

class Singleton(type):
    """
    Singleton metaclass for ensuring only one instance of a class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """

    def __init__(self):
        self.continuous_mode = False
        self.speak_mode = False
        # TODO - make these models be self-contained, using langchain, so we can configure them once and call it good 
config = langchain.Config()

config.add_param("fast_llm_model", "gpt-3.5-turbo")
config.add_param("smart_llm_model", "gpt-4")
config.add_param("fast_token_limit", 4000)
config.add_param("smart_token_limit", 8000)
config.add_param("openai_api_key")
config.add_param("elevenlabs_api_key")
config.add_param("google_api_key")
config.add_param("custom_search_engine_id")

# Initialize the OpenAI API client
openai.api_key = config.openai_api_key

config.set_env()

class selfcon:
    def __init__(self):
        self.fast_llm_model = config.fast_llm_model 
        self.smart_llm_model = config.smart_llm_model
        self.fast_token_limit = config.fast_token_limit
        self.smart_token_limit = config.smart_token_limit
        self.openai_api_key = config.openai_api_key
        self.elevenlabs_api_key = config.elevenlabs_api_key
        self.google_api_key = config.google_api_key
        self.custom_search_engine_id = config.custom_search_engine_id
        self.continuous_mode = False
        self.speak_mode = False
        
#Should be self-containted and config once and done
        
    def set_continuous_mode(self, value: bool):
        self.continuous_mode = value

    def set_speak_mode(self, value: bool):
        self.speak_mode = value

    def set_fast_llm_model(self, value: str):
        self.fast_llm_model = value

    def set_smart_llm_model(self, value: str):
        self.smart_llm_model = value

    def set_fast_token_limit(self, value: int):
        self.fast_token_limit = value

    def set_smart_token_limit(self, value: int):
        self.smart_token_limit = value

    def set_openai_api_key(self, value: str):
        self.openai_api_key = value
    
    def set_elevenlabs_api_key(self, value: str):
        self.elevenlabs_api_key = value
        
    def set_google_api_key(self, value: str):
        self.google_api_key = value
    
    def set_custom_search_engine_id(self, value: str):
        self.custom_search_engine_id = value