# IntelligentXray-Server

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Installation](#installation)
* [Usage](#usage)



<!-- ABOUT THE PROJECT -->
## About The Project

This repo is the server for [IntelligentXray](https://github.com/carloslago/IntelligentXray), in charge of deploying the developed model.

### Built With
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Tensorflow](https://www.tensorflow.org/)
* [Keras](https://keras.io/)
* [Lime](https://github.com/marcotcr/lime)

### Installation

1. Clone the repository
```sh
git clone https://github.com/carloslago/IntelligentXray_Server.git
```

2. Install Python packages
```sh
pip install requirements.txt
```



## Usage
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```





