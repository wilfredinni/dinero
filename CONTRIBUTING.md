Thank you for considering improving `Dinero`, any contribution is much welcome!

## Asking questions

If you have any question about `Dinero`, if you are seeking for help, or if you would like to suggest a new feature, you are encouraged to `open a new issue` so we can discuss it. Bringing new ideas and pointing out elements needing clarification allows to make this library always better!

## Reporting a bug

If you encountered an unexpected behavior using `Dinero`, please `open a new issue` and describe the problem you have spotted. Be as specific as possible in the description of the trouble so we can easily analyze it and quickly fix it.

An ideal bug report includes:

- The Python version you are using
- The `Dinero` version you are using (you can find it with `print(dinero.__version__)`)
- Your operating system name and version (Linux, MacOS, Windows)
- Your development environment and local setup (IDE, Terminal, project context, any relevant information that could be useful)
- Some `minimal reproducible example`

## Implementing changes

If you are willing to enhance `Dinero` by implementing non-trivial changes, please `open a new issue` first to keep a reference about why such modifications are made (and potentially avoid unneeded work).

Prefer using a relatively recent Python version as some dependencies required for development may have dropped support for oldest Python versions. Then, the workflow would look as follows:

1.  Fork the `Dinero` project from GitHub.
2.  Clone the repository locally:

        $ git clone git@github.com:your_name_here/Dinero.git
        $ cd dinero

3.  Install `Dinero`:

        $ poetry install
        $ poetry shell

4.  Create a new branch from `master`:

        $ git checkout master
        $ git branch fix_bug
        $ git checkout fix_bug

5.  Implement the modifications wished. During the process of development, honor `PEP 8` as much as possible.
6.  Add unit tests (don't hesitate to be exhaustive!) and ensure none are failing using:

        $ pytest

7.  Remember to update the documentation if required.
8.  If your development modifies `Dinero` behavior, update the `CHANGELOG.md` file with what you improved.
9.  `add` and `commit` your changes, then `push` your local project::

        $ git add .
        $ git commit -m 'Add succinct explanation of what changed'
        $ git push origin fix_bug

10. If previous step failed due to the tests, fix reported errors and try again.
11. Finally, `open a pull request` before getting it merged!
