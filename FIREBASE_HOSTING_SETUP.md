# DS Labs — Firebase Hosting for AdMob app-ads.txt

Purpose: Publish a *public*, free DS Labs developer site containing
`app-ads.txt` at the **hostname root** so Google AdMob can verify ScanNexa.
This does **not** change Aruba, the Android app, signing, or GitHub Pages.

## Status

- Static contents and deployment configuration are prepared in this repository.
- **Firebase project creation, account authorization and deployment have NOT been completed.**
- The project ID and public URL are unknown until a Firebase project is created and deployed.
- Existing GitHub Pages URL `https://joshuads1994-code.github.io/ds-labs-legal/`
  is a *path-based* site. Its `/ds-labs-legal/app-ads.txt` is **not**
  the `/app-ads.txt` path checked at the hostname root.
- No GitHub Actions, merges, Android release changes, billing activation or paid services.

## Firebase account setup (owner action)

1. Open https://console.firebase.google.com/ with the intended Google account.
2. Create a Firebase project (e.g. display name **DS Labs Public**).
   Select the **Spark** plan; do not activate **Blaze** or billing.
   A project ID must be confirmed by Firebase; do not assume an ID is available.
3. Use **Firebase Hosting** (static hosting), not **Firebase App Hosting**.
   The default free subdomain will be `https://<PROJECT_ID>.web.app`
   once the project exists and Hosting is deployed.

## Deploy from a trusted local Mac terminal

Prerequisites: Firebase CLI (see https://firebase.google.com/docs/cli),
Google sign-in, and an up-to-date local checkout of this repository.

```bash
cd ds-labs-legal
python3 tools/sync-firebase-site.py
firebase login
firebase projects:list
firebase deploy --only hosting --project <PROJECT_ID>
```

Replace `<PROJECT_ID>` with the **actual** Firebase project ID shown in
the Firebase Console. Do not type the angle brackets. The CLI can also run
in Google Cloud Shell if local installation is not convenient.

The project has a committed `firebase.json`: do **not** run
`firebase init hosting` and overwrite it. No `.firebaserc` is necessary
because the deployment explicitly chooses the Firebase project ID.

The deploy directory is **only** `firebase-site/`, so private code,
`README.md`, the Git repository metadata and source documentation cannot
be accidentally published.

## Verify the live result BEFORE updating Play Console

After a successful deploy, inspect these exact URLs:

- `https://<PROJECT_ID>.web.app/` — public DS Labs homepage.
- `https://<PROJECT_ID>.web.app/app-ads.txt` — HTTP 200 with content:
  `google.com, pub-5743584111440579, DIRECT, f08c47fec0942fa0`
- `https://<PROJECT_ID>.web.app/privacy/scannexa/` — ScanNexa privacy.
- `https://<PROJECT_ID>.web.app/privacy/arrowflow/` — ArrowFlow privacy.

Verify the `app-ads.txt` response is `text/plain`, readable without
authentication, not an HTML rewrite/redirect to a sign-in page.
A 404 means Hosting was not deployed or the project/URL is wrong.

## Connect the public website to the Google Play listing

1. Open Google Play Console, select ScanNexa.
2. Go to **Grow users / Store presence / Store settings / Store listing contact details**.
3. Set **Developer website** to exactly `https://<PROJECT_ID>.web.app/`.
   Do not enter the `/app-ads.txt` path and do not use the old
   GitHub Pages path, since its hostname root is different.
4. Save, check the public Play listing's app-support developer website,
   and allow time for Google to ingest the change.
5. Open AdMob / ScanNexa / app verification. Select the existing
   `com.dslabs.scannexa` Play listing, then choose the verification/
   `Check for updates` action. AdMob reviews the site and subsequently
   the app; immediate approval is not guaranteed.

No new AdMob application or Android app update is required.

## Maintenance

Keep the existing root pages as canonical. After changing an existing privacy
page or `app-ads.txt` record, run `python3 tools/sync-firebase-site.py`,
commit both sources and public copies, and redeploy Hosting.

For a new DS Labs app, add its publicly safe policy page to the source root
and update the allowlist in the script. Only add an additional authorized ad
seller if the corresponding publisher account and status justify it.

## Official references

- https://support.google.com/admob/answer/9820295
- https://support.google.com/admob/answer/9363762
- https://firebase.google.com/docs/hosting/quickstart
- https://firebase.google.com/docs/cli
