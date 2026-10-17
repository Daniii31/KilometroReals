# -*- coding: utf-8 -*-
"""Resume los precios de todas las gasolineras de España (API del Ministerio) por provincia.
Uso: python3 tools/provincias.py estaciones.json provincias.json
La API: https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/
La GitHub Action .github/workflows/precios-provincias.yml lo ejecuta cada mañana."""
import json, sys, re

PROV = {"01": ("Álava", "alava"), "02": ("Albacete", "albacete"), "03": ("Alicante", "alicante"), "04": ("Almería", "almeria"),
 "05": ("Ávila", "avila"), "06": ("Badajoz", "badajoz"), "07": ("Baleares", "baleares"), "08": ("Barcelona", "barcelona"),
 "09": ("Burgos", "burgos"), "10": ("Cáceres", "caceres"), "11": ("Cádiz", "cadiz"), "12": ("Castellón", "castellon"),
 "13": ("Ciudad Real", "ciudad-real"), "14": ("Córdoba", "cordoba"), "15": ("A Coruña", "a-coruna"), "16": ("Cuenca", "cuenca"),
 "17": ("Girona", "girona"), "18": ("Granada", "granada"), "19": ("Guadalajara", "guadalajara"), "20": ("Gipuzkoa", "gipuzkoa"),
 "21": ("Huelva", "huelva"), "22": ("Huesca", "huesca"), "23": ("Jaén", "jaen"), "24": ("León", "leon"), "25": ("Lleida", "lleida"),
 "26": ("La Rioja", "la-rioja"), "27": ("Lugo", "lugo"), "28": ("Madrid", "madrid"), "29": ("Málaga", "malaga"), "30": ("Murcia", "murcia"),
 "31": ("Navarra", "navarra"), "32": ("Ourense", "ourense"), "33": ("Asturias", "asturias"), "34": ("Palencia", "palencia"),
 "35": ("Las Palmas", "las-palmas"), "36": ("Pontevedra", "pontevedra"), "37": ("Salamanca", "salamanca"),
 "38": ("Santa Cruz de Tenerife", "santa-cruz-de-tenerife"), "39": ("Cantabria", "cantabria"), "40": ("Segovia", "segovia"),
 "41": ("Sevilla", "sevilla"), "42": ("Soria", "soria"), "43": ("Tarragona", "tarragona"), "44": ("Teruel", "teruel"),
 "45": ("Toledo", "toledo"), "46": ("Valencia", "valencia"), "47": ("Valladolid", "valladolid"), "48": ("Bizkaia", "bizkaia"),
 "49": ("Zamora", "zamora"), "50": ("Zaragoza", "zaragoza"), "51": ("Ceuta", "ceuta"), "52": ("Melilla", "melilla")}
FIELDS = {"g95": "Precio Gasolina 95 E5", "g98": "Precio Gasolina 98 E5", "die": "Precio Gasoleo A",
          "die_plus": "Precio Gasoleo Premium", "glp": "Precio Gases licuados del petróleo"}
SMALL = {"de", "del", "la", "las", "el", "los", "y", "a", "en"}

def price(v):
    try: p = float(str(v).replace(",", "."))
    except ValueError: return None
    return p if 0.4 < p < 4 else None

def nice(s):
    s = re.sub(r"\s+", " ", (s or "").strip())
    words = s.lower().split(" ")
    out = [w if (i and w in SMALL) else (w[:1].upper() + w[1:]) for i, w in enumerate(words)]
    s = re.sub(r"([/(\-])(\w)", lambda m: m.group(1) + m.group(2).upper(), " ".join(out))
    s = re.sub(r"\b(E\.s\.|Ee\.ss\.)", lambda m: m.group(1).upper(), s)
    return re.sub(r"\b(Km|Kms)\b", "km", s).replace("Nº", "nº")

def muni(s):
    """'Palmas de Gran Canaria (Las)' -> 'Las Palmas de Gran Canaria'"""
    m = re.match(r"^(.*)\s+\(([^)]+)\)$", s.strip())
    if m: s = f"{m.group(2)} {m.group(1)}"
    return nice(s)

def avg(xs): return round(sum(xs) / len(xs), 3) if xs else None

def main(src, dst):
    D = json.load(open(src, encoding="utf-8-sig"))
    rows = D.get("ListaEESSPrecio") or []
    if len(rows) < 5000: raise SystemExit(f"Datos incompletos: {len(rows)} gasolineras")
    fecha = D.get("Fecha", "")
    m = re.match(r"(\d{2})/(\d{2})/(\d{4})", fecha)
    date = f"{m.group(3)}-{m.group(2)}-{m.group(1)}" if m else ""
    by = {k: [] for k in PROV}
    for r in rows:
        if r.get("Tipo Venta", "P") != "P": continue
        pid = str(r.get("IDProvincia", "")).zfill(2)
        if pid not in by: continue
        st = {"r": nice(r.get("Rótulo", "")) or "Sin marca", "d": nice(r.get("Dirección", "")), "l": muni(r.get("Municipio", "") or r.get("Localidad", "")),
              "cp": r.get("C.P.", ""), "lat": r.get("Latitud", "").replace(",", "."), "lon": r.get("Longitud (WGS84)", "").replace(",", ".")}
        for k, f in FIELDS.items():
            p = price(r.get(f))
            if p: st[k] = p
        by[pid].append(st)
    nat = {k: avg([s[k] for v in by.values() for s in v if k in s]) for k in FIELDS}
    out = {"fecha": fecha, "date": date, "n": sum(len(v) for v in by.values()), "nac": nat, "prov": []}
    for pid, (name, slug) in PROV.items():
        S = by[pid]
        if not S: continue
        P = {"id": pid, "name": name, "slug": slug, "n": len(S), "avg": {k: avg([s[k] for s in S if k in s]) for k in FIELDS}, "cheap": {}, "dear": {}, "muni": []}
        for k in ("g95", "die", "glp"):
            have = sorted([s for s in S if k in s], key=lambda s: s[k])
            if not have: continue
            P["cheap"][k] = [{x: s[x] for x in ("r", "d", "l", "cp", "lat", "lon", k)} for s in have[:10]]
            P["dear"][k] = have[-1][k]
        towns = {}
        for s in S: towns.setdefault(s["l"], []).append(s)
        mu = [{"l": t, "n": len(v), "g95": avg([s["g95"] for s in v if "g95" in s]), "die": avg([s["die"] for s in v if "die" in s])} for t, v in towns.items() if len(v) >= 3]
        mu = [x for x in mu if x["g95"] and x["die"]]
        P["muni"] = sorted(mu, key=lambda x: x["g95"])[:10]
        P["big"] = sorted(mu, key=lambda x: -x["n"])[:6]
        out["prov"].append(P)
    json.dump(out, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=0, separators=(",", ":"))
    print("OK", out["n"], "gasolineras,", len(out["prov"]), "provincias,", fecha)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
