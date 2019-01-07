# Carthage API Assignment

This api allows 
1. Getting an Object
2. Getting List of all objects
3. Deleting S3 Object
4. Uploading S3 Object

## Getting Started



### Prerequisites

1. Python 2.7
2. GIT
3. IAM Role should be attached to the EC2 instance with S3 access.
### Installing

In Linux we need to run the makefile.

```
make makefile
```
For running the application in container.
The docker file should be used.

```
docker build -t dockerimage .
docker run dockerimage
```

## Built With

* [Python](https://www.python.org/download/releases/2.7/) - Back End Logic
* [Flask](http://flask.pocoo.org/docs/1.0/) - Web Framework Used


## Versioning

We use [GIT](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Sumit Kumar Kar** 

