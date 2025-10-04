# Contributing to dsa-drills

Thanks for your interest in contributing! This repository is a personal practice playground for data structures and algorithms, but contributions and improvements are welcome.

Please follow these simple guidelines so contributions remain consistent and easy to review.

1. Pick a problem or topic

- Browse the directory structure and find a topic folder (for example `arrays/` or `graphs/`).
- If the problem isn't present, create a new folder named with a short, kebab-case identifier (for example `shortest-path-bellman-ford/`). Add a `problems.md` with the problem statement and links.

2. Create or update language solutions

- Add your solution under the appropriate language folder: `cpp/`, `python/`, `go/`, or `java/`.
- Prefer a single canonical file named `solution.*` (for example `solution.cpp`) unless you intentionally provide multiple approaches; then use descriptive filenames like `solution_recursive.cpp` or `solution_dp.py`.

3. Tests and examples

- If your solution expects stdin, provide an `example.txt` or `tests/` folder with sample input(s) and their expected output(s).
- Keep test inputs small so they are easy to run locally.

4. Formatting and style

- Keep code readable and documented with brief comments explaining tricky parts.
- C++: target C++17. Run `clang-format` or `astyle` where convenient.
- Python: format with `black` and lint with `flake8` or `pylint` if possible.
- Go: run `gofmt` and `go vet`.

5. Commits and PRs

- Use a descriptive branch name: `feat/<topic>-<short-desc>` or `fix/<topic>-<short-desc>`.
- Make small, focused commits. Write clear commit messages (subject line and optional body).
- Open a pull request and describe what you added (language, complexity, special notes).

6. What not to commit

- Compiled binaries, build artifacts, editor config files and virtual environments. The repo `.gitignore` already contains common patterns for these.

7. Licensing and ownership

- Add only code you are comfortable sharing publicly. If you copy from other sources, include attribution and ensure the license allows redistribution.

8. Questions or suggestions

- Open an issue explaining your idea or request.

Thank you for helping keep this repo useful and tidy!
