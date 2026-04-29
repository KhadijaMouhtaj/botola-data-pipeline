import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_FOOTBALL_KEY")

BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}

LEAGUE_ID = 200
SEASON = 2024

RAW_DIR = "data/raw"


def fetch_api(endpoint, params):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code != 200:
        raise Exception(f"API error {response.status_code}: {response.text}")

    data = response.json()

    if not data.get("response"):
        raise Exception(f"No data returned for endpoint: {endpoint}")

    return data


def get_standings():
    data = fetch_api("standings", {"league": LEAGUE_ID, "season": SEASON})
    standings = data["response"][0]["league"]["standings"][0]

    rows = []
    for team in standings:
        rows.append({
            "rank": team["rank"],
            "team": team["team"]["name"],
            "played": team["all"]["played"],
            "win": team["all"]["win"],
            "draw": team["all"]["draw"],
            "lose": team["all"]["lose"],
            "goals_for": team["all"]["goals"]["for"],
            "goals_against": team["all"]["goals"]["against"],
            "points": team["points"],
            "form": team["form"],
        })

    return pd.DataFrame(rows)


def get_top_scorers():
    data = fetch_api("players/topscorers", {"league": LEAGUE_ID, "season": SEASON})

    rows = []
    for item in data["response"]:
        stats = item["statistics"][0]

        rows.append({
            "player": item["player"]["name"],
            "team": stats["team"]["name"],
            "goals": stats["goals"]["total"],
            "assists": stats["goals"]["assists"],
            "games": stats["games"]["appearences"],
        })

    return pd.DataFrame(rows)


def get_fixtures():
    data = fetch_api("fixtures", {"league": LEAGUE_ID, "season": SEASON})

    rows = []
    for match in data["response"]:
        rows.append({
            "date": match["fixture"]["date"][:10],
            "home_team": match["teams"]["home"]["name"],
            "away_team": match["teams"]["away"]["name"],
            "home_goals": match["goals"]["home"],
            "away_goals": match["goals"]["away"],
            "status": match["fixture"]["status"]["short"],
        })

    return pd.DataFrame(rows)


def save_raw_data():
    os.makedirs(RAW_DIR, exist_ok=True)

    print("Fetching standings...")
    get_standings().to_csv(f"{RAW_DIR}/standings.csv", index=False)

    print("Fetching top scorers...")
    get_top_scorers().to_csv(f"{RAW_DIR}/top_scorers.csv", index=False)

    print("Fetching fixtures...")
    get_fixtures().to_csv(f"{RAW_DIR}/fixtures.csv", index=False)

    print("Raw data saved successfully.")


if __name__ == "__main__":
    save_raw_data()