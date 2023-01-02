import os
import subprocess
from datetime import datetime, timedelta
import random

# 📌 CHEMIN DU DÉPÔT LOCAL (MODIFIE LE SI NÉCESSAIRE)
repo_path = "C:\\Users\\JIHED\\Downloads\\gitclone"  # Mets ton chemin exact ici
os.chdir(repo_path)

# 🔹 PARAMÈTRES : Commence en 2023 et finit en 2024 (Évite les Weekends)
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)

max_commits_per_day = 10  # 📌 Jusqu'à 10 commits par jour

# 🔹 BOUCLE POUR AJOUTER DES COMMITS RÉTROACTIFS
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() < 5:  # 📌 Éviter Samedi (5) et Dimanche (6)
        commits_today = random.randint(3, max_commits_per_day)
        for _ in range(commits_today):
            commit_time = (current_date + timedelta(seconds=random.randint(0, 86400))).strftime("%Y-%m-%d %H:%M:%S")
            with open("contribute.txt", "a") as f:
                f.write(f"Contribution du {commit_time}\n")
            subprocess.run(["git", "add", "contribute.txt"])
            subprocess.run(["git", "commit", "--date", commit_time, "-m", f"Contribution du {commit_time}"])

    current_date += timedelta(days=1)

# 🔹 POUSSER TOUS LES COMMITS EN FORCE
subprocess.run(["git", "push", "--force", "origin", "main"])
print("✅ Commits rétroactifs générés avec succès pour 2023 et 2024 !")
