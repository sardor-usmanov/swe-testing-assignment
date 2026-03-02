# TESTING.md — Quick-Calc Testing Strategy

## 1) Testing Strategy Overview
This project uses a multi-layered strategy:
- **Unit tests** validate the calculator logic in isolation (fast and deterministic).
- **Integration tests** validate the interaction between the application layer (`QuickCalcApp`) and the calculator logic.

### What we tested
- Core operations: add, subtract, multiply, divide
- Edge cases (e.g., division by zero, decimals, large numbers)
- App-layer behavior: full calculation flow and clear/reset behavior

### What we did not test (and why)
- **UI/visual testing**: The application is CLI-based and UI is not a grading focus.
- **Non-functional testing** (performance, load, security): Out of scope for this small local tool.
- **End-to-end (E2E)** with real user devices: The CLI is minimal; unit + integration give sufficient confidence for the assignment.

## 2) Lecture 3 Concepts Applied

### Testing Pyramid
The test suite follows the testing pyramid:
- **Many unit tests** (majority) cover calculation correctness and edge cases.
- **A small number of integration tests** verify that layers work together.
This keeps feedback fast while still validating the application flow.

### Black-box vs White-box Testing
- **Unit tests** are closer to **white-box** testing because they call specific methods with knowledge of the internal API.
- **Integration tests** are closer to **black-box** testing because they validate behavior through the app interface (`compute`, `clear`) without focusing on internal implementation details.

### Functional vs Non-Functional Testing
- The tests focus on **functional correctness** (correct results, correct error handling, correct reset behavior).
- **Non-functional tests** (performance, usability, security) were intentionally excluded as not required for this scope.

### Regression Testing
This suite can be used as regression protection in future updates. If a change breaks an existing operation or behavior, tests will fail and prevent accidental regressions.

## 3) Test Results Summary
| Test Name | Type | Status |
|---|---|---|
| test_addition | Unit | Pass |
| test_subtraction | Unit | Pass |
| test_multiplication | Unit | Pass |
| test_division | Unit | Pass |
| test_division_by_zero_raises | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_very_large_numbers | Unit | Pass |
| test_full_user_interaction_addition | Integration | Pass |
| test_clear_resets_display_to_zero | Integration | Pass |