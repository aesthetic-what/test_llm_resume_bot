from aiogram import Bot, Router, F
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from file_reader import reader



from config import Config
from keyboards import job_keyboard_test

config = Config()


router = Router()
bot = Bot(config.tg_token)

class DownloadResume(StatesGroup):
    document = State()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, это бот для поиска работы")


@router.message(Command("resume"))
async def upload_resume(message: Message, state: FSMContext):
    await message.answer("Загрузите ваше резюме, а я прочту его")
    await state.set_state(DownloadResume.document)



@router.message(F.document)
async def download_resume(message: Message):
    file_id = message.document.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    file_type = file_path.split(".")[-1]
    if file_type != "pdf" and file_type != "docx":
        await message.answer("Извините, но я не поддерживаю файлы такого формата")
        return
    user_resume_name = f"resume_{message.chat.id}.{file_type}"
    await bot.download_file(file_path, destination=user_resume_name)
    text = await reader(file_path=user_resume_name, file_type=file_type)
    await message.answer(text)


@router.message(Command("search"))
async def search_job(message: Message):
    await message.answer("Исходя из вашего резюме, вам подходят такие вакансии",
                         reply_markup=job_keyboard_test())

