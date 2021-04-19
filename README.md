# Yo momma API
**An API that insults yo momma**
<br />

(Yo mommma API URL under development)

## API Usage

#### GET ```/```

Returns yo mamma

#### GET ```/jokes```

Returns random joke(s)
- Optional query parameter ```count``` to return count number of jokes.  Default count is 1<br/>Example: ```/jokes?count={count}```..

#### GET ```/jokes/{index}```<url to be added>

To return a joke based on index in ```jokes.json``` file

#### GET ```/search?query={query}```

To return a list of quotes matching the query.

## Development

This API is based on [FastAPI](https://fastapi.tiangolo.com/)

To contribute to the list of jokes or code, list an issue or send a pull request.

## Acknowledgements

Thanks to [rdegges](https://github.com/rdegges) and [szymex](https://github.com/szymex73) for the jokes. Yo momma would be proud.

## License

This software is licensed under the terms of the [MIT License](./LICENSE).