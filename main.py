from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import logging
import config as cfg
import datetime


logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)

dp = Dispatcher(bot)

btn_ras = KeyboardButton("Расписание 👀")
btn_email = KeyboardButton("Email 📨")
btn_kab = KeyboardButton("Кабинеты 🔎")
btn_ned = KeyboardButton("Неделя ❓")
btn_tel = KeyboardButton("Телефон куратора 📱")

nums = int(datetime.datetime.utcnow().isocalendar()[1])
x = datetime.datetime.now()

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_ras, btn_ned, btn_email, btn_kab, btn_tel)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}!", reply_markup=main_menu)


@dp.message_handler()
async def raspisanie(message: types.Message):
    if message.text == "Расписание 👀":
        await bot.send_photo(message.from_user.id, open("ras.png", "rb"))
    elif message.text == "Неделя ❓":
        if (nums % 2) == 0:
            await bot.send_message(message.from_user.id, "Нечетная".format(nums))

        if (nums % 2) != 0:
            await bot.send_message(message.from_user.id, "Четная".format(nums))

    elif message.text == "Email 📨":
        await bot.send_message(message.from_user.id, "n.m.nechaeva@mail.ru - Наталья Мирсаабовна\n"
                                                     "informatics64@yandex.ru - Илья Сергеевич\n"
                                                     "model.1974@mail.ru - обж\n"
                                                     "shlykova-olga11@mail.ru - история, общество\n"
                                                     "darja.staroverova@yandex.ru - ино 1 группа\n"
                                                     "stntiv@mail.ru - ино 2 группа\n"
                                                     "buravchik65rus@yandex.ru - химия, биология")

    elif message.text == "Кабинеты 🔎":
        await bot.send_message(message.from_user.id, "Архитектура аппаратных средств - 404\n"
                                                     "Операционные системы и среды - 410\n"
                                                     "Дискретная математика - 311\n"
                                                     "История - 403\n"
                                                     "Психология общения - 204-М (Второй корпус)\n"
                                                     "Экология - 408\n"
                                                     "Русский - 413\n"
                                                     "Основы алгоритмизации - 305\n"
                                                     "Иностранный язык - 413/312\n"
                                                     "Физра - С.з (Первый этаж)")
    elif message.text == "Телефон куратора 📱":
        await bot.send_message(message.from_user.id, "89648484100 - Наталья Мирсаабовна")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
