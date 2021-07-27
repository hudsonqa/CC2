import pyaudio
import wave
import struct

class Mic():
    def __init__(self, segundos):
        self.chunk = 1024
        self.formato = pyaudio.paInt16
        self.canais = 1
        self.taxaDeAmostragem = 44100
        self.tempoDeGravacao = segundos
        self.nomeArquivoSaida = "saidaMic.wav"
        self.deltaX= 1.0/self.taxaDeAmostragem
        self.objetoPyAudio = pyaudio.PyAudio()

    def rec(self):
        print ("Gravando durante " , self.tempoDeGravacao ,"  segundos...")
        streamMic = self.objetoPyAudio.open(format=self.formato,channels=self.canais, rate=self.taxaDeAmostragem, input=True, frames_per_buffer=self.chunk) 
        framesWav = []    
        for nLoop in range(0, int(self.taxaDeAmostragem / self.chunk * self.tempoDeGravacao)):
            dadosLidosMic = streamMic.read(self.chunk)
            framesWav.append(dadosLidosMic)
        streamMic.stop_stream()
        streamMic.close()
        self.objetoPyAudio.terminate()        
        framesWavJuntos= b''.join(framesWav)    
        arquivoWav = wave.open(self.nomeArquivoSaida, 'wb')
        arquivoWav.setnchannels(self.canais)
        arquivoWav.setsampwidth(self.objetoPyAudio.get_sample_size(self.formato))
        arquivoWav.setframerate(self.taxaDeAmostragem)
        arquivoWav.writeframes(framesWavJuntos)
        arquivoWav.close()     
               
        print("Fim de gravação")


