import re
import unicodedata

def clean_text(raw_text):
    text = raw_text.replace("\\n", "\n")

    text = re.sub(r"\n\s*\n+", "\n", text)

    # Remove bullet points (●, ○ and similar)
    text = re.sub(r"[●○•]", "", text)

    # Normalize and remove any unicode special characters (non-ASCII)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")

    # Strip leading/trailing whitespace and extra spaces within lines
    text = "\n".join(line.strip() for line in text.strip().splitlines())

    return text