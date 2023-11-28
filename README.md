
# GameLib

This project was developed to study the use of the Python language in web development. Using the Flask framework to create simple pages to register games in a kind of online library.




## Requirements

[Python](https://www.python.org/downloads/) and [MySQL](https://www.mysql.com/downloads/)
## How to run Locally

Clone the project

```bash
  git clone https://github.com/notyourpedroo/gamelib-flask.git
```

Go to the project directory

```bash
  cd gamelib-flask
```

Create a virtual environment and activate it

```bash
  python -m venv your_venv_name

  (MacOS and Linux) source your_venv_name/bin/activate
  (Windows) your_venv_name/Scripts/Activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the script to create and populate the database

```bash
  python create_db.py
```

Finally, run the project

```bash
  python gamelib.py
```


## Authors

- [@notyourpedroo](https://www.github.com/notyourpedroo)

