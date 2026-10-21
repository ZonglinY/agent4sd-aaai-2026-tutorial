#!/usr/bin/env python3
"""Check a freshly built Jekyll site without third-party dependencies."""
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images = []
        self.h1_count = 0
        self.feed(text)

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.h1_count += 1
        if tag in ("a", "link") and "href" in attrs:
            self.links.append(attrs["href"])
        if tag in ("img", "script") and "src" in attrs:
            self.links.append(attrs["src"])
        if tag == "img":
            assert attrs.get("alt"), f"Image missing alternative text: {attrs}"
            self.images.append(attrs["src"])


def main():
    root = Path(sys.argv[1]).resolve()
    baseurl = sys.argv[2].rstrip("/") if len(sys.argv) > 2 else ""
    pages = {}
    for route in ("/", "/list/", "/2027/", "/2026/", "/404.html"):
        file = root / (route.lstrip("/") + "index.html" if route.endswith("/") else route.lstrip("/"))
        text = file.read_text()
        assert not re.search(r"\{%|\{\{", text), f"Unrendered Liquid in {file}"
        pages[route] = Page(text)
        if route != "/2026/":
            assert pages[route].h1_count == 1, f"Expected one h1 in {route}"

    checked = 0
    for route, page in pages.items():
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = urlsplit(urljoin(baseurl + route, link))
            path = unquote(target.path)
            if baseurl:
                assert path.startswith(baseurl + "/"), f"Link bypasses baseurl: {link}"
                path = path[len(baseurl):]
            file = root / path.lstrip("/")
            if file.is_dir():
                file /= "index.html"
            assert file.is_file(), f"Missing local target from {route}: {link}"
            if target.fragment and file.suffix == ".html":
                destination = Page(file.read_text())
                assert unquote(target.fragment) in destination.ids, f"Missing anchor: {route} -> {link}"
            checked += 1

    text = (root / "2027/index.html").read_text()
    assert "MiroMind" not in text, "Outdated affiliation in latest edition"
    for removed_class in ("speaker-role", "speaker-affiliation", "speaker-topics"):
        assert f'class="{removed_class}"' not in text, "Presenter cards must be name-only"
    assert "Zonglin Yang received his PhD from Nanyang Technological University" in text
    names = ["Dianbo Liu", "Zonglin Yang", "Tingting Chen", "Chandan K. Reddy"]
    indices = [text.index(f'alt="{name}"') for name in names]
    assert indices == sorted(indices), "Incorrect speaker order"
    assert len([src for src in pages["/2027/"].images if "/assets/img/2027/" in src]) == 4, "Expected four presenter photos"
    for name, email in zip(names, ["dianbo@nus.edu.sg", "zonglin001@ntu.edu.sg", "tingting.c@u.nus.edu", "reddy@cs.vt.edu"]):
        assert f'aria-label="Email {name}"' in text
        assert pages["/2027/"].links.count("mailto:" + email) == (2 if email == "zonglin001@ntu.edu.sg" else 1)
    assert '<a href="mailto:zonglin001@ntu.edu.sg">Feedback &amp; suggestions ↗</a>' in text
    assert 'href="#speakers">Contact the presenters' in text
    assert "AAAI 2027 · Tutorial" in text
    assert "Accepted" not in text
    assert baseurl + "/assets/img/brand/aaai-logo.png" in pages["/2027/"].images
    assert "https://aaai.org/conference/aaai/aaai-27/" in pages["/2027/"].links
    assert "Tentative schedule" not in text and 'class="schedule"' not in text
    assert "0:00" not in text and "30-minute break" not in text
    assert (root / "CNAME").read_text().strip() == "agent4sd.io"
    assert "https://agent4sd.io" + baseurl + "/2027/" in text
    for route in ("/", "/2026/", "/2027/"):
        assert baseurl + "/list/" in pages[route].links, f"Missing overview link in {route}"
    for route in ("/2026/", "/2027/"):
        assert baseurl + route in pages["/list/"].links, f"Edition missing from overview: {route}"
    def main_text(markup):
        main = re.search(r'<main id="main">(.*?)</main>', markup, re.S).group(1)
        return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", main)).split())
    home = (root / "index.html").read_text()
    assert main_text(home) == main_text(text), "Homepage differs from latest edition"
    assert "legacy-links.js" not in home, "Homepage must not redirect 2027 anchors to 2026"
    for anchor in ("overview", "motivation", "tutorial-outline", "target-audience",
                   "learning-outcomes", "reading-list", "speakers", "slides"):
        assert anchor in pages["/"].ids and anchor in pages["/2027/"].ids

    # Cover every distinct citation in the accepted tutorial proposal.
    proposal_keys = set("reddy2025towards luo2025llm4sr TPSR SNIP LLM-SR LLM-SRBench SurfaceBench DecAEvolve EvoDiverse LLEMA LLM-AutoSciLab LLM-ACES MOOSE yang2024moose MC2 MC3 ResearchBench MOOSE-Copilot MOOSE-Star HypoSpace AutoDiscoveryBench FML-bench".split())
    rendered_keys = re.findall(r'data-proposal-key="([^"]+)"', text)
    assert len(rendered_keys) == len(set(rendered_keys)) == 22
    assert set(rendered_keys) == proposal_keys, "Missing proposal reading"
    venues = re.findall(r'<span class="reading-venue">([^<]+)</span>', text)
    assert len(venues) == 20 and all(v.strip() for v in venues), "Incorrect publication metadata"
    assert "arXiv preprint" not in text and "Senior Member Track" not in text
    assert "AAAI 2025" in venues
    assert "ACL 2026 · Findings" in venues
    assert "ACL 2024 · Findings" in venues
    assert "NeurIPS 2025 AI for Science Workshop" in venues

    # Fixture captured from the pre-migration revision 9b3d573.
    # Preserve original 2026 slide URLs and reading-list links.
    source = Path(__file__).resolve().parents[1]
    original_urls = json.loads((source / "scripts/legacy-2026-urls.json").read_text())
    archive_source = (source / "2026/index.md").read_text()
    for url in original_urls:
        assert url in archive_source, f"Original resource removed: {url}"

    print(json.dumps({"result": "PASS", "pages": len(pages), "local_targets": checked,
                      "baseurl": baseurl, "speakers": names}, indent=2))


if __name__ == "__main__":
    main()
