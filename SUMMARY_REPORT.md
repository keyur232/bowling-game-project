# Summary Report — Bowling Game Project

## Overview
The project tested and fixed the backend scoring logic for a ten-pin bowling game. 
Goals: ensure correct scoring rules (strikes, spares, open frames, 10th frame), 
write unit tests, refactor code, and document results.

## Approach
- Designed a test plan (see TEST_PLAN.md).
- Built 12 unit tests with `unittest`.
- Debugged scoring logic and applied fixes.
- Used Git for version control.
- Generated PythonDoc HTML from docstrings.

## Findings
- **Bugs found:** only 9 frames scored, open frames only added one roll, 10th frame not handled.
- **Fixes implemented:** corrected scoring loop, added 10th-frame handling, fixed open frame, added validation.
- **Validation added:** pins range 0–10, frame totals ≤ 10, no rolls after complete.

## Refactoring
- Removed unused `current_roll`.
- Added docstrings to all functions.
- Cleaner frame/bonus helper methods.
- Input validation prevents invalid state.

## Test Results
- 12 tests written and passed.
- Screenshot attached of test run (`python -m unittest -v`).

## Git
- Repository link: [INSERT YOUR REPO LINK HERE]
- Commits show step-by-step fixes, tests, and documentation.

## Recommendations
- Add GUI and multiplayer turn handling later.
- Use CI (GitHub Actions) to run tests on every push.
- Add more property-based tests for random games.
