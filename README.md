# `smolagents` test

Let's have some fun with `smolagents`!

## Prerequisites

```sh
brew install mise uv common-fate/granted/granted
mise install
```

## Setup

```sh
uv pip sync -r requirements.txt
```

## Run

## Hugging Face model

```sh
huggingface-cli login
python hf.py
```

## AWS Bedrock model

```sh
assume
python bedrock.py
```
