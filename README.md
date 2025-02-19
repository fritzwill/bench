# bench
Various tools to help benchmark and compare different workflows, computations, performance

![current picture from ChatGPT on 2/18/2025](img/bench_picture_chatgpt.png)

## Table of Contents
- [Installation](#installation)

## Installation
Install `requirements.txt` file into your virtual environment (I use pyenv-virtualenv):
```bash
$ pyenv virtualenv 3.13.2 bench-3.13.2-venv
$ pyenv local bench-3.13.2-venv
```
A `.python-version` file will be created with "bench-3.13.2-venv". If configured correctly with pyenv-virtualenv, your env should be auto-activated when navigating into repo and added to shell. If not, activaate youre virtual environment:
```bash
$ pyenv activate bench-3.13.2-venv
```

Finally, install repo dependencies
```bash
(bench-3.13.2-venv) $ pip install -r requirements.txt
```