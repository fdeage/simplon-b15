# API specification

Our API ...

## List available clustering methods

`/list_methods` lists available clustering methods (GET).

Response :
```
?> curl http://localhost:8000/list_methods
{"resp": "ok", "score": score}
```

## Get the score associated with a method

`/methods/<method>/get_score` (GET) gets the score associated with a method and returns a dict with
Response :
```
?> curl http://localhost:8000/list_methods
{"resp": "ok", "score": score}
```



## Retrain a model

- `/methods/xx/retrain` (POST) will redo the clustering for the given method
