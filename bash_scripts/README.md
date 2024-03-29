# Bash scripts

## For development
- [`init_compile.sh`](init_compile.sh) populates the database and compiles `Babel` message catalog (for i18n).
- [`pull_data.sh`](pull_data.sh) downloads data files from the [data repository](https://github.com/lemontree210/langworld_db_data/) with `git subtree`, merges changes into `master` (note that an editor for a commit message will pop up) and re-populates the SQL database. This script does **not** automatically push the changes to remote repository of `langworld_db_pyramid` (this project). Do that when you're ready.

## For running on the web server
- [`update.sh`](update.sh) pulls `langworld_db_pyramid` from GitHub, populates the SQL database, compiles `Babel` message catalog for i18n.
