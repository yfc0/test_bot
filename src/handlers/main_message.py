from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter

from states.states import MainState

from chatgpt import conversation

router = Router()

@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer("Привет, я твой личный консультант по продажи авто!")
    await state.set_state(MainState.main)


@router.message(F.text, StateFilter(MainState.main))
async def answers(message: Message, state: FSMContext):
    print(conversation(message.text))


@router.message(Command("help"))
async def help(message: Message, state: FSMContext):
    await message.answer(text='Инструкция:')
