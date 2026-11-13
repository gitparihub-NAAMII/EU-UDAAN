# Program Management – Work Record

_Record of how UDAAN programme management was set up on the EU UDAAN dashboard: what was done, why, the problems met and how they were solved._

| | |
|---|---|
| **Owner** | Sumi Dhakal, Project Manager, EU UDAAN (NAAMII) |
| **Period** | 4–13 November 2026 |
| **How** | Work done by Sumi with help from Claude (an AI assistant) for code, file conversion and testing |
| **Repository** | https://github.com/gitparihub-NAAMII/EU-UDAAN (formerly AI-Native-Cohort-Depo) |
| **Live dashboard** | https://gitparihub-naamii.github.io/EU-UDAAN/ |

---

## 1. Why this work was needed

- The UDAAN team tracked goals, weekly plans, targets, to-dos, deliverables, challenges and risks in an Excel workbook (`UDAAN_Project_Tracker.xlsx`) and Markdown files. Updates depended on one person editing the Excel file, so information was often out of date.
- What each partner committed to the EU, and progress on it, was not visible in one place (raised as a challenge in the tracker itself).
- Team members needed a simple way to report their own progress without editing the master tracker, and the Project Manager needed those updates to land in the tracker without retyping them.
- The cohort dashboard already had a Project Tracking tab for cohorts and participants, but nothing for programme management.

## 2. What was done (timeline)

| Date | What | Result |
|---|---|---|
| 4 Nov | Project tracker set up: Excel workbook plus Markdown files (goals, team, targets, to-do, deliverables, challenges, risks and decisions) | Uploaded to `Program Management/Udaan_project_tracker/` |
| 6 Nov | Tracker review: added 7 challenges, 8 risks, 4 decisions and 8 follow-ups | Excel and Markdown updated; owners marked "please confirm" |
| 13 Nov | Git installed on the Project Manager's laptop and the dashboard repository cloned | Changes can now be made and pushed from the laptop |
| 13 Nov | **Program Management tab** added to the dashboard, next to Project Tracking | Lists programmes; UDAAN opens the full tracker in the same layout as Project Tracking |
| 13 Nov | Tracker data moved from a public Excel file to a **private Firebase database** | Only the owner can read or change it |
| 13 Nov | **Owner-only editing**: add, edit and delete rows on every sheet; export to Excel; replace from Excel | Sumi manages the tracker directly on the dashboard |
| 13 Nov | **Team "My updates" form** for Drabid, Ramesh and Pradip, with automatic merge into the tracker | Team members update only their own items; updates merge automatically |
| 13 Nov | Markdown versions of all reports and project files in `NAAMII_Report/` and `Project_Infos/` | Much smaller files that are faster to read and search (originals kept) |
| 13 Nov | Updated tracker Excel and Markdown pushed to GitHub | GitHub matches the latest tracker |
| 13 Nov | Team changed: Unisa removed; `sumi.dhakal@naamii.org.np` added as owner and listed as Sumi Dhakal | Ready for Sumi's new login |
| 13 Nov | **My updates for the owner** and **Add a to-do** on the update form | Sumi and the team can write updates and add to-dos that merge into the To-do sheet |

## 3. How it works now

**Who sees what**

| Person | Login | What they see and can do |
|---|---|---|
| Sumi Dhakal (owner) | `sumi@naamii.org.np` now; `sumi.dhakal@naamii.org.np` once set up | Full UDAAN tracker: overview, every sheet, add/edit/delete, Team updates, My updates, Export to Excel |
| Drabid Subedi | `drabid@naamii.org.np` | My updates: only his own items |
| Ramesh Lama | `ramesh@naamii.org.np` | My updates: only his own items |
| Pradip Chaudhary | `pari@naamii.org.np` | My updates: only his own items |
| Everyone else | – | The tab is hidden |

**Flow of a team update**

1. The tracker is loaded once from `UDAAN_Project_Tracker.xlsx` into the private database.
2. Each team member automatically receives a private copy of only the rows where they are the Owner.
3. In **My updates** they change progress, status, actuals and notes, add weekly tasks, add to-dos, raise a challenge or write a note, then press **Submit my update**.
4. The update is merged into the tracker automatically while the owner's dashboard is open (on any tab), or the next time the owner signs in. Each update is merged once, and only into rows the sender owns.
5. **Team updates** shows who sent what and when, with the merge result.

**Where the data lives** (Firebase project `ai-native-cohort-calendar`, Firestore):

| Collection | Holds | Who can read / write |
|---|---|---|
| `udaan_program_management` | The full tracker | Owner only |
| `udaan_pm_people` | Each team member's own rows | That member reads; owner writes |
| `udaan_pm_updates` | Submitted updates | Members create their own; owner reads and marks them merged |

The exact Firestore rules are written in the header of the Program Management code in `index.html` ("UDAAN add-on patch 18").

## 4. Why it was done this way

