# 🗣️ Assistente Virtual com PLN - Projeto Didático

## 🎯 Objetivo do Projeto
Este projeto tem como objetivo demonstrar na prática a aplicação de Processamento de Linguagem Natural (PLN) e técnicas de desenvolvimento de assistentes virtuais, utilizando:

- **Reconhecimento de Voz (STT)**
- **Síntese de Voz (TTS)**
- **Processamento de Comandos por Voz**
- **Integração com APIs e Serviços Web**

Serve como material didático para aprendizado de Python aplicado a sistemas de voz e assistentes virtuais.

## 🛠️ Ferramentas e Tecnologias Utilizadas

| Tecnologia | Finalidade | Biblioteca/Pacote |
|------------|------------|-------------------|
| **Reconhecimento de Voz** | Converter fala em texto | `SpeechRecognition`, `PyAudio` |
| **Síntese de Voz** | Converter texto em fala | `pyttsx3` |
| **Processamento de Comandos** | Interpretar intenções do usuário | Expressões regulares nativas |
| **Integração Web** | Acessar serviços online | `webbrowser`, `wikipedia-api` |
| **Gerenciamento de Projeto** | Organização e logs | `logging` nativo |

## 📌 Visão Geral
Assistente virtual com reconhecimento de voz em português que pode abrir sites, pesquisar na Wikipedia, sugerir filmes, tocar músicas e mais.

## 🛠️ Funcionalidades Principais
- **Reconhecimento de voz** em português (STT)
- **Síntese de voz** (TTS) com respostas faladas
- **Comandos por voz** para diversas ações
- **Sistema de logs** para monitoramento

## 📋 Comandos Disponíveis

### 🎬 Entretenimento
| Comando | Ação |
|---------|------|
| "Abrir YouTube" | Abre o YouTube no navegador |
| "Tocar uma música" | Reproduz música no YouTube |
| "Ver um filme" | Sugere filmes populares |
| "Pesquisar filme [nome]" | Busca informações sobre um filme |

### 🔍 Pesquisas
| Comando | Ação |
|---------|------|
| "Abrir Wikipédia" | Abre a Wikipedia |
| "Pesquisar na Wikipedia [termo]" | Faz pesquisa na Wikipedia |

### ⏰ Utilidades
| Comando | Ação |
|---------|------|
| "Que horas são" | Informa a hora atual |
| "Ajuda" | Mostra todos os comandos disponíveis |
| "Parar" | Encerra o assistente |

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- Microfone funcionando

### Instalação
bash
~~~
# Clone o repositório
git clone [URL_DO_REPOSITORIO]

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Instale as dependências
pip install -r requirements.txt

# Execução
python main.py
~~~
# 🛠️ Estrutura do Projeto
/projeto_assistente/  
├── core/               # Módulos principais  
│   ├── speech.py       # Reconhecimento e síntese de voz  
│   └── commands.py     # Processamento de comandos  
├── utils/              # Utilitários  
│   └── logger.py       # Sistema de logs  
├── main.py             # Ponto de entrada  
└── requirements.txt    # Dependências  

# 🔄 Fluxo de Trabalho
- O assistente inicia com mensagem de boas-vindas
- Aguarda comando por voz
- Processa o comando e executa a ação
- Fornece feedback verbal
- Volta a aguardar novos comandos

# 📈 Próximas Melhorias
- Adicionar previsão do tempo
- Integrar com serviços de streaming
- Implementar lembretes por voz
- Adicionar controle por gestos

# 🤝 Contribuição
Contribuições são bem-vindas! Siga os passos:
1. Faça um fork do projeto
2. Crie sua branch (git checkout -b feature/nova-funcionalidade)
3. Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade')
4. Push para a branch (git push origin feature/nova-funcionalidade)
5. Abra um Pull Request

# 📜 Licença
MIT License - veja o arquivo LICENSE.md para detalhes
