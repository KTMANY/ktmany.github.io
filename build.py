#!/usr/bin/env python3
"""
Erzeugt die Webseite in Deutsch (/) und Englisch (/en/) aus einer gemeinsamen Vorlage.

Texte ändern: unten in TEXT (je Sprache) bzw. COMPANY anpassen, dann `python3 build.py` ausführen
und die erzeugten HTML-Dateien committen. Keine Abhängigkeiten außer Python 3.
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).parent

COMPANY = {
    "name": "KTMANY UG (haftungsbeschränkt)",
    "street": "Rheinstr. 14",
    "city": "53757 Sankt Augustin",
    "country_de": "Deutschland",
    "country_en": "Germany",
    "managers": ["Nayim Yerlikaya", "Kaan Tugay Mehmet Aydin"],
    "phone": "+49 151 54059552",
    "phone_href": "+4915154059552",
    "email": "kontakt@ktmany.de",
    # sobald vorhanden eintragen, z. B. "Amtsgericht Siegburg, HRB 12345" bzw. "DE123456789"
    "register": "",
    "vat_id": "",
    "github": "https://github.com/KTMANY",
}

# ---------------------------------------------------------------- Symbole (Lucide-Stil, inline)

ICONS = {
    "cloud": '<path d="M17.5 19a4.5 4.5 0 1 0-1.4-8.8 6 6 0 0 0-11.6 2A4 4 0 0 0 6 19h11.5z"/>',
    "monitor": '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 8h18M8 21h8M12 18v3"/>',
    "phone": '<rect x="7" y="2" width="10" height="20" rx="2.5"/><path d="M11 18h2"/>',
    "ai": '<path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4M5.6 18.4 7 17M17 7l1.4-1.4"/><circle cx="12" cy="12" r="4"/><path d="M12 10v4M10 12h4"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "shieldcheck": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5v14z"/><path d="M8 7h8M8 11h6"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
    "checklist": '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>',
    "code": '<path d="m16 18 6-6-6-6M8 6l-6 6 6 6"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "alert": '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
    "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
    "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21.2l8.8-8.8a5.5 5.5 0 0 0 0-7.8z"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "wrench": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/>',
    "camera": '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
    "rings": '<circle cx="9" cy="14" r="6"/><circle cx="15" cy="14" r="6"/><path d="m10 3 2 3 2-3"/>',
    "apple": '<path d="M12 7c-1.5-1-4-1.3-5.6.3C4.5 9.2 4.7 13 6.5 16c1.3 2.2 3 4 4.5 3.5.6-.2 1-.5 1-.5s.4.3 1 .5c1.5.5 3.2-1.3 4.5-3.5 1.8-3 2-6.8.1-8.7C16 5.7 13.5 6 12 7z"/><path d="M12 7c0-2 1-4 3-4"/>',
}


def icon(name: str, cls: str = "") -> str:
    attrs = f' class="{cls}"' if cls else ""
    return (
        f'<svg{attrs} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'
    )


# ---------------------------------------------------------------- Texte

TEXT = {
    "de": {
        "lang": "de",
        "locale": "de_DE",
        "title": "KTMANY – Software, KI & Cyber-Security-Beratung",
        "description": "KTMANY entwickelt SaaS-Produkte, Webanwendungen und Mobile Apps mit künstlicher Intelligenz und berät Unternehmen in Cyber Security und BSI IT-Grundschutz.",
        "skip": "Zum Inhalt springen",
        "menu_open": "Menü öffnen",
        "nav": [("leistungen", "Leistungen"), ("produkte", "Produkte"), ("security", "Cyber Security"), ("vorgehen", "Vorgehen"), ("ueber-uns", "Über uns")],
        "nav_contact": "Kontakt",
        "switch_label": "English",
        "switch_short": "EN",
        "hero_eyebrow": "Software · KI · Cyber Security",
        "hero_h1": 'Software mit KI. <span class="grad">Sicher von Anfang an.</span>',
        "hero_lead": "KTMANY entwickelt SaaS-Produkte, Webanwendungen und Mobile Apps mit künstlicher Intelligenz – und berät Unternehmen in Cyber Security und BSI IT-Grundschutz. Moderne Technik, klare Prozesse und Sicherheit als fester Bestandteil jedes Projekts.",
        "hero_cta": "Projekt anfragen",
        "hero_cta2": "Unsere Produkte",
        "hero_points": ["Security by Design", "KI, wo sie Nutzen bringt", "DSGVO-konform"],
        "panel": [
            ("KI-Analyse", "Bild &amp; Text", "badge-ok", "Aktiv"),
            ("Security-Scan", "Abhängigkeiten &amp; Code", "badge-ok", "0 kritisch"),
            ("IT-Grundschutz-Check", "Basis-Absicherung", "badge-info", "Geprüft"),
            ("Notfallvorsorge", "Wiederherstellungstest", "badge-warn", "Geplant"),
        ],
        "panel_foot": "Sicherheitsniveau",
        "services_eyebrow": "Leistungen",
        "services_h2": "Von der Idee zum sicheren, intelligenten Produkt",
        "services_lead": "Wir entwickeln eigene Produkte und setzen Software für Kunden um – mit dem gleichen Anspruch an Qualität, Benutzerfreundlichkeit und Sicherheit.",
        "services": [
            ("cloud", "SaaS-Produkte", "Eigene Software-as-a-Service-Lösungen, die konkrete Probleme lösen – skalierbar, wartungsarm und aus der Cloud.", ["Mandantenfähige Plattformen", "Abo- und Lizenzmodelle", "Betrieb &amp; Monitoring"]),
            ("monitor", "Webanwendungen", "Individuelle Webanwendungen und Portale – schnell, barrierearm und mit sauberer Architektur, die mitwächst.", ["Kundenportale &amp; Dashboards", "Schnittstellen (APIs)", "Progressive Web Apps"]),
            ("phone", "Mobile Apps", "Apps für Android und iOS, die gern genutzt werden – mit Offline-Fähigkeit, Push-Benachrichtigungen und sicherer Datenhaltung.", ["Android &amp; iOS", "Anbindung von Geräte- &amp; Gesundheitsdaten", "Veröffentlichung in den Stores"]),
            ("ai", "KI-Lösungen", "Künstliche Intelligenz dort, wo sie echte Arbeit abnimmt: Bilder und Dokumente verstehen, Texte erzeugen, Abläufe automatisieren.", ["Bild- &amp; Dokumentenanalyse", "Assistenten &amp; Textgenerierung", "Datenschutzkonformer KI-Einsatz"]),
            ("shield", "Cyber-Security-Beratung", "Wir machen Risiken sichtbar und bringen Ihre IT-Sicherheit Schritt für Schritt auf ein Niveau, das zu Ihrem Unternehmen passt.", ["Sicherheits-Check &amp; Risikoanalyse", "NIS2- &amp; ISO-27001-Vorbereitung", "Security by Design"]),
            ("book", "IT-Grundschutz &amp; Beratung", "Informationssicherheit nach der bewährten Methodik des BSI – strukturiert, nachweisbar und passend zur Größe Ihres Unternehmens.", ["BSI IT-Grundschutz-Check", "Sicherheitskonzepte &amp; Richtlinien", "Begleitung bis zur Zertifizierungsreife"]),
        ],
        "products_eyebrow": "Produkte",
        "products_h2": "Unsere Produkte",
        "products_lead": "Software, die wir selbst entwickeln und betreiben – jeweils mit KI dort, wo sie den Alltag spürbar erleichtert.",
        "products": [
            ("wrench", "Handwerker-CRM", "In Entwicklung", "badge-info", "Kundenverwaltung für Handwerksbetriebe: Kunden, Angebote, Aufträge, Termine und Rechnungen an einem Ort – im Büro und mobil auf der Baustelle."),
            ("camera", "KI-Schadensgutachten", "In Entwicklung", "badge-info", "Schäden fotografieren, die KI erkennt Art und Umfang und erstellt einen strukturierten Gutachten-Entwurf – schneller und einheitlicher für Sachverständige."),
            ("rings", "B2B-Plattform für Hochzeiten", "In Entwicklung", "badge-info", "Die Plattform für die Hochzeitsbranche: vernetzt Locations, Dienstleister und Planer – Anfragen, Angebote und Termine an einem Ort."),
            ("apple", "MealGlance", "Beta", "badge-ok", "KI-Ernährungstagebuch als App: Essen fotografieren, Nährwerte erhalten, passend zu LOGI, Keto &amp; Co. – mit Fitnessdaten-Sync und persönlichem Körper-Labor."),
        ],
        "sec_eyebrow": "Cyber Security &amp; Beratung",
        "sec_h2": "Sicherheit, die sich am Risiko orientiert – nicht an Schlagworten",
        "sec_lead": "Gerade kleine und mittlere Unternehmen sind beliebte Ziele. Wir helfen, die wichtigsten Schwachstellen zuerst zu schließen – verständlich erklärt und mit einem klaren Plan.",
        "grundschutz_h3": "BSI IT-Grundschutz",
        "grundschutz_text": "Der IT-Grundschutz des Bundesamts für Sicherheit in der Informationstechnik (BSI) ist der bewährte Standard für Informationssicherheit in Deutschland. Wir begleiten Sie von der ersten Bestandsaufnahme bis zum belastbaren Sicherheitskonzept.",
        "grundschutz_points": [
            "Strukturanalyse &amp; Schutzbedarfsfeststellung",
            "Modellierung nach dem IT-Grundschutz-Kompendium",
            "IT-Grundschutz-Check (Soll-Ist-Vergleich)",
            "Basis-, Standard- oder Kern-Absicherung",
            "Risikoanalyse nach BSI-Standard 200-3",
            "Vorbereitung auf ISO 27001 auf Basis von IT-Grundschutz",
        ],
        "sec_items": [
            ("search", "Sicherheits-Check", "Bestandsaufnahme Ihrer IT, Cloud-Dienste und Anwendungen. Ergebnis: eine priorisierte Liste der Risiken und konkreter Maßnahmen."),
            ("checklist", "NIS2 &amp; ISO 27001", "Wir prüfen, ob Sie von NIS2 betroffen sind, und begleiten den Aufbau eines Informationssicherheits-Managements (ISMS)."),
            ("code", "Security by Design", "Sicherheit gehört in die Architektur, nicht ans Ende. Wir unterstützen Teams bei Threat Modeling, sicherem Code und Reviews."),
            ("lock", "Cloud &amp; Zugriffe", "Sichere Konfiguration von Cloud-Umgebungen, Microsoft 365 und Identitäten – mit Mehr-Faktor-Anmeldung und minimalen Rechten."),
            ("alert", "Notfallvorsorge", "Backup-Konzept, Notfallplan und Übungen – damit im Ernstfall jeder weiß, was zu tun ist, und der Betrieb schnell wieder läuft."),
            ("users", "Awareness", "Praxisnahe Schulungen zu Phishing, Passwörtern und sicherem Arbeiten – denn die meisten Angriffe beginnen beim Menschen."),
        ],
        "chips": ["BSI IT-Grundschutz", "ISO/IEC 27001", "NIS2", "DSGVO", "OWASP"],
        "steps_eyebrow": "Vorgehen",
        "steps_h2": "So arbeiten wir zusammen",
        "steps_lead": "Transparent, in kurzen Schritten und mit messbaren Ergebnissen – egal ob neues Produkt oder Sicherheitsprojekt.",
        "steps": [
            ("Verstehen", "Im Erstgespräch klären wir Ziele, Rahmenbedingungen und Risiken. Kostenlos und unverbindlich."),
            ("Planen", "Sie erhalten ein klares Konzept mit Prioritäten, Aufwand und Zeitplan – ohne versteckte Kosten."),
            ("Umsetzen", "Agile Entwicklung bzw. Umsetzung der Maßnahmen in kurzen Zyklen, mit regelmäßigen Zwischenständen."),
            ("Begleiten", "Betrieb, Weiterentwicklung und regelmäßige Sicherheitsprüfungen – damit Ihre Lösung sicher bleibt."),
        ],
        "about_eyebrow": "Über uns",
        "about_h2": "Warum KTMANY?",
        "about_lead": "Wir verbinden Produktentwicklung, künstliche Intelligenz und Sicherheitsberatung unter einem Dach. Das Ergebnis: Software, die von Anfang an sicher gebaut ist.",
        "values": [
            ("shield", "Sicherheit im Kern", "Jedes Projekt startet mit einer Risikobetrachtung. Sicherheit ist bei uns kein Zusatzpaket, sondern Standard."),
            ("globe", "Datenschutz nach DSGVO", "Datensparsam, mit klaren Verträgen und Hosting-Optionen in der EU – auch auf eigener Infrastruktur."),
            ("ai", "KI mit Augenmaß", "Wir setzen KI dort ein, wo sie messbar hilft – nachvollziehbar, datenschutzkonform und mit dem Menschen als letzter Instanz."),
            ("heart", "Partnerschaft auf Augenhöhe", "Kurze Wege, direkte Ansprechpartner und ehrliche Empfehlungen – auch wenn die Antwort einmal „weniger ist mehr“ lautet."),
        ],
        "founding_eyebrow": "Jetzt in der Gründung",
        "founding_h2": "Werden Sie einer unserer ersten Partner",
        "founding_text": "KTMANY befindet sich im Aufbau. Für unsere ersten Kunden bedeutet das: besonders viel Aufmerksamkeit, direkte Mitgestaltung unserer Produkte und attraktive Konditionen für Pilotprojekte.",
        "founding_cta": "Pilotprojekt besprechen",
        "founding_points": ["Kostenloses Erstgespräch", "Direkter Draht zur Geschäftsführung", "Frühzeitiger Zugang zu neuen Produkten", "Sonderkonditionen für Pilotkunden"],
        "contact_eyebrow": "Kontakt",
        "contact_h2": "Lassen Sie uns über Ihr Vorhaben sprechen",
        "contact_text": "Ob neues Produkt, KI-Idee oder Sicherheitsfrage – schreiben Sie uns. Wir melden uns in der Regel innerhalb von zwei Werktagen.",
        "contact_cta": "E-Mail schreiben",
        "mail_subject": "Anfrage%20%C3%BCber%20die%20Webseite",
        "contact_labels": ("E-Mail", "Telefon", "Anschrift", "GitHub"),
        "rights": "Alle Rechte vorbehalten.",
        "legal_nav": "Rechtliches",
        "imprint": "Impressum",
        "privacy": "Datenschutz",
        "home": "Zur Startseite",
    },
    "en": {
        "lang": "en",
        "locale": "en_GB",
        "title": "KTMANY – Software, AI & Cyber Security Consulting",
        "description": "KTMANY builds SaaS products, web applications and mobile apps powered by artificial intelligence, and advises companies on cyber security and BSI IT-Grundschutz.",
        "skip": "Skip to content",
        "menu_open": "Open menu",
        "nav": [("leistungen", "Services"), ("produkte", "Products"), ("security", "Cyber Security"), ("vorgehen", "Approach"), ("ueber-uns", "About")],
        "nav_contact": "Contact",
        "switch_label": "Deutsch",
        "switch_short": "DE",
        "hero_eyebrow": "Software · AI · Cyber Security",
        "hero_h1": 'Software with AI. <span class="grad">Secure from day one.</span>',
        "hero_lead": "KTMANY builds SaaS products, web applications and mobile apps powered by artificial intelligence – and advises companies on cyber security and BSI IT-Grundschutz. Modern technology, clear processes and security built into every project.",
        "hero_cta": "Start a project",
        "hero_cta2": "Our products",
        "hero_points": ["Security by design", "AI where it adds value", "GDPR compliant"],
        "panel": [
            ("AI analysis", "Image &amp; text", "badge-ok", "Active"),
            ("Security scan", "Dependencies &amp; code", "badge-ok", "0 critical"),
            ("IT-Grundschutz check", "Basic protection", "badge-info", "Verified"),
            ("Disaster recovery", "Restore test", "badge-warn", "Scheduled"),
        ],
        "panel_foot": "Security level",
        "services_eyebrow": "Services",
        "services_h2": "From idea to secure, intelligent product",
        "services_lead": "We develop our own products and build software for clients – with the same standards of quality, usability and security.",
        "services": [
            ("cloud", "SaaS products", "Our own software-as-a-service solutions that solve real problems – scalable, low-maintenance and cloud-based.", ["Multi-tenant platforms", "Subscription &amp; licensing models", "Operations &amp; monitoring"]),
            ("monitor", "Web applications", "Custom web applications and portals – fast, accessible and built on a clean architecture that grows with you.", ["Customer portals &amp; dashboards", "APIs &amp; integrations", "Progressive web apps"]),
            ("phone", "Mobile apps", "Apps for Android and iOS that people enjoy using – with offline support, push notifications and secure data storage.", ["Android &amp; iOS", "Device &amp; health data integration", "App store publishing"]),
            ("ai", "AI solutions", "Artificial intelligence where it takes real work off your hands: understanding images and documents, generating text, automating workflows.", ["Image &amp; document analysis", "Assistants &amp; text generation", "Privacy-compliant AI"]),
            ("shield", "Cyber security consulting", "We make risks visible and raise your IT security step by step to a level that fits your organisation.", ["Security check &amp; risk analysis", "NIS2 &amp; ISO 27001 readiness", "Security by design"]),
            ("book", "IT-Grundschutz &amp; consulting", "Information security following the proven methodology of the German Federal Office for Information Security (BSI) – structured, verifiable and scaled to your business.", ["BSI IT-Grundschutz check", "Security concepts &amp; policies", "Support up to certification readiness"]),
        ],
        "products_eyebrow": "Products",
        "products_h2": "Our products",
        "products_lead": "Software we build and run ourselves – each using AI where it makes everyday work noticeably easier.",
        "products": [
            ("wrench", "CRM for tradespeople", "In development", "badge-info", "Customer management for trade businesses: customers, quotes, jobs, appointments and invoices in one place – in the office and on site."),
            ("camera", "AI damage assessment", "In development", "badge-info", "Photograph the damage, the AI identifies type and extent and drafts a structured assessment report – faster and more consistent for surveyors."),
            ("rings", "B2B wedding platform", "In development", "badge-info", "The platform for the wedding industry: connects venues, vendors and planners – enquiries, offers and dates in one place."),
            ("apple", "MealGlance", "Beta", "badge-ok", "AI food diary app: snap a photo of your meal, get the nutrition facts, matched to LOGI, keto and more – with fitness data sync and a personal body lab."),
        ],
        "sec_eyebrow": "Cyber security &amp; consulting",
        "sec_h2": "Security driven by risk – not by buzzwords",
        "sec_lead": "Small and medium-sized businesses are popular targets. We help you close the most important gaps first – clearly explained and with a concrete plan.",
        "grundschutz_h3": "BSI IT-Grundschutz",
        "grundschutz_text": "IT-Grundschutz by the German Federal Office for Information Security (BSI) is the established standard for information security in Germany. We support you from the first inventory to a robust security concept.",
        "grundschutz_points": [
            "Structure analysis &amp; protection requirements",
            "Modelling according to the IT-Grundschutz Compendium",
            "IT-Grundschutz check (target/actual comparison)",
            "Basic, standard or core protection",
            "Risk analysis according to BSI Standard 200-3",
            "Preparation for ISO 27001 based on IT-Grundschutz",
        ],
        "sec_items": [
            ("search", "Security check", "An inventory of your IT, cloud services and applications. Result: a prioritised list of risks and concrete measures."),
            ("checklist", "NIS2 &amp; ISO 27001", "We assess whether NIS2 applies to you and support you in building an information security management system (ISMS)."),
            ("code", "Security by design", "Security belongs in the architecture, not at the end. We support teams with threat modelling, secure code and reviews."),
            ("lock", "Cloud &amp; access", "Secure configuration of cloud environments, Microsoft 365 and identities – with multi-factor authentication and least privilege."),
            ("alert", "Business continuity", "Backup strategy, incident response plan and exercises – so everyone knows what to do and operations recover quickly."),
            ("users", "Awareness", "Practical training on phishing, passwords and secure work habits – because most attacks start with people."),
        ],
        "chips": ["BSI IT-Grundschutz", "ISO/IEC 27001", "NIS2", "GDPR", "OWASP"],
        "steps_eyebrow": "Approach",
        "steps_h2": "How we work together",
        "steps_lead": "Transparent, in short iterations and with measurable results – whether it is a new product or a security project.",
        "steps": [
            ("Understand", "In an initial call we clarify goals, constraints and risks. Free of charge and without obligation."),
            ("Plan", "You receive a clear concept with priorities, effort and timeline – no hidden costs."),
            ("Deliver", "Agile development or implementation of measures in short cycles, with regular progress updates."),
            ("Support", "Operations, further development and regular security reviews – so your solution stays secure."),
        ],
        "about_eyebrow": "About us",
        "about_h2": "Why KTMANY?",
        "about_lead": "We combine product development, artificial intelligence and security consulting under one roof. The result: software that is secure by design.",
        "values": [
            ("shield", "Security at the core", "Every project starts with a risk assessment. Security is not an add-on for us – it is the default."),
            ("globe", "GDPR-compliant privacy", "Data minimisation, clear contracts and hosting options in the EU – including on your own infrastructure."),
            ("ai", "AI with good judgement", "We use AI where it measurably helps – transparent, privacy-compliant and with humans in control."),
            ("heart", "Partnership on equal terms", "Short communication paths, direct contacts and honest advice – even when the answer is “less is more”."),
        ],
        "founding_eyebrow": "Now founding",
        "founding_h2": "Become one of our first partners",
        "founding_text": "KTMANY is in its founding phase. For our first clients this means: extra attention, direct influence on our products and attractive terms for pilot projects.",
        "founding_cta": "Discuss a pilot project",
        "founding_points": ["Free initial consultation", "Direct line to the managing directors", "Early access to new products", "Special terms for pilot clients"],
        "contact_eyebrow": "Contact",
        "contact_h2": "Let’s talk about your project",
        "contact_text": "A new product, an AI idea or a security question – get in touch. We usually reply within two business days.",
        "contact_cta": "Send an e-mail",
        "mail_subject": "Enquiry%20via%20website",
        "contact_labels": ("E-mail", "Phone", "Address", "GitHub"),
        "rights": "All rights reserved.",
        "legal_nav": "Legal",
        "imprint": "Legal notice",
        "privacy": "Privacy",
        "home": "Back to home",
    },
}

# Seitenpfade je Sprache (Schlüssel → Datei)
PAGES = {
    "de": {"index": "index.html", "imprint": "impressum.html", "privacy": "datenschutz.html"},
    "en": {"index": "en/index.html", "imprint": "en/imprint.html", "privacy": "en/privacy.html"},
}
BASE = "https://ktmany.github.io/"


def rel(from_lang: str, path: str) -> str:
    """Relativer Link von einer Seite der Sprache from_lang zu path (vom Wurzelverzeichnis aus)."""
    return ("../" if from_lang == "en" else "") + path


def link_to(from_lang: str, to_lang: str, page: str) -> str:
    target = PAGES[to_lang][page]
    if target.endswith("index.html"):
        target = target[: -len("index.html")] or "./"
        if from_lang == "en" and target == "./":
            return "../"
    return rel(from_lang, target)


# ---------------------------------------------------------------- Bausteine

LOGO = (
    '<svg viewBox="0 0 32 32" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="#2f6bff"/><stop offset="1" stop-color="#00c2ff"/></linearGradient></defs>'
    '<rect width="32" height="32" rx="9" fill="url(#lg)"/>'
    '<path d="M10 8v16M10 16l9-8M13 13.5L21 24" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>'
)


def head(lang: str, page: str, title: str, description: str, noindex: bool = False) -> str:
    t = TEXT[lang]
    alt = "en" if lang == "de" else "de"
    canonical = BASE + PAGES[lang][page].replace("index.html", "")
    alt_url = BASE + PAGES[alt][page].replace("index.html", "")
    de_url = BASE + PAGES["de"][page].replace("index.html", "")
    robots = '\n    <meta name="robots" content="noindex, follow" />' if noindex else ""
    return f"""<!doctype html>
