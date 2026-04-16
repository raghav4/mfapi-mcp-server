"""
MCP server for the mfapi.in Indian mutual funds API.

Exposes four tools:
  - search_mf         : search schemes by name/keyword
  - list_mf           : paginated list of all schemes
  - get_nav_history   : NAV history for a scheme (optional date range)
  - get_latest_nav    : latest NAV for a scheme
"""

import json
import httpx
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.mfapi.in"

mcp = FastMCP("mfapi")


def _client() -> httpx.Client:
    return httpx.Client(base_url=BASE_URL, timeout=15)


@mcp.tool()
def search_mf(query: str) -> str:
    """
    Search mutual fund schemes by name or keyword.

    Args:
        query: Search term, e.g. "HDFC", "Nifty 50", "ELSS"

    Returns:
        JSON list of matching schemes with schemeCode and schemeName.
    """
    with _client() as client:
        response = client.get("/mf/search", params={"q": query})
        response.raise_for_status()
        results = response.json()

    if not results:
        return json.dumps({"message": f"No schemes found for query: {query}"})

    return json.dumps(results, indent=2)


@mcp.tool()
def list_mf(limit: int = 50, offset: int = 0) -> str:
    """
    List all mutual fund schemes with pagination.

    Args:
        limit:  Number of schemes to return (default 50, max 1000).
        offset: Number of schemes to skip (default 0).

    Returns:
        JSON list of schemes with schemeCode and schemeName.
    """
    with _client() as client:
        response = client.get("/mf", params={"limit": limit, "offset": offset})
        response.raise_for_status()
        results = response.json()

    return json.dumps(results, indent=2)


@mcp.tool()
def get_nav_history(
    scheme_code: str,
    start_date: str = "",
    end_date: str = "",
) -> str:
    """
    Get NAV history for a mutual fund scheme.

    Args:
        scheme_code: Numeric scheme code, e.g. "125497". Use search_mf to find it.
        start_date:  Optional start date in DD-MM-YYYY format, e.g. "01-01-2023".
        end_date:    Optional end date in DD-MM-YYYY format, e.g. "31-12-2023".

    Returns:
        JSON with scheme metadata and NAV data array (date + nav pairs).
    """
    params: dict = {}
    if start_date:
        params["startDate"] = start_date
    if end_date:
        params["endDate"] = end_date

    with _client() as client:
        response = client.get(f"/mf/{scheme_code}", params=params)
        response.raise_for_status()
        result = response.json()

    # Summarise record count to avoid flooding context with huge histories
    data = result.get("data", [])
    meta = result.get("meta", {})
    summary = {
        "meta": meta,
        "record_count": len(data),
        "data": data,
    }
    return json.dumps(summary, indent=2)


@mcp.tool()
def get_latest_nav(scheme_code: str) -> str:
    """
    Get the latest NAV for a mutual fund scheme.

    Args:
        scheme_code: Numeric scheme code, e.g. "125497". Use search_mf to find it.

    Returns:
        JSON with scheme name, fund house, latest NAV value, and date.
    """
    with _client() as client:
        response = client.get(f"/mf/{scheme_code}/latest")
        response.raise_for_status()
        result = response.json()

    return json.dumps(result, indent=2)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
