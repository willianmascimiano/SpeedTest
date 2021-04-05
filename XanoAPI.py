import requests



# Acessar https://xano.io/1zgzwnvj e criar uma instância. 
base_url= "https://x8ki-letl-twmt.n7.xano.io/api:vFrDc6RD/speedtest"

def speedTestRecordSave(data_atual,hora_atual,velocidade):
    requests.post(base_url, data={'data':  data_atual, 
                                'hora':hora_atual, 
                                'velocidade' : velocidade
                                })