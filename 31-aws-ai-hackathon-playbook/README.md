# Section 31: AWS AI Hackathon Playbook (for teams who can't code)

> **New here? Open [start-here.md](start-here.md) first.** It gets your team building tonight and splits the work.
>
> Built for the **RELX | Reed Elsevier Philippines AI Hackathon 2026, "Ideas to Impact: Building the Future with AI"** (Oct 2, 2026, U.P. Ayala Land Technohub, Quezon City). It also works for any one-day hackathon where the challenge is revealed on the day, AWS tools are provided, and nobody on the team codes.

---

## The event in one table

| What | Detail (from the official letter) |
|---|---|
| Date | **Friday, October 2, 2026** |
| Theme | *Future Ready: Exploring AI, Careers, and the Evolving World of Work* |
| Challenge | Announced **on the day** by REPH representatives. The brief: "apply AI concepts to real-world business and social challenges" |
| Team | 3 currently enrolled students from the same school (different programs/levels OK). Max 2 teams per school. Each student joins only one team. The project must be student-led |
| Laptops | Provided by REPH, released **October 1** |
| Tools | "Walkthrough of the AWS environment" at 11:30. Expect Amazon's AI tools (see [aws-no-code-guide.md](aws-no-code-guide.md)) |
| Build time | **12:30 PM – 3:30 PM (3 hours)**, then 30 min to prepare the presentation |
| Presentation | **15 minutes per team**, 4:00–5:30 PM |
| Prizes | Champion ₱50,000 · 1st Runner-Up ₱30,000 · 4 × ₱5,000 consolation (tax free, credited ~30 business days after) |
| Must bring | **Signed parent/guardian waiver (no waiver, no entry)**, school ID, and a bank account per member for the prize |
| Contact | Ann Kristy Huelar, REPH Talent Acquisition (details in your invitation letter) |

### Judging criteria

| Criterion | Weight | What it means for a no-code team |
|---|---|---|
| Innovation & Creativity | **30%** | A fresh angle on the problem. Not "a chatbot", but "a chatbot that does X for Y that nobody serves today" |
| Impact on the Problem Statement | **30%** | You solve *the problem they announced*, for a specific person, with a number attached (hours saved, people reached, errors caught) |
| Usability & Feasibility | 20% | It works live, it's simple to use, and it could realistically be rolled out |
| Presentation & Demo | 20% | Clear story, confident demo, calm answers |

**60% of the score comes from thinking, not building.** A team of beginners can beat a team of programmers here if it picks a sharper problem and tells a better story. That's the whole strategy.

---

## How we win: five rules

1. **Answer their challenge, word for word.** Write the challenge statement on paper. Every slide and every feature must point back to a phrase in it. Teams that drift into their "cool idea" lose the 30% Impact score.
2. **One user, one pain, one moment of magic.** "Fresh graduate in Quezon City preparing for their first tech interview" beats "students". Build the single flow that makes the judges say "oh, nice". Skip everything else.
3. **Use AWS AI, visibly.** It's AWS's environment and RELX's event. Show the tool on screen, and name the model you used. Say why AI is needed (it reads/writes/understands language at scale), not just that you used it.
4. **Freeze features at 2:45 PM.** After that you only fix, test, and rehearse. A working small app beats a broken big one every time.
5. **Always have a backup demo.** Screenshots of every step and a 60-second screen recording on the laptop *and* a phone. If the Wi-Fi dies, you still demo.

---

## Roles (all three are non-coding)

| Role | Owns | During the build |
|---|---|---|
| **Builder (AI operator)** | The AWS/PartyRock app | Builds the app, writes the widget prompts, tests with sample inputs. The person most comfortable with computers. |
| **Product + Research lead** | The problem and the proof | Turns the challenge into one user + one pain. Finds 2–3 real facts or numbers (ask mentors/REPH staff too). Writes the test cases. Watches the clock. |
| **Pitch + Demo lead** | The story | Builds slides from minute 1 (not minute 150). Writes the script, plans the demo, prepares Q&A answers, records the backup video. |

Everyone presents. The Pitch lead opens and closes, the Builder runs the demo, and the Product lead covers problem and impact. More on non-coding roles: [Section 24: Non-Coder Guide](../24-non-coder-guide/README.md).

---

## Your 3-day timeline

| When | Do this |
|---|---|
| **Wed (today)** | Start with [start-here.md](start-here.md): pick roles and do your first build together on a call. Read this section (30 min each). Each person signs in to PartyRock and does the 45-min warm-up in [practice/mock-hackathon.md](practice/mock-hackathon.md). Print the waivers and get them signed. Confirm each member has a bank account. |
| **Thu (Oct 1)** | Pick up the laptops. Run the **full 3-hour mock hackathon** in [practice/mock-hackathon.md](practice/mock-hackathon.md) as a team, then rehearse the pitch once with a timer. Build your slide *template* (title, problem, user, demo, impact, roadmap, team) so Friday you only fill it in. Print [templates/day-of-card.md](templates/day-of-card.md). Sleep 7+ hours. |
| **Fri (Oct 2)** | Follow the minute-by-minute plan below. |

