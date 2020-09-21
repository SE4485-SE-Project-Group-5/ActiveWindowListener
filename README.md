# Developer Onboarding Guide

**Disclaimer**: This project is extremely disorganized and incomplete. Many *many* parts were left unfinished (to see what I mean do a global search for "TODO"). There are duplicate assets scattered among the root directory and in `react-ui`. There are unfinished attempts at an installation process and/or an automation process. The main script is `flair.py`, which took me a while to find out. Several different locations have (differing) lists of (most not deprecated) dependencies for various different platforms. There is no "clean" script and the "build" script is a hacky pseudo-shell script that is meant to be run with Git Bash.

I went through and made attempt to mitigate some of these issues by adding [Poetry](https://python-poetry.org/), a Python dependency management tool and by cleaning up a bunch of the code to the best of my ability.

Here is a revamped step-by-step guide on getting a development environment properly set up for this project:

## Requirements

1. Windows 10
2. [Python 3.7.9](https://www.python.org/downloads/release/python-379/)
   - Add to User Path
   - Add to System Path
   - Ensure `python` command points to Python 3.7.9 (run `get-command python` in PowerShell)
3. [Poetry](https://python-poetry.org/)
4. [Nodejs 14.x.x.x](https://nodejs.org/en/download/current/)
5. [Yarn](https://classic.yarnpkg.com/en/docs/install/#windows-stable)
6. [MongoDB Server 4.4](https://www.mongodb.com/download-center/community)
   - Add to User Path
7. [Graphviz 2.38](https://graphviz.gitlab.io/_pages/Download/Download_windows.html)
   - Add to User Path
   - Add to System Path

For each of these, I used the `winget` CLI to install as opposed to downloading and installing manually from the website, but you can use whatever tool you'd like provided you are able to install the above versions.

If you're not too attached to PyCharm, consider using [VS Code](https://code.visualstudio.com/). It provides a built-in Git GUI, an integrated terminal, IntelliSense for every language relevant to this project, and you can also configure it to automatically activate Poetry.

## Setup


#### Clone this repository with Git

   - Navigate to project parent directory and run `git clone https://github.com/SE4485-SE-Project-Group-5/ActiveWindowListener.git`

#### Install Python dependencies

   - Navigate to project root with `cd ActiveWindowListener`
   - Create Poetry virtualenv with `poetry env use python`
   - Install dependencies with `poetry install`

#### Activate Poetry virtualenv

   - Run `poetry shell` (always make sure this has been done before running any Python scripts)

#### Install npm dependencies

   - Navigate to the UI directory with `cd react-ui`
   - Install dependencies by running `yarn`

#### Navigate back to the project root

   - Run `cd ../`

## Test the Environment

#### Test development environment

Run `python flair.py` to run the application in development mode. This should open the app and present the typical interface once the server starts.

After a couple of seconds, the various processes that are running should show up in the table and the various details of your activity should show up underneath.

Click the button to generate a visual and a PDF should be opened with a graphical view of your activity.

This entire GUI is accessible at `http://localhost:43968/` in your web browser. From there you can use you browser's development tools for the React side of things.

#### Test Build

In Git Bash, run `create_windows_exe.sh`. Ensure application built successfully by running `./dist/flair.exe` and comparing application to that of the development environment.


## Notes

Use the `poetry shell` command to activate Python virtualenv. If you come across any problems first make sure this was done.

The application essentially consists of a Python activity monitor connected with the help of some obscure Python libraries to a [React](https://reactjs.org/) frontend.

`flair.py` is the (unaptly named) main script. Run with python for dev experience `python flair.py`. This does the same thing as running `flair.exe` after a build.

The `flair.exe` and the entire `flair` directory seem to be leftover builds from the previous group. Removing since we can now build all by ourselves :sunglasses:.

The multiple batch scripts seem to be attempts to create an installation process and addition to the list of startup programs. We probably won't ever mess with these as we'll create a separate solution with the `.msi`, but I'll leave for now.

For some godforsaken reason the chart will not update at certain hours according to `flask_blueprints/example_bp.py`. This took me hours to find as I could not understand why half the app wasn't working. We should bring this up with Tom...something like "Are there certain hours the app shouldn't log/present information or can we strip this functionality entirely please?"

There was a ridiculous error with a "Failed to load flair.exe" message or something like that after a build. With extensive research I found it was due to the `pynput` dependency being on "too new" of a version. There was apparently some obscure breaking change, so I downgraded to `v1.6.8` and made a note in the `pyproject.toml` file.

I now understand for the most part how this app is structured (thanks to hours of looking for explanations to the above bugs) so please ask if you have any questions or issues.

## Next Steps for Development

- [x] Add poetry for Python dependency management (specify platform-specific dependencies)
- [x] Replace npm with yarn in `react-ui`
- [ ] Clean up old code (an ongoing process, old code is extremely chaotic and messy with no documentation)
  - [ ] Localize UI code in `react-ui` -- currently everywhere with some duplicates (e.g. `default.png` and `static` folder)
  - [ ] Remove old unused code (things like mac/linux support)
  - [ ] Use poetry scripts for cleaning and building (remove need for hacky `create_windows_exe.sh` "shell" script)
- [ ] Write out installation process
- [ ] Convert pyinstaller build process to cx_Freeze `.msi` build process
- [ ] Automate `.msi` build using GitHub workflow