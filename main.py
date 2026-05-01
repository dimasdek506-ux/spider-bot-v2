import telebot
import random
import time
from flask import Flask
from threading import Thread

# --- CONFIGURAÇÕES ---
TOKEN = "8764470817:AAF-mZPaqtcx7rL9Jg13UX0JWiM1TZa49DQ"
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
    return f"🚀 **SPIDER BOT - AVIATOR** 🕸️\n\n✅ **SINAL CONFIRMADO!**\n🎯 Saída Sugerida: {multiplicador}x\n🏛️ Plataforma: BantuBet\n\n[APOSTAR AGORA]({LINK_AFILIADO})"

def sinal_bacbo():
    opcoes = ["JOGADOR 🔵", "BANQUEIRO 🔴", "EMPATE ⚪"]
    escolha = random.choices(opcoes, weights=[45, 45, 10], k=1)[0]
    return f"🎲 **SPIDER BOT - BAC BO** 🕸️\n\n✅ **PADRÃO IDENTIFICADO!**\n🎯 Entrada: {escolha}\n🏛️ Plataforma: BantuBet\n\n[APOSTAR AGORA]({LINK_AFILIADO})"

def iniciar_bot():
    print("🕸️ Spider Bot System Iniciado!")
    while True:
        try:
            # Envia o primeiro sinal logo que o bot liga
            bot.send_message(CHANNEL_ID, sinal_aviator(), parse_mode="Markdown")
            time.sleep(300)
            bot.send_message(CHANNEL_ID, sinal_bacbo(), parse_mode="Markdown")
            time.sleep(300)
        except Exception as e:
            print(f"Erro: {e}")
            time.sleep(10)

if __name__ == "__main__":
    t = Thread(target=run_server)
    t.start()
    iniciar_bot()
