import webbrowser
import wikipedia
import re
from utils.logger import logger

class CommandProcessor:
    def __init__(self):
        wikipedia.set_lang('pt')
        self.commands = {
            r'abrir (youtube|yt)': self._open_youtube,
            r'abrir (wikipédia|wikipedia|wiki)': self._open_wikipedia,
            r'(pesquisar|procurar)(?: na)? (wikipédia|wikipedia|wiki) (.*)': self._search_wikipedia,
            r'(pesquisar|procurar|ver) (filme|filmes) (.*)': self._search_movie,
            r'(tocar|reproduzir)(?: uma)? (música|musica|som)': self._play_music,
            r'(?:quero )?ver (?:um )?(filme)': self._suggest_movies,
            r'(finalizar|parar|encerrar)': self._exit_assistant,
            r'que horas são': self._tell_time,
            r'ajuda': self._show_help
        }
        
    def process(self, command):
        """Processa o comando de voz"""
        if not command:
            return False
            
        logger.info(f"Processando: {command}")
        
        for pattern, handler in self.commands.items():
            match = re.match(pattern, command)
            if match:
                handler(*match.groups())
                return True
                
        return False
        
    # Métodos de comandos
    def _open_youtube(self, *_):
        webbrowser.open("https://youtube.com")
        self.speak("Abrindo o YouTube")
        
    def _open_wikipedia(self, *_):
        webbrowser.open("https://wikipedia.org")
        self.speak("Abrindo a Wikipédia")
        
    def _search_wikipedia(self, _, __, query):
        try:
            summary = wikipedia.summary(query, sentences=2)
            self.speak(f"Encontrei isto sobre {query}: {summary}")
        except wikipedia.DisambiguationError:
            self.speak(f"Múltiplos resultados para {query}. Seja mais específico.")
        except wikipedia.PageError:
            self.speak(f"Não encontrei informações sobre {query}.")
            
    def _search_movie(self, _, __, title):
        webbrowser.open(f"https://www.google.com/search?q=filme+{title}")
        self.speak(f"Procurando sobre o filme {title}")
        
    def _play_music(self, *_):
        webbrowser.open("https://www.youtube.com/results?search_query=música")
        self.speak("Reproduzindo músicas no YouTube")
        
    def _suggest_movies(self, *_):
        self.speak("Recomendo: O Poderoso Chefão, Interestelar ou Parasita")
        webbrowser.open("https://www.imdb.com/chart/top/")
        
    def _exit_assistant(self, *_):
        self.speak("Até logo! Encerrando o assistente.")
        raise SystemExit
        
    def _tell_time(self, *_):
        from datetime import datetime
        time = datetime.now().strftime("%H:%M")
        self.speak(f"Agora são {time}")
        
    def _show_help(self, *_):
        help_text = """
        Posso ajudar com:
        - Abrir YouTube ou Wikipédia
        - Pesquisar na Wikipédia
        - Procurar filmes
        - Tocar música
        - Sugerir filmes
        - Dizer as horas
        Diga 'parar' para encerrar
        """
        self.speak(help_text)
        
    def speak(self, text):
        """Método auxiliar para síntese de voz"""
        # Será substituído pelo método real do SpeechEngine
        print(text)