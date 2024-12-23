import telebot
import emoji
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

animals = {
    "Огонь 🔥": [
        {"name": "Александрийский попугай", "habitat": "Леса 🌲", "trait": "Сила 💪", "image": "images/fire1.png", "link": "https://moscowzoo.ru/animals/kinds/aleksandriyskiy_popugay"},
        {"name": "Алый ибис", "habitat": "Леса 🌲", "trait": "Мудрость 🧙", "image": "images/fire2.png", "link": "https://moscowzoo.ru/animals/kinds/alyy_ibis"},
        {"name": "Андский кондор", "habitat": "Горы 🌄", "trait": "Скорость 🏃", "image": "images/fire3.png", "link": "https://moscowzoo.ru/animals/kinds/andskiy_kondor"},
        {"name": "Белоголовый сип", "habitat": "Горы 🌄", "trait": "Хитрость 🥷", "image": "images/fire4.png", "link": "https://moscowzoo.ru/animals/kinds/belogolovyy_sip"},
        {"name": "Африканский марабу", "habitat": "Пустыни 🏜", "trait": "Сила 💪", "image": "images/fire5.png", "link": "https://moscowzoo.ru/animals/kinds/afrikanskiy_marabu"},
        {"name": "Беркут", "habitat": "Пустыни 🏜", "trait": "Мудрость 🧙", "image": "images/fire6.png", "link": "https://moscowzoo.ru/animals/kinds/berkut"},
        {"name": "Полосатая гиена", "habitat": "Водоемы 🌊", "trait": "Хитрость 🥷", "image": "images/fire7.png", "link": "https://moscowzoo.ru/animals/kinds/polosataya_giena"},
        {"name": "Гривистый волк", "habitat": "Водоемы 🌊", "trait": "Скорость 🏃", "image": "images/fire8.png", "link": "https://moscowzoo.ru/animals/kinds/grivistyy_volk"}
    ],
    "Вода 🌊": [
        {"name": "Африканский водонос", "habitat": "Леса 🌲", "trait": "Сила 💪", "image": "images/water1.png", "link": "https://moscowzoo.ru/animals/kinds/afrikanskiy_vodonos_royuschaya_lyagushka"},
        {"name": "Гавиаловый крокодил", "habitat": "Леса 🌲", "trait": "Мудрость 🧙", "image": "images/water2.png", "link": "https://moscowzoo.ru/animals/kinds/gavialovyy_krokodil"},
        {"name": "Нильский крокодил", "habitat": "Горы 🌄", "trait": "Скорость 🏃", "image": "images/water3.png", "link": "https://moscowzoo.ru/animals/kinds/nilskiy_krokodil"},
        {"name": "Сиамский крокодил", "habitat": "Горы 🌄", "trait": "Хитрость 🥷", "image": "images/water4.png", "link": "https://moscowzoo.ru/animals/kinds/siamskiy_krokodil"},
        {"name": "Розовый фламинго", "habitat": "Пустыни 🏜", "trait": "Сила 💪", "image": "images/water5.png", "link": "https://moscowzoo.ru/animals/kinds/rozovyy_flamingo"},
        {"name": "Капибара", "habitat": "Пустыни 🏜", "trait": "Мудрость 🧙", "image": "images/water6.png", "link": "https://moscowzoo.ru/animals/kinds/kapibara"},
        {"name": "Пингвин Гумбольдта", "habitat": "Водоемы 🌊", "trait": "Скорость 🏃", "image": "images/water7.png", "link": "https://moscowzoo.ru/animals/kinds/pingvin_gumboldta"},
        {"name": "Морж", "habitat": "Водоемы 🌊", "trait": "Хитрость 🥷", "image": "images/water8.png", "link": "https://moscowzoo.ru/animals/kinds/morzh"}
    ],
    "Земля 🌍": [
        {"name": "Большая панда", "habitat": "Леса 🌲", "trait": "Сила 💪", "image": "images/earth1.png", "link": "https://moscowzoo.ru/animals/kinds/bolshaya_panda"},
        {"name": "Домашний як", "habitat": "Леса 🌲", "trait": "Мудрость 🧙", "image": "images/earth2.png", "link": "https://moscowzoo.ru/animals/kinds/domashniy_yak"},
        {"name": "Викунья", "habitat": "Горы 🌄", "trait": "Скорость 🏃", "image": "images/earth3.png", "link": "https://moscowzoo.ru/animals/kinds/vikunya"},
        {"name": "Амурский тигр", "habitat": "Горы 🌄", "trait": "Хитрость 🥷", "image": "images/earth4.png", "link": "https://moscowzoo.ru/animals/kinds/amurskiy_tigr"},
        {"name": "Индийский лев", "habitat": "Пустыни 🏜", "trait": "Сила 💪", "image": "images/earth5.png", "link": "https://moscowzoo.ru/animals/kinds/indiyskiy_lev"},
        {"name": "Щетинистый броненосец", "habitat": "Пустыни 🏜", "trait": "Мудрость 🧙", "image": "images/earth6.png", "link": "https://moscowzoo.ru/animals/kinds/schetinistyy_bronenosec"},
        {"name": "Манул", "habitat": "Водоемы 🌊", "trait": "Скорость 🏃", "image": "images/earth7.png", "link": "https://moscowzoo.ru/animals/kinds/manul"},
        {"name": "Кустарниковая собака", "habitat": "Водоемы 🌊", "trait": "Хитрость 🥷", "image": "images/earth8.png", "link": "https://moscowzoo.ru/animals/kinds/kustarnikovaya_sobaka"}
    ],
    "Воздух 🌬": [
        {"name": "Большой желтохохлый какаду", "habitat": "Леса 🌲", "trait": "Сила 💪", "image": "images/air1.png", "link": "https://moscowzoo.ru/animals/kinds/bolshoy_zheltohohlyy_kakadu"},
        {"name": "Малый желтохохлый какаду", "habitat": "Леса 🌲", "trait": "Мудрость 🧙", "image": "images/air2.png", "link": "https://moscowzoo.ru/animals/kinds/malyy_zheltohohlyy_kakadu"},
        {"name": "Большой тукан", "habitat": "Горы 🌄", "trait": "Скорость 🏃", "image": "images/air3.png", "link": "https://moscowzoo.ru/animals/kinds/bolshoy_tukan"},
        {"name": "Голубая сорока", "habitat": "Горы 🌄", "trait": "Хитрость 🥷", "image": "images/air4.png", "link": "https://moscowzoo.ru/animals/kinds/golubaya_soroka"},
        {"name": "Желтолобый амазон", "habitat": "Пустыни 🏜", "trait": "Сила 💪", "image": "images/air5.png", "link": "https://moscowzoo.ru/animals/kinds/zheltolobyy_amazon"},
        {"name": "Восточный венценосный журавль", "habitat": "Пустыни 🏜", "trait": "Мудрость 🧙", "image": "images/air6.png", "link": "https://moscowzoo.ru/animals/kinds/vostochnyy_vencenosnyy_zhuravl"},
        {"name": "Журавль-красавка", "habitat": "Водоемы 🌊", "trait": "Скорость 🏃", "image": "images/air7.png", "link": "https://moscowzoo.ru/animals/kinds/zhuravl_krasavka"},
        {"name": "Секретарь", "habitat": "Водоемы 🌊", "trait": "Хитрость 🥷", "image": "images/air8.png", "link": "https://moscowzoo.ru/animals/kinds/sekretar"}
    ]
}

