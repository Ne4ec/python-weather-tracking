# Python Weather Tracking
A program that tracks the weather using an API from OpenWeatherMap.
_____
## Installation of the necessary packages
### Linux  
Before we begin, we need to install Python to execute the program, as well as Git to install the repository
```bash
sudo pacman -S python git 
```
**Notice:** If you're using a different Linux distribution, make sure to use the correct `package manager`. The steps should be similar across distributions.
____
## Installation
First, install my repository and navigate into the directory
```bash
sudo git clone https://github.com/Ne4ec/PythonWeatherTracking
cd PythonWeatherTracking/
```
To execute the file, you need an API key (its free). Go to [OpenWeather](https://openweathermap.org/) <br>and complete your registration.
After a few minutes, you will receive an API key, via an Email. Copy it and replace it on line 10, like this
```python
api_key = "12345678901234567890" #Replace your API here  
```
Now you can execute it by
```bash
python3 main.py
```
![poc](https://github.com/Ne4ec/PythonWeatherTracking/blob/main/.poc.png)
____
## Conculution
Hopefully, everything is working. If not, please leave a comment in the Issues tab. Thank you for paying attention, and have a nice day :)<br>
~ Ne4ec
