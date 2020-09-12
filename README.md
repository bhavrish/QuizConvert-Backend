# Video-Quiz-Converter

## Install

You can clone this repo or download it as a zip.

```
git clone https://github.com/bhavrish/Video-Quiz-Converter.git
cd Video-Quiz-Converter
```


You can now install the packages and migrate the database to the models.

```
pipenv install
pipenv shell
python3 manage.py makemigrations
python3 manage.py migrate
```

If all of this works as expected, you should be able to now run the server.

```
python3 manage.py runserver
```

Endpoints

```
http://localhost:8000/quizzes : GET Request
```

## Contributing

We don't currently have a guideline set in stone, but any popular OSS format works well, and we'll adopt one soon. Our project is super open to contributions.