load_dotenv()

TOKEN = os.getenv("TOKEN")
admin_id = int(os.getenv("admin_id"))

bot = telebot.TeleBot(TOKEN)

user_data = {}


def ensure_user_data(chat_id):
    if chat_id not in user_data:
        user_data[chat_id] = {"category": None, "habitat": None, "trait": None}

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    ensure_user_data(message.chat.id)
    bot.send_message(
        message.chat.id,
        emoji.emojize(
            ":sparkles: Добро пожаловать в викторину Московского зоопарка! ❤️\n"
            "Мы поможем вам найти ваше тотемное животное и расскажем, как поддержать наших обитателей!\n\n"
            ":tiger: Выберите категорию: Огонь, Вода, Земля или Воздух."
        ),
        reply_markup=create_main_menu()
    )

# Главное меню
def create_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Огонь 🔥", "Вода 🌊")
    markup.row("Земля 🌍", "Воздух 🌬")
    return markup

# Меню с итоговыми кнопками
def create_result_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Перезапустить викторину 🔄", callback_data="restart"))
    markup.add(InlineKeyboardButton("Связаться с нами ✉️", callback_data="contact_us"))
    markup.add(InlineKeyboardButton("Оставить отзыв 📝", callback_data="feedback"))
    return markup

# Обработка выбора категории
@bot.message_handler(func=lambda message: message.text in ["Огонь 🔥", "Вода 🌊", "Земля 🌍", "Воздух 🌬"])
def choose_category(message):
    ensure_user_data(message.chat.id)
    user_data[message.chat.id]["category"] = message.text
    bot.send_message(
        message.chat.id,
        emoji.emojize(":national_park: Какую среду обитания вы предпочитаете?"),
        reply_markup=create_habitat_menu()
    )

