import subprocess

from rich.console import Console
from typer import Argument, Typer

console = Console()
app = Typer()


@app.command()
def serve():
    import os

    console.print('Buildando Docker container...')
    build_command = ['docker', 'build', '-t', 'fastdeploy', '.']
    subprocess.run(build_command, check=True)

    console.print('Startando Docker container')
    run_command = ['docker', 'run', '-p', '8000:8000', 'fastdeploy']
    subprocess.run(run_command, check=True)


if __name__ == '__main__':
    app()
