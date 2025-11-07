# AI Motivational Quote Agent

A small Python CLI that talks to OpenAI to generate concise motivational guidance and a short preparation checklist targeted at students preparing for FAANG/MAANG-style interviews.

## What this repository contains

- `app.py` – CLI entry point. Invokes the agent and writes output to `gpt_output.text`.
- `ai_motivational_agent.py` – The agent class that builds the prompt and formats the response.
- `openai_client.py` – Lightweight wrapper around the OpenAI Python client. Reads `OPENAI_API_KEY` from environment.
- `TestGPTAPI.py` – Example/test file (contains a hard-coded API key — see Security notes).
- `gpt_output.text` – (Generated) output file created by `app.py` when a response is written.

## Requirements

- Python 3.8 or newer
- `openai` Python package

You can install the package directly:

```powershell
python -m pip install --upgrade pip
python -m pip install openai
```

(Optionally create a `requirements.txt` with `openai` if you prefer.)

## Setup (PowerShell)

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install openai
```

3. Set your OpenAI API key in the environment (do NOT hard-code it):

```powershell
$env:OPENAI_API_KEY = "your_api_key_here"
# To persist the variable for the current user, use setx (re-open shell to take effect):
# setx OPENAI_API_KEY "your_api_key_here"
```

## Usage

Run the CLI. You may optionally provide a student name and a focus area.

```powershell
python app.py            # uses defaults: name -> "student", focus -> "DSA and System design"
python app.py Alice "system design"  # pass name and focus area
```

On success, the script writes an output file named `gpt_output.text` and prints the advice to the console.

## Notes & Security

- `openai_client.py` reads `OPENAI_API_KEY` from the environment. Do not put keys directly into source files.
- I noticed `TestGPTAPI.py` contains an embedded API key. That is a secret and must be removed immediately. If this repository has been committed to a public or shared VCS, consider rotating the API key and purging the secret from your git history.

Suggested quick actions:
- Delete or edit `TestGPTAPI.py` to remove the API key.
- Rotate the exposed API key in your OpenAI dashboard.
- If the key was committed, use tools such as `git filter-repo` or `git filter-branch` to remove the secret from history (follow your org's policy).

## File summaries

- `app.py`: CLI wrapper that validates the environment, creates the chat client and agent, invokes the agent, writes the result to `gpt_output.text`, and prints the result.
- `ai_motivational_agent.py`: Prompts the model with a structured prompt to produce a short motivation and a small checklist.
- `openai_client.py`: Thin wrapper using `openai.OpenAI()` to call `chat.completions.create(...)` and return text. It raises RuntimeError on failures.

## Troubleshooting

- If you see errors about authentication, confirm `OPENAI_API_KEY` is set in the shell you run the script from.
- If the model fails or returns empty, check network access and your OpenAI account quota/model access.

## Contact / Next steps

If you'd like, I can:
- Add a `requirements.txt` and a small `.gitignore` (to ignore `.venv` and output files).
- Remove or redact the API key from `TestGPTAPI.py` and create a safe example demonstrating environment variable usage instead.

---

Created automatically to document how to run and secure this project.

