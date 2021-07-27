from ibm_watson import TextToSpeechV1
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
import sys
import PySimpleGUI as sg
import simpleaudio as sa
from Mic import Mic
from Conversor import Conversor



mic64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAABmJLR0QA/wD/AP+gvaeTAAAD2UlEQVRIieWWbWiVZRjHf9dzXu7nnC0zYU5qus0ZYnMepHIiazSQoabFFosN0gqXZEhRfQjxQyuzF4TKIUtXK4Ji1kCoRkVIW2Nh6UIohi4dGu4lLYjMtZdz7vvqg44Wws5zxvzk/+NzX/fvf1/PfT3Xc8GNJpnJprxnNMY4t0kI1TBDA2/K6HU0Vln8JLWqbEO4Azh/dfNCoFfgYH8Tn4DorBkvr9fcZIg2hMvAnr4FHKVBHAAN6hUPscbCLoFYxOOhnw7IxXRML11A8Vad50GncRzqOyAbfIckBnknUa/HEvV6LDFAc8Sip5plvXG0hZJ0lmzXW9Jxw+kCYsr74mgpuMxB85g2SZI1Kuz1HK8BIJQiNJU+qt2L/uKp81lkm1HeBR6cccZlW7TMWBYez+eN4TivGEvOyGVWRcbojigVEaUiYumal8UqY8m94PPy9wXsNSkWlz+sa2ZsbBybjaNx7S8UmBQ1dpQt8w3r4sK3foolfoolvqXL/kHlzTG2GEttZT/5vqXRODZPx572VUct9+CxG0etBx/GxxAbYr8qFV9+LP0A99doswvxjf8nS53HR2KpCgltzvHczDNOMZQ9wbBvCfuO7yJxVhhL76QpwGdtciZq6bUeiaij27dEopYhY/ltOnZGqqvSdXXV2nrN82ptravSdZmw0lb1VBkLKlQ+8oD2hJQKACd0YClE+SATVsDOpfL4JvYLVInyo6c8nXs35wAuHKfACfsQ7kQ5fLBddsya8Y5NWiiOo4Vl9J/t4i5gZDxJIYAf4SyQtbicnnPdFGFZ/dZXci4dM23nAjDjmGiKuYMdlJgU7VkeRc1HuNR8hEtxj6JoivbBDkoiSebGHH4QZqA7jgJiOeGUF0PQxhg9DetZCZAcoycM84Ea4IWwDUIMaGwmQAT0yn+nvaFT6qYsF+2+979KDwXzDWYcdoyEwTjlbw9uuuZgljlOuCSKCQsjQZiB7nhXFwPGsmDOOKeMJdFYqnmTa/vKdJGxrMgeo8+3LHi2i4EgzMCDQNNqbVI47SnDCntQWq4S6j1hpyh5CoVP/BDscwqUMUC2R4Nv2RZ1hCJJNhpH0jiSsRQbTIpo1FIfH+WloLyMZq7WlXqrFd5DyfGELq7MOeWqXAjB1roTMnRdjCfVVqLP2/ls9QC5SEvNz/J6poyMjD9drvcBG1GKQ1FyBHAT/I7Si/L5ppPyxawbf71Mb3dwBGWnpyT/BxEiCq8irK08KadnxbhzqW5XpRolHyEucJIpA+xkdSosA/4R+BXlcPkZeXs6btoGEk/R7uBYurip8iDteHvj6V98NG1phU/XMwAAAABJRU5ErkJggg=='
play64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAABmJLR0QA/wD/AP+gvaeTAAABu0lEQVRIie3WsWsUQRTH8e9Lltyc3IFXaKGdRcRCu8SgoJ2VoE0a+yQEg5WFXVb3EATDXbCK/gdJoZbaiJWghWCQ3O4FuzQRvUJJINmZZ6EnId7GJLs3VX7VLrNvP/PYebBwFE+RrIVSlFwX0TmBlc20eovw1EaR8ED2jrSJMqzKDRP8WC5F7WteYIWfO27OCO6ViZLFysP2ib7CgnR6bGc8tRqbB8kkqpmfKRecHa0humDq8ZtS1DrrEe5Grgry0URxSPh5yCMMQBmYLQ8GH8r1eNQnDIDCBVXemXq8wKNW1Rv8913KpNmSlWNRfNMn3M1pB89NlCxWwtWTPuE/0fE0cC0TtWd7jV4fYUC1Bi4s19t3dy8FWTXb374XAAMC+vtqf3Ax0Y7AvG2OzfmDhSUbuBkeX17vtdwPeA1kxjYuvtjroSIPlwOe2qH0nG3ujUJBHSt8GhQ3sd249H6/NXk73hT0vjteHTkICrk6lrdWB6aYH4kPU31wWOgA92xj9BnIP/OZG1akJrvnXliy6dZtnlz5eljwv7DgKjt+Qr+IMJ02xl7nBbvJPlxO7iiSAC/tRnC+SPQoXvML5X+UEwTdbd8AAAAASUVORK5CYII='
close64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsSAAALEgHS3X78AAAE30lEQVRIiZ2VXYgdRRqGn6+quvucM/85iRoTNevMBJFEWY0GFQTBC1HBlaz/jMpoFFfXBdmFvdiLvRIEFRHFGBXMjUQhF/6Bol6sSNaIruCNir/R/Dlx5iRzck736e6qby/6JDlx9CIWFN10Ue/7vW+9X7XcDn8bryWPL2vERkNQQPj9Q72K7F3s7Hxb9bZ98L0bj91jt1y23kxNTxIEGUQ/aTYR6WW9cud/Prx01zf7/7FP5EHXHG7Y6bVTpBPLMSegCWKEEMKvkihgjEWDP+FbEjxTa1bjv9l/CsIKF3ypHhUDSFGACCKC956iKKjV6/hfkCjgUNK0TW1oCA3h+EJk8UUBYFCsQaSyRajArUWLnEONcTrT68nTLtZaEKmmMTiUlsREGy9HO0dgcL1y6lgtZrAsEYFexhwxq2buYfru+1mcOo+828UYg4rgUH7OSkY3zbDq1lkaV1yFP9TqEyy18jiBCMF7DjYmOOu+hxifnCSKItZuvp/F6fPJ05TEwE+dHhN33MfpGy4iFAVjf7qF8etvBV9y1IilBApGIMt6TExOM372JKqKqhLFMdOz93Jk6jx+bHVoztzLyj9eiHqP2Gq7O3UlGAuq1RwYDlUwhoChMdSAz3ZxaEeD8T/fBggaAnGtxpqZWdKFBSbOPLMCCQGJItJPdrHw4lOYRgNsBM6dSCDGErIuodtGkhoyPEr68U5svcbI1ZsQY0CV2vAw9ZGRKjEiSBTR/fQjDm9/AddcjqoSul182kYHVDhJauRffUH7wD7ilatxzVOwI6PM7XiJLO2x4rob0CgGVTSEKigidD94j/ltW9Dg0b0/4BfmyQ8ewKUdWLZ6wCIB9SXFXJvQ+hLkc6QeEznHf199jY1rpjh1w0ZUFTGm7z18/tSj2Hffor5shKLdhhJCADMcw7IlKRIkAqkJRIa4LPl6d5c/PPJkBd5vpArcArD+ue101l1Md08bFxuIBUlOyOUggUIAVIl94Kv5wKqtz7L+7r/0bRHEmApcFbwnHhljw6tv0b3kEtK5gDWmj/GbfQAWZbdaztjyPOfP3oN6D8GDCO133uDAvx9CyxKsRX1JMjbBBa+8Rnbl5RSpR35RfXUGfVLnYGFBcTfdwLo77yLkPYy14CLa773JngfuoNy7QOh2WPnw09WVkufUm8s598G/s+eT9wmBJZ1m+sVTFNBc4Wi8vJ3v//kAJk7AOhbf3MGezTfjWwuYCcv8s1s58K+/okWOxDGdjz5g7+YZtKRSoL+igCp5FKVntGk48sTTzDWb1C+4mB833wgETD2CELBjEfNbtyAjo4xdcz27N11L6B5GGoZQhN+26KiSoII9LebnJx9BkggzNIQkyfEdItiRQGvbM7S2bQHJMGN1NO8ds2dQhBORYBCjAFEE1kFSw0QxuAiTJCAGce64vz4gviTkOTJcErIMMRbyDIxg7bHTFnc47clcmpdj43VkeBRJEkytgdTqSL2OiRMkSRDroH9t4EtCUaBZhmYpIUurZ9pFfVnuX+w62xfjeq3D3/6vbifXrT1XkzgWdREmipA4RlwMUYRY21cg/X+lJ5gSbIHGOVovCHmOCSX7DrbMx599icIhVI2cA5c5mC1gbGnITm4oqAOr0PoOXs9g51HAGiITyCDByXDp4KuiaoESmP8/YC0Y5GajmEsAAAAASUVORK5CYII='


 

