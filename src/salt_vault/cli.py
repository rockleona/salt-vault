import click
from .hash import hash

@click.group()
def cli():
    pass

cli.add_command(hash)
