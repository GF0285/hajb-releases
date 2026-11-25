# Hajb (حاجب) — releases and website

**Website:** https://hajb.torshblock.workers.dev  (العربية · [English](https://hajb.torshblock.workers.dev/en/) · [Español](https://hajb.torshblock.workers.dev/es/))

Hajb is a free ad and tracker blocker for Chrome, Edge, Brave, Opera, Vivaldi and Firefox (Manifest V3). It collects no data; everything runs on your device.

This repository holds **only the public website and the release packages**. Downloads are on the [Releases page](https://github.com/GF0285/hajb-releases/releases/latest):

| File | For |
|---|---|
| `Hajb-2.0.0-chrome.zip` | Chrome, Edge, Brave, Opera, Vivaldi (unzip, then "Load unpacked" in developer mode) |
| `Hajb-2.0.0-firefox.xpi` | Firefox, **unsigned**: load it as a temporary add-on from `about:debugging` |
| `SHA256SUMS` | checksums of both files |

The full illustrated install guide (every browser, update, removal, FAQ) is on the website.

## العربية
حاجب مانع إعلانات ومتتبّعات مجاني لكروم وإيدج وبريف وأوبرا وفيفالدي وفايرفوكس، لا يجمع أي بيانات. الملفات في صفحة [الإصدارات](https://github.com/GF0285/hajb-releases/releases/latest)، ودليل التثبيت المصوّر في [الموقع](https://hajb.torshblock.workers.dev).

## Español
Hajb es un bloqueador gratuito de anuncios y rastreadores para Chrome, Edge, Brave, Opera, Vivaldi y Firefox, que no recoge ningún dato. Los archivos están en [Releases](https://github.com/GF0285/hajb-releases/releases/latest) y la guía ilustrada en la [web](https://hajb.torshblock.workers.dev/es/).

## Website source
`public/` is the static site served by a Cloudflare Worker with static assets (`wrangler.jsonc`). `src/build.py` and `src/t_*.py` generate the three language pages. No trackers, no analytics, no third-party requests.

Filter-list credits and licences are listed on the website and in `NOTICE.md` inside each package. Fonts: Reem Kufi and IBM Plex Sans Arabic (SIL OFL 1.1).

Made with ♥ by GF0285, a member of GeeksFamily and DWM.

## Deploy (maintainer)
1. Edit copy in `src/t_ar.py`, `src/t_en.py`, `src/t_es.py`; run `python3 src/build.py` (reads sizes and SHA256SUMS from `$HAJB_RELEASE_DIR`).
2. New version: attach the files to a new GitHub release, update `VERSION` in `src/content_meta.py` and the URLs in `public/_redirects`.
3. `WRANGLER_CACHE_DIR=.wrangler/cache wrangler deploy` (Worker `hajb`, static assets only, free plan).
