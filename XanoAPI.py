import requests



# Acessar https://xano.io/ e criar uma instância. 
base_url= "https://my_url/speedtest"

def speedTestRecordSave(data_atual,hora_atual,velocidade):
    requests.post(base_url, data={'data':  data_atual, 
                                'hora':hora_atual, 
                                'velocidade' : velocidade
                                })
