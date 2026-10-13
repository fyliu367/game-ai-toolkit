# Daily update procedure

The site is built from `src/toolkit.html`. Never edit `index.html` by hand.

## Each run

1. Read `CHANGELOG.md` to see when the last update was and what it covered.
2. For each tab (2D, 3D, retopo/texturing, rigging, animation, VFX, engine integration, rendering, audio, QA, localization, trailers and UA), search for:
   - new AI tools or major versions released since the last update
   - tools on the site that were discontinued, acquired, renamed, or changed licence or pricing
   - new published efficiency figures for tools already listed
3. Only make a change when it has a primary source (vendor announcement, docs, release notes or paper). For any claim beyond the vendor's own description, also find one independent source (established press, benchmark or study).
4. Edit the `TABS` data in `src/toolkit.html`, following the format of existing cards. Every card needs a `u` field with its official link(s), e.g. `u:[["Vendor","https://..."]]`. Open each link and confirm it loads the right product page before adding it.
5. Run `python3 tools/build.py`. It checks the script and rebuilds `index.html`.
6. Add a dated entry to `CHANGELOG.md` listing each change with its source URLs.
7. Commit on a new branch `update/YYYY-MM-DD`, push it, and open a pull request for review. Never push to `main`.

## Data rules

- **No made-up numbers.** An efficiency figure must come from a published source and carry its grade: `measured` (a studio's own production report, shown as "Studio-reported"), `bench` (independent test or research), or `vendor` (the maker's claim). Otherwise use `e:{v:"—",l:"No published figure yet",g:"none",s:""}`.
- Say "stage-level; tool not isolated" when a figure covers a whole stage of work rather than one tool.
- Do not name the studio behind case-study figures. Use "Studio case study".
- Write uncertain or single-source claims as such ("per one comparison", "reported").
- If nothing new meets these rules, change nothing and open no pull request.