<html lang="{t['lang']}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{escape(title)}</title>
    <meta name="description" content="{escape(description)}" />{robots}
    <meta name="theme-color" content="#050b1a" />
    <link rel="canonical" href="{canonical}" />
    <link rel="alternate" hreflang="{lang}" href="{canonical}" />
    <link rel="alternate" hreflang="{alt}" href="{alt_url}" />
    <link rel="alternate" hreflang="x-default" href="{de_url}" />
    <link rel="icon" href="{rel(lang, 'assets/favicon.svg')}" type="image/svg+xml" />
    <link rel="stylesheet" href="{rel(lang, 'assets/style.css')}" />
    <meta property="og:title" content="{escape(title)}" />
    <meta property="og:description" content="{escape(description)}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{canonical}" />
    <meta property="og:locale" content="{t['locale']}" />
  </head>
  <body>
    <a class="skip-link" href="#inhalt">{t['skip']}</a>
"""


def lang_switch(lang: str, page: str) -> str:
    t = TEXT[lang]
    other = "en" if lang == "de" else "de"
    return (
        f'<a class="lang-switch" href="{link_to(lang, other, page)}" hreflang="{other}" lang="{other}" '
        f'aria-label="{t["switch_label"]}">{icon("globe")}{t["switch_short"]}</a>'
    )


def header_home(lang: str) -> str:
    t = TEXT[lang]
    links = "\n".join(f'          <li><a href="#{a}">{label}</a></li>' for a, label in t["nav"])
    return f"""    <header class="site-header">
      <div class="container nav">
        <a class="brand" href="#top" aria-label="KTMANY">{LOGO}KTMANY</a>
        <button class="nav-toggle" aria-expanded="false" aria-controls="menu" aria-label="{t['menu_open']}">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" /></svg>
        </button>
        <ul class="nav-links" id="menu">
{links}
          <li>{lang_switch(lang, 'index')}</li>
          <li><a class="btn btn-primary" href="#kontakt">{t['nav_contact']}</a></li>
        </ul>
      </div>
    </header>
