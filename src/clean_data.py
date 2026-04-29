
import pandas as pd
import os

os.makedirs("data/clean", exist_ok=True)

# ── 1. STANDINGS ──────────────────────────────────────
df_s = pd.read_csv("./data/standings.csv")

# Calcul différence de buts
df_s["goal_diff"] = df_s["goals_for"] - df_s["goals_against"]

# Calcul % victoires
df_s["win_rate"] = (df_s["win"] / df_s["played"] * 100).round(1)

# Forme : convertir "WDLWW" en score numérique
# W=3, D=1, L=0 sur les 5 derniers matchs
def form_score(form_str):
    if pd.isna(form_str):
        return 0
    score_map = {"W": 3, "D": 1, "L": 0}
    return sum(score_map.get(c, 0) for c in form_str[-5:])

df_s["form_score"] = df_s["form"].apply(form_score)

# Statut zone (title/europe/safe/relegation)
def get_zone(rank):
    if rank == 1:   return "Champion"
    if rank <= 3:   return "CAF"
    if rank <= 13:  return "Safe"
    return "Relegation"

df_s["zone"] = df_s["rank"].apply(get_zone)

df_s.to_csv("data/clean/standings_clean.csv", index=False)
print("standings_clean.csv — OK")


# ── 2. TOP SCORERS ────────────────────────────────────
df_sc = pd.read_csv("data/top_scorers.csv")

# Remplir les NaN assists par 0
df_sc["assists"] = df_sc["assists"].fillna(0).astype(int)

# Contribution totale (buts + passes)
df_sc["contributions"] = df_sc["goals"] + df_sc["assists"]

# Moyenne de buts par match
df_sc["goals_per_game"] = (df_sc["goals"] / df_sc["games"]).round(2)

# Supprimer les lignes sans buts
df_sc = df_sc[df_sc["goals"] > 0].reset_index(drop=True)

df_sc.to_csv("data/clean/scorers_clean.csv", index=False)
print("scorers_clean.csv — OK")


# ── 3. FIXTURES ───────────────────────────────────────
df_f = pd.read_csv("data/fixtures.csv")

# Garder seulement les matchs terminés
df_done = df_f[df_f["status"] == "FT"].copy()

# Convertir la date
df_done["date"] = pd.to_datetime(df_done["date"])
df_done["month"] = df_done["date"].dt.strftime("%Y-%m")

# Résultat du match (H/D/A)
def get_result(row):
    if row["home_goals"] > row["away_goals"]:  return "Home win"
    if row["home_goals"] < row["away_goals"]:  return "Away win"
    return "Draw"

df_done["result"] = df_done.apply(get_result, axis=1)

# Total buts par match
df_done["total_goals"] = df_done["home_goals"] + df_done["away_goals"]

df_done.to_csv("data/clean/fixtures_clean.csv", index=False)
print("fixtures_clean.csv — OK")

print("\nResume des donnees propres :")
print(f"  Standings : {len(df_s)} equipes")
print(f"  Scorers   : {len(df_sc)} joueurs")
print(f"  Fixtures  : {len(df_done)} matchs termines")