from procmanager import ProcManager
from typing import Optional
import typer

app = typer.Typer()

@app.command("kill")
def execKill(process: str = typer.Argument(...)):
    proc = ProcManager(process)
    proc.get_pid()
    proc.killTasks()

@app.command("proclist")
def execProcList(process: Optional[str] = typer.Argument(None)):
    proc = ProcManager(process)
    proc.proclist()
                

if __name__ == "__main__":
    app()