# Start Here: Your First Build + Who Does What

Read this first. By the end of tonight all three of you will have built an AI app, and everyone will know their jobs until Friday.

---

## Step 1: Pick roles (5 minutes)

Don't overthink it. Use these rules:

| If you are... | Your role | You own |
|---|---|---|
| The most comfortable with computers and apps | **Builder** | The PartyRock app and its link |
| The most organized, the one who keeps deadlines | **Product + Research lead** | The problem, the facts, the test inputs, the clock |
| The most comfortable speaking in front of people | **Pitch + Demo lead** | The slides and their link, the script, the backup video |

Roles decide who *owns* something, not who is allowed to help. Everyone still presents on Friday.

---

## Step 2: Your first build tonight (60 minutes, on a video call)

Get on a call (Messenger, Discord, Zoom, anything) with screen sharing. The app you'll build is a small version of **SkillBridge** from the [idea bank](idea-bank.md): paste a job post, get the skills it needs and interview questions.

### Everyone (10 min)
1. Go to **partyrock.aws** on a laptop.
2. Sign in with Google, Apple, or Amazon.
3. Say "I'm in" on the call. If someone can't sign in, fix that first; it's the only real blocker.

### Builder shares their screen (15 min)
1. Click **Generate app** (the App Builder).
2. Paste:
   ```
   Build an app called SkillBridge for Filipino fresh graduates.
   The user pastes a job post. The app lists the top 5 skills the job needs
   as a table (skill, why it matters, how to show it on a resume), then
   writes 3 interview questions about those skills.
   Use simple English and clear formatting.
   ```
3. Click generate. PartyRock builds the boxes (called **widgets**) for you.
4. Paste any real job post from JobStreet or LinkedIn into the input box. Watch it answer.

You've built an AI app. Now each person improves one part **on their own account**: everyone clicks **Remix** on the Builder's app (share the link in chat first), so each person has a copy.

### Everyone works in parallel (25 min)

| Who | Task | Done when |
|---|---|---|
| **Builder** | Open the skills widget's settings (the pencil/edit icon). Replace its prompt with the widget template from [prompts.md](prompts.md), section 3. Try two different models and keep the better one. | The skills come back as a clean table, and you know which model you picked |
| **Product lead** | Write 3 test inputs: a normal job post, a job post in Taglish, and a nonsense sentence ("I like mangoes"). Paste each one into your copy. Note what went wrong. | All 3 inputs + what broke are posted in the group chat |
| **Pitch lead** | Add a **Chatbot** widget. In its instructions, type `@` and pick the skills widget so the chatbot knows the results. Ask it "Which skill should I learn first?" Then screen-record a 60-second run of the app. | The video is in the group chat |

### Wrap up together (10 min)
- Builder copies the best prompt ideas from the others into the main app.
- Everyone says one thing that confused them. Write those down; that's what to practice Thursday.
- Pitch lead posts the main app link in the group chat, pinned.

---

## Step 3: The delegation board (Wednesday → Friday)

Every task has **one owner** and a **"done when"** line, so there's never a question of whether something is finished. The same list is on the **Team board** tab of your shared game-plan page, where you can tick things off together.

### Wednesday (tonight)

| Owner | Task | Done when |
|---|---|---|
| Everyone | Pick roles | Names written on the team board |
| Everyone | Sign in to partyrock.aws | Each person sees the PartyRock home page |
| Builder | Generate SkillBridge lite and share screen | The app answers a real job post |
| Builder | Rewrite the skills prompt with the template | Output is a clean table |
| Product | Write 3 test inputs (normal, Taglish, nonsense) | Inputs + what broke posted in chat |
| Pitch | Add a chatbot widget with an `@` reference, record 60 s | Video posted in chat |
| Everyone | Get the waiver signed by a parent/guardian | Signed waiver is in your bag |
| Everyone | Confirm you have a bank account | Said "yes" in chat |
| Pitch | Make the 7-slide template (Title · Problem · User · Demo · Impact · Built on AWS · Team) | Slide link pinned in chat |

### Thursday (Oct 1)

| Owner | Task | Done when |
|---|---|---|
| Everyone | Pick up the REPH laptops | Laptops + chargers in hand |
| Product | Run the mock hackathon: draw a challenge, run the 20-min idea pick, call the times | One-liner written; every time check called |
| Builder | Build the mock app in 2 h 40 min (on the REPH laptop if possible) | Main flow works end to end by the 2:15 freeze |
| Pitch | Fill in the slides and write the script | `python3 tools/pitch-timer.py --file script.txt --target-minutes 9` says "In range" |
| Everyone | Give the 15-min pitch to a friend or a camera, then score it | Scoresheet filled in (target 75+) |
| Product | Write the debrief: the 3 things to fix for Friday | Posted in chat |
| Pitch | Prepare 2-sentence answers to the judge questions in [templates/pitch-15min.md](templates/pitch-15min.md) | Each person can answer any 3 without notes |
| Everyone | Pack: waiver, ID, chargers, power bank, pen; sleep 7+ hours | Bag by the door |

### Friday (Oct 2)

| Time | Owner | Task | Done when |
|---|---|---|---|
| 10:30 | Product | Write the challenge word for word; ask REPH who the user is | Challenge written on paper |
| 11:30 | Builder | Note which AWS tools are allowed during the walkthrough | List of allowed tools written down |
| 12:30 | Product | Run the 20-minute idea pick | One-liner agreed by 12:50 |
| 12:50 | Builder | First working version | Input → AI → output works by 1:30 |
| 12:50 | Pitch | Problem + user slides | Done by 1:30 |
| 1:30 | Product | Test every change, find 1–2 facts or numbers | Facts on the impact slide by 2:30 |
| 2:30 | Everyone | Scope check, then **feature freeze at 2:45** | Nothing new gets added after 2:45 |
| 2:45 | Pitch | Record the backup video and screenshots | Saved on the laptop **and** a phone by 3:15 |
| 3:15 | Everyone | Two timed rehearsals | Both under 11 minutes before 4:00 |

---

## Handoff rules (how three beginners stay in sync)

1. **Stand-up every 30 minutes on Friday (2 minutes total).** Each person says: what I finished, what I'm doing next, where I'm stuck. The Product lead calls it.
2. **Stuck for 10 minutes? Say so.** Don't suffer silently. Someone else takes a look, or you cut that feature.
3. **One group chat, pinned links.** Pin the app link (Builder) and the slides link (Pitch). No one should ever ask "where's the latest version?"
4. **Done means the "done when" line is true,** not "almost."
5. **The owner decides.** Everyone can suggest; the person who owns a thing makes the call on it. On the idea itself, the rubric decides; on a tie, the Product lead decides.
6. **Nobody works alone on the demo.** At 2:45 the Builder walks the other two through the app so anyone could run it if needed.

Next: the full Friday plan is in the [section README](README.md), and the Thursday practice run is in [practice/mock-hackathon.md](practice/mock-hackathon.md).
