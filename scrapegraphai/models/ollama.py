"""
Ollama Module
"""
from langchain_community.chat_models import ChatOllama


class Ollama(ChatOllama):
    """
    A wrapper for the ChatOllama class that provides default configuration
    and could be extended with additional methods if needed.

    Args:
        llm_config (dict): Configuration parameters for the language model.
    """

    def __init__(self, llm_config: dict):
        # Ensure the model name is set to 'orca-mini', which is a valid model from the Ollama library
        llm_config['model'] = 'orca-mini'
        super().__init__(**llm_config)
