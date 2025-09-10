import os
import requests
from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = os.getenv("8115154712:AAHPTQk0qleGeNoGVOLgK6-9memRwHjvjSE")  # из переменных окружения Render
HF_TOKEN = os.getenv("HF_TOKEN")
MODEL = "mistralai/Mistral-7B-Instruct-v0.2"  # модель HF

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def ask_hf(prompt):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt}
    url = f"https://api-inference.huggingface.co/models/{MODEL}"
    r = requests.post(url, headers=headers, json=payload)
    try:
        return r.json()[0]["generated_text"]
    except Exception:
        return "⚠️ Ошибка при обращении к модели."

@dp.message_handler()
async def reply(message: types.Message):
    answer = ask_hf(message.text)
    await message.answer(answer)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
