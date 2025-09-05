# Bowling Game — Test Plan

## 1. Scope & Objectives
Validate the backend scoring logic of a ten-pin bowling game. Ensure rules for strikes, spares, open frames, and 10th-frame bonuses are correctly implemented. Verify robustness through input validation and constraints.

## 2. In-Scope Features
- Recording rolls
- Scoring frames 1–9 (strike, spare, open)
- 10th frame handling (strike with bonuses, spare with bonus, open)
- Validation of inputs: pin range, frame totals, preventing extra rolls

## 3. Out of Scope
- GUI
- Database / file input
- Multiplayer turn rotation
- Performance testing

## 4. Test Strategy
- **Unit tests** with Python `unittest`
- Example-based tests (from provided `example_usage.py`)
- Edge-case tests for 10th frame
- Negative tests for validation rules

## 5. Test Environment
- Python 3.10+
- OS: Windows / macOS / Linux
- No external dependencies

## 6. Test Data
- Gutter game: 20×0 → 0
- All ones: 20×1 → 20
- Perfect game: 12×10 → 300
- All spares: 21×5 → 150
- Regular game (no strikes/spares) → 72
- Mixed game (given in `example_usage.py`) → 190
- 10th-frame spare with bonus → 15
- 10th-frame open → 9
- Consecutive strikes (X, X, 4,2) → 46
- Invalid rolls (−1, 11, frame >10) → raise ValueError
- No rolls allowed after complete game → raise ValueError

## 7. Entry / Exit Criteria
- **Entry:** BowlingGame compiles and runs
- **Exit:** All unit tests pass with expected results

## 8. Risks & Mitigations
- Miscounting frames → Dedicated 10-frame tests
- Bonus calculation errors → Explicit tests for spares and strikes
- 10th-frame complexity → Separate directed tests
- Invalid inputs → Negative tests included

## 9. Traceability
- **Strikes**: `test_perfect_game`, `test_consecutive_strikes`
- **Spares**: `test_all_spares`, `test_tenth_frame_spare_bonus`
- **Open frames**: `test_regular_game`, `test_tenth_frame_open`
- **10th frame rules**: `test_tenth_frame_spare_bonus`, `test_tenth_frame_open`
- **Validation rules**: `test_invalid_pin_count_raises`, `test_frame_total_exceeds_ten_raises`, `test_no_rolls_after_game_complete`

## 10. Execution
Run all tests locally:
```bash
python -m unittest -v
