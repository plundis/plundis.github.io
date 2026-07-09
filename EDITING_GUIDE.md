# Portfolio Editing Guide — index.html

Your site is a single self-contained HTML file. Three logical zones:

1. **`<style>`** (in `<head>`) — all colors, fonts, layout
2. **HTML body** — the visible "list view" content (hero, experience cards, project cards, skills, education, contact, notes)
3. **`<script>`** at the bottom — the `DETAILS` object (full detail-page text) + all interactive behavior

The site has two views: the **list view** (cards) and the **detail view** (full write-ups generated from the `DETAILS` JS object). Most content lives in TWO places — the short card in the HTML, and the long version in `DETAILS`. Update both when changing a project/role.

---

## QUICK INDEX — "I want to change X"

| What | Where | Search for |
|------|-------|-----------|
| Colors / theme | `<style>` → `:root` | `--bg:` |
| Page title / tab name | `<head>` | `<title>` |
| Your name / tagline | hero section | `<h1>Monil Arora</h1>` |
| Status pill text | hero | `Open to embedded` |
| Termlog "CURRENT/BUILDING/NEXT" | hero | `class="termlog"` |
| Residency date range / progress bar | JS bottom | `residency progress` |
| Top-bar links (resume/email/linkedin) | `.topbar` | `class="tb-link"` |
| Region sidebar labels | `.regions` | `class="reg"` |
| Experience card (short) | `#sec-experience` | `data-detail="exp/lzh"` |
| Experience full write-up | JS `DETAILS` | `'exp/lzh'` |
| Project card (short) | `#sec-projects` | `class="proj"` |
| Project full write-up | JS `DETAILS` | `'proj/self-balancing-robot'` |
| Skills chips | `#sec-skills` | `class="skbucket"` |
| Courses | `#sec-education` | `class="course"` |
| Contact cards | `#sec-contact` | `class="ccard"` |
| Notes / hobbies block | `#sec-notes` | `class="notes"` |
| Footer ticker (rotating status) | JS bottom | `const TICKER` |
| **Removing any element** | guide §10 | `REMOVING ELEMENTS` |
| Boot animation lines | top of body | `<div class="boot"` |

---

## 1. CHANGING COLORS / THEME

All colors are CSS variables at the very top of `<style>`, in `:root{...}`. Change the hex value once and it updates everywhere.

```
--bg:#07090a        /* darkest background */
--paper-bg:#f8f2e0  /* the cream "paper" content panel */
--phos:#7cf58a      /* the green phosphor (sidebar, terminal) */
--amber:#f0b64a     /* amber accent (buttons, logo) */
--paper-ink:#0e0f10 /* main text color on paper */
```
Example: to make the accent blue instead of amber, change `--amber:#f0b64a` to `--amber:#5ad1ff`.

---

## 2. HERO SECTION (name, tagline, status)

Find `<div class="hero">`. Inside:

- **Name:** `<h1>Monil Arora</h1>`
- **Taglines:** the two `<div class="tagline">` lines
- **Status pill:** `<div class="status-pill">...Open to embedded / hardware roles</div>`
- **Termlog block** (`<div class="termlog">`): edit the text after each `tl-k` label (CURRENT, BUILDING, DEPLOYED, NEXT). The `[····]` bar and "day …/…" are auto-filled by JS — don't edit those by hand.

### Changing the deployment date range / progress bar
At the bottom of the `<script>`, find the comment `// residency progress`:
```js
var S=new Date(2026,0,25),E=new Date(2026,6,31),W=20,now=new Date();
```
- `S` = start date. **Months are 0-indexed** → `0`=Jan, `6`=July. So `(2026,0,25)` = Jan 25 2026.
- `E` = end date. `(2026,6,31)` = Jul 31 2026.
- `W` = bar width in characters.
The "JAN 25th ⟶ JUL 12th" label is separate hardcoded text in the termlog HTML — update it there too.

---

## 3. TOP BAR & SIDEBAR LINKS

**Top bar:** find `<div class="tb-right">`. Each link is an `<a class="tb-link">`. The GitHub link is commented out (`<!-- ... -->`) — uncomment to show it.

