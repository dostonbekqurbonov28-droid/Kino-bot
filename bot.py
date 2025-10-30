# Kino-bot
Kino kod orqali qildiruvchi bot
import telebot

# 🔑 Token joyi — bu yerga o'z tokeningni yozasan
TOKEN = "BU_YERGA_TOKENINGNI_YOZ"
bot = telebot.TeleBot(8440109755:AAGJbqx7p5p4NxS48iLcTpyqG5WpYYibZao)

# 🔗 Kanal username
CHANNEL = "@Tarjimakinolarc0m"

# 🎥 Kinolar ro‘yxati (kod: ma'lumot)
movies = {
    "1": """🎥 *Swat - Olovli boron* (2011)
📹 1080p
🎬 Nomi: Yomon yigitlar 4: Hayda yoki o'l
💾 Hajmi: 1.3 GB
🌎 Davlati: AQSH
📹 Sifati: 720p
🇺🇿 Tili: O‘zbek tili
#⃣ Janri: jangari kriminal
🗓 Yili: 2024
⌚️ Davomiyligi: 1 soat 56 daqiqa
📺 Kino kanal: https://t.me/Tarjimakinolarc0m
""",
    "2": """🎥 *Fast & Furious X* (2023)
💾 Hajmi: 1.8 GB
🌎 Davlati: AQSH
📹 Sifati: 1080p
🇺🇿 Tili: O‘zbek tili
#⃣ Janri: jangari sarguzasht
🗓 Yili: 2023
⌚️ Davomiyligi: 2 soat 10 daqiqa
📺 Kino kanal: https://t.me/Tarjimakinolarc0m
"""
}

# 🔹 Start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    text = f"👋 Salom, {message.from_user.first_name}!\n\n"
    text += f"Botdan foydalanish uchun quyidagi kanalga a'zo bo‘ling:\n👉 {CHANNEL}"
    bot.send_message(message.chat.id, text)

# 🔹 Har qanday matn (kodi)ni qabul qiladi
@bot.message_handler(func=lambda message: True)
def check_code(message):
    user_id = message.from_user.id

    # Kanalga a'zolikni tekshirish
    try:
        member = bot.get_chat_member(CHANNEL, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            code = message.text.strip()
            if code in movies:
                bot.send_message(message.chat.id, movies[code], parse_mode="Markdown")
            else:
                bot.send_message(message.chat.id, "❌ Bunday kodli kino topilmadi.")
        else:
            bot.send_message(message.chat.id, f"🚫 Iltimos, avval kanalga a'zo bo‘ling: {CHANNEL}")
    except Exception:
        bot.send_message(message.chat.id, f"⚠️ Iltimos, kanalga a'zo bo‘ling: {CHANNEL}")

print("✅ Bot ishga tushdi...")
bot.infinity_polling()
