#!/usr/bin/env python3
"""Build a 5–7 minute Google Slides–ready deck about Enzo (FRC 1577 / Crescendo).

No match results, rankings, awards, or scoreboard claims.
"""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

# --- Visual system: Steampunk / industrial (not purple, cream-serif, or neon) ---
BG = RGBColor(0x14, 0x16, 0x1A)
PANEL = RGBColor(0x1E, 0x22, 0x28)
BRASS = RGBColor(0xC4, 0x96, 0x4A)
COPPER = RGBColor(0xB8, 0x6B, 0x3D)
CREAM = RGBColor(0xF2, 0xEB, 0xDF)
MUTED = RGBColor(0xA8, 0xA0, 0x93)
LINE = RGBColor(0x3A, 0x34, 0x2C)

W, H = Inches(13.333), Inches(7.5)
SLIDE_W = 12192000  # 13.333" EMUs
SLIDE_H = 6858000


def set_run(run, *, size=18, bold=False, color=CREAM, font="Georgia"):
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    # Force Latin font for Google Slides import friendliness
    rPr = run._r.get_or_add_rPr()
    latin = rPr.find(qn("a:latin"))
    if latin is None:
        latin = rPr.makeelement(qn("a:latin"), {})
        rPr.insert(0, latin)
    latin.set("typeface", font)


def add_bg(slide, color=BG):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    spTree = slide.shapes._spTree
    sp = shape._element
    spTree.remove(sp)
    spTree.insert(2, sp)
    return shape


def add_accent_bar(slide, top=Inches(0)):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, top, W, Inches(0.08))
    bar.fill.solid()
    bar.fill.fore_color.rgb = BRASS
    bar.line.fill.background()


def add_footer(slide, page: int, total: int = 11):
    box = slide.shapes.add_textbox(Inches(0.6), Inches(7.05), Inches(10), Inches(0.3))
    tf = box.text_frame
    tf.clear()
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = f"ENZO  ·  FRC Crescendo  ·  Team 1577 Steampunk  ·  {page}/{total}"
    set_run(run, size=11, color=MUTED, font="Calibri")


def add_title_block(slide, kicker: str, title: str, subtitle: str | None = None):
    k = slide.shapes.add_textbox(Inches(0.7), Inches(0.45), Inches(12), Inches(0.4))
    tf = k.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = kicker.upper()
    set_run(run, size=13, bold=True, color=BRASS, font="Calibri")

    t = slide.shapes.add_textbox(Inches(0.7), Inches(0.85), Inches(12), Inches(1.1))
    tf = t.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = title
    set_run(run, size=36, bold=True, color=CREAM, font="Georgia")

    if subtitle:
        s = slide.shapes.add_textbox(Inches(0.7), Inches(1.9), Inches(11.5), Inches(0.6))
        tf = s.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        run = p.add_run()
        run.text = subtitle
        set_run(run, size=16, color=MUTED, font="Calibri")


def add_bullets(slide, items: list[str], left=0.8, top=2.5, width=11.5, height=3.8, size=20):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.level = 0
        p.space_after = Pt(12)
        run = p.add_run()
        run.text = item
        set_run(run, size=size, color=CREAM, font="Calibri")
    return box


def add_card(slide, left, top, width, height, heading: str, body: str):
    card = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height)
    )
    card.fill.solid()
    card.fill.fore_color.rgb = PANEL
    card.line.color.rgb = LINE
    card.line.width = Pt(1)
    card.adjustments[0] = 0.08

    h = slide.shapes.add_textbox(
        Inches(left + 0.25), Inches(top + 0.25), Inches(width - 0.5), Inches(0.5)
    )
    tf = h.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = heading
    set_run(run, size=18, bold=True, color=BRASS, font="Georgia")

    b = slide.shapes.add_textbox(
        Inches(left + 0.25), Inches(top + 0.85), Inches(width - 0.5), Inches(height - 1.15)
    )
    tf = b.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = body
    set_run(run, size=14, color=CREAM, font="Calibri")


def set_notes(slide, text: str):
    notes = slide.notes_slide.notes_text_frame
    notes.clear()
    p = notes.paragraphs[0]
    run = p.add_run()
    run.text = text


