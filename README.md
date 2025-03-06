# Locust implemented in docker
here is a little projet to manage load test with locust in his last docker version
3 files :
* Dockerfile to build the custom image base on locustio/locust
* docker-locust.py the python script using the locust python modules
 requirements.txt the python dependencies

## Building the image
```shell
docker build <project_dir> <imageName:imangeTag>
```

## Runing the image
```shell
docker run --env TARGET=http://192.169.0.2 <imageName:imageTag>
```
