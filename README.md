# mfapi-mcp-server

A local [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that wraps
[mfapi.in](https://mfapi.in) — a free, open API for Indian mutual fund NAV data — so you can
query mutual fund schemes, NAV history, and latest prices directly from Claude or any MCP-compatible client.

> **All mutual fund data is provided by [mfapi.in](https://mfapi.in).**
> This server is just a thin MCP wrapper; mfapi.in does all the heavy lifting.
> Please respect their service and avoid hammering it with bulk requests.

---

## one-click install

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=mfapi&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--from%22%2C%22git%2Bhttps%3A//github.com/raghav4/mfapi-mcp-server%22%2C%22mfapi-mcp%22%5D%7D)
[![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=mfapi&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--from%22%2C%22git%2Bhttps%3A//github.com/raghav4/mfapi-mcp-server%22%2C%22mfapi-mcp%22%5D%7D&quality=insiders)
[![Install in Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=mfapi&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyItLWZyb20iLCJnaXQraHR0cHM6Ly9naXRodWIuY29tL3JhZ2hhdjQvbWZhcGktbWNwLXNlcnZlciIsIm1mYXBpLW1jcCJdfQ==)

> **requires [uv](https://docs.astral.sh/uv/) to be installed** — `brew install uv` or see [uv docs](https://docs.astral.sh/uv/getting-started/installation/)

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

## manual installation

### claude desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mfapi": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/raghav4/mfapi-mcp-server", "mfapi-mcp"]
    }
  }
}
```

### claude code (cli)

```bash
claude mcp add --scope user mfapi uvx -- --from git+https://github.com/raghav4/mfapi-mcp-server mfapi-mcp
```

### other clients (cursor, windsurf, etc.)

```json
{
  "mcpServers": {
    "mfapi": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/raghav4/mfapi-mcp-server", "mfapi-mcp"]
    }
  }
}
```

---

## example prompts

```
search for hdfc top 100 fund
get latest nav for scheme 125497
show me nav history for mirae asset large cap from january to december 2023
list 20 elss funds
```

---

## data source & credits

All mutual fund data — scheme codes, NAV history, fund metadata — comes from
**[mfapi.in](https://mfapi.in)**, a free and open Indian mutual fund API built and maintained by
the open-source community. This project is not affiliated with mfapi.in; it simply provides an
MCP interface on top of their public API.

If you find mfapi.in useful, consider supporting their project.

---

## license

MIT — see [LICENSE](LICENSE).
