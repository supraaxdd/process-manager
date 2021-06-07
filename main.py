import typer
import psutil
import os

app = typer.Typer()

def get_pid(name):

    pids = []

    for proc in psutil.process_iter():
        if name in proc.name():
            pids.append(proc.pid)

    return pids


def killTasks(pids):
    try:
        for pid in pids:
            os.kill(pid, 9)
            print(f"Killed process {pid}")
    except Exception as error:
        print(error)



@app.command()
def kill(process: str):
    try:
        PIDS = get_pid(process)
        killTasks(PIDS)
        return print(f"Successfully killed all processes with the name: {process}")
    except Exception as err:
        return print(err)

@app.command()
def proclist(process: str = typer.Argument(None)):
    if not process:
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['name', 'pid', 'status'])
                print(pinfo)
            except psutil.NoSuchProcess:
                pass
    else:
        for proc in psutil.process_iter():
            if process in proc.name():
                try:
                    pinfo = proc.as_dict(attrs=['name', 'pid', 'status'])
                    print(pinfo)
                except psutil.NoSuchProcess:
                    pass
                

if __name__ == "__main__":
    app()