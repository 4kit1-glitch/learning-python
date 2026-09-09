from pathlib import Path

x = Path("/home/kit/Kitstdios/learning-python/files_database") / "NIT.log"
t = [8,0,.02]
with x.open("w") as file:
    file.write(f"{t}")