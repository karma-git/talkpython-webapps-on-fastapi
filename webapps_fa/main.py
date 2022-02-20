from pathlib import Path

import fastapi
import uvicorn

import fastapi_chameleon

from webapps_fa.views import (
    account,
    home,
    packages
)

app = fastapi.FastAPI()

dev_mode = True

BASE_DIR = Path(__file__).resolve().parent
template_folder = str(BASE_DIR / 'templates')
fastapi_chameleon.global_init(template_folder, auto_reload=dev_mode)


def main():
    configure()
    uvicorn.run(app, host='127.0.0.1', port=8000, reload=True)


def configure():
    configure_templates()
    configure_routes()


def configure_templates():
    fastapi_chameleon.global_init('templates')


def configure_routes():
    app.include_router(account.router)
    app.include_router(home.router)
    app.include_router(packages.router)


if __name__ == '__main__':
    main()
else:
    configure()
