import os
import shutil

from invoke import task


@task
def clean(c):
    c.run("pyclean .")


@task
def start(c):
    c.run("python flair.py")


@task
def build(c):
    # Build React app
    with c.cd("react-ui"):
        c.run("yarn build")

    # Clean previous build
    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("templates", ignore_errors=True)
    shutil.rmtree("static", ignore_errors=True)

    # Transfer assets
    os.mkdir("templates")
    shutil.copy("react-ui/build/index.html", "templates/index.html")

    shutil.copytree("react-ui/build/static", "static")
    os.mkdir("static/icons")
    shutil.copy("default.png", "static/icons")

    # Build exe with Pyinstaller
    c.run("python -O -m PyInstaller -w --clean --add-data \"templates;templates\"  --add-data \"static;static\" --add-data \"mongo;mongo\" -y flair.py")

    # Remove .spec file
    os.remove("flair.spec")
