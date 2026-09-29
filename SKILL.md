---
name: tiktok-script-writer
description: Write US-audience TikTok and short-form scripts in English with complete Chinese translation, including hooks, storyboards, title/cover copy, 二创 commentary, and fact-grounded social-news or true-crime workflows. Use when the user requests TikTok scripts, English short-form copy, or commentary and needs Chinese translation.
metadata:
  short-description: TikTok scripts in English + Chinese translation
  version: "1.1.0"
---

# TikTok Script Writer (English + Chinese)

Write platform-native TikTok and short-form video scripts for a US audience.
Do not promise virality. Optimize for a clear hook, retention, useful payoff,
and natural spoken language.

For every full deliverable, output English first and a complete Chinese
translation below it. The Chinese translation is mandatory.

## Mode Selection

Choose one primary mode before writing:

| Mode | Use when | Default output |
| --- | --- | --- |
| General | Standard TikTok topic, story, hack, hot take, review, or POV | Full script package |
| Commentary | Film, TV, sports, variety, or mashup clip commentary | Full commentary package |
| Social news / true crime | Reports, public safety, police, court, surveillance, viral incidents, or real cases | Full sourced package |

If the request spans modes, use the mode that controls the risk. For example,
commentary about an ongoing criminal case uses the social-news source and legal
rules.

If the user explicitly asks for only a script or a compact response, output
Hook, Script, and the Chinese translation of both. Do not add a storyboard,
cover, or engagement section unless requested. For social news, always retain
the Fact and Risk Notes and Sources sections because they carry legal and
factual limits.

## Core Rules

- Hook: use the first 0-3 seconds for one core idea. The spoken hook is
  normally 8-12 words, not a hard five-word limit. A visual, evidence, or
  result hook can lead instead of spoken text.
- Duration: use one length standard across the skill.

| Mode | Default | Supported |
| --- | --- | --- |
| General | 80 seconds, about 190-210 spoken words | 15, 30, 45, 60, or 80 seconds |
| Commentary | 80 seconds, about 190-210 spoken words | 15-30 seconds only on request; otherwise 45-90 seconds |
| Social news | 60-80 seconds | 30, 60, or 80 seconds |

The user's explicit duration wins. Adapt the word count to speaking pace and
language rather than padding to hit a number.

- Write natural American English for the intended US audience. Use
  contractions, short sentences, and concrete details.
- Write for a US TikTok viewer, not a newspaper reader or encyclopedia.
  Remove press-release and Wikipedia-style framing without weakening
  attribution, legal limits, or factual accuracy. Calibrate the tone to the
  topic: measured for news and true crime, conversational for celebrity and
  creator stories, energetic for sports, analytical for technology, and
  fan-native for film, TV, and music.
- Define one primary viewer and one clear promise for the video. Do not mix
  separate stories or audiences unless the relationship between them is the
  central point. Aim to answer one main question per script.
- The spoken script contains spoken words only. Put camera angles, actions,
  text overlays, props, B-roll, and scene notes in the storyboard.
- Use natural Chinese that preserves the source tone. For news, legal, and
  true-crime content, use restrained standard Chinese and preserve every
  factual and legal qualifier. Do not add slang that strengthens a claim.
- Do not present attention-span statistics, platform benchmarks, current
  trends, slang, audio, or pop-culture references as current unless they were
  verified for the current date. If they cannot be verified, keep the script
  evergreen and omit the time-sensitive reference.
- Do not describe trends, sounds, or format rules as guaranteed performance.
  Frame them as hypotheses to test.
- When the deliverable involves realistic synthetic media, synthetic voice, or
  materially altered footage, flag applicable platform disclosure
  requirements.

## Workflow

### 1. Topic and Angle

Infer the niche and angle from the request. Ask only when the missing choice
would materially change the script. If the user wants candidate ideas, read
`references/tiktok-formats.md`; when local script execution is useful, resolve
the absolute path to this skill's root directory and run:

```bash
python /absolute/path/to/tiktok-script-writer/scripts/generate-ideas.py <niche>
```

Treat generated ideas as seeds. Verify any trend, statistic, or current-event
claim before using it.

### 2. Hook in the First 3 Seconds

