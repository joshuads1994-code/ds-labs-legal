# DS Labs Public — Firebase Hosting and AdMob verification

**Current operational status: 2026-10-21, Europe/Rome (owner screenshots)**

## Confirmed milestones

| Item | Status | Evidence |
|---|---|---|
| Firebase project | **CREATED** — `DS Labs Public`, project ID `ds-labs-public` | Firebase Console screenshot |
| Plan | **Spark (free)** | Firebase Console screenshot |
| Static Firebase Hosting deployment | **COMPLETE (owner Cloud Shell)** | CLI screenshot with `Deploy complete!` and Hosting URL |
| Canonical Hosting domain | `https://ds-labs-public.web.app/` | Firebase Hosting dashboard/CLI |
| AdMob `app-ads.txt` | Source staged in `firebase-site/app-ads.txt`; expected at hostname root | GitHub source and deployment command |
| Google Play association | **LINKED** — ScanNexa `com.dslabs.scannexa` | AdMob app settings screenshot |
| AdMob app verification | **SUCCEEDED** — `Verifica eseguita` and `La verifica ... è andata a buon fine` | AdMob verification screenshots at 23:43 |
| AdMob advertising approval | **PENDING** — `In preparazione`; review reportedly ~2–3 days, not a guarantee | AdMob app settings/confirmation screenshots |
| AdMob consent messages / UMP | **NOT RE-QUALIFIED here** | Existing Android qualification has UMP network failure |
| AdMob ad delivery restrictions | **NOT YET LIFTED** | App approval not yet granted |

Deployment and successful AdMob verification are based on screenshots supplied by the owner. A separate HTTP 200/content-type check of the live Firebase endpoint was not obtained through the current ChatGPT environment; do not claim independent live-server verification.

## Public URLs and record

- **Developer website (enter in Google Play):** `https://ds-labs-public.web.app/`
- **AdMob seller list (root of hostname):** `https://ds-labs-public.web.app/app-ads.txt`
- ScanNexa public privacy page: `https://ds-labs-public.web.app/privacy/scannexa/`
- ArrowFlow public privacy page: `https://ds-labs-public.web.app/privacy/arrowflow/`
- Legacy GitHub Pages policies: `https://joshuads1994-code.github.io/ds-labs-legal/privacy/scannexa/` and `.../privacy/arrowflow/` (still referenced by existing Android builds; do not break).

Exact `app-ads.txt` line:

```text
google.com, pub-5743584111440579, DIRECT, f08c47fec0942fa0
```

**Only this publisher is authorized in the current source.** Do not add ad sellers or modify it without confirming ownership.

## Architecture

- Repository: `joshuads1994-code/ds-labs-legal` (main).
- Firebase config: `firebase.json` uses `hosting.public = "firebase-site"`, not the repository root.
- Project selection: `.firebaserc` defaults to `ds-labs-public`.
- Canonical source pages: `index.html`, `app-ads.txt`, `privacy/scannexa/index.html`, `privacy/arrowflow/index.html`.
- Deploy copies: corresponding allowlisted paths in `firebase-site/`.
- Sync helper: `tools/sync-firebase-site.py`, verifies copied bytes and publisher record.
- GitHub Pages legal site remains available; this deployment does not modify Aruba, `.htaccess`, Android code, Play releases, ads IDs or billing.

**Do not use Firebase App Hosting or upgrade to Blaze.** The Spark static Hosting site is sufficient for the AdMob use case.

## Deployment / updates

For future changes to canonical public pages, update the source files first, then from a trusted checkout:

```bash
python3 tools/sync-firebase-site.py
firebase deploy --only hosting --project ds-labs-public
```

Or on a new Cloud Shell checkout:

```bash
git clone --depth 1 https://github.com/joshuads1994-code/ds-labs-legal.git
cd ds-labs-legal
python3 tools/sync-firebase-site.py
firebase deploy --only hosting --project ds-labs-public
```

Use a newly cloned directory or `git pull --ff-only` if an existing checkout has been updated safely. No changes should be deployed without reviewing the source; no public keys/passwords belong in the repo.

For a new DS Labs app, add its privacy page to the canonical sources, explicitly add its relative path to the allowlist and public index, sync, commit and redeploy. Do not add unrelated files to `firebase-site/`.

## Remaining AdMob / Play work

1. Keep the verified developer site `https://ds-labs-public.web.app/` in the public **ScanNexa Google Play** listing. Check it stays correct if the listing is edited.
2. AdMob app `ScanNexa: QR & Barcode Scanner` is **verified**, but **approval remains `In preparazione`**. Wait for AdMob's review status/email; do not re-create the app or repeatedly restart verification.
3. In AdMob **Privacy & messaging**, confirm an appropriate Google-certified CMP message is active for EEA/UK/Switzerland and applicable US states as needed. The AdMob screenshot advised this, but it did not prove publication or correct display on device.
4. Use Google official TEST ad units for any implementation/runtime tests, **no live impression/click testing by family/developer devices**.
5. Following approval, examine real AdMob request, match, impression, show, eCPM and policy-center metrics to plan low-disruption placements for ScanNexa 1.0.2. Historical tiny sample (2026-10-21): 24 requests, 2 impressions, 100% match, eCPM EUR 0.74; **not a revenue forecast**.

## Source-of-truth and constraints

User's 2026-10-21 screens show a completed Firebase deploy and successful AdMob verification. These do not independently prove DNS, HTTP status, CMP display, unrestricted monetization, or Play Console public metadata. The earlier AdMob error said *developer website missing from Play listing*; the later success supersedes **that** verification blocker only.

No GitHub Actions were manually launched, no app binary was built, no merge was performed, no Play release was changed, and no new paid Firebase service was enabled as part of this documentation update.

## References

- https://firebase.google.com/docs/hosting/quickstart
- https://firebase.google.com/docs/cli
- https://support.google.com/admob/answer/9820295
- https://support.google.com/admob/answer/9363762
