# EDITING.md — how to change anything on plundis.github.io yourself

Everything on the live site lives in **one file: `index.html`** (in the repo root).
You never need to touch anything else to change text, projects, skills, links, or
write-ups. This guide shows you exactly where each thing is and gives you
copy-paste templates.

The way to find a spot is always the same: open `index.html` in a text editor
(or press `.` on the GitHub repo page to open the web editor), hit
**Ctrl+F / Cmd+F**, and paste the "find this" anchor from each recipe below.
Line numbers move around as you edit, so search by text, not by line number.

---

## 0. Read this first (the two footguns)

**Footgun 1 — the repo has a pile of old `index` files.**
`index(minimal hex).html`, `index(no hex minimal).html`, `index_old.html`,
`index_patched.html`, `index1.html`, `no_recuiter_mode.html`, etc. These are old
drafts. **GitHub Pages only serves the file named exactly `index.html`.** Edit
that one. The rest are ignored by the site. If they annoy you, you can delete
them (your call, they don't affect anything).

**Footgun 2 — the long write-ups live inside backticks.**
The detailed project pages are stored as JavaScript strings wrapped in
backticks: `` body:`...lots of HTML...` ``. Inside one of those `body` blocks you
must **never type a raw backtick `` ` ``**, and if you ever need a literal
`${` you must write it as `\${`. Everything else (normal text, `<p>`, `<h2>`,
`<code>`, quotes) is fine. Break this and the site page goes blank until you
fix it.

Every commit on GitHub is a restore point, so if something breaks you can always
open the repo's commit history and revert. Nothing you do here is permanent.

---

## 1. Where does each thing live?

| I want to change...                        | Search `index.html` for...                      | Zone |
|--------------------------------------------|--------------------------------------------------|------|
| Your name / tagline / "UBC BASc..." line   | `<h1>Monil Arora</h1>`                           | list card |
| The green "Open to ... roles" pill         | `class="status-pill"`                            | list card |
| The CURRENT / BUILDING / DEPLOYED / NEXT box | `class="termlog"`                              | list card |
| The DEPLOYED progress bar dates            | `var S=new Date(`                                | script |
| resume / email / linkedin buttons          | `class="links"`                                  | list card |
| An **experience** card (short version)     | `data-detail="exp/lzh"`                          | list card |
| A **project** card (short version)         | `data-detail="proj/self-balancing-robot"`        | list card |
| Skills chips                               | `data-struct="skillset_t"`                       | list card |
| Education / coursework                     | `data-struct="degree_t[1]"`                       | list card |
| Contact cards                              | `data-struct="contact_t"`                        | list card |
| The "notes" / hobbies block at the bottom  | `class="notes"`                                  | list card |
| A **long write-up** page (the blog view)   | `const DETAILS =`                                | DETAILS |

"List card" = the short scrollable card. "DETAILS" = the long page you get when
you click a card. **They are two separate places.** Editing the card does NOT
edit the long write-up, and vice versa. See section 6 for how they link.

---

## 2. Quick text edits (the 90% case)

### Your name / tagline
Find:
```
<h1>Monil Arora</h1>
<div class="tagline">Embedded firmware engineer · STM32/FreeRTOS · Verilog · YAMCS</div>
```
Change the text between the tags. Leave the tags alone.

### The green status pill
Find `status-pill`. Change the words after the `<span class="dot"></span>`:
```
<div class="status-pill"><span class="dot"></span>Open to embedded / hardware roles</div>
```

### The CURRENT / BUILDING / DEPLOYED / NEXT status box
Find `class="termlog"`. It's one long line. The four rows each start with a
`<span class="tl-k">LABEL</span>` — the text right after each label is what
shows. For example, to change what you're looking for next, find:
```
<span class="tl-k">NEXT</span>looking for 4 or 8 months internships · September 2026
```
and edit that trailing text. Same pattern for `CURRENT`, `BUILDING`, `DEPLOYED`.

### The DEPLOYED progress bar (day X/Y)
The bar fills itself in automatically from two dates in the script. Find:
```
var S=new Date(2026,0,25),E=new Date(2026,6,10),
```
`S` is the start, `E` is the end. **Months are 0-based** in this format, so
`0` = January, `6` = July. `new Date(2026,0,25)` = 25 Jan 2026,
`new Date(2026,6,10)` = 10 Jul 2026. Change these and the bar recomputes.
(The human-readable "JAN 25th ⟶ JUL 12th" text is separate — it's in the
`termlog` line, edit it there to match.)

### resume / email / linkedin buttons
Find `class="links"`:
```
<a class="pri" href="resume.pdf" target="_blank" rel="noopener">resume.pdf ↗</a>
<a href="mailto:monilarora2003@gmail.com">email</a>
<a href="https://linkedin.com/in/monil-arora-a26851290" ...>linkedin</a>
```
To swap your resume, just overwrite `resume.pdf` in the repo with a new file of
the same name — no HTML change needed. There's a commented-out `github` link
right below; delete the `<!--` and `-->` around it to show it.

---

## 3. Skills, education, contact, hobbies

### Add or remove a skill chip
Find `data-struct="skillset_t"`. Each chip is `<span class="sk">NAME</span>`.
Copy an existing one, change the text. To add "Rust" to Languages:
```
<span class="sk">Verilog</span><span class="sk">VHDL</span><span class="sk">Rust</span>
```
The buckets are `Languages`, `Tools`, `Hardware`, `Protocols` (each is a
`<div class="skbucket">`).

### Edit a course
Find `data-struct="degree_t[1]"`. Each course is a `<div class="course">` with a
`code` (e.g. `CPEN&nbsp;311`), a `nm` (course name) and a `top` (description).
The `&nbsp;` is just a non-breaking space so the code doesn't wrap — keep it.
Copy a whole `<div class="course">...</div>` block to add another course.

### Edit contact info
Find `data-struct="contact_t"`. Each entry is a
`<div class="ccard"><div class="k">label</div><div class="v">value</div></div>`.

### Edit the hobbies / notes block
Find `class="notes"`. It's a little table: each row is
`<tr><td class="k">label</td> <td class="v">text</td></tr>`. Edit the text in the
`v` cells (football, games, rabbit holes, travel). There are two commented-out
rows (`reading`, `tinkering`) — remove the `<!--` `-->` to bring them back.

---

## 4. Editing an experience or project **card** (the short one)

Cards are the summaries in the scroll list. Find the card by its `data-detail`:

- Experience: `data-detail="exp/lzh"`, `data-detail="exp/sharang"`
- Projects: `data-detail="proj/self-balancing-robot"`,
  `proj/dnn-accelerator`, `proj/metal-detector-robot`, `proj/reflow-oven-controller`

An experience card looks like:
```
<div class="exp" data-detail="exp/lzh">
  <div class="exp-top"><h3>Laser Zentrum Hannover (LZH) — Research Intern</h3><span class="when">Jan – Jul 2026</span></div>
  <div class="role">MOONRISE · Hannover, Germany</div>
  <p>...summary paragraph...</p>
  <div class="chips"><span class="chip">STM32F401CC</span>...</div>
</div>
```
Edit the `<h3>` title, the `when` date, the `role` line, the `<p>`, and the
`chip` list freely. A project card is the same idea with `class="proj"`,
a `proj-top`, a `tag` line, and a `<p>` (projects don't show chips on the card).

**`data-detail="..."` is the link to the long write-up.** Don't change that
string unless you also rename the matching key in `DETAILS` (section 6).

---

## 5. Editing a **long write-up** (the DETAILS page)

Find `const DETAILS =`. Below it is one entry per page, keyed by the same slug
as the card's `data-detail`. One entry looks like:
```
'exp/lzh': {
  type:'exp',            // 'exp' or 'proj' — controls which prev/next list it's in
  addr:'0x0200',         // decorative hex, cosmetic only
  struct:'role_t',       // decorative label, cosmetic only
  badge:'EXPERIENCE',    // the little uppercase pill at the top
  title:'Laser Zentrum Hannover — Research Intern',
  sub:'CubeSat ground station for the Moonrise mission',
  meta:[
    {k:'duration', v:'Jan – Jul 2026'},
    {k:'location', v:'Hannover, DE'},
  ],
  stack:['STM32F401CC','C++','FreeRTOS', ...],   // chips at the top of the page
  links:[
    {label:'lzh.de ↗', url:'https://www.lzh.de/en', primary:false},
  ],
  //hero:'images/experience/lzh/hero.jpg',        // optional big top image
  body:`
    <h2 data-addr="0x0210">The brief</h2>
    <p>...</p>
    ...
  `,
},
```

**To edit the words:** just change the text inside `title`, `sub`, `meta`
values, and inside `body`. In `body` you're writing plain HTML.

**To add a section heading inside a write-up**, add an `<h2>`:
```
<h2 data-addr="0x02F0">My new section</h2>
<p>Text goes here.</p>
```
The `data-addr` hex is pure decoration (the memory-dump look). Nothing breaks if
it clashes; just make it bigger than the one above it if you want it to look
tidy. You can also drop the `data-addr` entirely — `<h2>My new section</h2>`
works fine.

**To add a chip** to a write-up's stack, add a string to the `stack:[...]` array.
**To add a link**, add `{label:'text ↗', url:'https://...', primary:false}` to
`links`. Set `primary:true` to make one link stand out.

---

## 6. How cards and write-ups connect (important)

A card opens a write-up **only if** its `data-detail` matches a key in
`DETAILS`. So:

- Card `data-detail="proj/metal-detector-robot"` → opens `DETAILS['proj/metal-detector-robot']`.
- If a card has no `data-detail`, it's just a card, not clickable.
- If a card points to a slug that isn't in `DETAILS`, clicking does nothing.

**Prev/next arrows on a write-up** are generated automatically from the order
the entries appear inside `DETAILS`, filtered by `type`. So the order you list
projects in the `DETAILS` object = the order the prev/next buttons walk through.
Reorder the entries in `DETAILS` to reorder the navigation.

The "prev project" label uses the part of `title` before ` — ` (space-dash-space),
so keep the format `Name — subtitle` if you want a clean short label.

---

## 7. Adding a brand-new project (end to end)

Say you build "GPS Tracker" and want a card + a full write-up.

**Step 1 — add the card.** Find the projects grid (`data-struct="project_t[4]"`),
copy one whole `<div class="proj" ...>...</div>` block, paste it, and edit:
```
<div class="proj" data-detail="proj/gps-tracker">
  <div class="proj-top"><h3>GPS Tracker</h3><span class="when">Aug 2026</span></div>
  <div class="tag">STM32 · u-blox · LoRa</div>
  <p>One or two sentence summary.</p>
</div>
```

**Step 2 — add the write-up.** Find `const DETAILS =`, and paste a new entry.
Put it wherever you want it in the prev/next order:
```
'proj/gps-tracker': {
  type:'proj',
  addr:'0x1800',
  struct:'project_t',
  badge:'PROJECT',
  title:'GPS Tracker — LoRa asset tag',
  sub:'Low-power position beacon',
  meta:[
    {k:'when', v:'Aug 2026'},
    {k:'stack', v:'STM32 · LoRa'},
  ],
  stack:['STM32','u-blox','LoRa','Low-power'],
  links:[],
  body:`
    <h2 data-addr="0x1810">The brief</h2>
    <p>What it is and why you built it.</p>

    <figure>
      <img src="images/projects/gps-tracker/01-hero.png" alt="GPS tracker" onerror="imgFallback(this)"/>
      <figcaption>fig 01 — the finished board.</figcaption>
    </figure>

    <h2 data-addr="0x1820">Interesting problems</h2>
    <p>The part worth telling someone about.</p>
  `,
},
```
The slug (`proj/gps-tracker`) must be **identical** in the card and the DETAILS
key. That's the whole link.

**Step 3 — add the images** (next section).

---

## 8. Images

Images live in folders that mirror the slug:
- Experience: `images/experience/<name>/`  (e.g. `images/experience/lzh/`)
- Projects:   `images/projects/<name>/`     (e.g. `images/projects/self-balancing-robot/`)

For a new project, make a folder `images/projects/gps-tracker/`, drop your PNG/JPG
files in, and reference them by that path inside a `body` block:
```
<figure>
  <img src="images/projects/gps-tracker/02-block-diagram.png" alt="block diagram" onerror="imgFallback(this)"/>
  <figcaption>fig 02 — signal chain.</figcaption>
</figure>
```
Always keep `onerror="imgFallback(this)"` — if the image is missing or the path
is wrong, the site shows a tidy placeholder instead of a broken-image icon.
Naming like `01-hero.png`, `02-block-diagram.png` keeps them ordered and matches
your existing folders.

---

## 9. Your own writing rules (so future-you stays consistent)

These are the rules you set for the site's voice. Keep to them when you edit:

- No em-dashes. Use commas, or split into two sentences.
- No semicolons except inside code snippets.
- Avoid "However", "Furthermore", "Moreover", "Additionally", "leverage".
- Short direct sentences, mixed with the occasional longer one.
- Tell it like a story, not a bullet list. Engineer explaining over coffee.
- Structure for a write-up: brief intro → hardware → the interesting problems and
  how you solved them → results → what you'd do differently. No wrap-up paragraph.
- Figures from your PDF reports go inline where they're relevant.

---

## 10. Preview before you publish

**Fastest:** double-click `index.html` on your computer — it opens in the browser
and works, because the site loads nothing over the network.

**Cleaner (recommended for checking image paths):** in the repo folder run
```
python3 -m http.server
```
then open `http://localhost:8000` in your browser. Ctrl+C to stop.

Check: does the page load (not blank)? If it's blank, you almost certainly typed
a stray backtick inside a `body:` block (Footgun 2) — undo your last edit and
try again.

---

## 11. Publish

**Option A — edit on GitHub directly (no tools needed):**
open the repo, click `index.html`, click the pencil icon, make your edit,
scroll down, "Commit changes". GitHub Pages redeploys in about a minute.

**Option B — edit locally and push:**
```
git add -A
git commit -m "update projects"
git push
```
Then wait ~1 minute and refresh plundis.github.io (hard-refresh with
Ctrl+Shift+R if you still see the old version — that's browser cache, not you).

If something looks broken after publishing, open the repo's commit history,
find the last good commit, and revert. You can't lose anything.

---

### One-line cheat sheet
Edit `index.html` only → find your spot with Ctrl+F using the anchors above →
short summaries are the cards, long pages are in `DETAILS` → never put a raw
backtick inside a `body:` block → commit → wait a minute → hard-refresh.
