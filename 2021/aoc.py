from pathlib import Path


def read_input(f: str) -> str:
    text_file = Path(f).with_suffix(".txt")
    return text_file.read_text()
