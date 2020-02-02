<h1 align="center">
  PredictMe
</h1>

## Configuration

Configuration used to run the project:
- Python version: 3.7.4
- R version: 3.6.2 (https://cran.r-project.org/)
- rpy2 version: 3.1.0

### Setup R

1. Point to R in .bashrc (example)

```python
export R_HOME="/Library/Frameworks/R.framework/Resources"
```

2. Install R libraries required using the script located inside the R directory

```python
R < R/install_R_libraries.R --no-save  
```

## Run PredictMe

- Install Python requirements

``python3 -m pip install -r requirements.txt``

**Note that you might have to run "python" instead of "python3" in your computer.
The only reason why I use python3 is to ensure I use the python3 version and not
the python3 one.**

- Run locally

``python3 manage.py runserver`` (Run locally the web application on http://127.0.0.1:8000/)