| Decision | Reason |
|---|---|
| Build Program Management as a tab inside the existing dashboard | The team already uses the dashboard and its admin logins; one place, one sign-in, the same look as Project Tracking. |
| Keep the tracker in a private database, not as an Excel file on GitHub | The repository and website are public. Team names, risks and internal challenges should not be downloadable by anyone. |
| Only the owner can edit the tracker directly | One accountable person keeps the master record consistent and avoids conflicting edits. |
| Team members submit updates instead of editing the tracker | They can report progress without risk of changing other people's rows; the owner keeps control and still saves retyping. |
| Merge only into rows the sender owns | Stops anyone (by mistake or on purpose) from changing someone else's items. |
| Merge in the owner's browser instead of a server | The project has no backend; a Firebase server function would need a paid plan. The trade-off is that merging happens when the owner's dashboard is open. |
| Keep Export to Excel and Replace from Excel | Reports and the EU still need Excel; the team can move between the dashboard and the file at any time. |
| Convert reports and project files to Markdown | Plain-text copies are far smaller (e.g. 1.7 MB grant PDF → 67 KB) and easier to search, read and reuse; originals are kept. |
| Test everything in a local preview with a stand-in database first | Nothing was written to the real database until the behaviour was confirmed. |

## 5. Challenges and how they were solved

| Challenge | What happened | How it was solved |
|---|---|---|
| Dashboard link showed "404 not found" | The repository had been renamed from AI-Native-Cohort-Depo to **EU-UDAAN**. | Used the new address; GitHub redirects the old one for code, not for the website. |
| Git was not installed | The laptop could not download or upload the code. | Installed Git for Windows and set up the GitHub sign-in. |
| Windows "filename too long" errors | Some course folders in the repository have very long names. | Turned on long-path support for the repository. |
| Tracker Excel would have been public | The first version read the Excel file from the public repository. | Moved the data into a private Firebase collection that only the owner can read. |
| Firebase rules could only be set by the project owner | Sumi's Google account has no access to the Firebase project. | Pradip added the rules; the exact rule text is kept in the code and in this record. |
| Two email addresses for Sumi | Signed in as `sumi@naamii.org.np`, but wants to use `sumi.dhakal@naamii.org.np`. | Both are treated as the same owner in the code; Pradip needs to add the new login and rules (see section 6). |
| Owner could not write "My updates" | The update form was built only for team members. | Added a My updates page for the owner as well. |
| No way to add to-dos from the form | The form could update existing to-dos only. | Added "Add a to-do"; new tasks merge into the To-do sheet with the sender as owner. |
| Testing without real logins | The real logins could not be used for testing. | Built a local preview with stand-in logins and a pretend database. |
| Bugs found during testing | The form showed "1 change" before anything was edited (line breaks in Excel notes), and a merge could be counted twice. | Both fixed before release. |
| Other people pushing at the same time | Uploads were rejected because teammates had pushed changes. | Fetched their changes and added ours on top; nobody's work was overwritten. |
| "I don't see the changes" | The tab is hidden until the right person signs in, and the Markdown files at first existed only on the laptop. | Explained sign-in; uploaded the Markdown files to the matching GitHub folders. |
| PDF conversion | Word got stuck on a hidden prompt; changing the Word setting was not allowed. | Read the PDFs directly and wrote clean Markdown; Excel and slide decks were read from their internal files. |

## 6. Still open

- [ ] **Pradip:** create the Firebase login `sumi.dhakal@naamii.org.np`, add its UID to `udaan_admins`, and add the address to the three Program Management rules.
- [ ] After that, switch the short username "sumi" on the login screen to the new address.
- [ ] Bishesh, Alok and Kaushal own tracker items but have no dashboard login, so they cannot use My updates yet.
- [ ] The tracker Excel and Markdown files on GitHub do not update by themselves. Use **Export to Excel** on the dashboard and upload the file when an updated copy is needed.
- [ ] Owners marked "please confirm" on the 6 Nov challenges, risks and follow-ups still need confirming.

## 7. How to maintain it

- **Add or remove a team member:** edit `PM_TEAM` in `index.html` (search for "WHO CAN USE PROGRAM MANAGEMENT"). Each person needs a dashboard login.
- **Add or remove an owner:** edit `PM_EDITORS` in `index.html` **and** the email list in the three Firebase rules.
- **Reload the tracker from Excel:** Program Management → UDAAN → **Replace from Excel…** (this replaces everything in the dashboard copy).
- **Get a copy for reports:** **Export to Excel**.

## 8. Where things are

| What | Location |
|---|---|
| Dashboard code (Program Management) | `index.html`, section "UDAAN add-on patch 18" |
| Tracker Excel and Markdown | `Program Management/Udaan_project_tracker/` |
| Monthly reports and major updates (PDF and Markdown) | `Program Management/NAAMII_Report/` |
| Grant application, decks, Karmashala outreach, NAAMII's role (originals and Markdown) | `Program Management/Project_Infos/` |
| This record | `Program Management/Program_Management_Work_Record.md` |
