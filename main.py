import random
import time
from twilio.rest import Client

# Informações da sua conta Twilio
account_sid = ''
auth_token = ''
twilio_phone_number = ''

# Número de telefone para o qual você deseja enviar o SMS
to_phone_number = ''

# Função para enviar o SMS
def enviar_sms(message):
    # Criação do cliente Twilio
    client = Client(account_sid, auth_token)

    # Envio do SMS
    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=to_phone_number
    )
    print('SMS enviado com sucesso!')

def megaSena():
    def gerar_numeros_mega_sena():
        numeros = random.sample(range(1, 61), 1)
        return sorted(numeros)

    def verificar_ganhador(jogo_usuario, numeros_sorteio):
        acertos = set(jogo_usuario) & set(numeros_sorteio)
        return sorted(acertos)

    # Sortear números aleatórios para o jogo do usuário e para a Mega-Sena
    jogo_usuario = gerar_numeros_mega_sena()
    numeros_sorteio = gerar_numeros_mega_sena()

    # Verificar os números do usuário e exibir os resultados
    acertos = verificar_ganhador(jogo_usuario, numeros_sorteio)
    print("Números sorteados pela Mega-Sena:", numeros_sorteio)
    print("Seus números:", jogo_usuario)
    print("Você acertou", len(acertos), "número(s):", acertos)

    # Verificar se o usuário ganhou
    if len(acertos) == 1:
        print("Parabéns! Você ganhou na Mega-Sena!")
        enviar_sms("Você ganhou na Mega-Sena!")  # Chamando a função para enviar o SMS
    else:
        print("Infelizmente, você não ganhou na Mega-Sena. Tente novamente!")
        time.sleep(1/25)

# Chamando a função megaSena para iniciar o jogo
megaSena()
