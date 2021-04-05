import speedtest
from datetime import datetime
import pandas as pd
from threading import Timer

import XanoAPI



# função para gravar dados da velocidade da internet
def internet():
    df = pd.read_excel('dados.xlsx', sheet_name='base')
    s = speedtest.Speedtest()
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')
    velocidade = s.download(threads=None)*(10**-6)
    df.loc[len(df)] = [data_atual, hora_atual, round(velocidade)]
    df.to_excel('dados.xlsx', sheet_name='base', index=False)


    XanoAPI.speedTestRecordSave(data_atual,hora_atual,velocidade)
    


    Timer(30,internet).start()


internet()