"""


def header_sub(lang: str, page: str) -> str:
    t = TEXT[lang]
    return f"""    <header class="site-header">
      <div class="container nav">
        <a class="brand" href="{link_to(lang, lang, 'index')}" aria-label="KTMANY">{LOGO}KTMANY</a>
        <div class="nav-right">
          {lang_switch(lang, page)}
          <a class="btn btn-ghost" href="{link_to(lang, lang, 'index')}">{t['home']}</a>
        </div>
      </div>
    </header>
"""


def footer(lang: str) -> str:
    t = TEXT[lang]
    return f"""    <footer class="site-footer">
      <div class="container">
        <span>© <span id="year">2026</span> {COMPANY['name']}. {t['rights']}</span>
        <nav aria-label="{t['legal_nav']}">
          <a href="{link_to(lang, lang, 'imprint')}">{t['imprint']}</a>
          <a href="{link_to(lang, lang, 'privacy')}">{t['privacy']}</a>
          {lang_switch(lang, 'index')}
        </nav>
      </div>
    </footer>

    <script src="{rel(lang, 'assets/main.js')}" defer></script>
  </body>
</html>
"""


def checklist(items: list[str], cls: str = "") -> str:
    attr = f' class="{cls}"' if cls else ""
    return f"<ul{attr}>" + "".join(f"<li>{icon('check')}{x}</li>" for x in items) + "</ul>"


def plain_list(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


# ---------------------------------------------------------------- Startseite

def home(lang: str) -> str:
    t = TEXT[lang]
    c = COMPANY
    country = c["country_de"] if lang == "de" else c["country_en"]
    panel = "\n".join(
        f'              <div class="panel-row"><div>{a} <small>{b}</small></div><span class="badge {cls}">{s}</span></div>'
        for a, b, cls, s in t["panel"]
    )
    hero_points = "".join(f"<li>{icon('check')}{p}</li>" for p in t["hero_points"])
    services = "\n".join(
        f"""            <article class="card reveal">
              <div class="icon">{icon(ic)}</div>
              <h3>{title}</h3>
              <p>{text}</p>
              {plain_list(points)}
            </article>"""
        for ic, title, text, points in t["services"]
    )
    products = "\n".join(
        f"""            <article class="card product reveal">
              <div class="product-head"><div class="icon">{icon(ic)}</div><span class="badge {cls}">{status}</span></div>
              <h3>{title}</h3>
              <p>{text}</p>
            </article>"""
        for ic, title, status, cls, text in t["products"]
    )
    sec_items = "\n".join(
        f"""            <div class="sec-item reveal">
              <div class="icon">{icon(ic)}</div>
              <h3>{title}</h3>
              <p>{text}</p>
            </div>"""
        for ic, title, text in t["sec_items"]
    )
    chips = "".join(f'<span class="chip">{x}</span>' for x in t["chips"])
    steps = "\n".join(f'            <div class="step reveal"><h3>{a}</h3><p>{b}</p></div>' for a, b in t["steps"])
    values = "\n".join(
        f"""            <div class="value reveal">
              <div class="icon">{icon(ic)}</div>
              <div><h3>{title}</h3><p>{text}</p></div>
            </div>"""
        for ic, title, text in t["values"]
    )
    mail = f"mailto:{c['email']}?subject={t['mail_subject']}"
    lab = t["contact_labels"]
    return (
        head(lang, "index", t["title"], t["description"])
        + header_home(lang)
        + f"""
    <main id="inhalt">
      <section class="hero" id="top">
        <div class="container">
          <div>
            <span class="eyebrow"><span class="dot"></span> {t['hero_eyebrow']}</span>
            <h1>{t['hero_h1']}</h1>
            <p class="lead">{t['hero_lead']}</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="#kontakt">{t['hero_cta']} {icon('arrow')}</a>
              <a class="btn btn-ghost" href="#produkte">{t['hero_cta2']}</a>
            </div>
            <ul class="hero-points">{hero_points}</ul>
          </div>
          <div class="hero-visual" aria-hidden="true">
            <div class="panel">
              <div class="panel-head"><span></span><span></span><span></span></div>
{panel}
              <div class="panel-bar"><i></i></div>
              <div class="panel-foot"><span>{t['panel_foot']}</span><span>78 %</span></div>
            </div>
            <div class="shield">{icon('shieldcheck')}</div>
          </div>
        </div>
      </section>

      <section id="leistungen">
        <div class="container">
          <div class="section-head reveal">
            <span class="eyebrow">{t['services_eyebrow']}</span>
            <h2>{t['services_h2']}</h2>
            <p>{t['services_lead']}</p>
          </div>
          <div class="grid grid-3">
{services}
          </div>
        </div>
      </section>

      <section class="section-soft" id="produkte">
        <div class="container">
          <div class="section-head reveal">
            <span class="eyebrow">{t['products_eyebrow']}</span>
            <h2>{t['products_h2']}</h2>
            <p>{t['products_lead']}</p>
          </div>
          <div class="grid grid-2">
{products}
          </div>
        </div>
      </section>

      <section class="security" id="security">
        <div class="container">
          <div class="section-head reveal">
            <span class="eyebrow">{t['sec_eyebrow']}</span>
            <h2>{t['sec_h2']}</h2>
            <p>{t['sec_lead']}</p>
          </div>
          <div class="featured reveal">
            <div>
              <div class="icon">{icon('book')}</div>
              <h3>{t['grundschutz_h3']}</h3>
              <p>{t['grundschutz_text']}</p>
            </div>
            {checklist(t['grundschutz_points'], 'featured-list')}
          </div>
          <div class="sec-grid">
{sec_items}
          </div>
          <div class="sec-note reveal">{chips}</div>
        </div>
      </section>

      <section id="vorgehen">
        <div class="container">
          <div class="section-head reveal">
            <span class="eyebrow">{t['steps_eyebrow']}</span>
            <h2>{t['steps_h2']}</h2>
            <p>{t['steps_lead']}</p>
          </div>
          <div class="steps">
{steps}
          </div>
        </div>
      </section>

      <section class="section-soft" id="ueber-uns">
        <div class="container">
          <div class="section-head reveal">
            <span class="eyebrow">{t['about_eyebrow']}</span>
            <h2>{t['about_h2']}</h2>
            <p>{t['about_lead']}</p>
          </div>
          <div class="grid grid-2">
{values}
          </div>
          <div class="founding reveal">
            <div>
              <span class="eyebrow">{t['founding_eyebrow']}</span>
              <h2>{t['founding_h2']}</h2>
              <p>{t['founding_text']}</p>
              <a class="btn btn-primary" href="#kontakt">{t['founding_cta']}</a>
            </div>
            {checklist(t['founding_points'])}
          </div>
        </div>
      </section>

      <section class="contact" id="kontakt">
        <div class="container contact-box">
          <div class="reveal">
            <span class="eyebrow">{t['contact_eyebrow']}</span>
            <h2>{t['contact_h2']}</h2>
            <p>{t['contact_text']}</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="{mail}">{t['contact_cta']} {icon('arrow')}</a>
            </div>
          </div>
          <div class="contact-card reveal">
            <dl>
              <dt>{lab[0]}</dt>
              <dd><a href="mailto:{c['email']}">{c['email']}</a></dd>
              <dt>{lab[1]}</dt>
              <dd><a href="tel:{c['phone_href']}">{c['phone']}</a></dd>
              <dt>{lab[2]}</dt>
              <dd>{c['name']}<br />{c['street']}, {c['city']}<br />{country}</dd>
              <dt>{lab[3]}</dt>
              <dd><a href="{c['github']}" rel="noopener">github.com/KTMANY</a></dd>
            </dl>
          </div>
        </div>
      </section>
    </main>