**Region sidebar:** find `<div class="reg-list">`. Each `<a class="reg">` is one section. The `data-target` must match a section's `id` (e.g. `sec-about`). The `addr` and `sz` text is cosmetic, change freely. If you add/remove a region, also update the colored `.memmap` bar below it (the `<div class="seg">` flex values are just visual proportions).

---

## 4. EXPERIENCE — two places to edit

### A) The card (list view)
Find `#sec-experience`. Each role is `<div class="exp" data-detail="exp/lzh">`. Edit the `<h3>` title, `.when` date, `.role` line, the `<p>` summary, and the `.chip` tags. **`data-detail` must match a key in the `DETAILS` object.**

### B) The full write-up
In `<script>`, find the `DETAILS` object and the key `'exp/lzh':`. Fields:
- `title`, `sub`, `addr`, `struct` — header info
- `meta:` — the key/value rows (duration, location)
- `stack:` — chip tags array
- `links:` — external links array (set `primary:true` for filled style)
- `body:` — the full HTML write-up (backtick string). Use `<h2 data-addr="0x...">` for section headers, `<p>`, `<pre><code>`, `<figure><img.../><figcaption>`, and `<div class="callout">` for highlighted notes.

---

## 5. PROJECTS — same two-place pattern

**Card:** `#sec-projects` → `<div class="proj" data-detail="proj/...">`.
**Write-up:** `DETAILS` object → matching `'proj/...'` key. Same field structure as experience.

To **add a new project:**
1. Copy an existing `<div class="proj">` card, change its text and `data-detail` to a new slug like `proj/my-thing`.
2. Copy an existing `DETAILS` entry, rename the key to `'proj/my-thing'`, set `type:'proj'`, fill in fields.
3. Done — prev/next nav and routing update automatically.

---

## 6. IMAGES

