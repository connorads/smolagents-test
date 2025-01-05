# `smolagents` test

Let's have some fun with `smolagents`!

## Prerequisites

```sh
brew install mise uv
mise install
```

## Setup

```sh
uv pip sync -r requirements.txt
huggingface-cli login
```

## Run

```sh
python test.py
```
