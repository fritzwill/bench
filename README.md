# bench
Various tools to help benchmark and compare different workflows, computations, performance

![current picture from ChatGPT on 2/18/2025](img/bench_picture_chatgpt.png)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation
Install `requirements.txt` file into your virtual environment (I use pyenv-virtualenv):
```bash
pyenv virtualenv 3.13.2 bench-3.13.2-venv
pyenv local bench-3.13.2-venv
```
A `.python-version` file will be created with "bench-3.13.2-venv". If configured correctly with pyenv-virtualenv, your env should be auto-activated when navigating into repo and added to shell. If not, activate youre virtual environment:
```bash
pyenv activate bench-3.13.2-venv
```

You should now see "(bench-3.13.2-venv)" prepended before your prompt (example: `(bench-3.13.2-venv) YOUR_PROMPT`)

Finally, install repo dependencies
```bash
pip install -r requirements.txt
```

## Usage
### Example of each method
Run example of each method in `src/`:
```shell
python example-usage
```
Expected output:
```
Bisection method solution: x = 1.5213871002197266
Fixed point solution: x = 4.493409457909262
Newton's method solution: x = 0.00681932148757599
Secant method solution: x = 0.006819324067985225
```

### Benchmark
Run:
```shell
python benchmark.py
```
Expected output:
```
running Secant Method on Easy Function ... done
running Newton's Method on Easy Function ... done
running Bisection Method on Easy Function ... done
running Secant Method on Really Hard Function ... done
running Newton's Method on Really Hard Function ... done
running Bisection Method on Really Hard Function ... done

Method               Function                  Time (s) for 100 runs    
================================================================================
Secant Method        Easy Function             0.00125237               
Newton's Method      Easy Function             0.00042610               
Bisection Method     Easy Function             0.00159225               
Secant Method        Really Hard Function      0.00171304               
Newton's Method      Really Hard Function      0.00122889               
Bisection Method     Really Hard Function      0.00039348
```
