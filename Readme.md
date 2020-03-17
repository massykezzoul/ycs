# YCS (Youtube Comment Scrapper)

## Introduction

A small command line utility for scraping YouTube comments using Python3 and Youtube API.

## Quick start

### Requirements

- A youtube api key
- Python3

### Installation

#### Linux

1- First, install python3

```
    # On ubuntu for example
    sudo apt install python3
```

2- Then install all requirement for python

```
    # install python requirements
    pip3 install -r requirements.txt
```

3- Get an API Key from Youtube : follow this [tutorial](https://www.youtube.com/watch?v=pP4zvduVAqo)

4- Clone this repository

```
    git clone git@github.com:massykezzoul/ycs.git
    cd ycs/
```

5- Write your API key in file named `api.key` in the `src/` directory by running this command or other way

```
    touch src/api.key
    echo "<YOUR_API_KEY>" > src/api.key
```

6- Run the programme and pray

```
    python3 src/ycs.py > output.json # this print the result in the file 'output.json'
```

#### Windows

In futur update inchalah...

## In futur version

- Write the output in a file given by argument
- Set a number maximum of comments extracted

## Author

- Massili Kezzoul -> (massy.kezzoul@gmail.com)
- Last update -> march 18, 2020
