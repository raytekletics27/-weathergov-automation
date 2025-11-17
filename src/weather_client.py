import requests
from typing import Dict, Any

# IMPORTANT: replace with your contact info per weather.gov API policy
# Example: "your-email@example.com (raytekletics27/weathergov-automation)"
USER_AGENT = "your-email@example.com (weathergov-automation)"

HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "application/geo+json"
}

def get_point(lat: float, lon: float, timeout: int = 10) -> Dict[str, Any]:
    """
    Query the Weather.gov points endpoint to get URLs for forecast and grid data.
    Returns the parsed JSON response.
    """
    url = f"https://api.weather.gov/points/{lat},{lon}"
    resp = requests.get(url, headers=HEADERS, timeout=timeout)
    resp.raise_for_status()
    return resp.json()

def get_forecast_by_point(lat: float, lon: float, timeout: int = 10) -> Dict[str, Any]:
    """
    Get the forecast (7-day forecast) for the given lat/lon by following the 'forecast' link
    returned in the points endpoint.
    """
    point = get_point(lat, lon, timeout=timeout)
    forecast_url = point.get("properties", {}).get("forecast")
    if not forecast_url:
        raise RuntimeError("Forecast URL not found in points response")
    resp = requests.get(forecast_url, headers=HEADERS, timeout=timeout)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    # Simple smoke test (run locally)
    lat, lon = 38.8894, -77.0352  # Example: Washington, D.C.
    try:
        data = get_forecast_by_point(lat, lon)
        props = data.get("properties", {})
        print("Forecast retrieved. Keys in properties:", list(props.keys()))
    except Exception as e:
        print("Error fetching forecast:", e)