def ShowMeTheButtons():
    
    conversor = Conversor() 
    
    layout = [                 
              [sg.Text('Digite o texto e pressione o play para ouvir o áudio', size =(60, 1))], 
              [sg.InputText(size=(60, 2)), sg.Button('', image_data=play64[22:],button_color=('white', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='texto', tooltip='Fechar') ], 
              [sg.Text('Informe quantos segundos deseja falar e pressione o microfone para iniciar', size =(60, 1))], 
              [sg.InputText(size=(10, 2), key='seconds'), sg.Button('',size=(1,1), image_data=mic64[22:],button_color=('white', sg.COLOR_SYSTEM_DEFAULT), pad=(0,0), key='microfone', tooltip='Fechar') ],                  
              [sg.Output(size=(60, 10), font=('Helvetica 10'), key='-OUTPUT-')],              
              [sg.Text('Computação Cognitiva 2', relief=sg.RELIEF_SUNKEN,
                    size=(55, 1), pad=(0, 3), key='-status-')]                
              ]
    window = sg.Window('Conversor', layout, finalize=True)
    window.finalize()
    window['seconds'].update(value='5')
    while True:
        button, value = window.read()
        window['-OUTPUT-'].update(value='')
        if button in ('-close-', 'Exit') or button is None:
            break       
        
        if button == 'texto':      
            try:      
                print('Processando... Aguarde!')            
                text = value[0]            
                conversor.textToSpeech(text)
                filename = 'audio.wav'
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
                print('Executando áudio...')
                play_obj.wait_done()
                print('Áudio finalizado')
            except:
                print('Erro ao executar tarefa. Tente Novamente!')
           
        if button == 'microfone':                  
            try:
                segundos = int(value['seconds'])
                mic =  Mic(segundos)
                mic.rec()  
                conversor.speechToText()
            except:
                print('Erro ao executar tarefa. Tente Novamente!')


if __name__ == '__main__':
    ShowMeTheButtons()
    
