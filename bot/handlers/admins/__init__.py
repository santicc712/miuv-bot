from . import admin_menu
from aiogram import Dispatcher
from . import broadcast


def setup(dp: Dispatcher):
    for module in (
            admin_menu, broadcast
    ):
        module.setup(dp)
