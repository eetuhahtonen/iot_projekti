# Automaation IoT-projekti

Raspberry Pi -harjoitustehtäviä IoT-kurssilta. Toteutettu Python 3:lla.

## Viikko 1 — GPIO perusteet

LED:n ohjaus ja nappi-keskeytykset RPi.GPIO-kirjastolla.

## Viikko 2 — Lämpötilasensori

DS18B20-lämpötilasensorin lukeminen 1-Wire-väylältä (`/sys/bus/w1/`). Kynnysarvo-ohjaus: LED syttyy kun lämpötila ylittää 25 °C.

## Viikko 3 — ThingSpeak, etäohjaus

CPU-lämpötilan luku (`/sys/class/thermal/`) ja lähettäminen ThingSpeak-pilvipalveluun. LED:n ohjaus ThingSpeak-kanavan kentän arvon perusteella. Yksinkertainen HTML-sivu, jonka napeilla lähetetään ohjausarvo (0/1) ThingSpeakiin.

## Ympäristö

- Raspberry Pi + Raspbian
- Python 3
- `RPi.GPIO`, `python-dotenv`
- API-avaimet `.env`-tiedostossa (`WRITE_API_KEY`, `READ_API_KEY`, `CHANNEL_ID`)
