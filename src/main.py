import sys
import os

nolog = False
def log(*e):
    if not nolog:
        print("\n" + "pray:", *e, "\n")

run_status = 0
run_statuses = {
    "start": 0,
    "success": 1,
    "path_parse_error": 2,
    "prayer_not_found": 3,
    "parse_error": 4
}

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

    curPath = os.getcwd()
    if "/" in curPath:
        curPath = curPath.split("/")
    elif "\\" in curPath:
        curPath = curPath.split("\\")
    else:
        run_status = run_statuses["path_parse_error"]
        curPath = []

    while len(curPath) > 0:
        try:
            prayer_path = "/".join(curPath) + "/.prayer"
            with open(prayer_path, "r") as file:
                lines = file.readlines()
                line_num = 0
                for line in lines:
                    line_num += 1
                    if line == "nolog":
                        nolog = True
                    elif line.startswith("#"):
                        pass
                    else:
                        record = line.split(":", maxsplit=1)
                        if not (len(record) == 2):
                            log(".prayer contains invalid record on line ", line_num)
                            run_status = run_statuses["parse_error"]
                            break

                        cmd = record[1].lstrip()
                        if len(cmd) < 1:
                            log(".prayer contains invalid command on line ", line_num)
                            run_status = run_statuses["parse_error"]
                            break

                        if cmdname == record[0]:
                            curPath = []
                            cmd_built = cmd + cmdargs
                            log("running command:", cmd_built)
                            os.system(cmd_built)
                            run_status = run_statuses["success"]
                            break

        except FileNotFoundError:
            run_status = run_statuses["prayer_not_found"]

        except Exception as e:
            log(e)
            break

        # curPath can be an empty list
        if len(curPath) > 0:
            curPath.pop()

    if not run_status == run_statuses["success"]:
        status_text = "?"
        for k in run_statuses:
            if run_statuses[k] == run_status:
                status_text = k
                break
        log("error:", status_text)

except Exception as error:
    log("exception raised:", error)