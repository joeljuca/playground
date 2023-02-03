# Hey, Python!

[![hey-python](https://github.com/joeljuca/playground/actions/workflows/hey-python.yml/badge.svg)](https://github.com/joeljuca/playground/actions/workflows/hey-python.yml)
[![Black Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This is literally my _Hello, World_ in the Python ecosystem. Here I'm mostly concerned about understand Python strengths, its modularization system, techniques, and best practices - as well as playing with it by writing some random and fun code.

## Set up

It uses Python's built-in module [`venv`](https://docs.python.org/3/library/venv.html) and [pip](https://pypi.org/project/pip/) for virtual environments an dependency management, respectively.

### Virtual environment

Create the virtual environment with:

```bash
python3 -m venv .venv
```

Then, activate it with:

```bash
source .venv/bin/activate
```

You can eventually deactivate it (exit the virtual environment) with:

```bash
deactivate
```

**From now on, all commands assume you have the virtual environment currently active in your shell.**

### Dependencies

To install dependencies, run:

```bash
pip3 install -r requirements.txt
```

You should be ready to run it now.

## Run

Run it with:

```
flash --app src/server.py run
```

It should be available in [localhost:5000](https://localhost:5000).

## License

[MIT](license)
