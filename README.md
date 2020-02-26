# Polly Audio Book Generator

Uses [AWS's Polly text-to-speech service](https://aws.amazon.com/polly/) to generate audio files from text files from my books...in theory to create audio books. Not that exciting right now or that fleshed out. It's a WIP.

## Requirements

- Python 3.7.4
- [Pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)
- AWS Account setup and desire to spend money via Polly

## Setup

- `pipenv install --dev`
- `pipenv shell`
- `cp config.example.yml config.yml` and change accordingly

## Usage

- `pipenv run python synthesize.py`

## Linting

- `pipenv run flake8`

## TODO

- [ ] Somehow parse RTF into [SSML](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html) to utilize more of the effects.
  Problems: bolding/italics have multiple meanings in my books due to their usage in stream of consciousness so the effects may not match intent.
- [ ] Lexicon creation support and instant playback to verify the words sound right.
