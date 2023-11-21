## Namegen Utility

Generates a name and copies it to clipboard. Useful for quickly naming prototypes or scrap files.

For personal use, but if you find this and think it's useful that's cool too. Currently, I use it as a 
bind to my keyboard that takes the clipboard contents and adds a time stamp before. For example:

```sh
namegen -Cc --time %y-%m-%d #Takes the clipboard contents and puts a date timestamp in front. Useful for file archiving.
```

## Installation

Depending on the system, you might need to create a virtual environment (venv). Here's one compatible with the included bash script.

```sh
python -m venv ./.venv # Creates a virtual environment in this repo.
source .venv/bin/activate # Enters the virtual environment, proceed to next steps.
```

On Debian, for example, it will often pester you when you try to run `pip` without being in a virtual environment. If this is the 
case on your system, use the included shell script once the installation process is finished.

Next, install the dependencies.
```sh
pip install -r requirements.txt
```

Lastly, you can install and test using the following command:

```sh
pip install -e . # Installs in editable mode. I haven't configured it to install properly otherwise, but it will work well enough.
namegen --help # Prints the expected help menu.
```

You can either choose to always run namegen in the venv container or you can use my included bash script (`namegen` file at root of git repo) to run with the dependencies from inside the virtual environment.

