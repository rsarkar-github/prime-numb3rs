# prime-numb3rs
Fun project containing various prime number bounds.

## Installation of dependencies
```
> Python 3.13

conda install anaconda::numpy
conda install anaconda::sympy
conda install conda-forge::numba
conda install anaconda::tqdm
conda install conda-forge::matplotlib
```

### Additionally to generate documentation files
```
conda install anaconda::sphinx
conda install conda-forge::sphinx_rtd_theme
```

## Running files in **scripts** directory
- First make sure that you are inside the root level directory of this project.
- Run `python -m scripts.scriptname`.

## Building documentation help
- First cd into `docs/`.
- Execute the command `make html`.
- Using any browser, open `docs/build/html/index.html`.