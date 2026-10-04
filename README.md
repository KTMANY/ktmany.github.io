# KTMANY – Unternehmenswebseite

Zweisprachige statische Webseite (Deutsch unter `/`, Englisch unter `/en/`) aus HTML/CSS und etwas JavaScript für das Handymenü. Sie kommt ohne Cookies, ohne Tracking und ohne externe Schriften aus.

## Inhalte ändern

Alle Texte, Firmendaten und Produkte stehen in **`build.py`**, für beide Sprachen an einer Stelle (`COMPANY`, `TEXT["de"]`, `TEXT["en"]`). Die HTML-Dateien werden daraus erzeugt. Bitte nicht direkt bearbeiten, Änderungen dort gehen beim nächsten Erzeugen verloren.

```
python3 build.py     # erzeugt alle HTML-Seiten, sitemap.xml und robots.txt neu
git add -A && git commit -m "Texte aktualisiert" && git push
```

GitHub Pages braucht keinen Build. Die erzeugten Dateien werden mit eingecheckt.

## Veröffentlichen mit GitHub Pages

1. In der Organisation **KTMANY** ein **öffentliches** Repository mit dem Namen **`ktmany.github.io`** anlegen.
2. Diese Dateien in den Branch `main` hochladen (per `git push` oder im Browser über „Add file → Upload files“).
3. Unter **Settings → Pages** prüfen: *Source: Deploy from a branch*, Branch `main`, Ordner `/ (root)`.
4. Nach 1–2 Minuten ist die Seite unter **https://ktmany.github.io** erreichbar.

### Eigene Domain (später)

1. Domain (z. B. `ktmany.de`) bei einem Anbieter registrieren.
2. Datei `CNAME` mit dem Inhalt `www.ktmany.de` ins Repository legen (oder unter Settings → Pages → Custom domain eintragen).
3. Beim Domain-Anbieter einen CNAME-Eintrag `www` → `ktmany.github.io` anlegen (für die Domain ohne `www` die A-Einträge von GitHub Pages).
4. In Settings → Pages **Enforce HTTPS** aktivieren.

## Vor dem Veröffentlichen ausfüllen

Offene Angaben sind auf den Seiten gelb markiert. Sie werden in `build.py` im Block `COMPANY` eingetragen:

| Feld | Was |
|---|---|
| `register` | Registergericht und HRB-Nummer, z. B. `Amtsgericht Siegburg, HRB 12345` |
| `vat_id` | USt-IdNr., sobald erteilt |
| `email` | E-Mail-Adresse. Derzeit steht dort `kontakt@ktmany.de`; falls sie abweicht, ersetzen. |

Impressum und Datenschutzerklärung sind Vorlagen – vor dem Livegang bitte rechtlich prüfen lassen.

## Aufbau

```
build.py            Generator mit allen Texten (DE/EN)
index.html          Startseite DE (Leistungen, Produkte, Cyber Security, Vorgehen, Über uns, Kontakt)
impressum.html      Impressum (§ 5 DDG)
datenschutz.html    Datenschutzerklärung
en/                 Englische Fassung (index, imprint, privacy)
404.html            Seite „nicht gefunden“ (zweisprachig)
sitemap.xml         Sitemap mit hreflang-Verweisen
robots.txt
assets/style.css    Gestaltung (Farben oben als CSS-Variablen)
assets/main.js      Handymenü, Jahreszahl, Einblenden beim Scrollen
assets/favicon.svg  Logo-Zeichen
.nojekyll           GitHub Pages ohne Jekyll ausliefern
```

Lokal ansehen: `python3 -m http.server` im Ordner starten und http://localhost:8000 öffnen.
