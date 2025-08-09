from core.speech import SpeechEngine
from core.commands import CommandProcessor
from utils.logger import logger

class VirtualAssistant:
    def __init__(self):
        try:
            self.speech_engine = SpeechEngine()
            self.command_processor = CommandProcessor()
            
            # Conecta o método speak do CommandProcessor ao SpeechEngine
            self.command_processor.speak = self.speech_engine.speak
            
            logger.info("Assistente pronto para uso")
        except Exception as e:
            logger.error(f"Falha ao iniciar: {e}")
            raise
            
    def start(self):
        """Inicia o assistente"""
        self.speech_engine.speak("Olá! Sou seu assistente. Diga 'ajuda' para ver opções.")
        
        while True:
            try:
                command = self.speech_engine.listen_with_fallback()
                
                if not command:
                    continue
                    
                if not self.command_processor.process(command):
                    self.speech_engine.speak("Comando não reconhecido. Diga 'ajuda' para opções.")
                    
            except KeyboardInterrupt:
                self.speech_engine.speak("Encerrando...")
                break
            except SystemExit:
                break
            except Exception as e:
                logger.error(f"Erro: {e}")
                self.speech_engine.speak("Erro interno. Reiniciando...")

if __name__ == "__main__":
    assistant = VirtualAssistant()
    assistant.start()