---

## Friday minute-by-minute

| Time | Official program | What your team does |
|---|---|---|
| Before 10:00 | Arrive | Eat breakfast. Waivers, IDs, chargers, phone hotspot ready. |
| 10:00–10:30 | Team check-in | Sit together. Open the day-of card. |
| 10:30–11:30 | Team setup + lunch | Eat. Log in to everything you'll need. Open your slide template. **Listen hard to the challenge.** Write it down word for word, and ask REPH: *"Who is the user? What does success look like to you?"* |
| 11:30–12:30 | AWS walkthrough | Builder takes notes on exactly which tools you're allowed to use and clicks along. Others write down every example REPH shows: they're hinting at what they want. |
| **12:30–12:50** | Build starts | **Pick the problem (20 min, hard stop).** Use the adapt-a-shell method in [idea-bank.md](idea-bank.md). Score 2–3 options with the rubric below. Pick one. |
| 12:50–1:30 | | Builder: first working version (input → AI → output). Product: user persona + 3 test inputs + 1–2 facts. Pitch: fill problem/user slides. |
| 1:30–2:30 | | Builder: improve output quality (better prompts, a second widget, formatting). Product: test every change, write down what breaks. Pitch: demo script + impact slide. |
| 2:30–2:45 | | **Check-in (5 min):** does the main flow work end to end? If not, cut scope now. |
| **2:45** | | **Feature freeze.** |
| 2:45–3:30 | | Fix bugs. Record backup video + screenshots. Final slides. First full rehearsal. |
| 3:30–4:00 | Snacks + prepare | Second rehearsal with a timer. Rehearse Q&A with [templates/pitch-15min.md](templates/pitch-15min.md). Reload the app so it's fresh. |
| 4:00–5:30 | Demo Day | Present. Watch other teams calmly. |
| 5:30–6:30 | Awards | Network with REPH people. They hire (see [Section 14](../14-resume-linkedin-leverage/README.md)). |

### The 20-minute problem-picking rubric

Score each candidate idea 1–5 on each line, multiply by the weight, and pick the highest total.

| Question | Weight |
|---|---|
| Does it directly answer the announced challenge? | ×3 |
| Would the judges say "I haven't seen that before"? | ×3 |
| Can we name one real user and one number that improves? | ×3 |
| Can the Builder get a working version in 40 minutes with PartyRock? | ×2 |
| Is the demo visual and fast (under 60 seconds to "wow")? | ×2 |

Anything under 40 out of 65: pick another idea. The CLI version for practice is `python3 tools/idea-scorer.py` (see [tools](../tools/README.md)).

---

## When things go wrong

| Problem | Do this |
|---|---|
| AI gives bad or long answers | Tighten the prompt: add the user, the format ("3 bullet points, max 20 words each"), and an example. See [prompts.md](prompts.md). |
| Tool/usage limit hit or site down | Switch to the backup video. Keep talking. The story still scores 60%. |
| We're behind at 2:30 | Cut to the single core flow. Fake secondary features with a slide ("next step"). |
| Team disagreement on the idea | The rubric decides. Rubric tie: the Product lead decides. No debate after 12:50. |
| A judge asks something we don't know | "Good question. We haven't tested that yet; here's how we would." Never bluff. |

---

## Files in this section

| File | Use it for |
|---|---|
| [start-here.md](start-here.md) | **Read first:** pick roles, first build tonight, who does what Wed → Fri |
| [aws-no-code-guide.md](aws-no-code-guide.md) | What AWS tools you might get and how to build with each, without code |
| [idea-bank.md](idea-bank.md) | 10 pre-built idea shells + the 20-minute adapt method |
| [prompts.md](prompts.md) | Copy-paste prompts for brainstorming, building, testing, and pitching |
| [practice/mock-hackathon.md](practice/mock-hackathon.md) | Wednesday warm-up + Thursday full 3-hour mock with scoring |
| [templates/pitch-15min.md](templates/pitch-15min.md) | 15-minute pitch structure, demo script, judge Q&A bank |
| [templates/day-of-card.md](templates/day-of-card.md) | One printable page for Friday |

Related sections: [11 Presentation](../11-presentation-winning/README.md) · [18 AI Prompt Engineering](../18-ai-prompt-engineering/README.md) · [20 Judging Insider](../20-judging-insider/README.md) · [29 Storytelling](../29-storytelling/README.md)
