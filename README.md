<h1 align="center">
  PredictMe
</h1>

Setup R
-------

Point to R in .bashrc

```python
export R_HOME="/Library/Frameworks/R.framework/Resources"
```

Configuration used to run the project (myMac):
- Python version: 3.7.4
- R version: 3.6.2 (https://cran.r-project.org/)
- rpy2 version: 3.1.0

Running PredictMe
-----------------

1. Start celery

```python
celery -A app worker -l info
```
