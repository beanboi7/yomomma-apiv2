# yomomma-apiv2
[![example workflow](https://github.com/beanboi7/yomomma-apiv2/actions/workflows/test.yml/badge.svg)](https://github.com/beanboi7/yomomma-apiv2/actions/workflows/test.yml)
[![Heroku](https://byob.yarr.is/beanboi7/yomomma-apiv2/heroku/)](https://yomomma-api.herokuapp.com/jokes/)

**An API that insults yo momma**
<br />

### [yomamma-api.herokuapp.com](https://yomomma-api.herokuapp.com/jokes)

## API Usage

#### GET ```/```

Returns "Yo momma"

#### GET ```/jokes```

Returns random joke(s)
- Optional query parameter ```count``` to return count number of jokes.  Default count is 1<br/>Example: ```/jokes?count={count}```..

#### GET ```/jokes/{index}```

To return a joke based on index in ```jokes.json``` file

#### GET ```/search?query={query}```

To return a list of jokes matching the query.

## Development

This API is based on [FastAPI](https://fastapi.tiangolo.com/) and currently hosted on [Heroku](https://www.heroku.com/)

To contribute to the list of jokes or code, list an issue or send a pull request.

## Acknowledgements

Thanks to [rdegges](https://github.com/rdegges) and [szymex](https://github.com/szymex73) for the jokes. Yo momma would be proud, atleast now.

## License

This software is licensed under the terms of the [MIT License](./LICENSE).