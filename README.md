# 🙏 pray
a terminal program that you can add in your PATH which runs commands specified in a file in the same directory.
> prayer refers to a `.prayer` file <br>

## Usage
- [install the program](#installation)
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
> the exe file may be incorrectly flagged as malware as it is not commonly downloaded or [code-signed](https://en.wikipedia.org/wiki/Code_signing) as it requires a lot of money. <br>
incase of any doubts, users can check any file in this repository and build the source themselves just like how non-windows users have to.<br>
- download the executable file from the latest release
- create a folder at a location of your choice
- move the downloaded executable file to that new folder
- ensure that the executable file's filename is `pray` so that `pray` is recognized as a command name in the terminal
- add the new folder's location to your PATH
- restart your terminal and run `pray` to check whether the installation was successful or not. if it was, you will most likely see an error stating that ".prayer is needed". if it was not, you will see something like "pray is not a valid command name" and you most likely messed up the folder paths / adding it to your PATH. recheck or restart the whole process again if required.
- done! now go back to [usage](#usage).


#### Other OS users need to build the program themselves using the following steps:
- requirements: [python](https://www.python.org/), [pip](https://pypi.org/project/pip/)
- install pyinstaller: 
```
pip install pyinstaller
```
- clone this repository, move it anywhere if required, open your favourite terminal and cd into the repository's root folder i.e the one that contains README.md, LICENSE etc.
- run the following command to generate the executable for your OS
```
pyinstaller -F src/main.py
```
- the executable will be generated inside a dist folder that is automatically created by running the previous command
- rename the executable file to `pray.exe`
- add the location of the dist folder in your PATH
- restart your terminal and run `pray` to check whether the installation was successful or not. If it was, you will most likely see an error stating that a prayer is needed. If it was not, you most likely messed up folder paths. recheck or restart if required.
- done! now go back to [usage](#usage).

## Contributing
- the [src/main.py](./src/main.py) file is all there is for now.
- pull requests are welcome.
