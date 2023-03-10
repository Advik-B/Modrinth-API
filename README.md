# Modrinth API
[modrinth-api]: https://docs.modrinth.com/api-spec/
[cfapi-docs]: https://wow.curseforge.com/api/docs
[not-working-modrinth]: https://github.com/BetaPictoris/modrinth.py
[cmpdl]: https://github.com/Advik-B/CMPDL

This is a no-compromise CurseForge API wrapper for python. It is a re-write of [Modrinth.py][not-working-modrinth] which (In my opinion) is trash
This project is a complete re-write of the original project, with a focus on simplicity and ease of use.

This project is still in development, and is not yet ready for production use.
It also speeds up the process by using disk caching, It will cache the response from the API and will only make a new request if the request is not cached.

This, of course can be disabled by setting the cache to False.

## Features
- Simple and easy to use
- Caches responses from the API to disk for faster response times
- Allows direct access to the API via the `fetch` method
- Allows exporting of the objects to DICT, JSON, or YAML

## Installation

```bash
pip install modrinth-api
```

## TODO
- [ ] Implement the export methods
- [ ] Implement the cache
- [ ] Implement the fetch method
- [ ] Deal with the download URL being a null value
- [ ] Implement the search method
- [ ] Wrap the ENTIRE API
- [ ] Rename the classes so they have a `Rinth` prefix

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
