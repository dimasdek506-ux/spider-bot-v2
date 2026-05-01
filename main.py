import telebot
import random
import time
from flask import Flask
from threading import Thread

# --- CONFIGURAÇÕES DO NOVO BOT ---
TOKEN = "8338986094:AAGpXPZVGvXJjUH789rK7rsHwWtGcmOrEuE"
CHANNEL_ID = "@SpiderCasinoBuster"
LINK_AFILIADO = "https://bantubet.co.ao/affiliates/?btag=2721516"

bot = telebot.TeleBot(TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Spider Bot V3 - Ativo"

def run_server():
    app.run(host='0.0.0.0', port=8080)

def sinal_aviator():
    multiplicador = round(random.uniform(1.5, 4.5), 2)
    return (f"🚀 **SPIDER BOT - AVIATOR** 🕸️\n\n"
            f"✅ **SINAL CONFIRMADO!**\n"
            f"🎯 Saída Sugerida: {multiplicador}x\n"
            f"🏛️ Plataforma: BantuBet\n\n"
            f"👉 [APOSTAR AGORA]({LINK_AFILIADO})")

def sinal_bacbo():
    opcoes = ["JOGADOR 🔵", "BANQUEIRO 🔴", "EMPATE ⚪"]
    escolha = random.choices(opcoes, weights=[45, 45, 10], k=1)[0]
    return (f"🎲 **SPIDER BOT - BAC BO** 🕸️\n\n"
            f"✅ **PADRÃO IDENTIFICADO!**\n"
            f"🎯 Entrada: {escolha}\n"
            f"🏛️ Plataforma: BantuBet\n\n"
            f"👉 [APOSTAR AGORA]({LINK_AFILIADO})")

def iniciar_bot():
    print("🕸️ Spider Bot V3: Sistema Iniciado com Sucesso!")
    while True:
        try:
            # Envia Aviator imediatamente
            bot.send_message(CHANNEL_ID, sinal_aviator(), parse_mode="Markdown")
            print("Sinal Aviator enviado ao canal.")
            time.sleep(300) # Espera 5 minutos
            
            # Envia Bac Bo
            bot.send_message(CHANNEL_ID, sinal_bacbo(), parse_mode="Markdown")
            print("Sinal Bac Bo enviado ao canal.")
            time.sleep(300)
        except Exception as e:
            print(f"Erro no envio: {e}")
            time.sleep(10)

if __name__ == "__main__":
    t = Thread(target=run_server)
    t.start()
    iniciar_bot()
