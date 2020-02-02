# -*- coding: utf-8 -*-

"""R script wrapped through r2py."""

import rpy2.robjects as ro
from rpy2.robjects import globalenv
from rpy2.robjects import pandas2ri


def run_r(user_df, **kwargs):
    """Run R Script."""
    # Activate additional conversions for Pandas
    pandas2ri.activate()

    # Store each argument in kwargs in the R environment
    for variable, value in kwargs.items():
        globalenv[variable] = value

    # Pass the dataframe to the R argument
    globalenv['userSNPs'] = user_df

    # Run code
    return ro.r(
        '''
        library(h2o)
        library(dplyr)

        h2o.init()

        ####################################################################################
        ####### Prepare input file for the prediction of the user data based on our trained autoencoder model ######
        ####################################################################################

        # load SNPs for each Meachnisms
        load(subgraph_15_rdata)

        #load User data
        # userSNPs <- read.csv(USER_FILE, row.names = 1, stringsAsFactors=FALSE)
        # userSNPs <- as.data.frame(t(userSNPs), stringsAsFactors = FALSE)

        # converting user snps data into mechanisms*patients*SNPs matrices
        snp_mat = list()
        k = 1
        for (i in subgraph15.snps){
          snp_mat[[k]] = select(userSNPs, i)
          k = k + 1
        }

        names(snp_mat) <- names(subgraph15.snps)

        ####################################################################################
        ######## Predict Mechanism Scores for the user data with our autoencoder model ######
        ####################################################################################

        # load our autoenocder models (#15) trained with AD-PD data
        modelnames <-list.files(path = autoencoder)
        models = lapply(paste0(autoencoder,"/", modelnames), h2o.loadModel)

        # load user data into h2o environment
        user_data <- snp_mat
        user_snps <- sapply(1:length(user_data), function(x) as.h2o(user_data[[x]]))

        # create an empty list to hold predicted mechanisms score
        predicted_user_matrix = list()

        # predict mechanism socres for user data
        for(i in 1:length(models)){
          if (length(models[[i]]@parameters[["hidden"]]) == 1) {
            predicted_user_matrix[[i]] = as.data.frame(h2o.deepfeatures(models[[i]], user_snps[[i]], 1))
          } else if (length(models[[i]]@parameters[["hidden"]]) == 2) {
            predicted_user_matrix[[i]] = as.data.frame(h2o.deepfeatures(models[[i]], user_snps[[i]], 2))
          } else if (length(models[[i]]@parameters[["hidden"]]) == 3) {
            predicted_user_matrix[[i]] = as.data.frame(h2o.deepfeatures(models[[i]], user_snps[[i]], 3))
          }
        }

        # convert it to data frame (Patients*Mechanism scores)
        predicted_user_matrix = do.call(cbind,predicted_user_matrix)

        names(predicted_user_matrix) <- names(user_data) #change column names to Mechanism names
        rownames(predicted_user_matrix) <- rownames(user_data[[1]]) # change rownames to patient IDs

        ####################################################################################
        ###### Predict Cluster assignments for the user data with our autoencoder model #######
        ####################################################################################

        ### Start up a 1-node H2O server on the local machine, and allow it to use all CPU cores and up to 6GB of memory:
        h2o.init(nthreads=-1, min_mem_size="6G")

        ### Import autoencoder data set #subgraph15
        load(autoencoder_trainer_matrix)
        main_data <- data.frame(autoen)

        #### read the cluster assignments of each patients
        load(trained_patient_clusters)
        rownames(clusters) <- clusters[,1]
        clusters[,1] <- NULL


        ##### merge cluster assignment to the dataset
        fin_data <- merge(clusters,main_data,by="row.names")
        fin_data$clusters <- as.factor(fin_data$clusters)
        rownames(fin_data) = fin_data$Row.names
        fin_data <- fin_data[,-1]
        fullD <- as.h2o(fin_data) # get complete data set into h2o frame for cross validation approach

        ##### Training Classifier ######

        y = "clusters" # response variable
        #x = names(trainData)
        x = names(fullD)
        x = x[-which(x==y)] # predictor variables

        ### Train Model
        snpModel = h2o.glm(
            training_frame = fullD,
           #training_frame = trainD, # keep it commented while using cross validation
           #validation_frame = validD, # keep it commented while using cross validation
           x = x,
           y = y,
           nfolds = 10,
           family='multinomial',
           solver='L_BFGS',
           lambda_search=TRUE
           )

        testh2o <- as.h2o(predicted_user_matrix)

        ### prediction on test data set
        prediction = h2o.predict(snpModel, newdata=testh2o)

        predicted.cl = as.data.frame(prediction$predict)
        names(predicted.cl) <- "clusters"
        predicted.cl$clusters <- as.integer(as.character(gsub("Cluster_", "", predicted.cl$clusters)))

        # merge predicted clusters to test data
        # so all patients in test data set get a cluster assignment based on their mechanism profile (predictro variables)
        predicted_cl.testdata <- cbind(predicted.cl,predicted_user_matrix)
        '''
    )
