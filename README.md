# job-application-agent

A small Playwright-based agent that reads a résumé from JSON and auto-fills a web form.
It's a working boilerplate for browser-automation tasks (form filling, scraping, flows).

## How it works

- `src/resume_parser.py` — loads `data/resume.json` into a dict.
- `src/web_agent.py` — `WebAgent` wraps Playwright (launch Chromium, navigate, fill fields, submit).
- `src/main.py` — wires them together: loads the résumé, opens `data/test_form.html` via `file://`,
  fills `#email` and a message field, and submits.

`filled_form.png` is a sample screenshot of a completed run.

## Setup

```bash
cd job_application_agent
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
```

## Run

```bash
cd job_application_agent/src
python main.py
```

## Test

```bash
cd job_application_agent
python -m pytest tests/
```

## Adapt it

Point `main.py` at a real form URL instead of the local `test_form.html`, and map your
`resume.json` fields to that form's selectors in the `agent.fill_field(...)` calls.
