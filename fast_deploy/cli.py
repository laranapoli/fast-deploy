import subprocess

from rich.console import Console
from typer import Argument, Option, Typer, prompt

console = Console()
app = Typer()


def check_docker_installed():
    try:
        subprocess.run(
            ['docker', '--version'],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except FileNotFoundError:
        console.print(
            '[bold red]Docker não está instalado. Por favor, instale o Docker para usar esta aplicação.'
        )
        raise SystemExit(1)


@app.command()
def deploy(
    image_name: str = Argument('fastdeploy', help='Nome da imagem Docker'),
    port: int = Argument(8000, help='Porta para expor a API'),
    verbose: bool = Option(
        False, '--verbose', help='Flag para exibir logs do container'
    ),
):
    check_docker_installed()
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
