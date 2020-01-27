if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install(version = "3.10")

# Install packages required to run PredictMe
install.packages("https://cran.r-project.org/src/contrib/Archive/h2o/h2o_3.26.0.2.tar.gz", repo=NULL, type="source")
install.packages("randomForest")
install.packages("glmnet")
install.packages("gbm")
install.packages("bnlearn")
install.packages("ggplot2")
install.packages("CORElearn")
install.packages("dplyr")