Images use a path like `src="images/projects/self-balancing-robot/01-robot.png"`. If the file is missing, a dashed "missing image" placeholder shows automatically (via the `imgFallback` function — don't remove the `onerror="imgFallback(this)"` attribute).

Put image files at the matching path relative to `index.html`. Your photo is `photo.jpg`, resume is `resume.pdf`, both in the same folder as `index.html`.

To enable a hero image at the top of a detail page: uncomment the `hero:` line in that `DETAILS` entry (some are commented out with `//`).

---

## 7. SKILLS / EDUCATION / CONTACT / NOTES

- **Skills:** `#sec-skills` → each `<div class="skbucket">` is a category; chips are `<span class="sk">`.
- **Courses:** `#sec-education` → each `<div class="course">` has a `.code`, `.nm` (name), `.top` (description).
- **Contact:** `#sec-contact` → each `<div class="ccard">` has a `.k` (label) and `.v` (value).
- **Notes block:** `#sec-notes` → edit the `<table>` rows (`td.k` = label, `td.v` = value). Some rows are commented out — uncomment to show.

---

## 8. FOOTER TICKER

In `<script>`, find `const TICKER`. It's an array of `[LABEL, text]` pairs that rotate every 4.5s. Add/remove/comment lines. Change `setInterval(tick, 4500)` to adjust speed (ms).

---

## 9. BOOT ANIMATION

The fake terminal boot is `<div class="boot" id="boot">` near the top of the body. Edit/add `<div class="bl">` lines. It only plays once per browser session (stored in sessionStorage) and is skipped if the URL has a `#hash` or the user prefers reduced motion.

---

## 10. REMOVING ELEMENTS (read this before deleting anything)

General rule: **HTML-only elements are safe to delete. Anything touched by JavaScript needs the JS cleaned up too**, or you'll get console errors / dead behavior. Below, each removal is marked SAFE (just delete the HTML) or LINKED (delete HTML + JS).

### Two ways to remove: comment out vs delete
- **Comment out** (reversible): wrap HTML in `<!-- ... -->`, or put `//` before a JS line. Good for trying things.
- **Delete** (permanent): remove the lines entirely. Do this once you're sure.

### Residency progress bar — LINKED
The bar has two parts:
1. **HTML** — inside the termlog, the `DEPLOYED` line:
   ```html
   <span class="tl-line">...<span class="tl-k">DEPLOYED</span><span class="tl-bar" data-termlog="bar">[····················]</span>  <span data-termlog="day">day …/…</span>  <span class="tl-at">JAN 25th ⟶ JUL 12th</span></span>
   ```
   Delete that whole `<span class="tl-line">`. You can also delete the `<span class="tl-sep"></span>` next to it to remove the gap.
2. **JS** — the entire `// residency progress` block at the bottom of the script (the `(function(){ var S=new Date... })();` IIFE). Delete the whole function.

If you leave the JS but delete the HTML, nothing breaks (the JS just finds no elements and does nothing) — but it's cleaner to remove both. If you keep the JS, it keeps targeting `[data-termlog="bar"]` and `[data-termlog="day"]`, so those are the hooks.

### Whole termlog block — SAFE-ish
Delete the entire `<div class="termlog">...</div>`. The residency JS will then find nothing and silently do nothing — harmless, but delete that JS block too for tidiness.

### Footer ticker — LINKED
1. **HTML** — the `<span class="ticker" id="ticker">...</span>` in the `.statusbar`.
2. **JS** — the `const TICKER = [...]` array and the whole `if(tkK && tkV){...}` block below it.
Safe to leave the JS if you delete the HTML (it null-checks `tkK`/`tkV` and bails), but cleaner to remove both.

### Boot animation — SAFE
Delete the entire `<div class="boot" id="boot">...</div>`. The JS guards with `if(skipBoot)` and an existence check, so it won't error if the element is gone. To disable it *without* deleting, just leave it — it already only plays once per session.

### A whole section (e.g. drop Education entirely) — LINKED to sidebar
1. Delete the `<div class="section" id="sec-education">...</div>`.
2. Delete its sidebar entry: the `<a class="reg" data-target="sec-education">` in `.reg-list`.
3. Fix the `.memmap` bar: remove the matching `<div class="seg" ... title=".education">` so the colored proportions still add up visually (optional, purely cosmetic).
The keyboard/scroll nav rebuilds from whatever sections exist, so no JS edit needed beyond the sidebar link.

### A single project or experience card — LINKED (data integrity)
1. Delete the `<div class="proj" data-detail="proj/foo">` (or `.exp`) card.
2. Delete the matching `'proj/foo': {...}` entry in the `DETAILS` object.
Delete **both** or you'll have a dead detail page with no way in (or a card linking to nothing, which sends the user to a blank detail view). The prev/next nav recomputes automatically from remaining `DETAILS` keys.

### A sidebar region but KEEP the section — not recommended
If you remove a `.reg` link but keep its section, the section still scrolls into view and the scroll-spy still tries to highlight a region that no longer exists — it just won't highlight anything for that range. Works, looks slightly broken. Better to remove both or neither.

### Top-bar / hero links — SAFE
Any `<a class="tb-link">` or hero `.links` `<a>` can be deleted freely. No JS depends on them.

### Status pill, notes block, contact cards, skills, courses — SAFE
All pure HTML. Delete the element (`.status-pill`, `#sec-notes`, a `.ccard`, a `.skbucket`, a `.course`) and nothing else needs touching.

### Quick "is it LINKED?" check
Search the script for the element's `id`, `class`, or a `data-*` attribute. If it appears in the JS, it's LINKED — clean up those references. If it doesn't appear, it's SAFE to just delete the HTML.

---

## TIPS

- **Always edit the card AND the `DETAILS` entry** for any project/role change, or the two views will disagree.
- Test by opening `index.html` directly in a browser (double-click). Hard-refresh (Ctrl/Cmd+Shift+R) to bypass cache.
- The `body:` strings are JavaScript template literals (backticks). If you write a literal backtick or `${` inside them, escape it. Apostrophes inside are fine.
- Keep `data-detail` (card) and the `DETAILS` key identical — that's the link between the two views.
- Don't rename section `id`s without updating the matching `data-target` in the sidebar.
