# MLflow and FastAPI Integration

This repository demonstrates a workflow for building, tracking, and deploying machine learning models using MLflow, FastAPI, Docker, and Flask. Follow the steps below to set up, train models, create REST APIs, and consume them using Postman.



## 1. Tracking Model Performance

In this section, I implemented preprocessing for the data and trained multiple machine learning models, including logistic regression, decision tree, SVM, random forest, and LGBM. After thorough evaluation, the random forest model emerged as the best-performing model based on predefined criteria.


## 4. Saving Best Model and Preprocessing Transformations<a name="random forest"></a>

Save the best model in ONNX format and its dedicated preprocessing transformations using the Transformers API in pickle format.

## 5. Creating a FastAPI REST API

![Machine Learning](fastAPI1.jpg)
<img width="602" alt="image3" src="https://github.com/SalmaTADLAOUI/Cloud-Native-AI-ML/assets/76519142/b7676888-6210-4fe1-8915-409113aa4955">

![Machine Learning](fastAPI2.jpg)

## 6. Packaging Model as a Docker Container

I created a DockerFile to create a container in docker and requirements.txt contains the require packages
![Machine Learning](docker1.jpg)
![Machine Learning](docker2.jpg)
## 7. Consuming APIs with Postman

Test the deployed API endpoints using Postman. Send requests and verify the responses to ensure the proper functioning of the deployed model.
![Machine Learning](postman.jpg)

## 8. Creating a Flask Application to consume the api
![Machine Learning](flask.jpg)
