# Kilómetro Real · distintivos propios de cada marca (iniciales + país). No son los logos oficiales.
ORIGIN = {"Abarth": "Italia", "Alfa Romeo": "Italia", "Alpine": "Francia", "Audi": "Alemania", "BMW": "Alemania", "BYD": "China",
    "Citroën": "Francia", "Cupra": "España", "DS": "Francia", "Dacia": "Rumanía", "Deepal": "China", "Dongfeng": "China", "Ebro": "España",
    "Fiat": "Italia", "Ford": "Estados Unidos", "Geely": "China", "Honda": "Japón", "Hyundai": "Corea del Sur", "Jaecoo": "China",
    "Jeep": "Estados Unidos", "KGM": "Corea del Sur", "Kia": "Corea del Sur", "Lancia": "Italia", "Land Rover": "Reino Unido",
    "Leapmotor": "China", "Lexus": "Japón", "Lynk & Co": "China", "MG": "China", "Mazda": "Japón", "Mercedes": "Alemania",
    "Mini": "Reino Unido", "Mitsubishi": "Japón", "Nissan": "Japón", "Omoda": "China", "Opel": "Alemania", "Peugeot": "Francia",
    "Polestar": "Suecia", "Porsche": "Alemania", "Renault": "Francia", "Seat": "España", "Skoda": "Chequia", "Smart": "Alemania y China",
    "Subaru": "Japón", "Suzuki": "Japón", "Tesla": "Estados Unidos", "Toyota": "Japón", "Volkswagen": "Alemania", "Volvo": "Suecia",
    "XPENG": "China", "Zeekr": "China"}
ORIGIN_EN = {"Italia": "Italy", "Francia": "France", "Alemania": "Germany", "China": "China", "España": "Spain", "Rumanía": "Romania",
    "Estados Unidos": "United States", "Japón": "Japan", "Corea del Sur": "South Korea", "Reino Unido": "United Kingdom",
    "Suecia": "Sweden", "Chequia": "Czechia", "Alemania y China": "Germany and China"}
# Color del sello según el país de origen (tonos oscuros con texto blanco, contraste AA)
TONE = {"China": "#9b1c1c", "Japón": "#7a1f3d", "Corea del Sur": "#1e4f8a", "Alemania": "#2b2f36", "Francia": "#1f3f8f", "Italia": "#17663a",
    "España": "#8a3b0c", "Rumanía": "#1d4f6e", "Estados Unidos": "#283a75", "Reino Unido": "#3f2a6b", "Suecia": "#0f5566", "Chequia": "#2f5a2a",
    "Alemania y China": "#4a2c2c"}

def initials(b):
    w = [x for x in b.replace("&", " ").replace("-", " ").split() if x]
    if len(w) > 1: return (w[0][0] + w[-1][0]).upper()
    return b[:2].upper() if b.isupper() else b[0].upper() + b[1].lower()

def badge(b, cls=""):
    o = ORIGIN.get(b, "")
    return f'<span class="bmark {cls}" style="--bm:{TONE.get(o, "#2b2f36")}" aria-hidden="true">{initials(b)}</span>'