"""
        + footer(lang)
    )


# ---------------------------------------------------------------- Rechtliches

def todo(text: str) -> str:
    return f'<span class="todo">{text}</span>'


def imprint(lang: str) -> str:
    c = COMPANY
    managers = " und ".join(c["managers"]) if lang == "de" else " and ".join(c["managers"])
    if lang == "de":
        register = c["register"] or todo("Registergericht und Registernummer werden nach der Eintragung ergänzt")
        vat = c["vat_id"] or todo("wird nach Erteilung ergänzt")
        body = f"""        <h1>Impressum</h1>
        <p>Angaben gemäß § 5 Digitale-Dienste-Gesetz (DDG)</p>

        <h2>Anbieter</h2>
        <p>{c['name']}<br />{c['street']}<br />{c['city']}<br />{c['country_de']}</p>

        <h2>Vertreten durch die Geschäftsführer</h2>
        <p>{managers}</p>

        <h2>Kontakt</h2>
        <p>Telefon: <a href="tel:{c['phone_href']}">{c['phone']}</a><br />E-Mail: <a href="mailto:{c['email']}">{c['email']}</a></p>

        <h2>Registereintrag</h2>
        <p>Eintragung im Handelsregister.<br />{register}</p>

        <h2>Umsatzsteuer-ID</h2>
        <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a Umsatzsteuergesetz: {vat}</p>

        <h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
        <p>{c['managers'][0]}, {c['street']}, {c['city']}</p>

        <h2>Verbraucherstreitbeilegung</h2>
        <p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

        <h2>Haftung für Inhalte und Links</h2>
        <p>Die Inhalte dieser Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte können wir jedoch keine Gewähr übernehmen. Für Inhalte verlinkter externer Seiten sind ausschließlich deren Betreiber verantwortlich; zum Zeitpunkt der Verlinkung waren keine Rechtsverstöße erkennbar.</p>
