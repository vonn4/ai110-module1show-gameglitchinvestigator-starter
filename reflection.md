## 1. What was broken when you started?

When I first ran the game, it looked functional but several parts of the logic were broken. The biggest issue was that the high and low hints were reversed, which made it difficult to play correctly. I also found that clicking the New Game button did not fully reset the game state. Finally, changing the difficulty changed the displayed range but did not generate a new secret number.

### Bug Reproduction Log

| Input Used                     | Expected Behavior                  | Actual Behavior                       | Console Output / Error |
| ------------------------------ | ---------------------------------- | ------------------------------------- | ---------------------- |
| Guess of 4 when secret was 60  | Game should say guess is too low   | Game gave the wrong hint direction    | none                   |
| Guess of 99 when secret was 51 | Game should say guess is too high  | Game gave the wrong hint direction    | none                   |
| Click New Game after winning   | Game should fully reset            | Game remained stuck in win/loss state | none                   |
| Change difficulty to Easy      | New secret should be in Easy range | Old secret number remained active     | none                   |

---

## 2. How did you use AI as a teammate?

I used Claude and GitHub Copilot while working on this project. Claude helped me understand the project requirements and identify possible causes of bugs. Copilot helped explain sections of the code and suggested fixes for the session state issues.

One correct AI suggestion was to reset the secret number whenever the difficulty changes. I verified this by testing the game after switching between difficulty levels.

One misleading AI suggestion was to focus only on changing the hint text rather than fixing the comparison logic itself. After testing, I realized that changing the text alone would not fix the root cause of the bug.

---

## 3. Debugging and testing your fixes

I considered a bug fixed only after I could reproduce it before the change and verify it worked afterward. I manually tested the hint logic by making guesses above and below the secret number. I also used pytest to verify that the game logic returned the expected outcomes for winning, high, and low guesses. AI helped suggest some test cases, but I still reviewed the results myself.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the script whenever the user interacts with the page. Because of this, important values need to be stored in session state so they are not lost between reruns. Session state acts like memory for the application. Without it, the game would not be able to keep track of things like the secret number, score, or attempts.

---

## 5. Looking ahead: your developer habits

One habit I want to continue using is documenting bugs before trying to fix them. Having a clear list of bugs made it easier to verify my changes later. Next time I work with AI, I will ask more targeted questions instead of accepting larger suggestions immediately. This project showed me that AI can be a useful tool, but it still requires testing and human verification before code should be trusted.
## 1. What was broken when you started?

When I first ran the game, it looked functional but several parts of the logic were broken. The biggest issue was that the high and low hints were reversed, which made it difficult to play correctly. I also found that clicking the New Game button did not fully reset the game state. Finally, changing the difficulty changed the displayed range but did not generate a new secret number.

### Bug Reproduction Log

| Input Used                     | Expected Behavior                  | Actual Behavior                       | Console Output / Error |
| ------------------------------ | ---------------------------------- | ------------------------------------- | ---------------------- |
| Guess of 4 when secret was 60  | Game should say guess is too low   | Game gave the wrong hint direction    | none                   |
| Guess of 99 when secret was 51 | Game should say guess is too high  | Game gave the wrong hint direction    | none                   |
| Click New Game after winning   | Game should fully reset            | Game remained stuck in win/loss state | none                   |
| Change difficulty to Easy      | New secret should be in Easy range | Old secret number remained active     | none                   |

---

## 2. How did you use AI as a teammate?

I used Claude and GitHub Copilot while working on this project. Claude helped me understand the project requirements and identify possible causes of bugs. Copilot helped explain sections of the code and suggested fixes for the session state issues.

One correct AI suggestion was to reset the secret number whenever the difficulty changes. I verified this by testing the game after switching between difficulty levels.

One misleading AI suggestion was to focus only on changing the hint text rather than fixing the comparison logic itself. After testing, I realized that changing the text alone would not fix the root cause of the bug.

---

## 3. Debugging and testing your fixes

I considered a bug fixed only after I could reproduce it before the change and verify it worked afterward. I manually tested the hint logic by making guesses above and below the secret number. I also used pytest to verify that the game logic returned the expected outcomes for winning, high, and low guesses. AI helped suggest some test cases, but I still reviewed the results myself.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the script whenever the user interacts with the page. Because of this, important values need to be stored in session state so they are not lost between reruns. Session state acts like memory for the application. Without it, the game would not be able to keep track of things like the secret number, score, or attempts.

---

## 5. Looking ahead: your developer habits

One habit I want to continue using is documenting bugs before trying to fix them. Having a clear list of bugs made it easier to verify my changes later. Next time I work with AI, I will ask more targeted questions instead of accepting larger suggestions immediately. This project showed me that AI can be a useful tool, but it still requires testing and human verification before code should be trusted.
