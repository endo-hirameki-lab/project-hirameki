from pathlib import Path


def load_prompt(prompt_name):
    """
    Load prompt file from prompts directory.
    """

    project_root = Path(__file__).resolve().parents[2]

    prompt_path = project_root / "prompts" / prompt_name

    if not prompt_path.exists():
        raise FileNotFoundError(
            f"Prompt file not found: {prompt_path}"
        )

    return prompt_path.read_text(
        encoding="utf-8"
    )
