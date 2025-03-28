import click
import hashlib


@click.command()
@click.option("--method", default="sha1", help="select the hashing method")
@click.argument("text")
def hash(method, text):
    if method == "sha1":
        hasher = hashlib.sha1(text.encode())
    elif method == "sha256":
        hasher = hashlib.sha256(text.encode())
    elif method == "sha512":
        hasher = hashlib.sha512(text.encode())
        
    click.echo(hasher.hexdigest())
    pass
