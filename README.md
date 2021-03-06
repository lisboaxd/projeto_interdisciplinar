<p align="center">
  <a href="#">
    <img src="https://raw.githubusercontent.com/lisboaxd/projeto_interdisciplinar/master/static/images/recicla-mais-brand.png" width="200px" alt="Recicla+ App">
  </a>

  <h3 align="center">Projeto interdisciplinar</h3>
</p>

Trabalho acadêmico desenolvido em Python 3, usando Django 3.

### Settings

Create a virtualenv to start the settings. Install if you don't have using the following commands: `sudo apt install python-virtualenv` and `sudo apt-get install python3-venv`.

Create the local virtualenv: `python3 -m venv venv`

Activate the virtualenv: `source venv/bin/activate`

### Installation

Mappets requires [Python3](https://www.python.org/) v3+ to run.

Install the dependencies and devDependencies and start the server.

```shell
cd mappets
```

Use the `pip install` to install from `requirements.txt` file.

```python
pip install -r requirements.txt
```

Run all database migrations:

```python
python manage.py migrate
```

Use the `manage.py` file to run the server.

```python
python manage.py runserver
```
