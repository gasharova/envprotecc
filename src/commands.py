import click
import subprocess
import os

@click.group()
def protecc():
    pass

@protecc.command()
def hello():
    """Example script."""
    click.echo('Hello World!')

@protecc.command()
@click.option("--config-path", default="./config", show_default=True, type=click.Path())
def init(config_path):
    """
    Initializes the project folder with .pysa and taint.config files
    """
    click.echo("Initializing...")
    if not os.path.isdir(config_path):
        os.mkdir(config_path)
    model_path = os.path.join(config_path, "models.pysa")
    if os.path.isfile(model_path):
        click.echo("models.pysa already exists...")
    else:
        with open(model_path, 'w') as fp:
            pass
        click.echo("Created models.pysa file...")
    taint_config_path = os.path.join(config_path, 'taint.config')
    if os.path.isfile(taint_config_path):
        click.echo("taint.config already exists...")
    else:
        with open(taint_config_path, 'w') as fp:
            pass
        click.echo("Create taint.config file...")
    click.echo(f"Configuration files generated at '{config_path}'")
