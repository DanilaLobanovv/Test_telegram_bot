from telegram.ext import Application
import importlib
from pathlib import Path

def register_handlers(application: Application):
    # Автоматически импортируем все модули в папке handlers
    for module_file in Path(__file__).parent.glob("*.py"):
        if module_file.name not in ["__init__.py", "base_handler.py"]:
            module_name = module_file.stem
            module = importlib.import_module(f"handlers.{module_name}")
            if hasattr(module, "register"):
                module.register(application)