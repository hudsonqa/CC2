## **Computação Cognitiva 2: Interface do usuário baseada em voz**
O presente projeto tem como objetivo transforma texto em voz e voz em texto, e foi  elaborado como atividade da disciplina Computação Cognitiva 2 da Pós-Graduação em Inteligência Artifical .

## Instalação

Baixe o pacote e instale as dependências que estão no arquivo requirements.txt	

    $ pip install -r requirements.txt
Informe as chaves do IBM Watson TextToSpeechV1 e SpeechToTextV1 no arquivo Conversor.py

    self.authenticatorTextToSpeechV1 = IAMAuthenticator('api key')
    self.authenticatorSpeechToTextV1 = IAMAuthenticator('api key')

## Execução
Execute o arquivo Main.py

![enter image description here](https://raw.githubusercontent.com/hudsonqa/CC2/main/imgs/speechtotext.JPG)![enter image description here](https://raw.githubusercontent.com/hudsonqa/CC2/main/imgs/texttospeech.JPG)




