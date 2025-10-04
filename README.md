# dsa-drills

Repository for practicing data structures & algorithms.

This repo contains small practice problems and reference solutions organized by topic and language (C++, Python, Go, Java). The layout is intentionally simple so you can add solutions and keep them grouped by problem and language.

## Repository layout

Top-level folders correspond to high-level topics. Inside each topic are problem folders which usually contain:

- `problems.md` — problem descriptions, links or notes.
- language folders (`cpp/`, `python/`, `go/`, `java/`) — solution files for that problem.

Example:

```
arrays/
	maximum-subarray/
		problems.md
		cpp/
			solution.cpp
		python/
			solution.py
```

## How to run solutions

Below are common commands you can use from the repository root. Replace paths and filenames to match the specific problem and file.

C++ (g++):

```
g++ -std=c++17 -O2 path/to/solution.cpp -o /tmp/solution && /tmp/solution
```

Java:

```
javac path/to/Solution.java
java -cp path/to package.and.ClassName   # or: java -cp . Solution
```

Python:

```
python3 path/to/solution.py
```

Go:

```
go run path/to/solution.go
```

Notes:

- Some problems require input via stdin; you can redirect a file: `./solution < input.txt` or `python3 solution.py < input.txt`.
- If you prefer an IDE, open the specific language folder and run using your IDE's run configuration.

## Adding a new solution

1. Find or create the appropriate problem folder under the relevant topic (for example `arrays/new-problem/`).
2. Add a `problems.md` (or update it) with the problem statement and any test cases you used.
3. Add your solution file inside the language folder (e.g., `cpp/solution.cpp` or `python/solution.py`).
4. Do not commit compiled binaries, build artifacts, or virtualenvs — those are ignored by the repo `.gitignore`.

Naming suggestions:

- Use descriptive file names if you keep multiple variants (e.g., `solution_recursive.cpp`, `solution_iterative.py`).
- Prefer `solution.*` when there's a single canonical file per language.

## Code style & tools

- C++: Use `clang-format` or `astyle` with a consistent style. Target C++17 unless the problem needs otherwise.
- Python: Use `black` for formatting and `flake8` or `pylint` for linting where helpful.
- Go: Use `gofmt` (or `go fmt`) and `go vet`.
- Java: Use your preferred formatter; keep code readable and well-commented.

## Git workflow

- Create a topic branch for larger additions: `git checkout -b feat/<short-description>`.
- Keep commits small and focused; use clear commit messages (e.g., `arrays: add Kadane solution in C++`).
- Open a pull request when ready for review.

## .gitignore

A repository-level `.gitignore` has been added to ignore common build artifacts, editor files and virtual environments. If you need to exclude additional generated files from a particular subfolder, either add them to the repository `.gitignore` or add a folder-specific `.gitignore`.

## Tests

There are no automated test harnesses included by default. If you add unit tests, add commands here documenting how to run them.

## Contact / License

This repository is for personal practice. If you'd like to collaborate or suggest improvements, open an issue or a pull request.
