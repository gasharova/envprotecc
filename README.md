# Protecc
![](banner_last.png)

# Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Inspiration](#inspiration)
- [What it does](#what-it-does)
- [How we built it](#how-we-built-it)
- [Challenges we ran into](#challenges-we-ran-into)
- [Accomplishments that we're proud of](#accomplishments-that-were-proud-of)
- [What's next for protecc](#whats-next-for-protecc)

## Installation

### Installing the repository for contribution purposes
Please refer to [our CONTRIBUTING.md file](CONTRIBUTING.md).

### Installing the package

Our package is publicly available on PyPi.
To install using `pip`, run the command:

```bash
    $ pip install envprotecc
```

## Usage

#### Init command

```bash
    $ envprotecc init
```

#### Analyze command
Runs the static analysis.

```bash
    $ envprotecc analyze
```

## Inspiration
We wanted to create the ultimate tool for finding environment variable leakages - and thats how EnvProtecc was born.  
Using a few modest, but useful underlying packages, EnvProtecc is the only dependency you need for env security.

## What it does
EnvProtecc is a Python tool which uses dataflow analysis tools to check for leakages of any of the environment variables. In case leakages are found, they're displayed at runtime after running the `analyze` command.

## How we built it
EnvProtecc is build on `pysa`, a part of the `pyre-check` project package (see more about `pysa` [here](https://pyre-check.org/docs/pysa-running)).  
Additionally, since it's a CLI tool, we also make use of `click` (see more [here](https://click.palletsprojects.com/en/7.x/)).

## Challenges we ran into

## Accomplishments that we're proud of

## What we learned

## What's next for protecc
