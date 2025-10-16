# 🙏 pray
a terminal program that you can add in your PATH which runs commands specified in a file in the same directory.
> prayer refers to a `.prayer` file <br>

## Usage
- [Install the program](#installation)
- create a prayer in your project's root directory
- if you do not want to see any debug logs from this program, the top line of your prayer should be "nolog".
- every command is specified as `command name: command` in subsequent lines.
- the default command that runs when no command name is specific is named `default`.
- commands can be executed by running the following command in the terminal with the working directory set as the one which contains the prayer.
```
pray <command-name> arg1 arg2 ...
```
- command-name is optional and set to "default" by default.
- arg1, arg2.... are optional too, and are simply appended to the command specified by the command name.
- command-name can be set to "default" to specify args for the default command.


## Prayer examples
#### prayer for running your python script
- running the command `pray` in the directory where this prayer is saved would result in the execution of `python script.py` whereas running the command `pray script2` would result in the execution of `python script2.py`.
```
default: python script.py
script2: python script2.py
```

#### prayer for running your `__main__.py` file with no debug logs (if any) from the pray program.
```
nolog
default: python __main__.py
```

#### prayer for simply renaming the mkdir command to pray
```
default: mkdir
```

# Installation

> how to add stuff to PATH in 
[windows](https://stackoverflow.com/questions/9546324/adding-a-directory-to-the-path-environment-variable-in-windows), 
[macos](https://stackoverflow.com/questions/22465332/setting-path-environment-variable-in-macos-permanently),
[linux](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)

Prebuilt binaries are available for windows only.<br>
#### Windows users:
- download the executable file from the latest release
- create a folder at a location of their choice
- move the downloaded executable file to that new folder
- ensure that the executable file's filename is `pray.exe`
- add the new folder's location to your PATH
- restart your terminal and run `pray` to check whether the installation was successful or not. If it was, you will most likely see an error stating that a prayer is needed. If it was not, you most likely messed up folder paths. recheck or restart if required.
- Done! now go back to [usage](#usage).


#### Other OS users need to build the program themselves using the following steps:
- Requirements: [python](https://www.python.org/), [pip](https://pypi.org/project/pip/)
- Install pyinstaller: 
```
pip install pyinstaller
```
- clone this repository, move it to somewhere if needed, open your favourite terminal and cd into the repository's root folder i.e the one that contains README.md, LICENSE etc.
- run the following command to generate the executable for your OS
```
pyinstaller -F src/main.py
```
- the executable will be generated inside a dist folder that is automatically created by running the previous command
- rename the executable file to `pray.exe`
- add the location of the dist folder in your PATH
- restart your terminal and run `pray` to check whether the installation was successful or not. If it was, you will most likely see an error stating that a prayer is needed. If it was not, you most likely messed up folder paths. recheck or restart if required.
- Done! now go back to [usage](#usage).

## Contributing
- The [src/main.py](./src/main.py) file is all there is for now.
- Pull requests are welcome.