"""
        title, desc = "Impressum – KTMANY", "Impressum der KTMANY UG (haftungsbeschränkt)"
    else:
        register = c["register"] or todo("Register court and number will be added after registration")
        vat = c["vat_id"] or todo("will be added once issued")
        body = f"""        <h1>Legal notice</h1>
        <p>Information pursuant to Section 5 of the German Digital Services Act (DDG). The German version (<a href="../impressum.html" lang="de">Impressum</a>) is legally binding.</p>

        <h2>Provider</h2>
        <p>{c['name']}<br />{c['street']}<br />{c['city']}<br />{c['country_en']}</p>

        <h2>Represented by the managing directors</h2>
        <p>{managers}</p>

        <h2>Contact</h2>
        <p>Phone: <a href="tel:{c['phone_href']}">{c['phone']}</a><br />E-mail: <a href="mailto:{c['email']}">{c['email']}</a></p>

        <h2>Commercial register</h2>
        <p>Registered in the German commercial register.<br />{register}</p>

        <h2>VAT ID</h2>
        <p>VAT identification number according to Section 27a of the German VAT Act: {vat}</p>

        <h2>Responsible for content according to Section 18 (2) MStV</h2>
        <p>{c['managers'][0]}, {c['street']}, {c['city']}</p>

        <h2>Consumer dispute resolution</h2>
        <p>We are neither willing nor obliged to participate in dispute resolution proceedings before a consumer arbitration board.</p>

        <h2>Liability for content and links</h2>
        <p>The content of these pages has been created with the utmost care. However, we cannot guarantee that it is accurate, complete or up to date. The operators of linked external websites are solely responsible for their content; no legal violations were apparent at the time of linking.</p>
