# AWS for Vibecoders: Building AI Apps Without Code

You won't know exactly which AWS tools you get until the 11:30 walkthrough. This guide covers the likely options, from easiest to hardest. **Rule: use what the walkthrough shows you. If it confuses you or breaks, fall back to PartyRock.**

| Tool | Code needed? | AWS account needed? | Best for | Beginner fit |
|---|---|---|---|---|
| **PartyRock** | None | No (sign in with Google, Apple, or Amazon) | Full mini-apps: form → AI → result, chatbots, file readers | ⭐⭐⭐ Start here |
| **Amazon Bedrock playground** (in the AWS console) | None | Yes (REPH would provide) | Testing prompts and models, chat demos | ⭐⭐ |
| **Bedrock Knowledge Base / "chat with your documents"** | None (setup by clicking) | Yes | Q&A over PDFs or company docs | ⭐⭐ if the walkthrough shows it |
| **Amazon Q** (Business apps / Developer) | None to little | Yes | Company-data assistants, simple apps from a description | ⭐⭐ if provided |
| **Kiro** (AWS's AI coding editor) | AI writes it, you steer | Yes / sign-in | Real web apps from a spec | ⭐ only if a mentor helps |

---

## 1. PartyRock (your main tool)

PartyRock is AWS's free, browser-based playground for building generative-AI apps. It runs on Amazon Bedrock models, so it's legitimately "building on AWS". Each piece of your app is a **widget**:

| Widget | What it does |
|---|---|
| **User Input** | A text box the user types into (e.g. "Paste your resume") |
| **Document** | Lets the user upload a file (PDF/text) for the AI to read |
| **Text Generation** | AI writes something based on a prompt that can reference other widgets |
| **Image Generation** | AI makes an image from a prompt |
| **Chatbot** | A back-and-forth conversation with instructions you set |
| **Static Text** | Fixed instructions or a title for the user |

Widgets connect with **`@` references**. A Text Generation prompt like `Summarize @Resume for a fresh graduate` automatically reruns when the user changes the Resume input. That chaining is how you build "apps" without code.

### Build flow (practice this until it takes 15 minutes)

1. Go to **partyrock.aws** and sign in (Google, Apple, or Amazon account). **Do this on Wednesday**, not Friday.
2. Click **Generate app** / the App Builder. Describe your app in 2–4 sentences (use the builder prompt in [prompts.md](prompts.md)).
3. PartyRock creates widgets for you. Now **edit each widget**:
   - Rename widgets to clear names (`Resume`, `Target Job`, `Gap Analysis`).
   - Open each AI widget's prompt and rewrite it with a role, a format, and rules.
   - Choose the model in the widget settings. Try two and keep the better one. Note its name for the pitch.
4. Add a **Chatbot** widget at the end ("Ask follow-up questions about your results") if it fits. Judges like interaction.
5. Test with your 3 prepared inputs: normal, tricky, and a bad input (empty or off-topic).
6. **Share**: make the app public and copy the link, or use a snapshot to share a specific result. Put the link and a QR code on your last slide.

### Tips that make a PartyRock app look pro

- **Output format is your UI.** Ask for headings, bullet points, tables, emoji status markers ("✅ Ready / ⚠️ Gap"). Formatted output looks like a real product.
- **Chain 3 steps, not 1.** Input → analysis → action plan looks much smarter than input → answer.
- **Add guardrails in the prompt**: "If the input is not a resume, reply: 'Please paste a resume.'" Judges test weird inputs.
- **Localize.** "Answer in simple English; if the user writes in Filipino or Taglish, answer in the same language." Instant Innovation + Impact points for a PH audience.
- **Usage is metered.** PartyRock gives free daily/trial usage. Don't burn it regenerating 50 times; test deliberately. If you run out, another teammate's account works too.

---

## 2. Amazon Bedrock playground (if REPH gives you AWS console access)

1. In the AWS console, search **Bedrock**.
2. Open **Playgrounds → Chat** (or Text).
3. Pick a model (e.g. Anthropic Claude, Amazon Nova, Meta Llama; whatever is enabled).
4. Put your instructions in the **system prompt** box, then chat.

Good for: live-demoing a single powerful prompt, comparing models, or showing "we tested 3 models and picked X because…" (a nice feasibility point). It's weaker as an "app": there's no custom input form. If you only have Bedrock, present it as "the engine" and show the user flow on slides.

### Knowledge Bases ("chat with your documents")

If the walkthrough shows **Knowledge Bases**, you can upload a few documents (sample policies, FAQs, articles) and chat with them. The AI answers only from those files and cites them. That's excellent for challenges like "help employees find information" or "help researchers." Follow the walkthrough's steps exactly, since setup has several clicks and takes time to sync. Start it early.

---

## 3. Amazon Q / Kiro (only if provided and shown)

- **Amazon Q** apps: describe the app in plain English and Q builds a simple form-based AI app. The concept is similar to PartyRock. If REPH demos it, it's a safe choice.
- **Kiro** is an AI code editor. You describe features and it writes the code. It's powerful, but debugging it in 3 hours with no coding experience is risky. Only use it if a mentor sits with you, and keep PartyRock as the fallback.

---

## Saying "AWS" in the pitch (feasibility points)

Judges from a tech company want to hear that it could really ship. One slide, three lines:

> **Built with:** PartyRock on Amazon Bedrock (model: *name the one you used*)
> **To scale it:** move the same prompts to Amazon Bedrock with an API, add a Knowledge Base of real [company/school] documents, host it with AWS Amplify.
> **Safety:** guardrails in the prompts, no personal data stored, human reviews important decisions.

You don't have to build any of that. You just have to show you know the path.

---

## Pre-flight checklist (Wednesday/Thursday)

- [ ] Every member can sign in to partyrock.aws
- [ ] Each member has built at least one app (warm-up in [practice/mock-hackathon.md](practice/mock-hackathon.md))
- [ ] You know how to: add a widget, reference with `@`, change model, share a link
- [ ] You know where daily usage is shown and what happens when it runs out
- [ ] Bookmarks saved on the REPH laptops (if allowed): PartyRock, your slide template, this page
