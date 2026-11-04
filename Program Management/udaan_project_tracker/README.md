# UDAAN Project Tracker

A shared tracker for the Education and Outreach teams: team and roles, goals (weekly, monthly, quarterly, yearly), weekly plan, per-person targets, deliverables, challenges, and a risk and decision log, with a dashboard that summarises them.

It is a static site (`index.html`), so it runs on GitHub Pages. Team sharing uses Firebase.

## Put it on GitHub
1. Upload this whole folder to `Program Management/udaan_project_tracker` in the repo.
2. Repo Settings > Pages > Deploy from branch > `main` > `/ (root)`.
3. The tracker opens at `https://<owner>.github.io/<repo>/Program%20Management/udaan_project_tracker/`.

## Turn on team sharing (about 10 minutes)
1. Firebase console: create a project (a new one for this tracker is cleaner).
2. Build > Authentication > Sign-in method > enable Google.
3. Build > Authentication > Settings > Authorized domains > add your `github.io` domain.
4. Build > Firestore Database > Create database.
5. Firestore > Rules: paste `firestore.rules`, put your team's email addresses in the list, Publish.
6. Project settings > Your apps > Web app: copy the config into `firebase-config.js` and commit.

Until step 6 is done the tracker runs in local mode: it works, but each person's edits stay in their own browser. The Firebase config is not a secret; the rules are what protect the data.

## Using it
- On an empty tracker, the Dashboard offers "Add starter rows" with the team and the plan to December 2026. Edit or remove anything.
- Add people on the Team tab. They then appear in every owner dropdown.
- Click any cell to edit. Changes save automatically.
