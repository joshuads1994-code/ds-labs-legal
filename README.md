# DS Labs — Public developer website and legal pages

Public static site, privacy policies and AdMob `app-ads.txt` for the DS Labs Android portfolio. No private source or credentials belong in this repository.

## Current websites

- **Firebase Hosting (Spark):** https://ds-labs-public.web.app/
- **AdMob seller record:** https://ds-labs-public.web.app/app-ads.txt
- **ScanNexa privacy:** https://ds-labs-public.web.app/privacy/scannexa/
- **ArrowFlow privacy:** https://ds-labs-public.web.app/privacy/arrowflow/
- **Legacy GitHub Pages legal site:** https://joshuads1994-code.github.io/ds-labs-legal/

The Firebase deploy was confirmed by an owner screenshot on 2026-10-21; ScanNexa's Google Play store association and AdMob verification were confirmed by later AdMob screenshots. **AdMob approval remains pending** at the time of this entry. Independent HTTP verification was not available in the ChatGPT environment.

## Maintenance

Canonical pages live at repository root and under `privacy/`. Firebase deploys the allowlisted copies under `firebase-site/`. Keep these synchronized with:

```bash
python3 tools/sync-firebase-site.py
firebase deploy --only hosting --project ds-labs-public
```

The project is on the free Firebase Spark plan; do not enable Blaze billing for this use case. For detailed instructions, constraints and verification status, see [FIREBASE_HOSTING_SETUP.md](FIREBASE_HOSTING_SETUP.md).
