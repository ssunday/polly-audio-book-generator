# Polly Audio Book Generator

Uses [AWS's Polly text-to-speech service](https://aws.amazon.com/polly/) to generate audio files from text files from my books, in theory to create audio books. It's a basic tool.

## Requirements

- Python 3.10.4+
- [Pipenv](https://pypi.org/project/pipenv/#installation) (`pip install pipenv`)
- AWS Account setup and desire to spend money via Polly

## Setup

- `pipenv install --dev`
- `pipenv shell`
- `cp config.example.yml config.yml` and change accordingly

## Usage

- `pipenv run python synthesize.py`

## Linting

- `pipenv run flake8`
