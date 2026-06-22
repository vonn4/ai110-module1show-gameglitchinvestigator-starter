def get_range_for_difficulty(difficulty: str):
    """Return the inclusive number range for the selected difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """Parse user input into an integer guess."""
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """Compare a guess to the secret number."""
    # FIX: After reviewing AI suggestions and manual testing,
    # corrected the high/low comparison logic so hints match the guess.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update the score based on the guess result."""
    if outcome == "Win":
        points = max(10, 100 - 10 * attempt_number)
        return current_score + points

    return current_score