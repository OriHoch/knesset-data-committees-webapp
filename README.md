# knesset-data-committees-webapp

**Work In Progress**

Webapp that displays data about Knesset committees, committee meetings and related data

## Status and features

Partially developed to support a frontend (which doesn't exist yet)

Deployed as part of the [knesset-data-pipelines kubernetes environment](https://github.com/hasadna/knesset-data-pipelines/blob/master/devops/k8s/committees-webapp.yaml)

Available API Endpoints:

* [list of all available tables and columns in DB](https://next.oknesset.org/committees/)
* [list of rows from kns_committee table](https://next.oknesset.org/committees/commitees)
* [list of sub-committees related to given parent committee id](https://next.oknesset.org/committees/commitee/childof/21)
* [json of all committee ids and names](https://next.oknesset.org/committees/commiteeNames)

## Development Quickstart

* Install Docker and Docker compose
* Fork and clone the project, change to the project directory
* `docker-compose build`
* `./initialize_db.sh`
* `docker-compose up -d`
* API should be available at http://localhost:15050/
