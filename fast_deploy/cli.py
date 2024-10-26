import subprocess

from rich.console import Console
from typer import Argument, Option, Typer, prompt

console = Console()
app = Typer()


@app.command()
def serve(
    image_name: str = Argument('fastdeploy', help='Nome da imagem Docker'),
    port: int = Argument(8000, help='Porta para expor a API'),
    verbose: bool = Option(
        False, '--verbose', help='Flag para exibir logs do container'
    ),
):

    import os

    console.print('Buildando Docker container...')
    build_command = ['docker', 'build', '-t', image_name, '.']
    if verbose:
        subprocess.run(build_command, check=True)
    else:
        subprocess.run(
            build_command,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    console.print('Startando Docker container.')
    if verbose:
        run_command = ['docker', 'run', '-p', f'{port}:8000', image_name]
    else:
        run_command = ['docker', 'run', '-d', '-p', f'{port}:8000', image_name]
    subprocess.run(run_command, check=True)


if __name__ == '__main__':
    app()
