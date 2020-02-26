# Audio Book Generator

Uses AWS's Polly text-to-speech service to generate audio books from text files from my books.

## Requirements

- Python 3.7.4
- [Pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)
- AWS Account setup and desire to spend money via Polly

## Setup

- `pipenv install --dev`
- `pipenv shell`
- `cp config.example.yml config.yml` and change accordingly

## Usage

- `S3_BUCKET=YOUR_BUCKET pipenv run python synthesize.py`

## Linting

- `pipenv run flake8`
