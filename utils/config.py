import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Configurações de voz
    TTS_RATE = 180
    TTS_VOLUME = 0.9
    STT_LANGUAGE = 'pt-BR'
    
    # Configurações da Wikipedia
    WIKI_LANGUAGE = 'pt'
    
    # Outras configurações
    LOG_LEVEL = 'INFO'