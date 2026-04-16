# mfapi-mcp-server

A local [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that wraps
[mfapi.in](https://mfapi.in) — a free, open API for Indian mutual fund NAV data — so you can
query mutual fund schemes, NAV history, and latest prices directly from Claude or any MCP-compatible client.

> **All mutual fund data is provided by [mfapi.in](https://mfapi.in).**
> This server is just a thin MCP wrapper; mfapi.in does all the heavy lifting.
> Please respect their service and avoid hammering it with bulk requests.

---

## tools

| tool | description | key params |
|---|---|---|
| `search_mf` | search schemes by name or keyword | `query` |
| `list_mf` | paginated list of all schemes | `limit`, `offset` |
| `get_nav_history` | full or date-ranged NAV history | `scheme_code`, `start_date`, `end_date` |
| `get_latest_nav` | current NAV for a scheme | `scheme_code` |

Scheme codes are numeric strings (e.g. `125497`). Use `search_mf` to find the code for any fund.

Dates for `get_nav_history` are in `DD-MM-YYYY` format (e.g. `01-01-2023`).

---

## requirements

- [uv](https://docs.astral.sh/uv/) — handles Python and dependency management
- Python ≥ 3.10 (uv will download one automatically if needed)
- No API key required — mfapi.in is free and open

---

## installation

```bash
git clone https://github.com/your-username/mfapi-mcp-server
cd mfapi-mcp-server
uv sync
```

---

## wiring into claude code

Add to `~/.claude/mcp.json` (create the file if it doesn't exist):

```json
{
  "mcpServers": {
    "mfapi": {
      "command": "uv",
      "args": [
        "run",
        "--project",
        "/absolute/path/to/mfapi-mcp-server",
        "mfapi-mcp"
      ]
    }
  }
}
```

Restart Claude Code — the four tools will be available immediately.

---

## example prompts

```
search for hdfc top 100 fund scheme code
get latest nav for scheme 125497
show me nav history for mirae asset large cap from january to december 2023
list 20 ELSS funds
```

---

## running manually

```bash
# start the server over stdio (for testing)
uv run mfapi-mcp
```

---

## data source & credits

All mutual fund data — scheme codes, NAV history, fund metadata — comes from
**[mfapi.in](https://mfapi.in)**, a free and open Indian mutual fund API built and maintained by
the open-source community. This project is not affiliated with mfapi.in; it simply provides an
MCP interface on top of their public API.

If you find mfapi.in useful, consider starring or contributing to their project.

---

## license

MIT — see [LICENSE](LICENSE).
