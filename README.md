# KTMANY – Unternehmenswebseite

Statische Webseite (HTML/CSS, etwas JavaScript für das Handymenü) – ohne Build-Schritt, ohne Cookies, ohne Tracking und ohne externe Schriften.

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

Alle Platzhalter sind auf den Seiten gelb markiert (`class="todo"`):

| Datei | Was |
|---|---|
| `impressum.html` | Rechtsform, Anschrift, Vertretungsberechtigte, Telefon, Handelsregister, USt-IdNr., Verantwortliche nach § 18 MStV |
| `datenschutz.html` | Rechtsform und Anschrift des Verantwortlichen |
| `index.html`, `impressum.html`, `datenschutz.html` | E-Mail `kontakt@ktmany.de` – durch die echte Adresse ersetzen, falls abweichend |

Impressum und Datenschutzerklärung sind Vorlagen – vor dem Livegang bitte rechtlich prüfen lassen.

## Aufbau

```
index.html          Startseite (Leistungen, Cyber Security, Vorgehen, Über uns, Kontakt)
impressum.html      Impressum (§ 5 DDG)
datenschutz.html    Datenschutzerklärung
404.html            Seite „nicht gefunden“
assets/style.css    Gestaltung (Farben oben als CSS-Variablen)
assets/main.js      Handymenü, Jahreszahl, Einblenden beim Scrollen
assets/favicon.svg  Logo-Zeichen
.nojekyll           GitHub Pages ohne Jekyll ausliefern
```

Lokal ansehen: `python3 -m http.server` im Ordner starten und http://localhost:8000 öffnen.
