---
category: Methods
url_path: '/jokes/{index}'
title: 'Specific Joke'
type: 'GET'

layout: null
---

This method returns a specific joke based on index in [jokes.json](https://github.com/beanboi7/yomomma-apiv2/blob/master/jokes.json)

### Parameters

```index: Returns joke of the given index. 
       Required```

Example: 

```/jokes/20```


### Response

JSON Response of indexed joke

If index is given as 300:

```Status: 200 OK```
```{
  "joke": "Yo momma is like a bag of potato chips, 'Free-To-Lay.'"
}```

For invalid index parameter:

```Status: 404 NOT FOUND```
```{
  "detail": "Invalid index paramter"
}```

If you put query as "yo momma":

```Status: 200 OK```
```{
  "results": "DONT"
}```