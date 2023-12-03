## Namegen Utility

Generates a name and copies it to clipboard. Useful for quickly naming prototypes or scrap files.

For personal use, but if you find this and think it's useful that's cool too. Currently, I use it as a 
bind to my keyboard that takes the clipboard contents and adds a time stamp before. For example:

```sh
namegen -Cc --time %y-%m-%d #Takes the clipboard contents and puts a date timestamp in front. Useful for file archiving.
```

## Installation

This is highly dependent on the system you're using, but I would recommend installing any python application from source with `pipx`.

On Debian, for example, you would run the following in the root of this repository.

```sh
sudo apt install pipx
pipx install .
```

