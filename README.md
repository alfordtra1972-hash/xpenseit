# SnapStub

Snap it. Name it. Send it. A home-screen web app for capturing expense receipts as named PDFs.

- Take one or more photos of a receipt (multi-page supported)
- Optional clean-up (black & white, sharper text)
- Name it from date, vendor, category, and amount, e.g. `2026-10-02_Delta_Airfare_412.50.pdf`
- Email right away, or add to a batch and send a trip's worth at once (separate PDFs or one combined PDF)
- Up to three saved email addresses, plus "Other…"
- History of past receipts, searchable and editable

Everything is stored on the phone. Nothing is uploaded to a server.

## Install on iPhone

1. Open https://alfordtra1972-hash.github.io/snapstub/ in **Safari**
2. Tap **Share**, then **Add to Home Screen**

## Files

- `index.html`: the whole app (UI, image processing, PDF builder, storage)
- `sw.js`: offline support
- `manifest.webmanifest`, `icons/`: home-screen icon and app info
- `make_icons.py`: regenerates the icons (needs Pillow)
