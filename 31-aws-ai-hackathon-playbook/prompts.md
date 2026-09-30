# Copy-Paste Prompts for a No-Code AWS Hackathon

Replace everything in `[brackets]`. These work in PartyRock widgets, the Bedrock chat playground, or any AI chat. For the general prompt patterns behind them, see [Section 18](../18-ai-prompt-engineering/README.md).

---

## 1. Right after the challenge is announced (12:30)

**Break down the challenge** (use any AI chat allowed on the laptop):

```
Here is a hackathon challenge, word for word:
"[paste the challenge]"

Our team has 3 hours, no coding skills, and must build with AWS PartyRock
(no-code AI app builder: text inputs, file upload, AI text generation,
image generation, chatbot widgets).

1. List the 3 most specific user groups this challenge is really about.
2. For each, give the single most painful problem, in one sentence.
3. Suggest 3 app ideas that a no-code team could demo in 3 hours.
   For each: one-line pitch, the widget flow (input → AI step → output),
   and one "wow" demo moment.
4. Rank the ideas by: fits the challenge, originality, and measurable impact.
Be concrete. No generic chatbots.
```

**Stress-test your chosen idea:**

```
Our idea: [one-liner].
Act as a strict judge from a global information-analytics company.
Scoring: Innovation 30%, Impact 30%, Usability & Feasibility 20%, Demo 20%.
Give the 3 hardest questions you would ask, the weakest part of the idea,
and one change that would raise the score the most.
```

---

## 2. PartyRock App Builder prompt

```
Build an app called [App Name] for [specific user] who [pain].
The user enters [input 1] and [input 2].
Step 1: the AI [analyzes X] and shows a table with [columns].
Step 2: the AI creates [action plan / rewrite / checklist] based on step 1.
Finally, add a chatbot that answers follow-up questions about the results.
Use simple English and friendly formatting with headings and bullet points.
```

---

## 3. Widget prompt template (the one that makes outputs good)

Paste this into each **Text Generation** widget and fill it in:

```
You are [role, e.g. a friendly career coach for Filipino fresh graduates].

Task: [what to do] using this input:
@[Input Widget Name]

Output format:
- Start with a one-line summary in bold.
- Then [a table with columns A | B | C] / [3–5 bullet points, max 20 words each].
- End with one clear next step the user can do today.

Rules:
- Use simple English. If the input is in Filipino or Taglish, reply in the same language.
- If the input is empty or unrelated to [topic], reply only:
  "Please paste [expected input] to get started."
- Do not invent facts, names, or numbers. If unsure, say so.
- Keep it under [150] words.
```

**Chatbot widget instructions:**

```
You are [App Name]'s assistant. Help the user understand their results:
@[Result Widget Name]
Answer in 3 sentences or fewer. Ask one follow-up question when helpful.
Stay on topic: if asked about something else, politely steer back.
Never give [medical/legal/financial] decisions. Suggest a professional for those.
```

---

## 4. Fixing bad AI output

| Symptom | Add this line to the prompt |
|---|---|
| Too long | `Maximum 100 words. Use bullet points only.` |
| Too generic | `Refer to at least 2 specific details from the input.` + give one example output |
| Wrong format | Paste an example of the exact format you want, starting with `Example output:` |
| Makes things up | `Only use information from the input. If it is not there, write "Not stated".` |
| Ignores Taglish | `Detect the language of the input and reply in that same language.` |
| Different every time | Lower the temperature/creativity in settings if available, and make the format stricter |

---

## 5. Test inputs (Product lead prepares these)

Ask the AI to generate them:

```
Create 3 realistic test inputs for an app that [does X] for [user]:
1. A typical, realistic case.
2. A tricky case (messy, incomplete, or in Taglish).
3. An edge case that should be politely rejected.
Make them Philippine-context and realistic. Plain text only.
```

Save the best typical case as your **demo input**. Rehearse with exactly that input.

---

## 6. Pitch helpers (Pitch lead)

**Draft the script:**

```
Write a pitch script for a 15-minute hackathon slot:
about 9 minutes of talking plus a 2-minute live demo, leaving time for Q&A.
Three speakers: [A] opens with a story, [B] covers problem and impact,
[C] runs the demo. [A] closes.
App: [one-liner]. User: [persona]. Key facts: [1–2 facts].
Judging: Innovation 30%, Impact 30%, Usability & Feasibility 20%, Demo 20%.
Hit each criterion explicitly. Short sentences. No jargon.
Open with a real, specific moment (a named person, a time, a feeling).
```

Check the length with `python3 tools/pitch-timer.py --file script.txt --target-minutes 9`.

**Predict judge questions:**

```
We are pitching [one-liner], built with PartyRock on Amazon Bedrock in 3 hours.
List the 10 most likely judge questions from AI and business leaders,
and a 2-sentence honest answer for each.
Include questions about accuracy, privacy, cost, scaling, and why AI is needed.
```

**Slide titles:**

```
Turn this pitch into 7 slide titles of 6 words max, each one a claim,
not a topic (e.g. "Scams cost Filipinos billions yearly", not "Problem").
[paste script]
```
