# recode

`recode` is a lightweight, open-source coding agent you run from your terminal. It reads and edits files in your current project directory, using an LLM (via [smolagents](https://github.com/huggingface/smolagents)) to reason about the task and act through a small set of tools.

Think of it as a minimal, hackable alternative to tools like Cursor's agent mode — built to be understood, not just used.

## Features

- **Read & write files** in your project directly from natural language instructions
- **Persistent memory** — the agent can remember facts across a session
- **Sandboxed by design** — the agent can only read/write inside the directory you run it from, never outside of it
- **Runs anywhere** — install once, use it in any project folder
- Built on [smolagents](https://github.com/huggingface/smolagents)' `CodeAgent`, meaning the LLM reasons by writing and executing real Python code, not by producing brittle JSON blobs

## Installation

`recode` is distributed via GitHub and installed with [pipx](https://pypa.github.io/pipx/), which keeps it isolated while making it available as a global command.

```bash
# install pipx if you don't have it
brew install pipx
pipx ensurepath

# install recode
pipx install git+https://github.com/arobaseSuulei/recode-ai.git
```

Once installed, the `recode` command is available in any terminal, from any directory.

## Configuration

`recode` needs an OpenAI API key to function. It reads it from the `OPENAI_API_KEY` environment variable — **your key is never stored, bundled, or transmitted anywhere by this project.**

```bash
export OPENAI_API_KEY=your_key_here
```

Add this line to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.) to avoid retyping it every session.

## Usage

Navigate to the project you want the agent to work on, then run:

```bash
cd ~/my-project
recode
```

You'll get an interactive prompt:

```
-- Recode.ai, What are we going to build chief --
> add docstrings to every function in utils.py
```

The agent will:
1. Read the relevant file(s)
2. Reason about the change needed
3. Write the updated content back to disk
4. Report back what it did

Type `exit` or `quit` to leave the session.

### Example

```
> create a function that subtracts two numbers and save it in math_utils.py
```

```
> read main.py and add a comment on every line
```

## How it works

`recode` follows the **ReAct** pattern (Reasoning + Acting), the same loop used by most modern coding agents:

```
Thought → Action → Observation → Thought → Action → ... → Final Answer
```

Instead of asking the LLM to produce JSON instructions, `recode` uses smolagents' **Code Agent** approach: the model writes real, executable Python code to call tools, which tends to be more reliable and expressive than JSON-based tool calling.

### Available tools

| Tool | Description |
|---|---|
| `read_file` | Reads the content of a file in the current workspace |
| `writing_code` | Writes or overwrites a file in the current workspace |
| `remember` | Stores a fact for later recall during the session |

All file operations are restricted to the directory you launched `recode` from — the agent cannot read or write anywhere else on your system.

## Project structure

```
recode-ai/
├── src/
│   └── recode/
│       ├── agent.py     # model + tools + agent assembly
│       ├── cli.py       # command-line entry point
│       └── tools/
│           ├── files.py   # read_file, writing_code
│           └── memory.py  # remember
├── pyproject.toml
└── README.md
```

## Safety notes

- `recode` can overwrite files without asking for confirmation. Use it inside a git repository, and commit your work before running the agent on real code, so you can always roll back with `git checkout`.
- Never commit your `.env` file or API keys to version control.

## Contributing

This project is open source and meant to be a learning resource as much as a tool — issues, questions, and pull requests are welcome.

## License

MIT