"""
        title, desc = "Legal notice – KTMANY", "Legal notice of KTMANY UG (haftungsbeschränkt)"
    return head(lang, "imprint", title, desc, noindex=True) + header_sub(lang, "imprint") + f'    <main id="inhalt" class="legal">\n      <div class="container">\n{body}      </div>\n    </main>\n\n' + footer(lang)


def privacy(lang: str) -> str:
    c = COMPANY
    managers = ", ".join(c["managers"])
    if lang == "de":
        body = f"""        <h1>Datenschutzerklärung</h1>
        <p>Stand: Oktober 2026</p>

        <h2>1. Verantwortlicher</h2>
        <p>{c['name']}, {c['street']}, {c['city']}, {c['country_de']}<br />Geschäftsführer: {managers}<br />Telefon: {c['phone']} · E-Mail: <a href="mailto:{c['email']}">{c['email']}</a></p>

        <h2>2. Grundsätze</h2>
        <p>Diese Webseite kommt ohne Cookies, ohne Analyse- oder Tracking-Werkzeuge und ohne eingebundene Inhalte Dritter (z. B. Schriftarten, Karten, Videos oder Social-Media-Plugins) aus. Wir verarbeiten personenbezogene Daten nur, soweit dies für den Betrieb der Seite oder die Beantwortung Ihrer Anfrage nötig ist.</p>

        <h2>3. Hosting über GitHub Pages</h2>
        <p>Die Webseite wird über GitHub Pages bereitgestellt, einen Dienst der GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Beim Aufruf der Seite verarbeitet GitHub technisch notwendige Daten, insbesondere Ihre IP-Adresse, Datum und Uhrzeit des Zugriffs, die aufgerufene Seite sowie Browser- und Geräteangaben (Server-Logfiles), um die Seite auszuliefern und die Sicherheit des Dienstes zu gewährleisten.</p>
        <p>Rechtsgrundlage ist unser berechtigtes Interesse an einer sicheren und zuverlässigen Bereitstellung der Webseite (Art. 6 Abs. 1 lit. f DSGVO). Dabei können Daten in die USA übermittelt werden. GitHub bzw. die Muttergesellschaft Microsoft ist unter dem EU-US Data Privacy Framework zertifiziert (Art. 45 DSGVO). Weitere Informationen: <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">Datenschutzerklärung von GitHub</a>.</p>

        <h2>4. Kontakt per E-Mail oder Telefon</h2>
        <p>Wenn Sie uns per E-Mail oder Telefon kontaktieren, verarbeiten wir Ihre Angaben (z. B. Name, Kontaktdaten, Inhalt der Anfrage), um Ihre Anfrage zu beantworten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, soweit die Anfrage auf einen Vertrag zielt, ansonsten unser berechtigtes Interesse an der Bearbeitung (Art. 6 Abs. 1 lit. f DSGVO). Die Daten werden gelöscht, sobald die Anfrage erledigt ist und keine gesetzlichen Aufbewahrungspflichten bestehen.</p>

        <h2>5. Ihre Rechte</h2>
        <p>Sie haben das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) sowie Widerspruch gegen Verarbeitungen auf Grundlage berechtigter Interessen (Art. 21). Wenden Sie sich dazu an die oben genannten Kontaktdaten.</p>
        <p>Sie können sich außerdem bei einer Datenschutz-Aufsichtsbehörde beschweren, zum Beispiel bei der für uns zuständigen Landesbeauftragten für Datenschutz und Informationsfreiheit Nordrhein-Westfalen.</p>

        <h2>6. Änderungen</h2>
        <p>Wir passen diese Datenschutzerklärung an, wenn sich die Webseite oder die Rechtslage ändert. Es gilt die jeweils hier veröffentlichte Fassung.</p>
