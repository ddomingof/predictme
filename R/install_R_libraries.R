if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install(version = "3.10")

# Install packages required to run PredictMe
install.packages("h2o")
install.packages("randomForest")
install.packages("glmnet")
install.packages("gbm")
install.packages("bnlearn")
install.packages("ggplot2")
install.packages("CORElearn")
install.packages("dplyr")
