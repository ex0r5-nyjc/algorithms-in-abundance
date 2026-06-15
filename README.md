# General Algorithm Practice Repository

This repository contains programming exercises focused on algorithm implementation and problem-solving techniques. Each exercise emphasizes different algorithmic approaches and computational thinking.

## Repository Structure

The exercises are organized by algorithm type:

### Greedy Algorithms
- **[Minimum Coins](minimum-coins/)**: Change-making problem using greedy approaches

### Backtracking Algorithms
- **[Sudoku Solver](sudoku-solver/)**: Recursive backtracking for solving puzzles

### Layout & Organization Algorithms
- **[Booklet Layout](booklet-layout/)**: Page order generation for booklet printing

### Text Algorithms (Stretch Task)
- **[Myers Diff](myers-diff/)**: Text comparison and difference generation

## How to Use This Repository

Each exercise directory contains:
- **README.md**: Detailed exercise description, examples, and challenges
- **main.py**: Starter code with function signatures and documentation
- **test_main.py**: Comprehensive test suite including property-based tests

## Running the Exercises

1. Navigate to an exercise directory:
   ```bash
   cd minimum-coins
   ```

2. Read the README.md to understand the exercise requirements

3. Implement the functions in main.py

4. Run the tests:
   ```bash
   python test_main.py
   ```

## Testing Philosophy

The test files use a combination of:
- **Unit tests**: Specific test cases for individual functions
- **Property-based tests**: Using Hypothesis library to test properties that should hold for all inputs
- **Integration tests**: Testing the complete functionality

To run property-based tests, install the Hypothesis library:
```bash
pip install hypothesis
```

## Learning Objectives

These exercises help develop skills in:
- **Algorithm Design**: Understanding and implementing fundamental algorithms
- **Problem Solving**: Breaking down complex problems into manageable steps
- **Recursion**: Implementing recursive solutions for appropriate problems
- **Optimization**: Balancing time and space complexity
- **Testing**: Writing comprehensive tests including property-based testing
- **Documentation**: Understanding and implementing from specifications

## Algorithm Categories

### Greedy Algorithms
Greedy algorithms make locally optimal choices at each step with the hope of finding a global optimum. They work well for certain problems like the change-making problem when the coin denominations are canonical.

### Backtracking
Backtracking is a systematic way to enumerate all possible solutions by trying partial solutions and abandoning them when they cannot lead to a valid solution. It's particularly useful for constraint satisfaction problems like Sudoku.

### Layout Algorithms
Layout algorithms involve organizing items in specific patterns for practical applications. The booklet layout algorithm demonstrates how mathematical patterns are used in real-world printing and publishing.

### Text Processing
Algorithms for comparing and processing text are essential for many applications, from version control systems to bioinformatics.

## Exercise Difficulty

- **Foundation**: minimum-coins, sudoku-solver, booklet-layout
- **Stretch**: myers-diff (complete after foundation exercises)

## Contributing

This repository is part of the NYJC Computing 2026 curriculum. For questions or issues, please refer to the course materials.

## License

Educational use for NYJC Computing curriculum.
