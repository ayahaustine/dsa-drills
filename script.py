import os

# Root repo
ROOT = "dsa-drills"

# Topic → Problems mapping
structure = {
    "arrays": [
        "two-sum", "rotate-array", "maximum-subarray"
    ],
    "strings": [
        "valid-anagram", "longest-substring-without-repeating", "longest-palindromic-substring"
    ],
    "matrices": [
        "rotate-image", "set-matrix-zeroes", "search-a-2d-matrix"
    ],
    "linked-lists": [
        "reverse-linked-list", "merge-two-sorted-lists", "linked-list-cycle", "remove-nth-node-from-end"
    ],
    "stacks-queues": [
        "valid-parentheses", "min-stack", "implement-queue-using-stacks", "daily-temperatures"
    ],
    "hashmaps-sets": [
        "group-anagrams", "two-sum-ii", "longest-consecutive-sequence"
    ],
    "recursion-backtracking": [
        "subsets", "permutations", "combination-sum", "word-search"
    ],
    "trees": [
        "maximum-depth-binary-tree", "validate-binary-search-tree", "lowest-common-ancestor", "binary-tree-level-order-traversal"
    ],
    "graphs": [
        "number-of-islands", "clone-graph", "course-schedule", "word-ladder"
    ],
    "dp-basics": [
        "climbing-stairs", "house-robber", "coin-change", "unique-paths"
    ],
    "dp-advanced": [
        "longest-increasing-subsequence", "word-break", "edit-distance", "maximal-square"
    ],
    "greedy": [
        "jump-game", "gas-station", "non-overlapping-intervals", "huffman-coding"
    ],
    "bit-manipulation": [
        "single-number", "counting-bits", "reverse-bits"
    ],
    "number-theory": [
        "sieve-of-eratosthenes", "gcd", "modular-exponentiation"
    ],
    "tries": [
        "implement-trie", "word-search-ii"
    ],
    "segment-fenwick-trees": [
        "range-sum-query-mutable", "fenwick-tree-demo"
    ],
    "advanced-graphs": [
        "network-delay-time", "critical-connections", "max-flow"
    ],
    "advanced-dp": [
        "traveling-salesman-bitmask", "digit-dp", "dp-optimization-techniques"
    ]
}

languages = ["python", "cpp", "java", "go"]

def create_structure():
    for topic, problems in structure.items():
        for problem in problems:
            base_path = os.path.join(ROOT, topic, problem)

            # Create problem folder
            os.makedirs(base_path, exist_ok=True)

            # Create problems.md
            problem_md = os.path.join(base_path, "problems.md")
            if not os.path.exists(problem_md):
                with open(problem_md, "w") as f:
                    f.write(f"# {problem.replace('-', ' ').title()}\n\n")
                    f.write("Link: \n\nNotes:\n")

            # Create language subfolders and starter files
            for lang in languages:
                lang_path = os.path.join(base_path, lang)
                os.makedirs(lang_path, exist_ok=True)

                # File naming convention
                if lang == "python":
                    filename = f"{problem.replace('-', '_')}.py"
                elif lang == "cpp":
                    filename = f"{problem.replace('-', '_')}.cpp"
                elif lang == "go":
                    filename = f"{problem.replace('-', '_')}.go"
                elif lang == "java":
                    filename = f"{''.join(word.capitalize() for word in problem.split('-'))}.java"

                filepath = os.path.join(lang_path, filename)
                if not os.path.exists(filepath):
                    with open(filepath, "w") as f:
                        f.write("// Solution placeholder\n" if lang != "python" else "# Solution placeholder\n")

if __name__ == "__main__":
    create_structure()
    print(f"Folder structure created under '{ROOT}/'")
