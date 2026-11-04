# Team guide: how to edit and push

Two ways to do it. The first needs no software and is the easiest to start with.

## Way 1: edit on the GitHub website

1. Open the repo on GitHub and go to `Program Management/udaan_project_tracker`.
2. Click the file you want to change, for example `todo.md`.
3. Click the pencil icon (Edit this file) at the top right of the file.
4. Change your own rows. In a table, each row is one line and each column is separated by `|`.
5. Scroll down and click **Commit changes**. Write a short message, such as `Mark CV link task done`, and confirm.

GitHub always shows the latest version when you open a file, so you do not need to pull first.

## Way 2: use Git on your computer

Do this once to get the files:

    git clone <repo link>
    cd EU-UDAAN/"Program Management"/udaan_project_tracker

Each time you work:

    git pull
    (edit the files in any text editor)
    git add .
    git commit -m "Update Pradeep's weekly plan"
    git push

## Editing a table

Keep the header row and the `|` characters. To add a row, copy a whole line and change the text. Do not put a `|` inside a cell; use a dash or a slash. For a line break inside a cell, type `<br>`.

Example row in `todo.md`:

    | Send the college visit schedule | High | Pradeep Chaudary | Outreach | 10 Nov 2026 | In progress | Waiting for dates |

## If two people edit the same file

Pull again before you push. If Git reports a conflict, do not guess: ask Drabid. To avoid conflicts, edit only your own rows and push small changes often.

## Where things go

- Your plan for the week: your section of `weekly-plan/<Monday date>.md`
- A new task: `todo.md`
- Something blocking you: `challenges.md`
- A decision the team made: `risks-and-decisions.md`
- Meeting notes: a new file in `meeting-notes/`, named with the date

## Do not

- Do not upload passwords, personal data of learners or private documents.
- Do not rename or move the files. The dashboard reads them by name.
