import os
import shutil
import tempfile

import wget
from invoke import task

TEMP = tempfile.gettempdir()


def remove(path: str):
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.isfile(path):
        os.remove(path)


def copy(from_path: str, to_path: str):
    if os.path.isdir(from_path):
        shutil.copytree(from_path, to_path)
    elif os.path.isfile(from_path):
        shutil.copy(from_path, to_path)


def mkdir(path: str):
    os.makedirs(path)


@task
def clean(c, build=False, lib=False, all=False):
    c.run("pyclean .")

    if all or build:
        remove("build")
        remove("templates")
        remove("static")
        remove("flair.spec")
        remove("dist")

    if all or lib:
        remove("lib")


@task
def start(c):
    c.run("python flair.py")


@task
def build(c):
    # Clean previous build
    clean(c, build=True)

    # Build React app
    with c.cd("react-ui"):
        c.run("yarn build")

    # Transfer assets
    mkdir("templates")
    copy("react-ui/build/index.html", "templates/index.html")
    copy("react-ui/build/static", "static")
    mkdir("static/icons")
    copy("default.png", "static/icons")

    # Build exe with Pyinstaller
    c.run("pyi-makespec -w --add-data \"templates;templates\" --add-data \"static;static\" --add-data \"mongo;mongo\" flair.py")
    c.run("python -O -m PyInstaller --clean --distpath \"lib\" -y flair.py")


@task
def package(c):
    # Build
    if not os.path.exists("lib/flair"):
        build(c)

    if not os.path.exists("lib/mongodb-windows-x86_64-4.4.0-signed.msi"):
        wget.download(
            "https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-4.4.0-signed.msi",
            out="lib/mongodb-windows-x86_64-4.4.0-signed.msi"
        )

    if not os.path.exists("lib/graphviz-2.38.msi"):
        wget.download(
            "https://graphviz.gitlab.io/_pages/Download/windows/graphviz-2.38.msi",
            out="lib/graphviz-2.38.msi"
        )

    # Get version number
    version = c.run("poetry version -s").stdout.rstrip()

    # Package with Inno Setup
    c.run(f'iscc /DMyAppVersion="{version}" package.iss')


@task
def release(c):
    # Get version number
    version = c.run("poetry version -s").stdout.rstrip()

    # Upload release with GitHub CLI tool
    c.run(
        f'gh release create v{version} dist/ActiveWindowListener-{version}-setup.exe -t "Active Window Listener v{version}" -n "" -p'
    )
