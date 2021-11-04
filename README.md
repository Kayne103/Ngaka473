# Doctor/Client Management System

![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)

## Getting Started

### For contributors
- Clone the repo into your machine.
- Create a branch for every task/issue you'll be working on. Do not push to master, instead make a pull request.
- Do not hard code secret keys,passwords, and other things that are supposed to be kept private.
- Follow these standards when [writing commit messages.](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/)
- Always mention issue number in your commit messages(i*f there's any*).
- Ignore cache files, virtual environment directory, IDE settings directory and dotenv file.


### Prerequisites
- Python3.9
- Django3.2
- Bootstrap 5
- dotenv
- mysqlclient

### Installing

1. Clone the repo into your local machine.

```
git clone https://github.com/Kayne103/doctorpatientmanagement.git
```

2. In the root of the project, Create a virtual environment and activate it.

```
python3 -m venv venv
source venv/bin/activate (on Ubuntu)
```
[How to create and activate python3 virtual environment](https://docs.python.org/3/library/venv.html)

3. Install requirements
```
pip3 install -r requirements.txt
```
4. Create a .env file.
```
touch .env
```
5. Copy and paste environment variables in the .env file. _They will be shared privately._
6. Make migrations.
```
python3 manage.py makemigrations
python3 manage.py migrate
```
7. Run the project.
```
python3 manage.py runserver
```
_Raise issues if there's any problem._

## Running the tests

Currently, there are no automated tests for this project because initially the requirements
were unclear. So it's all free styling until we have an idea of what we are doing.

## Deployment

We highly likely to deploy it on [Microsoft Azure](https://azure.microsoft.com/en-us/)

## Analytics
[DeepSource](https://deepsource.io/) is the way to go. Will be using it to analyze and improve code.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used

## Versioning

We might use [SemVer](http://semver.org/) for versioning. 

## Authors

* **Kaene K. Lebakeng**
* **Anesu Banda**
* **Bothe Tseme**
* **Pearl Rantolo**
* **Bokamoso Y. Mogotsi**

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

- Not yet decided. This project should is only available to the invited parties.