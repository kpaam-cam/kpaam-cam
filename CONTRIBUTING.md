Contributing
------------

Install the development environment:

```sh
$ pip install virtualenv  # might require sudo/admin privileges
$ git clone https://github.com/kpaam-cam/kpaamcam.git  # you may also clone a suitable fork
$ cd kpaamcam
$ python -m virtualenv .venv
$ source .venv/bin/activate  # Windows: .venv\Scripts\activate.bat
$ pip install -r requirements.txt  # installs the cloned version with dev-tools in development mode
```

Then create a database:

```sh
$ su - postgres
```
(or, if that doesn't work, try "psql -U postgres")

Then:

```sh
$ createdb kpaamcam
```

and initialize it, either
- loading a dump of the production DB, using the app's `load_db` task from the
`appconfig` package
- or by running `clld initdb development.ini --glottolog [/path/to/glottolog] --cldf [/path/to/cldf]`

The Glottolog can be found here: https://github.com/glottolog/glottolog

The current CLDF for this app can be found here: https://github.com/kpaam-cam/lowerfungom-wordlists

A sample development.ini file is included in the repository.

Now you should be able to run the tests:

```sh
$ pytest
```

More information on how to run a local server is here:
https://clld.readthedocs.io/en/latest/tutorial.html

It should be possible to activate by running:

```sh
pserve --reload development.ini
```
