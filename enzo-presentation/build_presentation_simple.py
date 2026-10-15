#!/usr/bin/env python3
"""Plain-language PPTX for Google Slides / 9th grade."""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt

BG = RGBColor(20, 22, 26)
BRASS = RGBColor(196, 150, 74)
CREAM = RGBColor(242, 235, 223)
MUTED = RGBColor(168, 160, 147)

SLIDE_W = 12192000
SLIDE_H = 6858000


def style(run, size=20, bold=False, color=CREAM):
    run.font.name = "Arial"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color


def fill_bg(slide):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = BG


def add_text(slide, left, top, width, height, text, *, size=20, bold=False, color=CREAM):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    lines = text.split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(8)
        run = p.add_run()
        run.text = line
        style(run, size=size, bold=bold, color=color)


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def build() -> Path:
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]

    slides = [
        {
            "kicker": "TEAM 1577 STEAMPUNK  ·  ROBOT GAME: CRESCENDO",
            "title": "ENZO",
            "body": "Why Enzo is the best robot in Crescendo\nA short talk about how it was built  ·  about 5 to 7 minutes",
            "notes": "Say the robot name clearly. Talk about design, not scores.",
        },
        {
            "kicker": "WHO IS ENZO?",
            "title": "Meet the robot",
            "body": "High school students on Team 1577 (Steampunk) built Enzo in Raanana, Israel.\n\nCrescendo is a robot sports game. Robots pick up foam rings called Notes, score points, and climb at the end.\n\nWe’ll talk about how Enzo was built — not about game scores.",
            "notes": "Keep this short and plain.",
        },
        {
            "kicker": "THE GAME",
            "title": "What robots had to do",
            "body": "• Pick up Notes from the floor fast\n• Shoot Notes into a big goal called the Speaker\n• Also put Notes in a side goal called the Amp\n• Climb a chain near the end of the match\n• Keep driving even when other robots block them",
            "notes": "Explain the game like a new sport.",
        },
        {
            "kicker": "WHAT “BEST” MEANS",
            "title": "Not the flashiest — the smartest",
            "body": "• Has a simple plan for the whole game\n• Picks up and scores Notes without drama\n• Can help its partners in more than one way\n• Gets fixed when something is wrong\n• Is easy for the drivers to use",
            "notes": "These five points guide the rest of the talk.",
        },
        {
            "kicker": "MAKING IT BETTER",
            "title": "They changed Enzo when they had to",
            "body": "In the middle of the season, the team took Enzo apart and built big parts again.\n\nThat’s smart. Good teams don’t stick with a bad first idea. They fix the robot.",
            "notes": "Praise fixing problems. No scores.",
        },
        {
            "kicker": "PICKING UP NOTES",
            "title": "No Notes = no points",
            "body": "Enzo is built to grab Notes quickly and hold onto them.\n\nIn this game, having the Notes is like having the basketball.\n\nEnzo was made to win that fight.",
            "notes": "Basketball comparison helps.",
        },
        {
            "kicker": "SCORING POINTS",
            "title": "Two ways to score",
            "body": "• Shoot into the Speaker\n• Score in the Amp to help its partners\n• Drivers can choose the better option when it’s crowded\n• Doing both jobs is better than only doing one",
            "notes": "Keep it simple: two scoring options.",
        },
        {
            "kicker": "END OF THE MATCH",
            "title": "Climbing without messing up scoring",
            "body": "Some robots focus so much on climbing that they get worse at scoring.\n\nEnzo stays good at scoring during the match, and it can still climb at the end.",
            "notes": "Score during the match, climb at the end.",
        },
        {
            "kicker": "THE ROBOT’S COMPUTER CODE",
            "title": "Good code makes driving easier",
            "body": "• Helps the robot aim better\n• Gives drivers simple controls\n• Uses cameras so the robot can “see” the field\n• When drivers trust the robot, they play better",
            "notes": "Code = the robot’s computer programs.",
        },
        {
            "kicker": "PUTTING IT TOGETHER",
            "title": "Why Enzo is the best",
            "body": "1. Built for the whole game, not just one trick\n2. The team changed it when it needed changes\n3. Great at grabbing and holding Notes\n4. Can score in more than one way\n5. The code helps the drivers a lot",
            "notes": "Slow down on each of the five points.",
        },
        {
            "kicker": "THE END",
            "title": "Enzo is best because of how it was built.",
            "body": "Simple plan. Willing to change. Easy to drive. Ready for the whole game.\n\nQuestions?",
            "notes": "Stop here and take questions.",
        },
    ]

    for i, data in enumerate(slides, 1):
        s = prs.slides.add_slide(blank)
        fill_bg(s)
        add_text(s, 0.7, 0.45, 12, 0.4, data["kicker"], size=13, bold=True, color=BRASS)
        add_text(s, 0.7, 1.0, 12, 1.4, data["title"], size=32, bold=True, color=CREAM)
        add_text(s, 0.7, 2.6, 11.8, 3.8, data["body"], size=20, color=CREAM)
        add_text(
            s,
            0.7,
            6.9,
            12,
            0.35,
            f"ENZO  ·  Crescendo  ·  Team 1577 Steampunk  ·  {i}/11",
            size=11,
            color=MUTED,
        )
        notes(s, data["notes"])

    out = Path(__file__).resolve().parent / "Enzo_Crescendo_GoogleSlides.pptx"
    prs.save(out)
    return out


if __name__ == "__main__":
    print(build())
