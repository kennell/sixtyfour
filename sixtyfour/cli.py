import click
import sys
import base64


@click.command()
@click.option('--file', '-f', type=click.File('rb'))
def main(file):
    isatty = sys.stdin.isatty()

    if not isatty and file:
        raise click.ClickException('Can not feed from stdin and file at the same time')

    if not isatty:
        stdin = click.get_binary_stream('stdin').read().strip()
        click.echo(
            base64.b64encode(stdin).decode('utf-8')
        )

    if file:
        click.echo(
            base64.b64encode(file.read()).decode('utf-8')
        )
