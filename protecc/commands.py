import click
import subprocess
import os
import json

taint_content = {
    "sources": [
        {
            "name": "Secret",
            "comment": "Environment secrets"
        }
    ],
    "sinks": [
        {
            "name": "Endpoint",
            "comment": "Registered API Endpoints"
        }
    ],
    "rules": [
        {
          "name": "Possible env var leakage",
          "code": 69,
          "sources": [ "Secret" ],
          "sinks": [ "Endpoint" ],
          "message_format": "Environment variables and data may leak from API Endpoints"
        }
    ]
}

model_content = """
protecc.vortex.Vortex.SECRETS: TaintSource[Secret]
protecc.vortex.Vortex.endpoints: TaintSink[Endpoint]
"""

@click.group()
def protecc():
    pass

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
    with open(model_path, 'w') as fp:
        fp.write(model_content)
    click.echo("Created models.pysa file...")
    taint_config_path = os.path.join(config_path, 'taint.config')
    with open(taint_config_path, 'w') as fp:
        content = json.dumps(taint_content, indent=2)
        fp.write(content)
    click.echo("Create taint.config file...")
    click.echo(f"Configuration files generated at '{config_path}'")
