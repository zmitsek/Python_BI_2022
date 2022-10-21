#  Ubuntu 22.04.1 LTS

### Python 3.10.6 or higher

 Open terminal with keyboard shortcut  Ctrl+Alt+T

## Install Python

```sh
sudo apt-get install python3
```

## Downloading files
```sh
git clone https://github.com/zmitsek/Virtual_environment_research
```
Then go to the directory with the script
```sh
cd Virtual_environment_research/
```

## Creating and activating environment
```sh
python -m venv venv
```
```sh
source venv/bin/activate
```

## Installing packages
```sh
pip install --upgrade pip
```
```sh
pip install -r requirements.txt
```


## Enjoy!
```sh
python pain.py
```
## After work
```sh
deactivate
```
