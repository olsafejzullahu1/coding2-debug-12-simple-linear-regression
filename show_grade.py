"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "7635dc5a7268b1ed7fad1ff31cef67c8"
GRADE_HASH = "8300a79ac24eeb89b677460e4547c16775b72109946a2fdfff3697ab51ed6009"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
