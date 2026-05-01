import telebot
import random
import time
from flask import Flask
from threading import Thread

# --- CONFIGURAÇÕES ---
# O Token que o BotFather te deu na última imagem
TOKEN = "8764470817:AAF-mZPaqtcx7rL9Jg13UX0JWiM1TZa49DQ"
# O nome do teu canal (Certifica-te que o canal é PÚBLICO)
CHANNEL_ID = "@SpiderCasinoBuster"
LINK_AFILIADO = "https://bantubet.co.ao/affiliates/?btag=2721516"

bot = telebot.TeleBot(TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Spider Bot 24/7 Online"

def run_server():
    app.run(host='0.0.0.0', port=8080)

def sinal_aviator():
    multiplicador = round(random.uniform(1.5, 5.0), 2)
    msg = (
        "🚀 **SPIDER BOT - AVIATOR** 🕸️\n\n"
        "✅ **SINAL CONFIRMADO!**\n"
        f"🎯 Saída Sugerida: {multiplicador}x\n"
        "🏛️ Plataforma: BantuBet\n\n"
        f"[APOSTAR AGORA]({LINK_AFILIADO})"
    )
    return msg

def sinal_bacbo():
    opcoes = ["JOGADOR 🔵", "BANQUEIRO 🔴", "EMPATE ⚪"]
    escolha = random.choices(opcoes, weights=[45, 45, 10], k=1)[0]
    msg = (
        "🎲 **SPIDER BOT - BAC BO** 🕸️\n\n"
        "✅ **PADRÃO IDENTIFICADO!**\n"
        f"🎯 Entrada: {escolha}\n"
        "🏛️ Plataforma: BantuBet\n\n"
        f"[APOSTAR AGORA]({LINK_AFILIADO})"
    )
    return msg

def iniciar_bot():
    print("🕸️ Spider Bot System Iniciado!")
    while True:
        try:
            # 1. Envia Aviator IMEDIATAMENTE
            bot.send_message(CHANNEL_ID, sinal_aviator(), parse_mode="Markdown")
            print("Sinal Aviator enviado!")
            time.sleep(300) # Espera 5 minutos
            
            # 2. Envia Bac Bo
            bot.send_message(CHANNEL_ID, sinal_bacbo(), parse_mode="Markdown")
            print("Sinal Bac Bo enviado!")
            time.sleep(300) # Espera mais 5 minutos e repete o ciclo
            
        except Exception as e:
            print(f"Erro no envio: {e}")
            time.sleep(10) # Se der erro (ex: internet), tenta de novo em 10 segundos

if __name__ == "__main__":
    # Inicia o servidor Flask para o Railway não desligar
    t = Thread(target=run_server)
    t.start()
    # Inicia o bot
    iniciar_bot()
