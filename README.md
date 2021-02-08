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
- [What's next for EnvProtecc](#whats-next-for-envprotecc)

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

### Init command

```bash
    $ envprotecc init
```

### Analyze command
Runs the static analysis.

```bash
    $ envprotecc analyze
```

## Inspiration
We wanted to create the ultimate tool for finding environment variable leakages - and thats how EnvProtecc was born.  
Using a few modest, but useful underlying packages, EnvProtecc is the only dependency you need for env security.

## What it does
EnvProtecc is a Python package which uses dataflow analysis tools to check for leakages of any of the environment variables. In case leakages are found, they're displayed at runtime after running the `analyze` command.

## How we built it
EnvProtecc is build on top of `pysa`, a part of the `pyre-check` project package (see more about `pysa` [here](https://pyre-check.org/docs/pysa-running)).  
Additionally, since it's a CLI tool, we also make use of `click` (see more [here](https://click.palletsprojects.com/en/7.x/)).

## Challenges we ran into
At integration time, we stumbled upon an undocumented `pyre-check` exception which took roughly 48 hours off our time. (Turned out the fix was elementary, but we were shooting in the dark before getting there).  
We wrote an issue on Github about it ([link](https://github.com/facebook/pyre-check/issues/378)), but the repository seems to be not so well-maintained as there are many open issues without any follow-up discussion at all, including 3 issues which had the same exception code as this one.

## Accomplishments that we're proud of
#### 1. Being able to finish the project and clear the bugs even with the deadline approaching
#### 2. Fully using the good Github practices (PRs, reviews, documentation, Kanban table, tags)
#### 3. Already having 5 stars on github

## What we learned
- Dataflow and usage of `pyre-check`'s `pysa` for static analysis
- How to use `click`, the python CLI tool
- How to submit devpost projects :)

## What's next for EnvProtecc
EnvProtecc is published on PyPi and is ready for use. It has no security issues and doesn't need any additional documentation apart from this one.  
It's also public on GitHub. Anyone can contribute following our contribution rules and guidelines [rules and guidelines](CONTRIBUTING.md).
