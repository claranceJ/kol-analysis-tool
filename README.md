# KOL Analysis Tool

A Python web app that tracks new device reviews from African YouTube tech creators (KOLs, or Key Opinion Leaders). It pulls their latest videos, transcribes them, and presents the key details in one organized dashboard.

> Status: early development. Currently provides a health check endpoint.

## Planned features

- Fetch new videos from a list of tracked YouTube channels
- Transcribe videos to text (YouTube captions, with Whisper as a fallback)
- Extract device names, specs, and prices from each transcript
- Show reviews in a searchable, sorted dashboard
- Optional AI summaries and sentiment tags

## Tech stack

- Python 3.12+
- FastAPI and Uvicorn for the web server
- pytest for testing

## Getting started

### Prerequisites

- Python 3.12 or newer
- Git

### Setup

```bash
git clone https://github.com/<your-username>/kol-analysis-tool.git
cd kol-analysis-tool
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

### Run the app

```bash
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/docs in your browser.

### Run the tests

```bash
python -m pytest -v
```

## Project structure