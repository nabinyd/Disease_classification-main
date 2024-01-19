# Disease_classification

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml


# How to run?
## Steps:

Clone the repository.


### Step 1- Create the environment after cloning the repository
```bash
python -m venv venv
```

### Activate
``` bash
venv\Scripts\activate
```
### Step 2- install the requirements

```bash
pip install -r requirements.txt
```
<!-- finally run the following command -->
```bash
python app.py
```
Now, open local host and port

## DVC command
1. dvc init
2. dvc repro
3. dvc dag

# AZURE-CICD-Deployment-with-Github-Actions
### Save pass:

### Run from terminal:

```bash
docker build -t flasksimpleapp.azurecr.iio/mltest:latest .

docker login flasksipmleapp.azurecr.io

docker push flasksimple.azurecr.io/mltest:latest
```

### Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to the Container Registry
3. Lunch the Web App Server in Azure
4. Pull the Docker image from the container registry to Web App server and run