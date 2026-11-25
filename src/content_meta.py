VERSION = "2.0.0"
REPO = "GF0285/hajb-releases"
SITE = "https://hajb.torshblock.workers.dev"
REL = f"https://github.com/{REPO}/releases/download/v{VERSION}"
CHROME_FILE = f"Hajb-{VERSION}-chrome.zip"
FF_FILE = f"Hajb-{VERSION}-firefox.xpi"
import subprocess, os
R = os.environ.get("HAJB_RELEASE_DIR", "/workspace/hajb-release-2.0.0")
SUMS = {l.split()[1]: l.split()[0] for l in open(f"{R}/SHA256SUMS").read().strip().splitlines()}
SIZE = {f: os.path.getsize(f"{R}/{f}") for f in (CHROME_FILE, FF_FILE)}
