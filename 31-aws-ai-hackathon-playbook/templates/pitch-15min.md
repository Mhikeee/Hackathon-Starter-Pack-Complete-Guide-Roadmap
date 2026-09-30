# 15-Minute Pitch Template (3 speakers, live AWS demo)

You get **15 minutes per team**. The letter doesn't say whether Q&A is inside those 15 minutes, so plan **~11 minutes of pitch + demo** and leave ~4 minutes for questions. If they give you extra time, spend it on Q&A, where confident teams gain the most.

Speakers: **P** = Pitch lead · **R** = Product/Research lead · **B** = Builder

---

## Structure

| # | Time | Slide title (make it a claim) | Who | Say | Scores |
|---|---|---|---|---|---|
| 1 | 0:00–1:00 | **Hook**: a real moment | P | A specific person and a specific moment. *"Last month, Mika, a BS Psych graduate from QC, applied to 40 jobs and heard back from 2."* No "Hi, we are team…" first; introduce yourselves after the hook. | Presentation |
| 2 | 1:00–2:30 | **The problem** in their words | R | Quote the challenge statement. Name your user. Give 1–2 facts or a number. Explain why current solutions fail. | Impact |
| 3 | 2:30–3:30 | **Our idea** in one line | P | The one-liner: *"For [user] who [pain], [App] is an AI [thing] that [result], unlike [today]."* Then name the twist that makes it new. | Innovation |
| 4 | 3:30–7:00 | **Live demo** | B (R narrates) | One flow, rehearsed input, show the "wow" by minute 5. Narrate what the *user* feels, not what the widget does. | Usability, Demo |
| 5 | 7:00–8:30 | **Impact** with a number | R | Before vs. after: time, money, people reached. Who pays or who deploys it (schools, HR teams, REPH itself?). | Impact |
| 6 | 8:30–9:45 | **How it's built and scales on AWS** | B | PartyRock on Amazon Bedrock (name the model). Next: Bedrock API + Knowledge Base + Amplify. Guardrails and privacy. What you'd test next. | Feasibility |
| 7 | 9:45–11:00 | **Close** | P | Return to the person from the hook: *"With [App], Mika would have…"*. One ask: pilot, feedback, mentorship. Thank you + team names. | Presentation |

Check your script: `python3 tools/pitch-timer.py --file script.txt --target-minutes 9` (≈9 minutes of speech + 2 minutes of demo clicking).

---

## Demo script (Builder + narrator)

1. **Before you walk up:** app open, logged in, inputs cleared, zoom at 125%+, notifications off, backup video open in another tab.
2. **Set the scene (10 sec):** *"I'm Mika. I just found this job post…"*
3. **Paste the rehearsed input.** Don't type live; paste.
4. **While it generates**, the narrator talks. Silence during loading kills energy.
5. **Point at the wow**: literally point or highlight it. *"See this red row? That's the skill she's missing."*
6. **One interaction**: ask the chatbot one follow-up question you rehearsed.
7. **If it fails:** *"Live AI, live Wi-Fi. Here's the run we recorded 20 minutes ago."* Switch to the video. No apologies beyond one sentence.

---

## Judge Q&A bank: prepare 2-sentence answers

| Likely question | Answer frame |
|---|---|
| How accurate is it? What about hallucinations? | "We tested it with [N] inputs including tricky ones; the prompts restrict it to the user's input and say 'not stated' when unsure. For production we'd add a Knowledge Base and human review for important decisions." |
| Why does this need AI? | "The task is reading and writing messy language at scale: [X]. Rules or templates can't handle that variety; a language model can." |
| What about privacy and personal data? | "We store nothing; it runs per session. In production we'd strip personal details before sending and follow the Data Privacy Act of 2012." |
| How much would it cost to run? | "Each run is a few AI calls: fractions of a peso to a few pesos on Bedrock depending on the model. A school could pilot it cheaply before scaling." |
| Who would actually use or pay for this? | Name the buyer: a school career office, an HR team, an LGU, or REPH itself. |
| How is this different from just using ChatGPT? | "A blank chat box needs the user to know what to ask. We built a guided flow for [user] with the right steps, format, language, and guardrails, so it works for someone who's never used AI." |
| What would you build next? | Two concrete items: e.g. Knowledge Base of real job posts, Filipino-language voice input. |
| What was the hardest part? | An honest, specific story: "Our first outputs were too long, so we added format rules and an example; quality jumped." |
| Did you test with real users? | "We tested with [classmates/each other] using realistic cases; our first step after today is 10 user interviews at [school]." |
| Could it cause harm? | Name one risk and your mitigation (disclaimers, human review, no final decisions by AI). |

**Q&A rules:** The person best placed to answer answers, in 2–3 sentences, then stops. Never argue. If you don't know: *"We haven't tested that yet; here's how we would."*

---

## Slide rules

- 7 slides, max ~12 words per slide except the title. Big text, one image or screenshot each.
- Titles are claims ("Fake job offers target fresh grads"), not topics ("Problem").
- Last slide: app name, one-liner, QR/link to the app, team names + school.
- More on slides and delivery: [Section 11](../../11-presentation-winning/README.md) · storytelling arcs: [Section 29](../../29-storytelling/README.md).