# Меню выбора среды
def create_habitat_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Леса 🌲", "Горы 🌄")
    markup.row("Пустыни 🏜", "Водоемы 🌊")
    return markup

@bot.message_handler(func=lambda message: message.text in ["Леса 🌲", "Горы 🌄", "Пустыни 🏜", "Водоемы 🌊"])
def choose_habitat(message):
    ensure_user_data(message.chat.id)
    user_data[message.chat.id]["habitat"] = message.text
    bot.send_message(
        message.chat.id,
        emoji.emojize("Какое качество вам ближе?"),
        reply_markup=create_trait_menu()
    )

# Меню выбора качества
def create_trait_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Сила 💪", "Скорость 🏃")
    markup.row("Мудрость 🧙", "Хитрость 🥷")
    return markup

@bot.message_handler(func=lambda message: message.text in ["Сила 💪", "Скорость 🏃", "Мудрость 🧙", "Хитрость 🥷"])
def choose_trait(message):
    ensure_user_data(message.chat.id)
    user_data[message.chat.id]["trait"] = message.text
    category = user_data[message.chat.id]["category"]
    habitat = user_data[message.chat.id]["habitat"]
    trait = user_data[message.chat.id]["trait"]

    # Фильтрация животных
    filtered_animals = [
        animal for animal in animals[category]
        if animal["habitat"] == habitat and animal["trait"] == trait
    ]

    if not filtered_animals:
        bot.send_message(
            message.chat.id,
            emoji.emojize(":warning: К сожалению, мы не смогли найти животное по вашим ответам.\n"
                          "Попробуйте другую категорию или перезапустите викторину."),
            reply_markup=create_result_menu()
        )
        return

    chosen_animal = filtered_animals[0]
    send_result_to_user(message.chat.id, chosen_animal)
    send_result_to_admin(message.chat.id, chosen_animal)

# Отправка результата пользователю
def send_result_to_user(chat_id, animal):
    with open(animal["image"], "rb") as photo:
        bot.send_photo(
            chat_id,
            photo,
            caption=emoji.emojize(
                f"Поздравляем! Ваше тотемное животное: {animal['name']}!\n\n"
                f"Узнайте больше: {animal['link']}\n\n"
                "Поддержите его через программу опеки Московского зоопарка!"
            ),
            reply_markup=create_result_menu()
        )

# Обработка нажатий на кнопки
@bot.callback_query_handler(func=lambda call: call.data in ["restart", "contact_us", "feedback"])
def handle_callback(call):
    if call.data == "restart":
        start(call.message)
    elif call.data == "contact_us":
        bot.send_message(
            call.message.chat.id,
            "Вы можете связаться с нами по email: info@moscowzoo.ru или через этот бот."
        )
    elif call.data == "feedback":
        bot.send_message(call.message.chat.id, "Напишите ваш отзыв:")
        bot.register_next_step_handler(call.message, save_feedback)

# Сохранение отзыва
def save_feedback(message):
    try:
        bot.send_message(admin_id, f"Отзыв от {message.chat.id}: {message.text}")
        bot.send_message(message.chat.id, "Спасибо за ваш отзыв!")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка отправки отзыва: {e}")

# Отправка результата админу
def send_result_to_admin(chat_id, animal):
    try:
        bot.send_message(
            admin_id,
            f"Пользователь {chat_id} выбрал:\n"
            f"Категория: {user_data[chat_id]['category']}\n"
            f"Среда: {user_data[chat_id]['habitat']}\n"
            f"Качество: {user_data[chat_id]['trait']}\n\n"
            f"Животное: {animal['name']}\n"
            f"Ссылка: {animal['link']}"
        )
    except Exception as e:
        print(f"Ошибка отправки админу: {e}")

# Обработка неизвестных сообщений
@bot.message_handler(func=lambda message: True)
def unknown_message(message):
    bot.send_message(
        message.chat.id,
        emoji.emojize("Извините, я вас не понял. Пожалуйста, выберите опцию из меню или начните с /start.")
    )

# Запуск бота
bot.polling(none_stop=True)