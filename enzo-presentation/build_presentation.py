#!/usr/bin/env python3
"""Build the Enzo deck (plain 9th-grade language)."""

from build_presentation_simple import build

if __name__ == "__main__":
    path = build()
    # Keep both filenames in sync for older README links.
    styled = path.with_name("Enzo_Crescendo_Presentation.pptx")
    styled.write_bytes(path.read_bytes())
    print(f"Wrote {path}")
    print(f"Wrote {styled}")