Pick a hook strategy from `references/tiktok-formats.md`. Lead with one clear
idea, tension, evidence, or outcome. For news, the hook must be supported by
the fact ledger.

### 3. Script Body

Use the duration standard in Core Rules. Build meaningful tension and deliver
the payoff without filler. End with a CTA that fits the content rather than
forcing controversy.

Read `references/us-audience.md` only when audience psychology, cultural
context, humor style, demographics, or calendar timing materially affects the
script.

### 4. Storyboard

Split the script into shots and use `assets/storyboard-template.md`. Include
camera angle, visual action, text overlay, and audio. Keep all visual direction
out of the spoken script.

### 5. Title and Cover

Use a short title, normally 3-6 words for general content and as concise as
legal accuracy permits for news. Specify the cover expression, composition,
text placement, and contrast.

### 6. Engagement Strategy

Give 2-3 comment prompts when useful, plus a save, share, duet, or stitch angle
that fits the content. Do not invite harassment, victim-blaming, or
uninformed accusations.

### 7. Commentary Scripts (二创解说)

For film, TV, sports, or mashup clip commentary, read
`references/commentary-scripts.md` and use
`assets/commentary-script-template.md`.

1. Fill the variable table: topic, source clips and timestamps, platform,
   duration, audience, key details, personal take, and background or angle.
2. Produce both English and Chinese in the final response.
3. Require 2-3 distinct angles and explain how each differs from typical
   videos on the topic.
4. Rewrite all on-screen text and subtitles. Never reuse the source's
   subtitles.
5. Output the shot list, then the pre-publish checklist covering rights,
   platform policy, transformed commentary, audio, and AI disclosure.

Do not state that a clip qualifies as fair use. Short excerpts, commentary,
attribution, and transformation reduce risk, but rights and platform policy
still require review.

### 8. Social News and True-Crime Scripts

For breaking news, public safety, police, court, surveillance, viral incidents,
or true-crime scripts, read `references/social-news-scripts.md` and use
`assets/social-news-script-template.md`.

Build a fact ledger before drafting. Separate confirmed facts, alleged claims,
disputed claims, and unknowns. Record the source, source type, publication
date, and verification date for every material fact. Include an `As of` date
near the hook or in the Fact and Risk Notes.

If the user provides only a headline, title, or social post, treat the story as
an unverified draft. Use placeholders and do not invent names, ages, roles,
charges, injuries, motives, evidence, or outcomes.

Add a `Sources` section with direct source links, publisher, publication date,
and access or verification date. If there is no independent source, state
`Source basis: user-supplied material only; not independently verified`.

Keep the narration neutral, direct, and source-aware. Do not upgrade an
arrest, suspicion, lawsuit, or allegation into a conviction or established
fact. Avoid unnecessary graphic detail and protect minors and victims.

### 9. Chinese Translation

After all English sections, provide a complete Chinese translation of every
English section, including the Fact and Risk Notes, Sources, and Cover Prompt
when present. Preserve uncertainty, attribution, dates, legal stage, and
source limitations.

General entertainment may use natural mainland Chinese internet phrasing when
it fits the creator's voice. Social-news, legal, and true-crime translation
must remain precise and low-slang.

### 10. Cover Prompt

Generate a self-contained image-generation prompt using:

```text
Primary request: [visual concept]
Subject: [expression, pose, angle]
Background: [color, style, environment]
Text overlay: "[title]" in bold white/yellow font with black outline
Lighting/mood: [mood]
Color palette: [main colors]
Aspect ratio: 9:16 vertical
Style: Photorealistic / digital art
Constraints: No watermarks, no logos, leave room for text in the upper third
```

For news or true crime, also prohibit fabricated evidence, fake documents,
altered surveillance frames, and misleading reenactment visuals.

### 11. Viral Copy Review (All Modes)

When the user asks for a stronger hook, more engaging copy, a rewrite, or a
viral-style review, read `references/viral-copy-review.md`.

Use its four diagnostic checks and S.T.O.R.M. structure as an editing layer:

1. Is the hook driven by a real conflict, contradiction, evidence, emotion, or
   concrete result?
2. Has news-release language been replaced with natural spoken English without
   damaging accuracy or attribution?
3. Does the pacing create a visual or audio cut every 2-3 seconds?
4. Does the CTA create a useful decision, prediction, debate, or identity
   response rather than a generic follow request?

