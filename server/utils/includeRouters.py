import importlib
import os
from fastapi import FastAPI

def include_all_routers(app: FastAPI, router_dir: str):
    for file in os.listdir(router_dir):
        if file.endswith(".py") and file != "__init__.py":
            module_name = file[:-3]
            module = importlib.import_module(f"{router_dir}.{module_name}")
            if hasattr(module, 'router'):
                app.include_router(module.router)
