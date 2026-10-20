# Wait or Walk? A Smart Commute Decision Assistant

Built for the 1M1B AI for Sustainability Virtual Internship (with IBM SkillsBuild and AICTE). SDG 11: Sustainable Cities and Communities.

## Problem
Mumbai commuters who rely on a connecting bus to the metro face inconsistent timings, so they can't tell whether to keep waiting or switch (walk or take another route).

## Approach
No public data exists for this bus stop, so this is a transparent rule-based decision-support tool, not a trained ML model. Instead of predicting arrival time, it answers one question: "Should I keep waiting right now?"

| Factor | Points |
|---|---|
| Raining | +2 |
| Weekday rush hour (8-10am or 6-8pm) | +1 |
| Already waited 10+ minutes | +1 |

| Score | Risk | Recommendation |
|---|---|---|
| 0-1 | Low | Wait, you're probably fine |
| 2 | Medium | Wait a bit longer, stay alert |
| 3-4 | High | Consider walking or switching now |

## Run
python commute_assistant.py

## Tools
Python 3. IBM Bob was used to turn the scoring logic into the Python function.

## Limitations (Responsible AI)
- The thresholds are reasoned assumptions, not measured from real bus data.
- It cannot see one-off events such as festivals, accidents or road closures.

## Author
Zohra Sayyed Abed Ali
