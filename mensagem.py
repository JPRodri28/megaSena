import random
import time
import requests
import json
def megaMensagem():
    url = "https://graph.facebook.com/v17.0/104678875998726/messages"
    headers = {
        "Authorization": "Bearer EAAEDUVGoETwBABZBzXgxZAWP5k9SdaoHcpZANhodQW6zHYmqnYZAQSRceOAwQC31ZBESjsztUoZAyr4lO4P4ib0n1ZA4H220vjZBQ7iMx8KQ2STZCmRzGxywu9q1GgzZCjPGKSDtMMpUsZBminiQM05FAoSEH97n1DrlvcdyJXZCZAeEh8d97z9WUjtGCySpiKoeZA8TL535mroLcqewZDZD",
        "Content-Type": "application/json"
    }
    message_content = "Você acertou na Mega-Sena"
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": "5554984369987",
        "type": "text",
        "text": {
            "preview_url": True,
            "body": message_content
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.text)

    if response.status_code == 200:
        response_data = json.loads(response.text)
        message_id = response_data["messages"][0]["id"]
        print("ID da mensagem:", message_id)

def esperarSegundos(segundos):
    time.sleep(segundos)
def megaSena():
    def gerar_numeros_mega_sena():
        numeros = random.sample(range(1, 61), 2)
        return sorted(numeros)

    def verificar_ganhador(jogo_usuario, numeros_sorteio):
        acertos = set(jogo_usuario) & set(numeros_sorteio)
        return sorted(acertos)

    # Gerar números aleatórios para o sorteio da Mega-Sena
    numeros_sorteio = gerar_numeros_mega_sena()

    # Solicitar que o usuário insira seus números
    print("Bem-vindo ao jogo da Mega-Sena!")
    #print("Insira 6 números entre 1 e 60:")
    jogo_usuario = []
    for _ in range(2):
        numero = random.randint(1, 60)  # Gera um número aleatório entre 1 e 60
        jogo_usuario.append(numero)
        #print("Número sorteado pelo computador:", numero)

    # Verificar os números do usuário e exibir os resultados
    acertos = verificar_ganhador(jogo_usuario, numeros_sorteio)
    print("Números sorteados:", numeros_sorteio)
    print("Seus números:", jogo_usuario)
    print("Você acertou", len(acertos), "número(s):", acertos)

    # Verificar se o usuário ganhou e enviar um SMS (exemplo básico)
    if len(acertos) != 2:
        # Aqui você pode adicionar o código para enviar o SMS usando um serviço de terceiros
        esperarSegundos(1/50)
        megaSena()
    else:
        megaMensagem()
megaSena()