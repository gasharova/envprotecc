import click
import subprocess
import os
import json
import shutil

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
protecc.vortex.Vortex.SECRETS: TaintSource[Secret] = ...
def dict.__getitem__(self: TaintInTaintOut[LocalReturn], k): ...
def dict.get(self: TaintInTaintOut[LocalReturn], key, default): ...
def protecc.vortex.Vortex.taint_arg(self, arg: TaintSink[Endpoint]): ...
def protecc.vortex.Vortex.taint_arg(self, arg: TaintInTaintOut[LocalReturn]): ...
"""

stubs_content = """
from typing import Any, Dict, Set

class Vortex:
    def __init__(self): ...
    SECRETS: Dict[Any, Any] = ...
    endpoints: Set[Any] = ...

    def get_yml(self, yml_path): ...
    def get_env(self): ...
    def register_endpoint(self, func): ...
    def taint_arg(self, arg): ...
"""

@click.group()
def protecc():
    pass

@protecc.command()
@click.option("--config-path", default=".", show_default=True, type=click.Path())
def init(config_path):
    """
    Initializes the project folder with .pysa and taint.config files
    """
    click.echo("Initializing...")
    os.system("pyre init")
    pyre_config = None
    with open('.pyre_configuration', 'r') as fp:
        pyre_config = json.load(fp)
        pyre_config["search_path"] = os.path.join(config_path, "stubs")
        pyre_config["taint_models_path"] = config_path
    if os.path.isfile('.pyre_configuration'):
        os.remove('.pyre_configuration')
    with open('.pyre_configuration', "w") as fp:
        fp.write(json.dumps(pyre_config))
    if not os.path.isdir(config_path):
        os.mkdir(config_path)
    stubs_path = os.path.join(config_path, "stubs")
    if os.path.isdir(stubs_path):
        shutil.rmtree(stubs_path)
    os.mkdir(stubs_path)
    os.mkdir(os.path.join(stubs_path, "protecc"))
    with open(os.path.join(stubs_path, "protecc", "vortex.pyi"), "w") as fp:
        fp.write(stubs_content)
    click.echo("Created stubs directory...")
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

@protecc.command()
def analyze():
    os.system("pyre analyze")
