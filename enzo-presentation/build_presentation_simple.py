#!/usr/bin/env python3
"""Simpler PPTX tuned for Google Slides mobile conversion."""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
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
    return box


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def build() -> Path:
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]

    slides = [
        {
            "kicker": "TEAM 1577 STEAMPUNK  ·  FRC CRESCENDO",
            "title": "ENZO",
            "body": "Why Enzo is the best robot of FRC Crescendo\nA design-first argument  ·  5–7 minutes",
            "notes": "Open with the brand. No scoreboards — design only.",
        },
        {
            "kicker": "MEET THE ROBOT",
            "title": "Enzo, built by Steampunk",
            "body": "FRC Team 1577 — Aviv High School, Raanana.\n\nCrescendo asks robots to collect Notes, score Speaker and Amp, and finish on Stage.\n\nToday we judge Enzo by design quality — never by match tallies.",
            "notes": "Introduce Enzo and set the evaluation lens.",
        },
        {
            "kicker": "THE PROBLEM SPACE",
            "title": "What Crescendo demanded",
            "body": "• Forgiving Note acquisition under contact\n• Fast Speaker cycles plus Amp utility for the alliance\n• Stage presence without wrecking teleop scoring\n• Mobility that survives defense\n• Software drivers can trust",
            "notes": "Walk the five demands. One-trick robots were not enough.",
        },
        {
            "kicker": "DEFINITION",
            "title": "How we define “best”",
            "body": "Strategy clarity — every subsystem serves one game plan\nCycle quality — intake → control → score is short and stable\nRole flexibility — scorer, cleaner, or endgame partner\nIteration courage — redesign when the field teaches better\nDriver trust — hard things feel ordinary at the controls",
            "notes": "This rubric is the rest of the talk.",
        },
        {
            "kicker": "DESIGN CULTURE",
            "title": "Enzo was rebuilt when it had to be",
            "body": "After early district play, Steampunk chose a substantial redesign.\n\nBest robots are not frozen at first CAD.\nThey update when reality disagrees with the design.\n\nThat discipline is rarer than clever mechanisms — and more decisive.",
            "notes": "Reference the public Enzo rebuild story without outcomes.",
        },
        {
            "kicker": "SUBSYSTEM THESIS",
            "title": "Notes first: possession is power",
            "body": "In Crescendo, the robot that owns Notes controls tempo.\n\nA best-in-class bot treats intake as reliability: wide capture, quick centering, clean handoff.\n\nEnzo’s architecture is organized around uninterrupted Note flow — every possession becomes an alliance asset.",
            "notes": "Keep claims qualitative. Possession quality first.",
        },
        {
            "kicker": "SCORING ARCHITECTURE",
            "title": "Speaker threat + Amp utility",
            "body": "• Speaker capability creates continuous cycle pressure\n• Amp capability turns alliance coordination into leverage\n• A unified package lets drivers choose under congestion\n• Enzo’s claim is versatility in chaos — not one highlight shot",
            "notes": "Dual-mode scoring = decision freedom.",
        },
        {
            "kicker": "ENDGAME",
            "title": "Stage-ready without compromise",
            "body": "Climbing only matters if the robot can still score for most of the match.\n\nDesigns that chase every endgame flourish often weaken teleop throughput.\n\nEnzo protects cycle identity first, then adds credible Stage presence alliances can trust.",
            "notes": "Balance teleop identity with real endgame.",
        },
        {
            "kicker": "HUMAN–MACHINE LOOP",
            "title": "Software makes Enzo feel inevitable",
            "body": "Hardware sets the ceiling. Controls decide whether drivers reach it.\n\n• State-aware scoring workflows cut button chaos\n• Vision turns “almost lined up” into “ready to release”\n• Honest autonomous feedback makes teleop trustworthy\n• When drivers trust the robot, strategy expands",
            "notes": "Software is the multiplier.",
        },
        {
            "kicker": "THE ARGUMENT",
            "title": "Why Enzo is the best",
            "body": "1. It answers Crescendo’s real problem: Notes, dual scoring, Stage\n2. It was rebuilt with courage when the field demanded better\n3. It prioritizes possession quality\n4. It stays versatile: Speaker pressure and Amp utility\n5. It closes the loop with software drivers can trust\n\nFive reasons — all design, no scoreboard.",
            "notes": "Thesis slide. Pause between the five reasons.",
        },
        {
            "kicker": "CLOSE",
            "title": "Enzo is best because it was designed to be.",
            "body": "Not because of a bracket.\nBecause Steampunk built clear strategy, fearless iteration, and a machine drivers — and alliances — can trust.\n\nQuestions?",
            "notes": "Close and invite design questions only.",
        },
    ]

    for i, data in enumerate(slides, 1):
        s = prs.slides.add_slide(blank)
        fill_bg(s)
        add_text(s, 0.7, 0.45, 12, 0.4, data["kicker"], size=13, bold=True, color=BRASS)
        add_text(s, 0.7, 1.0, 12, 1.4, data["title"], size=34, bold=True, color=CREAM)
        add_text(s, 0.7, 2.6, 11.8, 3.8, data["body"], size=18, color=CREAM)
        add_text(
            s,
            0.7,
            6.9,
            12,
            0.35,
            f"ENZO  ·  FRC Crescendo  ·  Team 1577 Steampunk  ·  {i}/11",
            size=11,
            color=MUTED,
        )
        notes(s, data["notes"])

    out = Path(__file__).resolve().parent / "Enzo_Crescendo_GoogleSlides.pptx"
    prs.save(out)
    return out


if __name__ == "__main__":
    print(build())
