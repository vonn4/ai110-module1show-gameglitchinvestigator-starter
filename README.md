# 🎮 Game Glitch Investigator: The Impossible Guesser

## Project Overview

This project is a number guessing game built with Streamlit. The goal was to investigate bugs in AI-generated code, fix the problems, and verify the fixes using testing. I used AI tools to help understand the code, but I reviewed and tested all changes myself.

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
5. Added pytest tests to verify game behavior.

## Demo Walkthrough

1. Start the Streamlit application.
2. Choose a difficulty level.
3. Enter a guess that is below the secret number and receive a "Go HIGHER!" hint.
4. Enter a guess that is above the secret number and receive a "Go LOWER!" hint.
5. Enter the correct number and win the game.
6. Click New Game and verify the game resets correctly.

## Test Results

```text
Paste your pytest output here after running pytest.
```

## AI Collaboration

I used Claude and GitHub Copilot during this project. AI helped explain the code, identify possible bugs, and suggest fixes. I verified each suggestion through testing and gameplay before accepting it.
