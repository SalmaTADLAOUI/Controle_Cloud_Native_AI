# MLflow and FastAPI Integration

This repository demonstrates a workflow for building, tracking, and deploying machine learning models using MLflow, FastAPI, Docker, and Flask. Follow the steps below to set up, train models, create REST APIs, and consume them using Postman.



## 1. Tracking Model Performance

In this section, I implemented preprocessing for the data and trained multiple machine learning models, including logistic regression, decision tree, SVM, random forest, and LGBM. After thorough evaluation, the random forest model emerged as the best-performing model based on predefined criteria.


## 4. Saving Best Model and Preprocessing Transformations<a name="random forest"></a>

Save the best model in ONNX format and its dedicated preprocessing transformations using the Transformers API in pickle format.

## 5. Creating a FastAPI REST API

<img width="325" alt="fastAPI1" src="https://github.com/SalmaTADLAOUI/Controle_Cloud_Native_AI/assets/76519142/2db3be15-e881-417e-b623-ee377b20655b">
<img width="275" alt="fastAPI2" src="https://github.com/SalmaTADLAOUI/Controle_Cloud_Native_AI/assets/76519142/9f623ba3-a151-45ff-9931-8f0ad528eada">


## 6. Packaging Model as a Docker Container

I created a DockerFile to create a container in docker and requirements.txt contains the require packages
<img width="635" alt="docker1" src="https://github.com/SalmaTADLAOUI/Controle_Cloud_Native_AI/assets/76519142/f66e48e8-b1b3-46e0-8a58-299bd24cb531">
<img width="728" alt="docker2" src="https://github.com/SalmaTADLAOUI/Controle_Cloud_Native_AI/assets/76519142/8eb7019d-fccb-46ac-9c67-57cb7408050f">


## 7. Consuming APIs with Postman

Test the deployed API endpoints using Postman. Send requests and verify the responses to ensure the proper functioning of the deployed model.
<img width="623" alt="postman" src="https://github.com/SalmaTADLAOUI/Controle_Cloud_Native_AI/assets/76519142/e4e4c0fc-9b91-4801-af85-2e543267880d">
## 8. Creating a Flask Application to consume the api
<img width="482" alt="flask" src="https://github.com/SalmaTADLAOUI/Controle_Cloud_Native_AI/assets/76519142/0018ae61-286e-4da4-b351-bd0adabcc679">

