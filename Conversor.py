from ibm_watson import TextToSpeechV1
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
class Conversor:
    def __init__(self):
        self.authenticatorTextToSpeechV1 = IAMAuthenticator('api key')
        self.authenticatorSpeechToTextV1 = IAMAuthenticator('api key')
        self.tts = TextToSpeechV1(
            authenticator=self.authenticatorTextToSpeechV1
        )
        self.speech_to_text = SpeechToTextV1(
            authenticator=self.authenticatorSpeechToTextV1
        )
    
    def textToSpeech(self, text):
        with open('audio.wav', 'wb') as audio_file:
            content = self.tts.synthesize(
                text,
                voice='pt-BR_IsabelaV3Voice',
                accept='audio/wav').get_result().content
            audio_file.write(content)
            audio_file.close()      
    
    def speechToText(self, audio='saidaMic.wav'):
        print('Processando... Aguarde!') 
        with open(audio,'rb') as audio_file:
            speech_recognition_results = self.speech_to_text.recognize(
                audio=audio_file,
                model = 'pt-BR_NarrowbandModel',
                content_type='audio/wav'       
            ).get_result()
        print('Transcrição da sua fala:')    
        print(f"     {speech_recognition_results['results'][0]['alternatives'][0]['transcript']}")