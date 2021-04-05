import speedtest
from datetime import datetime
import pandas as pd
from threading import Timer

import requests


# Acessar https://xano.io/1zgzwnvj e criar uma instância. 
base_url= "https://url/speedtest"


# função para gravar dados da velocidade da internet
def internet():
    df = pd.read_excel('dados.xlsx', sheet_name='base')
    s = speedtest.Speedtest()
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')
    velocidade = s.download(threads=None)*(10**-6)
    df.loc[len(df)] = [data_atual, hora_atual, round(velocidade)]
    df.to_excel('dados.xlsx', sheet_name='base', index=False)

    requests.post(base_url, data={'data':  data_atual, 'hora':hora_atual, 'velocidade' : velocidade})


    Timer(30,internet).start()


internet()