Do not force a false binary, invent a scandal, overstate legal claims, or
promise virality. For social news, legal, health, minor-related, and
sensitive-topic scripts, the Fact and Risk Notes and Sources always take
priority over engagement tactics.

### 12. Production, Publishing, and Learning

For full packages or when the user asks about captions, testing, performance,
corrections, accessibility, or recurring series, read
`references/production-and-publishing.md`.

Before final delivery, check:

- Caption text and searchable language
- Sound-off readability
- Voiceover pronunciation and pacing notes when relevant
- One-variable test plan when multiple hooks or covers are proposed
- The correct correction and update process for factual errors
- Rights, sponsorship, and platform-disclosure requirements

Do not hardcode posting times, current trends, or engagement benchmarks.
Those require current audience and platform verification.

## Output Format

Use this order for a full deliverable:

```markdown
## Hook
[English hook] - [hook type]

## Script
[Spoken English only. No camera angles, action notes, or timecodes.]

## Storyboard
[English storyboard table]

## Title and Cover
[English title and cover description]

## Caption and Search Text
[English caption, first-line hook, searchable keywords, and hashtags if useful]

## CTA
[English call to action]

## Alternative Angles (commentary only)
[2-3 distinct angles and how each differs from typical videos on the topic]

## Rights and Platform Notes (commentary only)
[Source excerpts / audio / copyright and platform risk / AI disclosure]

## Pre-Publish Checklist (commentary only)
[Short clips / rights and platform policy / rewritten text / opinion strength /
bilingual claim consistency / AI disclosure]

## Fact and Risk Notes (social-news only)
[As of / confirmed facts / alleged claims / disputed claims / unknowns /
legal-stage check / sensitive-content check / source gaps]

## Sources (social-news only)
[Publisher, source type, title, direct URL, publication date, verification
date, and the facts it supports]

## Cover Prompt
[Self-contained image-generation prompt]

---

## Chinese Translation
[Complete translation of every English section above, including Fact and Risk
Notes, Sources, commentary alternative angles, rights notes, pre-publish
checklist, and Cover Prompt when present. Preserve factual, legal, and source
qualifiers exactly.]
```

For a compact general or commentary request, use:

```markdown
## Hook
[English hook]

## Script
[Spoken English only]

---

## Chinese Translation
[English hook and script translated completely]
```

For a compact social-news request, omit the storyboard, title/cover, and cover
prompt, but keep:

```markdown
## Hook
## Script
## Fact and Risk Notes
## Sources

---

## Chinese Translation
[Translate every section above]
```

## Progressive Disclosure

Read only the resources needed for the current mode:

- `references/tiktok-formats.md`: formats, hook strategies, pacing, and
  time-sensitive trend rules.
- `references/us-audience.md`: evergreen audience context, cultural notes,
  humor, demographics, and calendar timing.
- `references/commentary-scripts.md`: 二创 prompts, anti-AI phrasing, rewrite
  guidance, rights checks, and pre-publish checks.
- `references/social-news-scripts.md`: sourcing, fact-ledger, legal-language,
  sensitive-content, and correction rules.
- `references/viral-copy-review.md`: four-check diagnostic, S.T.O.R.M.
  rewriting structure, visual pacing guidance, and safe engagement triggers.
- `references/production-and-publishing.md`: caption and discovery, sound-off
  accessibility, delivery notes, testing, analytics reviews, corrections, and
  recurring-series design.
- `assets/script-template.md`: general script package.
- `assets/storyboard-template.md`: general shot planning.
- `assets/commentary-script-template.md`: commentary package.
- `assets/social-news-script-template.md`: sourced news package.
- `scripts/generate-ideas.py`: optional seed generation for a requested niche.

## Triggers

Use this skill when the user mentions TikTok, short-form video, English script,
US audience, storyboard, hook, Chinese translation, 二创, 解说, commentary,
film/TV/sports commentary, mashup, clip commentary, breaking news, social news,
true crime, police report, court records, public safety, surveillance footage,
or viral incident commentary.

Also use this skill when the user asks for S.T.O.R.M. copy, a viral-style
rewrite, stronger retention hooks, or diagnostic feedback on a TikTok script.
