
---

### **PROJETO:** CONVERSATIONAL AI ASSISTANT

<br>

<div align="center">
<h1 align="center">🤖 Conversational AI Assistant 🤖</h1>
<p align="center">
Um assistente de IA conversacional modular que integra o poder do GPT-2 com ferramentas de análise de texto e saída de voz.
<br /><br />
<a href="https://github.com/jeffthedeveloper/conversational-ai-assistant/issues">Reportar Bug</a>
·
<a href="https://github.com/jeffthedeveloper/conversational-ai-assistant/issues">Solicitar Feature</a>
</p>
</div>

-----

### **Sumário**

1. [Sobre o Projeto](#sobre-o-projeto)  
   * [Principais Funcionalidades](#principais-funcionalidades)  
   * [Tecnologias Utilizadas](#tecnologias-utilizadas)  
2. [Começando](#começando)  
   * [Pré-requisitos](#pré-requisitos)  
   * [Instalação](#instalação)  
3. [Como Usar](#como-usar)  
4. [Roteiro (Roadmap)](#roteiro-roadmap)  
5. [Como Contribuir](#como-contribuir)  
6. [Licença](#licença)  

-----

## **Sobre o Projeto**

> Este projeto é uma implementação de um assistente de IA conversacional baseado em texto, projetado para ser simples, modular e fácil de estender. Ele serve como um excelente ponto de partida para quem deseja explorar a integração de modelos de linguagem generativos (como o GPT-2) com bibliotecas de PLN e interação com o usuário, como a conversão de texto em fala.

O assistente é capaz de entender a entrada do usuário e responder de três maneiras distintas:

1. Executando comandos pré-definidos (como contar caracteres).  
2. Fornecendo respostas personalizadas baseadas em padrões.  
3. Gerando respostas criativas e contextuais usando o modelo GPT-2.  

Toda resposta é então vocalizada, proporcionando uma experiência de interação mais rica.

### **Principais Funcionalidades**

* 🧠 **Inteligência Generativa com GPT-2:** Utiliza a biblioteca `transformers` da Hugging Face para gerar respostas contextualmente relevantes.  
* 🛠️ **Comandos Personalizáveis:** Permite definir respostas fixas para entradas específicas (ex: "que horas são?").  
* 📊 **Análise de Texto com NLTK:** Inclui uma função básica para contar caracteres da entrada do usuário.  
* 🔊 **Saída de Áudio com gTTS:** Converte respostas em áudio usando a API do Google Text-to-Speech.  

### **Tecnologias Utilizadas**

* **[Python 3](https://www.python.org/)**  
* **[NLTK](https://www.nltk.org/)**: Toolkit para tarefas de PLN.  
* **[Transformers (Hugging Face)](https://huggingface.co/docs/transformers/index)**: Carregamento e uso do GPT-2.  
* **[gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)**: Conversão de texto em áudio.  

-----

## **Começando**

Siga estas instruções para obter uma cópia local do projeto e executá-la.

### **Pré-requisitos**

Certifique-se de que você tem **Python 3.8+** e **pip** instalados em sua máquina.

```sh
python --version
pip --version

Instalação

1. Clone o repositório:

git clone https://github.com/jeffthedeveloper/conversational-ai-assistant.git


2. Navegue até o diretório do projeto:

cd conversational-ai-assistant


3. Instale as dependências:

pip install -r requirements.txt

(Recomendado: usar um ambiente virtual.)




---

Como Usar

Após a instalação, execute o script principal:

python main.py

O programa irá saudá-lo e entrar em loop aguardando entradas.
Digite sair para encerrar a sessão.

Exemplo de Interação:

Assistente: Olá! Como posso ajudar você hoje? (Digite 'sair' para encerrar)
Você: > conte os caracteres da frase: eu amo python
Assistente: A frase 'eu amo python' tem 14 caracteres.
Você: > qual a capital da França?
Assistente: A capital da França é Paris. (Resposta gerada pelo GPT-2)
Você: > sair
Assistente: Até logo!


---

Roteiro (Roadmap)

[ ] Adicionar interface gráfica (Tkinter ou PyQT).

[ ] Integrar modelos mais avançados (ex: GPT-3, LLaMA).

[ ] Implementar reconhecimento de voz.

[ ] Containerizar com Docker para facilitar deploy.

[ ] Expandir comandos e respostas personalizadas.


Veja as issues abertas para a lista completa.


---

Como Contribuir

1. Faça um Fork do projeto.


2. Crie sua Feature Branch (git checkout -b feature/AmazingFeature).


3. Faça Commit das mudanças (git commit -m 'Add some AmazingFeature').


4. Faça Push para a Branch (git push origin feature/AmazingFeature).


5. Abra um Pull Request.




---

Licença

Distribuído sob a Licença MIT. Veja o arquivo LICENSE para mais informações.

---