"""
        title, desc = "Datenschutz – KTMANY", "Datenschutzerklärung der KTMANY UG (haftungsbeschränkt)"
    else:
        body = f"""        <h1>Privacy policy</h1>
        <p>Last updated: October 2026. The German version (<a href="../datenschutz.html" lang="de">Datenschutzerklärung</a>) is legally binding.</p>

        <h2>1. Controller</h2>
        <p>{c['name']}, {c['street']}, {c['city']}, {c['country_en']}<br />Managing directors: {managers}<br />Phone: {c['phone']} · E-mail: <a href="mailto:{c['email']}">{c['email']}</a></p>

        <h2>2. Principles</h2>
        <p>This website uses no cookies, no analytics or tracking tools and no embedded third-party content (such as web fonts, maps, videos or social media plugins). We process personal data only where necessary to operate the website or to respond to your enquiry.</p>

        <h2>3. Hosting via GitHub Pages</h2>
        <p>This website is served via GitHub Pages, a service of GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. When you visit the site, GitHub processes technically necessary data, in particular your IP address, date and time of access, the page requested and browser and device information (server log files), in order to deliver the website and keep the service secure.</p>
        <p>The legal basis is our legitimate interest in providing the website securely and reliably (Art. 6(1)(f) GDPR). Data may be transferred to the USA. GitHub and its parent company Microsoft are certified under the EU-US Data Privacy Framework (Art. 45 GDPR). More information: <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub privacy statement</a>.</p>

        <h2>4. Contact by e-mail or phone</h2>
        <p>If you contact us by e-mail or phone, we process the information you provide (e.g. name, contact details, content of your enquiry) to respond to you. The legal basis is Art. 6(1)(b) GDPR where the enquiry relates to a contract, otherwise our legitimate interest in handling it (Art. 6(1)(f) GDPR). The data is deleted once the enquiry has been dealt with, unless statutory retention obligations apply.</p>

        <h2>5. Your rights</h2>
        <p>You have the right of access (Art. 15 GDPR), rectification (Art. 16), erasure (Art. 17), restriction of processing (Art. 18), data portability (Art. 20) and to object to processing based on legitimate interests (Art. 21). Please use the contact details above.</p>
        <p>You also have the right to lodge a complaint with a data protection supervisory authority, for example the State Commissioner for Data Protection and Freedom of Information of North Rhine-Westphalia, which is responsible for us.</p>

        <h2>6. Changes</h2>
        <p>We update this privacy policy when the website or the legal situation changes. The version published here applies.</p>
