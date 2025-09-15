# AI Agent Instructions for python-p3-sequences

This is a Python learning project focused on sequence data structures and their operations. When working in this codebase, keep these key aspects in mind:

## Project Structure

- `/lib/sequences.py`: Core implementation of sequence operations
- `/lib/testing`: Contains pytest test files
- Root directory contains example implementations (e.g., `fibbonnochi_sequence.py`)

## Key Patterns and Conventions

### Testing
- Uses pytest framework
- Tests are in `/lib/testing/lib_test.py`
- Tests capture stdout for validation using `io.StringIO()`
- Run tests using `pytest`

### Implementation Patterns
1. Sequence Operations:
   - Use zero-based indexing
   - Handle edge cases (empty, single element)
   - Follow Python's built-in sequence patterns (list, tuple, range, str)

2. Function Structure:
   ```python
   def function_name(params):
       # Handle edge cases first
       if edge_case:
           return special_value
       
       # Initialize sequence if needed
       sequence = initial_value
       
       # Main logic
       # ...
       
       # Print/return result
       print(result)  # if output required
       return result  # if return value needed
   ```

## Development Environment
- Python 3.8.13 required (specified in Pipfile)
- Uses pipenv for dependency management
- Key dependencies:
  - pytest for testing
  - ipdb for debugging
  - importlib-metadata and importlib-resources for imports

## Common Operations
- List manipulation: indexing, slicing, appending
- Sequence iteration using range()
- Print formatting for sequence output
- Test output capture and validation

When implementing new features:
1. Start with edge case handling
2. Follow existing patterns for sequence manipulation
3. Add corresponding tests in `/lib/testing/lib_test.py`
4. Ensure output matches existing format conventions