# 🎮 Game Glitch Investigator: The Impossible Guesser

## Project Overview

This project is a number guessing game built with Streamlit. The goal was to investigate bugs in AI-generated code, fix the problems, and verify the fixes using testing. I used AI tools to help understand the code, identify bugs, and suggest fixes, but I reviewed and tested all changes myself before accepting them.

## Bugs Found

1. The high and low hints were reversed.
2. The New Game button did not fully reset the game.
3. Changing the difficulty changed the displayed range but not the secret number.
4. The game sometimes converted the secret number to a string, causing inconsistent behavior.

## Fixes Applied

1. Moved game logic into `logic_utils.py`.
2. Fixed the high/low comparison logic.
3. Fixed the New Game button so it resets all game state.
4. Reset the secret number when the difficulty changes.
5. Updated difficulty ranges and attempt limits to better match the selected difficulty.
6. Added pytest tests to verify game behavior.

## Demo Walkthrough

1. Start the Streamlit application.
2. Choose a difficulty level.
3. Enter a guess that is below the secret number and receive a "Go HIGHER!" hint.
4. Enter a guess that is above the secret number and receive a "Go LOWER!" hint.
5. Enter the correct number and win the game.
6. Click New Game and verify the game resets correctly.
7. Change the difficulty and verify a new secret number is generated within the correct range.

## Test Results

```text
pytest
========================================================================================================================== test session starts ==========================================================================================================================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
collected 8 items

tests\test_game_logic.py ........ [100%]

=========================================================================================================================== 8 passed in 0.20s ===========================================================================================================================
```

## AI Collaboration

I used Claude and GitHub Copilot during this project. Claude helped me understand the project requirements and reason through the bugs I observed while testing the game. GitHub Copilot helped explain portions of the code and suggested fixes related to Streamlit session state and game logic.

One correct AI suggestion was resetting the secret number whenever the difficulty changes. I verified this by manually testing each difficulty level and confirming that a new secret number was generated within the correct range.

One misleading AI suggestion was to focus only on changing the displayed hint text instead of fixing the comparison logic itself. After testing, I realized that changing the text alone would not solve the root cause of the bug, so I corrected the comparison logic and verified the behavior through gameplay and automated tests.