"""
        title, desc = "Privacy – KTMANY", "Privacy policy of KTMANY UG (haftungsbeschränkt)"
    return head(lang, "privacy", title, desc, noindex=True) + header_sub(lang, "privacy") + f'    <main id="inhalt" class="legal">\n      <div class="container">\n{body}      </div>\n    </main>\n\n' + footer(lang)


def not_found() -> str:
    # wird unter beliebigen Pfaden ausgeliefert → absolute Links
    return """<!doctype html>
<html lang="de">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Seite nicht gefunden / Page not found – KTMANY</title>
    <meta name="robots" content="noindex" />
    <meta name="theme-color" content="#050b1a" />
    <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
    <link rel="stylesheet" href="/assets/style.css" />
  </head>
  <body>
    <header class="site-header">
      <div class="container nav">
        <a class="brand" href="/" aria-label="KTMANY">""" + LOGO + """KTMANY</a>
      </div>
    </header>
    <main class="legal">
      <div class="container">
        <h1>Seite nicht gefunden</h1>
        <p>Die aufgerufene Seite gibt es nicht (mehr). <span lang="en">This page does not exist.</span></p>
        <p><a class="btn btn-primary" href="/">Zur Startseite</a> &nbsp; <a class="btn btn-outline" href="/en/" lang="en">Go to homepage</a></p>
      </div>
    </main>
  </body>
</html>
"""


def main() -> None:
    out = {
        PAGES["de"]["index"]: home("de"),
        PAGES["en"]["index"]: home("en"),
        PAGES["de"]["imprint"]: imprint("de"),
        PAGES["en"]["imprint"]: imprint("en"),
        PAGES["de"]["privacy"]: privacy("de"),
        PAGES["en"]["privacy"]: privacy("en"),
        "404.html": not_found(),
        "sitemap.xml": sitemap(),
        "robots.txt": f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n",
    }
    for path, html in out.items():
        p = ROOT / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(html, encoding="utf-8")
        print(f"geschrieben: {path}")


def sitemap() -> str:
    urls = []
    for page in ("index", "imprint", "privacy"):
        for lang in ("de", "en"):
            loc = BASE + PAGES[lang][page].replace("index.html", "")
            alts = "".join(
                f'<xhtml:link rel="alternate" hreflang="{l}" href="{BASE + PAGES[l][page].replace("index.html", "")}"/>' for l in ("de", "en")
            )
            urls.append(f"  <url><loc>{loc}</loc>{alts}</url>")
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )


if __name__ == "__main__":
    main()
