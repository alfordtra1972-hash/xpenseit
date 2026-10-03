# XpenseIt

**Snap. Filed. Done.** A home-screen web app for capturing expense receipts as neatly named PDFs.

- Take one or more photos of a receipt (multi-page supported)
- Optional clean-up (black & white, sharper text)
- Named from date, vendor, category, and amount, e.g. `2026-10-14_Delta_Airfare_412.50.pdf`
- Email right away, or add it to a named **Trip** and send the whole trip at once (separate PDFs or one combined PDF)
- Up to three saved email addresses, plus "Other…"
- Searchable, editable history shown as boarding-pass style tickets
- Follows the iPhone's light/dark setting

Everything is stored on the phone. Nothing is uploaded to a server.

## Install on iPhone

1. Open https://alfordtra1972-hash.github.io/xpenseit/ in **Safari**
2. Tap **Share**, then **Add to Home Screen**

## Files

- `index.html`: the whole app (UI, image processing, PDF builder, storage)
- `sw.js`: offline support (bump `CACHE` when releasing changes)
- `manifest.webmanifest`, `icons/`: home-screen icon and app info
- `make_icons.py`: regenerates the icons (needs Pillow)
