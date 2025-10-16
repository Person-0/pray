import sys
import os

nolog = False
def log(*e):
    if not nolog:
        print("pray:", *e)

try:
    args = sys.argv[1:]
    cmdname = "default"
    cmdargs = ""
    i = 0
    while len(args) > 0:
        item = args[0]
        args = args[1:]
        if i == 0:
            cmdname = item
        else:
            cmdargs += " " + item
        i += 1

    didrun = False
    with open(".prayer", "r") as file:
        lines = file.readlines()
        line_num = 0
        for line in lines:
            line_num += 1
            if line == "nolog":
                nolog = True
            else:
                record = line.split(":", maxsplit=1)
                if len(record) == 2:
                    cmd = record[1].lstrip()
                    if len(cmd) > 0:
                        if len(cmd) > 0: 
                            if cmdname == record[0]:
                                didrun = True
                                os.system(cmd + cmdargs)
                                break
                        else:
                            log(".prayer contains invalid command on line ", line_num)
                    else:
                        log(".prayer contains invalid command name on line ", line_num)
                else:
                    log(".prayer contains invalid record on line ", line_num)

    if not didrun:
        log(f"command with name \"{cmdname}\" not found")

except FileNotFoundError:
    log("requires a .prayer")
except Exception as error:
    log("error: ", error)