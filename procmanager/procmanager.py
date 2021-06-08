import psutil
import os
import typer

class ProcManager:

    def __init__(self, name=None) -> None:
        self.name = name

    def get_pid(self):

        pids = []

        for proc in psutil.process_iter():
            if self.name in proc.name():
                pids.append(proc.pid)

        self.pids = pids

    def killTasks(self):
        try:
            for pid in self.pids:
                os.kill(pid, 9)
                print(f"Killed process {pid}")
            return print(f"Successfully killed all processes with the name: {self.name}")
        except Exception as error:
            print(error)

    def proclist(self):
        if not self.name:
            for proc in psutil.process_iter():
                try:
                    pinfo = proc.as_dict(attrs=['name', 'pid', 'status'])
                    print(pinfo)
                except psutil.NoSuchProcess:
                    pass
        else:
            for proc in psutil.process_iter():
                if self.name in proc.name():
                    try:
                        pinfo = proc.as_dict(attrs=['name', 'pid', 'status'])
                        print(pinfo)
                    except psutil.NoSuchProcess:
                        pass
