# LLMs for Scientific Discovery — tutorial series

Jekyll source for the existing `agent4sd.io` site. The original GitHub Pages
hosting setup and custom domain are retained.

## Routes

- `/` — the latest tutorial, currently AAAI 2027.
- `/2027/` — the stable URL for that same tutorial.
- `/list/` — series overview, linking to both 2026 and 2027.
- `/2026/` — archived AAAI 2026 page, retaining the original presenters,
  slides, reading list, and Beautiful Jekyll theme.

Both year pages link back to `/list/`. The root and `/2027/` render the same
`_includes/tutorial2027.html`, so their content cannot drift. Both use
`/2027/` as their canonical URL. GitHub Pages redirects directory paths such
as `/list` to `/list/`.

## Content and maintenance

The 2027 page follows the 2026 content structure: presenters, slides,
detailed tutorial description (overview, motivation, outline, target
audience, prerequisites, learning outcomes), and a grouped reading list.
There is no detailed timetable or session-by-session timing.

- `_includes/tutorial2027.html`: shared 2027 page content.
- `_data/tutorial2027.yml`: ordered presenters, biographies, reading links.
- `list/index.md`: series overview.
- `_layouts/series.html`, `assets/css/series.css`: shared new-page design.
- `2026/index.md`: archived original content with an overview link.

The acceptance email and proposal supply the AAAI-27 title, Montréal
location, presenter order, and tutorial content. Photos are copied unchanged
from the supplied workshop repository. Slides and demo materials are
explicitly marked as not yet available; no fake download links are added.
HypoSpace, Auto-Discovery-Bench, and LLM-AutoSciLab reading links were checked
against their arXiv/project pages; other reading links come from the old site.

Existing `/img/`, `/css/`, `/js/`, and external slide URLs are retained.
Root-page section bookmarks now refer to the latest edition, as requested.
Use `/2026/#reading-list` (and the other archived section IDs) for 2026
materials; the homepage no longer redirects these anchors to the archive.

## Build and checks

```sh
bundle install
bundle exec jekyll build --destination /tmp/agent4sd-site
python3 scripts/check_site.py /tmp/agent4sd-site
bundle exec jekyll serve --destination /tmp/agent4sd-site
```

The checks verify route links, local assets and anchors, presenter order,
homepage/2027 content equality, absence of the old timetable, and preservation
of the original resource URLs. New links support a GitHub project `baseurl`
as well as the custom-domain root.

The old tracked `_site/` folder is a stale build from an earlier template,
not the source of truth. Build into a fresh directory; never deploy that old
snapshot. `CNAME` remains `agent4sd.io`, matching `_config.yml`.

## Publishing and future editions

Commit and push the source to the existing GitHub Pages branch. Verify the
Pages build and the public `/`, `/list/`, `/2026/`, and `/2027/` routes after
publication.

For a future edition, add a year-specific page/include/data file, update the
root wrapper to that edition, and add it to the overview and navigation.
Keep existing year URLs and their materials intact.

### Public contact and branding sources

The 2027 presenters’ email links are based on the submitted proposal and public
profile/paper sources recorded in `_data/tutorial2027.yml` (`email_source`).
The AAAI logo at `assets/img/brand/aaai-logo.png` is the unmodified official asset:
https://aaai.org/wp-content/uploads/2024/03/AAAI-Logo-Title-FullColor.png
It links to AAAI.org. Brand guidance: https://aaai.org/about-aaai/aaai-logos/
The mark remains AAAI’s trademark and is not covered by any repository code license.
