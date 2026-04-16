# mfapi-mcp-server

Local MCP server for [mfapi.in](https://mfapi.in) — a free API for Indian mutual fund data.

## tools

| tool | description |
|---|---|
| `search_mf` | search schemes by name or keyword |
| `list_mf` | paginated list of all schemes |
| `get_nav_history` | NAV history for a scheme (optional date range) |
| `get_latest_nav` | latest NAV for a scheme |

## requirements

- [uv](https://docs.astral.sh/uv/) — used to run the server and manage dependencies
- Python ≥ 3.10 (uv downloads one automatically if needed)

## setup

```bash
# install dependencies into a local venv
cd /Users/raghavsharma/Documents/mfapi-mcp-server
uv sync
```

## wiring into claude code

Add to `~/.claude/mcp.json`:

```json
{
  "mcpServers": {
    "mfapi": {
      "command": "uv",
      "args": [
        "run",
        "--project",
        "/path/to/mfapi-mcp-server",
        "mfapi-mcp"
      ]
    }
  }
}
```

Then restart Claude Code. The four tools will appear automatically.

## example usage

```
search for hdfc top 100 fund
→ search_mf("HDFC Top 100")

get latest nav for scheme 125497
→ get_latest_nav("125497")

get nav history for 2023
→ get_nav_history("125497", start_date="01-01-2023", end_date="31-12-2023")
```

## date format

`get_nav_history` accepts dates as `DD-MM-YYYY` (e.g. `01-01-2023`), matching the mfapi.in convention.
