# Project Name

## Problem

There are multiple websites from different brands, each with its own quotation system. Users enter a zip code, and depending on the type of product, state, language, and brand, they are redirected to various form URLs. Additionally, in certain circumstances, it is necessary to direct users to different types of form URLs based on their state.

## Solution

It is proposed to develop a serverless microservice using AWS Lambda. This approach is designed to handle the high demand from all the brands that will integrate with the service. To structure the solution, the Domain-Driven Design (DDD) architecture and Command Query Responsibility Segregation (CQRS) pattern will be employed. This combination will allow for an efficient separation of business logic, data models, and specific use cases for each bounded context. With this, the system aims to optimize both the management of the variability in form redirection needs and the scalability and maintenance of the system.

Additionally, a log processing system based on SQS (Amazon Simple Queue Service) was implemented to avoid impacting the performance and response time of the main service. 

## Technologies Used

This project is a serverless Python application using several technologies.

- **Python**: The main programming language used for developing the application.
- **Docker**: Used for creating and managing the application's environment.
- **Alembic**: A database migration tool used with SQLAlchemy.
- **AWS Chalice**: A framework for writing serverless Python applications.

## Application Structure

- `src/`: This directory contains the main Python application code.
    - `app.py`: The entry point to the application.
    - `chalicelib/`: This directory contains the library code that the Chalice app depends on.
    - `tests/`: This directory contains test files.
    - `tools/`: This directory contains various tools related to the application.
- `docker/`: This directory contains Dockerfiles and related resources for building Docker images.
- `db/`: This directory contains files related to the database.



