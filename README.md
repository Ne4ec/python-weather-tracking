# Python Weather Tracking
A program that tracks the weather using an API from OpenWeatherMap.
_____
## Installation of the necessary packages
**Notice:*** this installation is for Linux distribution<br>
Before we begin, we need to install Python to execute the program, as well as Git to install the repository
```python
sudo pacman -S python git 
```
**Notice:** If you're using a different Linux distribution, make sure to use the correct `package manager`. The steps should be similar across distributions.
____
## Installation
First, install my repository and navigate into the directory
```python
sudo git clone https://github.com/Ne4ec/python-weather-tracking
cd python-weather-tracking/
```
To execute the file, you need an API key (its free). Go to [OpenWeather](https://openweathermap.org/) and complete your registration.
After a few minutes, you will receive an API key, via an Email. Copy it and replace it on line 10, like this
```python
api_key = "12345678901234567890" #Replace your API here  
```
Now you can execute it by
```python
python3 main.py
```
____
## Conculution
Hopefully, everything is working. If not, please leave a comment in the Issues tab. Thank you for paying attention, and have a nice day :)<br>
~ Ne4ec