def build() -> Path:
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]

    # 1. Title
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    brand = s.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.5), Inches(1.2))
    tf = brand.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "ENZO"
    set_run(run, size=72, bold=True, color=BRASS, font="Georgia")
    p.alignment = PP_ALIGN.LEFT

    sub = s.shapes.add_textbox(Inches(0.8), Inches(3.1), Inches(11.5), Inches(1.2))
    tf = sub.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "Why Enzo is the best robot of FRC Crescendo"
    set_run(run, size=28, color=CREAM, font="Georgia")

    meta = s.shapes.add_textbox(Inches(0.8), Inches(4.5), Inches(11.5), Inches(0.8))
    tf = meta.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "Team 1577 Steampunk  ·  A design-first argument  ·  5–7 minutes"
    set_run(run, size=16, color=MUTED, font="Calibri")
    add_footer(s, 1)
    set_notes(
        s,
        "TIMING ~40s\n"
        "Open with the brand: Enzo. Say this talk is not about scoreboards — it is about "
        "why Enzo’s design best answers Crescendo’s engineering problem. Mention Team 1577 "
        "Steampunk (Raanana, Israel). Note: Crescendo was the FRC game for the 2024 season; "
        "we will not discuss match outcomes.",
    )

    # 2. Meet Enzo
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    add_title_block(
        s,
        "Meet the robot",
        "Enzo, built by Steampunk",
        "FRC Team 1577 — Aviv High School, Raanana — for the Crescendo game challenge.",
    )
    add_card(
        s,
        0.7,
        2.7,
        3.8,
        3.4,
        "Who",
        "Enzo is Steampunk’s Crescendo competition robot — named, iterated, and prepared as a complete field machine, not a collection of demos.",
    )
    add_card(
        s,
        4.75,
        2.7,
        3.8,
        3.4,
        "What game",
        "Crescendo asks robots to collect foam Notes, score into the Speaker and Amp, and finish on Stage — under defense and time pressure.",
    )
    add_card(
        s,
        8.8,
        2.7,
        3.8,
        3.4,
        "Our lens today",
        "We judge Enzo by design quality: clarity of strategy, mechanism fit, adaptability, and alliance value — never by match tallies.",
    )
    add_footer(s, 2)
    set_notes(
        s,
        "TIMING ~35s\n"
        "Introduce Enzo and Steampunk briefly. Frame Crescendo in one sentence. Explicitly "
        "set the evaluation lens: design excellence, not results.",
    )

    # 3. Game demands
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    add_title_block(
        s,
        "The problem space",
        "What Crescendo demanded",
        "A “best” robot is the one whose architecture fits the game’s constraints cleanly.",
    )
    add_bullets(
        s,
        [
            "Ground and Source acquisition of Notes with high forgiveness under contact",
            "Fast, accurate Speaker cycles while still creating Amp leverage for the alliance",
            "Endgame Stage presence — climb readiness without destroying the scoring machine",
            "Mobility that survives defense: translation, rotation, and recovery under load",
            "Software that turns mechanisms into consistent driver workflows",
        ],
        top=2.6,
        size=18,
    )
    add_footer(s, 3)
    set_notes(
        s,
        "TIMING ~45s\n"
        "Walk the five demands. Emphasize that Crescendo punished one-trick robots: Speaker "
        "alone, Amp alone, or climb-only rarely defined excellence. Enzo’s case starts here.",
    )

    # 4. Criteria for best
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    add_title_block(
        s,
        "Definition",
        "How we define “best”",
        "If we ban the scoreboard, we need a sharper scorecard.",
    )
    criteria = [
        ("Strategy clarity", "Every major subsystem serves a coherent game plan."),
        ("Cycle quality", "Intake → control → score is short, stable, and repeatable."),
        ("Role flexibility", "Useful as scorer, cleaner, or endgame partner."),
        ("Iteration courage", "The team redesigns when the field teaches a better truth."),
        ("Driver trust", "The robot makes hard things feel ordinary at the controls."),
    ]
    for i, (h, b) in enumerate(criteria):
        y = 2.45 + i * 0.75
        label = s.shapes.add_textbox(Inches(0.8), Inches(y), Inches(3.2), Inches(0.55))
        tf = label.text_frame
        p = tf.paragraphs[0]
        run = p.add_run()
        run.text = h
        set_run(run, size=18, bold=True, color=BRASS, font="Georgia")
        body = s.shapes.add_textbox(Inches(4.1), Inches(y), Inches(8.3), Inches(0.55))
        tf = body.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        run = p.add_run()
        run.text = b
        set_run(run, size=16, color=CREAM, font="Calibri")
    add_footer(s, 4)
    set_notes(
        s,
        "TIMING ~40s\n"
        "Read the five criteria as the rubric for the rest of the talk. Preview that Enzo "
        "earns each one.",
    )

    # 5. Iteration
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    add_title_block(
        s,
        "Design culture",
        "Enzo was rebuilt when it had to be",
        "After early district play, Steampunk chose substantial redesign before championship stretch — a hallmark of elite engineering culture.",
    )
    add_bullets(
        s,
        [
            "Best robots are not frozen at bag day — they are updated when reality disagrees with CAD",
            "A mid-season rebuild signals ruthless prioritization: keep what works, cut what fights the game",
            "Enzo’s identity is improvement under pressure — the machine evolves toward the field’s true meta",
            "That discipline is rarer than clever mechanisms, and more decisive than either alone",
        ],
        top=2.85,
        size=18,
    )
    add_footer(s, 5)
    set_notes(
        s,
        "TIMING ~40s\n"
        "Reference the public rebuild narrative (Chief Delphi reveal titled Enzo 2024 Ready "
        "for World Championship) without mentioning outcomes. Argue that willingness to "
        "rebuild is itself a reason Enzo is “best.”",
    )

    # 6. Note control
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    add_title_block(
        s,
        "Subsystem thesis",
        "Notes first: possession is power",
        "In Crescendo, the robot that owns Notes controls tempo.",
    )
    add_card(
        s,
        0.7,
        2.7,
        5.9,
        3.5,
        "Acquisition philosophy",
        "A best-in-class Crescendo bot treats intake as a reliability problem: wide capture, quick centering, and handoff that never asks the driver for perfect alignment.",
    )
    add_card(
        s,
        6.9,
        2.7,
        5.7,
        3.5,
        "Why Enzo wins here",
        "Enzo’s architecture is organized around uninterrupted Note flow — ground cleanup and Source cycles feed the same scoring path, so every possession becomes an alliance asset.",
    )
    add_footer(s, 6)
    set_notes(
        s,
        "TIMING ~35s\n"
        "Keep claims qualitative. Stress that Enzo’s value starts with possession quality, "
        "not flashy scoring animations.",
    )

    # 7. Scoring versatility
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    add_title_block(
        s,
        "Scoring architecture",
        "Speaker threat + Amp utility",
        "Crescendo rewarded robots that could pressure both scoring modes without becoming two half-finished machines.",
    )
    add_bullets(
        s,
        [
            "Speaker capability creates continuous cycle pressure across the field",
            "Amp capability turns alliance coordination into leverage, not a side quest",
            "A unified scoring package lets drivers choose the right action for congestion",
            "Enzo’s “best” claim is versatility under chaos — not a single highlight reel shot",
        ],
        top=2.7,
        size=18,
    )
    add_footer(s, 7)
    set_notes(
        s,
        "TIMING ~40s\n"
        "Argue dual-mode scoring without citing points or match clips as proof of ranking. "
        "Focus on decision freedom for drivers and alliance partners.",
    )

    # 8. Endgame
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    add_title_block(
        s,
        "Endgame",
        "Stage-ready without compromise",
        "Climbing only matters if the robot can still score for 2:15 first.",
    )
    add_card(
        s,
        0.7,
        2.7,
        5.9,
        3.5,
        "The trap many robots fall into",
        "Designs that chase every endgame flourish often weaken teleop throughput. Best Crescendo robots protect cycle identity first, then add Stage presence that does not sabotage it.",
    )
    add_card(
        s,
        6.9,
        2.7,
        5.7,
        3.5,
        "Enzo’s balance",
        "Enzo is built as a full-match robot: scoring integrity through teleop, then a credible Stage finish. That balance is why alliances trust the machine in high-stakes minutes.",
    )
    add_footer(s, 8)
    set_notes(
        s,
        "TIMING ~35s\n"
        "Avoid trap-score debates that imply outcomes. Emphasize design balance: teleop "
        "identity preserved, endgame still real.",
    )

    # 9. Software / drivers
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    add_title_block(
        s,
        "Human–machine loop",
        "Software makes Enzo feel inevitable",
        "Hardware sets the ceiling. Controls decide whether drivers actually reach it.",
    )
    add_bullets(
        s,
        [
            "State-aware scoring workflows reduce button chaos in the final 30 seconds",
            "Vision and pose awareness turn “almost lined up” into “ready to release”",
            "Autonomous routines that respect real sensor feedback teach the teleop machine honesty",
            "When drivers trust the robot, strategy expands — that is competitive excellence",
        ],
        top=2.7,
        size=18,
    )
    add_footer(s, 9)
    set_notes(
        s,
        "TIMING ~40s\n"
        "Keep this accessible for a general audience. Software is the multiplier that makes "
        "Enzo’s mechanisms feel like the best robot, not merely a capable one.",
    )

    # 10. Synthesis
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    add_title_block(
        s,
        "The argument",
        "Why Enzo is the best",
        "Five reasons — all design, no scoreboard.",
    )
    reasons = [
        ("1", "It answers Crescendo’s real problem: Notes, dual scoring modes, and Stage."),
        ("2", "It was rebuilt with courage when the field demanded a better machine."),
        ("3", "It prioritizes possession quality — the root of every Crescendo strategy."),
        ("4", "It stays versatile: Speaker pressure and Amp utility in one package."),
        ("5", "It closes the loop with software drivers can trust under defense."),
    ]
    for i, (n, text) in enumerate(reasons):
        y = 2.45 + i * 0.72
        num = s.shapes.add_shape(
            MSO_SHAPE.OVAL, Inches(0.75), Inches(y), Inches(0.48), Inches(0.48)
        )
        num.fill.solid()
        num.fill.fore_color.rgb = BRASS
        num.line.fill.background()
        nbox = s.shapes.add_textbox(Inches(0.75), Inches(y + 0.05), Inches(0.48), Inches(0.4))
        tf = nbox.text_frame
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run = p.add_run()
        run.text = n
        set_run(run, size=14, bold=True, color=BG, font="Calibri")
        tbox = s.shapes.add_textbox(Inches(1.5), Inches(y + 0.05), Inches(10.8), Inches(0.5))
        tf = tbox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        run = p.add_run()
        run.text = text
        set_run(run, size=17, color=CREAM, font="Calibri")
    add_footer(s, 10)
    set_notes(
        s,
        "TIMING ~50s\n"
        "This is the thesis slide. Deliver the five reasons with pause and emphasis. "
        "Do not slip into results language.",
    )

    # 11. Close
    s = prs.slides.add_slide(blank)
    add_bg(s)
    add_accent_bar(s)
    close = s.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(11.5), Inches(1.2))
    tf = close.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "Enzo is best because it was designed to be."
    set_run(run, size=34, bold=True, color=CREAM, font="Georgia")

    sub = s.shapes.add_textbox(Inches(0.8), Inches(3.6), Inches(11.5), Inches(1.2))
    tf = sub.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = (
        "Not because of a bracket. Because Steampunk built a Crescendo robot with "
        "clear strategy, fearless iteration, and mechanisms that serve drivers — and alliances."
    )
    set_run(run, size=18, color=MUTED, font="Calibri")

    q = s.shapes.add_textbox(Inches(0.8), Inches(5.3), Inches(11.5), Inches(0.5))
    tf = q.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "Questions"
    set_run(run, size=20, bold=True, color=BRASS, font="Georgia")
    add_footer(s, 11)
    set_notes(
        s,
        "TIMING ~30s + Q&A\n"
        "Close on the line. Invite questions about design choices, rebuild culture, or "
        "Crescendo strategy — still no results talk unless someone asks; if they do, redirect "
        "to design.",
    )

    out = Path(__file__).resolve().parent / "Enzo_Crescendo_Presentation.pptx"
    prs.save(out)
    return out


if __name__ == "__main__":
    path = build()
    print(f"Wrote {path}")
