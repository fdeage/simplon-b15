# Correction brief 15

This project aims to demonstrate how to properly do CI for a simple clustering app.

## Services

The app is composed of only two services:

1. one service (the "back-end") declares an API that accepts a request for clustering in a given method

will perform clustering of a dataset, in several ways

Technologies used: `pandas` for CSV processing, `scikit-learn` for clustering, `fastapi`/`uvicorn` for the APi itself

2. another service (the "front-end") just shows a very bare-bones web page through which the user selects a clustering method. The JS then fetches the corresponding results from the back-end and displays the results. No JS library like `jQuery` is needed.

## How to launch the project

1. Natively:
```
?> python back/api.py
```
and
```
?> cd front && python -m http.server 8000
```

2. Through Docker:

```
?> cd back && docker build -t b15-back .
?> cd ..
?> cd front && docker build -t b15-front .
```

Then you can use Docker compose:
```
?> docker-compose up
```
and check your browser on `localhost:8001`.

3. Full deploy:

You will need the [azure CLI](https://learn.microsoft.com/en-us/cli/azure/) installed.

```
?> az

```

## Launch tests


```
?> pytest back/
```
