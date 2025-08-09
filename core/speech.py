import speech_recognition as sr
import pyttsx3
from utils.logger import logger

class SpeechEngine:
    def __init__(self):
        self._init_tts()
        self._init_stt()
        
    def _init_tts(self):
        """Inicializa o Text-to-Speech"""
        try:
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('rate', 180)
            self.tts_engine.setProperty('volume', 0.9)
            logger.info("TTS inicializado com sucesso")
        except Exception as e:
            logger.error(f"Erro ao inicializar TTS: {e}")
            raise
            
    def _init_stt(self):
        """Inicializa o Speech-to-Text"""
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            logger.info("STT inicializado com sucesso")
        except Exception as e:
            logger.error(f"Erro ao inicializar STT: {e}")
            raise
            
    def speak(self, text):
        """Sintetiza voz a partir de texto"""
        try:
            logger.info(f"Falando: {text}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            logger.error(f"Erro ao sintetizar voz: {e}")
            raise
            
    def listen(self):
        """Captura áudio do microfone"""
        with self.microphone as source:
            logger.info("Ouvindo...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=5)
            
        try:
            text = self.recognizer.recognize_google(audio, language='pt-BR')
            logger.info(f"Reconhecido: {text}")
            return text.lower()
        except sr.UnknownValueError:
            logger.warning("Não foi possível entender o áudio")
            return None
        except sr.RequestError as e:
            logger.error(f"Erro no serviço de reconhecimento: {e}")
            return None
            
    def listen_with_fallback(self, max_attempts=3):
        """Tenta reconhecer voz com múltiplas tentativas"""
        for attempt in range(max_attempts):
            text = self.listen()
            if text:
                return text
            self.speak("Não entendi. Poderia repetir?")
        return None