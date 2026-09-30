# Practice: Warm-Up (Wednesday) + Full Mock Hackathon (Thursday)

Friday's build is only 3 hours. Teams that have done it once before move twice as fast, because they're not learning the tool, the timing, and each other all at the same time. This file gives you that "once before."

---

## Part 1: 45-minute PartyRock warm-up (each person, Wednesday)

Everyone does this alone, so all three of you can operate the tool if the Builder gets stuck.

| Min | Task | Done when |
|---|---|---|
| 0–5 | Sign in at partyrock.aws (Google, Apple, or Amazon) | You see the home page and your usage allowance |
| 5–15 | App Builder: *"An app where the user pastes a job post and gets the top 5 skills needed, plus 3 interview questions."* | App generates and runs |
| 15–25 | Rename widgets. Rewrite the skills widget with the widget prompt template (section 3 of [../prompts.md](../prompts.md)) and make it output a **table** | Output is a clean table |
| 25–35 | Add a Chatbot widget that references the skills widget with `@`. Ask it "which skill should I learn first?" | Chatbot answers using the table |
| 35–40 | Test: an empty input, a Taglish job post, a random sentence | The app handles all 3 gracefully (fix the rules if not) |
| 40–45 | Change the model on one widget and compare. Share the app and open the link on your phone | You know how to switch models and share |

Post your app links in your group chat. Compare: whose prompts gave the best output? Steal each other's best tricks.

---

## Part 2: Full mock hackathon (team, Thursday, ~4 hours)

**Run it on the REPH laptops if you already have them** (released Oct 1), so you learn their quirks.

### Setup (10 min before)
- One timer on a phone, visible to everyone.
- The slide template made in advance (7 slides: Title · Problem · User · Solution/Demo · Impact · How it scales on AWS · Team/Ask).
- Pick **one** of the three mock challenges below by drawing lots. Don't pre-read the others; you want the surprise.

### Schedule (mirrors Friday exactly)

| Mock time | Friday equivalent | Do |
|---|---|---|
| 0:00–0:20 | 12:30–12:50 | Adapt a shell from [../idea-bank.md](../idea-bank.md), score with the rubric, write the one-liner |
| 0:20–1:00 | 12:50–1:30 | First working version |
| 1:00–2:00 | 1:30–2:30 | Improve + test + slides |
| 2:00–2:15 | 2:30–2:45 | Scope check, then **feature freeze** at 2:15 |
| 2:15–3:00 | 2:45–3:30 | Fix, record backup video, rehearse once |
| 3:00–3:30 | 3:30–4:00 | Rehearse with a timer, practice Q&A |
| 3:30–3:45 | 4:00+ | **Present for 15 minutes** to a friend, family member, or record yourselves |
| 3:45–4:15 | — | Score yourselves + debrief (below) |

### Mock challenge A: "Future-ready graduates"
> *Many Filipino graduates struggle to find jobs that match their degrees, while companies report skills gaps. Using AI, design a solution that helps bridge the gap between what graduates know and what employers need.*

### Mock challenge B: "Trusted information"
> *Professionals in research, health, and law rely on accurate information, but the volume is overwhelming and misinformation spreads quickly. Build an AI solution that helps a specific group find, understand, or verify trustworthy information faster.*

### Mock challenge C: "AI at work"
> *AI is changing everyday work. Propose an AI-powered tool that makes a specific job or workplace process more productive, fair, or humane, and show how employees would actually use it.*

---

## Scoring sheet (use the real weights)

Score each line 1–10. Be harsh; the real judges will be.

| Criterion | Weight | Questions to ask yourselves | Score /10 | Weighted |
|---|---|---|---|---|
| Innovation & Creativity | 30% | Would a judge have seen this 5 times today? What's our twist? | | ×3 = |
| Impact on the Problem Statement | 30% | Did we quote the challenge? Named user? A number? | | ×3 = |
| Usability & Feasibility | 20% | Did the demo work first try? Could a stranger use it without help? Did we explain how it scales on AWS? | | ×2 = |
| Presentation & Demo | 20% | Under time? Confident? Did the "wow" land? Did all 3 speak? | | ×2 = |
| **Total** | | | | **/100** |

**Target:** 75+ on Thursday means you're ready. Under 60 means focus the debrief on the lowest line.

---

## Debrief (30 min, write the answers down)

1. Where did we lose the most time? What's the rule to prevent it Friday?
2. Which prompt trick gave the biggest quality jump? Save it in your notes.
3. What did the audience not understand in the pitch?
4. Which Q&A question stumped us? Write a better answer now.
5. Who does what on Friday? Confirm roles (see the [section README](../README.md)).

Then check your script length:

```bash
python3 tools/pitch-timer.py --file our-pitch.txt --target-minutes 9
```

---

## Mini drills (if you have 15 spare minutes)

- **Prompt golf:** One person writes a bad widget prompt. Others fix it in under 3 minutes so the output is a clean table.
- **Crash drill:** Mid-rehearsal, someone says "Wi-Fi's down!" Switch to the backup video without stopping the story.
- **Hard question round:** Each person asks the others one tough judge question from [../templates/pitch-15min.md](../templates/pitch-15min.md). Answers must be 2 sentences max.
