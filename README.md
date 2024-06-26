# flask-interface-app

![Flask Logo](https://flask.palletsprojects.com/en/3.0.x/_images/flask-horizontal.png)

## Introduction

flask-interface-app is a Python package that simplifies the process of creating and managing Flask web applications. It provides a CLI command to quickly generate a full file structure for a Flask app, along with a user-friendly bash-like UI for executing commands.

## Get Started

To install flask-interface-app, simply run:

```bash
pip install flask-interface-app
```

## Create a New Flask App

To create a new Flask app, use the following command:

```bash
create-flask-app mynewapp # app name
```

Replace `mynewapp` with the desired name of your Flask application.

## Command UI Bash

flask-interface-app comes with a command-line interface (CLI) that mimics a bash terminal. You can use it to execute various commands related to your Flask app.

### Example Command:

```bash
> create-flask-app mynewapp
```

### What Executing Commands Do

The commands executed via the bash-like UI will handle all necessary steps for setting up a Flask application. This includes creating the project structure, setting up configuration files, and initializing essential Flask components such as blueprints, models, forms, and routes.

### Project Directory Structure

After running the command, the project directory structure will look like this:

```
mynewapp/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth_routes.py
│   ├── forms.py
│   ├── admin.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── scripts.js
│   │   └── img/
│   │       └── logo.png
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       ├── docs.html
│       ├── about.html
│       └── blog/
│           ├── create_post.html
│           └── post.html
├── config.py
├── app.py
└── README.md
```

### flask-interface-appApp Structure

The Flask app structure created by flask-interface-app follows a full-fledged MVC architecture, providing separation of concerns and scalability for your application.

### Included Libraries

flask-interface-app includes several libraries that are commonly used in Flask projects:

```
Click
Flask
Flask-SQLAlchemy
Flask-WTF
Flask-Bcrypt
Flask-Login
Flask-Admin
email-validator

```

## Contributing

Contributions are welcome! Please feel free to open issues or pull requests on the [GitHub repository](https://github.com/freebaizid/flask-interface-app).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
