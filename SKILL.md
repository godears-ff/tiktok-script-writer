---
name: tiktok-script-writer
description: Write US-audience TikTok and short-form scripts in English with complete Chinese translation, including hooks, storyboards, title/cover copy, 二创 commentary, and fact-grounded social-news or true-crime workflows. Automatically use the celebrity explainer series mode for celebrity, influencer, entertainment-person, and public-figure sources unless a higher-risk mode takes precedence. Use when the user requests TikTok scripts, English short-form copy, or commentary and needs Chinese translation.
metadata:
  short-description: TikTok scripts in English + Chinese translation
  version: "1.6.0"
---

# TikTok Script Writer (English + Chinese)

Write platform-native TikTok and short-form video scripts for a US audience.
Do not promise virality. Optimize for a clear hook, retention, useful payoff,
and natural spoken language.

For every full deliverable, output English first and a complete Chinese
translation below it. The Chinese translation is mandatory.

## Default Creator Style

Unless the user explicitly requests another format, default to an American
commentary/explainer voice:

- Primary market and audience: United States.
- Content form: commentary, reaction, opinion, discussion, chat, and
  explanatory narration, not a wire-service news report.
- Point of view: use a clear personal stance. The creator is allowed to say
  "I think," "what gets me is," "the wild part is," or "I'm not buying that."
- Tone: curious, conversational, opinionated, social, and discussion-driven.
- Topic energy: gossip, surprise, humor, playful exaggeration, debate, and
  audience reaction when the subject supports it.
- Structure: facts are evidence for commentary, not a chronological
  press-release recap.
- Avoid encyclopedia chronology, formal transitions, and institutional
  detachment.

Controlled exaggeration is allowed for style and emotion, but never for
numbers, quotes, injuries, charges, legal stage, or source certainty. Keep
facts exact while making the reaction human.

For death, abuse, health, minors, and active legal cases, preserve the
commentary voice but reduce slang and avoid joking about victims or harm.

Read `references/default-american-commentary-style.md` when the user asks for
a new script or a rewrite unless they explicitly request a neutral news brief.

## Mode Selection

Choose one primary mode before writing:

| Mode | Use when | Default output |
| --- | --- | --- |
| General | Standard TikTok topic, story, hack, hot take, review, or POV | Full script package |
| Commentary | Film, TV, sports, variety, or mashup clip commentary | Full commentary package |
| Social news / true crime | Reports, public safety, police, court, surveillance, viral incidents, or real cases | Full sourced package |
| Celebrity explainer series | Celebrity, influencer, streamer, actor, singer, athlete, royal, creator, public figure, or entertainment-person story about a personal decision, relationship, deal, career move, money, image, statement, controversy, or timeline | Fixed six-beat celebrity series package |

If the request spans modes, use the mode that controls the risk. For example,
commentary about an ongoing criminal case uses the social-news source and legal
rules.

### Automatic Celebrity Explainer Routing

When the source primarily concerns a celebrity, influencer, streamer, actor,
singer, athlete, royal, creator, entertainment figure, or other public
personality, automatically select `Celebrity explainer series` unless one of
these overrides applies:

1. The user explicitly requests another format or a neutral news brief.
2. The primary material is commentary on a film, TV, sports, or performance
   clip rather than the person's decision or public behavior.
3. Death, abuse, health, minors, active legal proceedings, criminal
   allegations, or another high-risk issue controls the story.

For an override, use the higher-risk mode and add the celebrity mode only as a
safe tonal layer. Never let the six-beat entertainment format weaken fact,
legal, privacy, or sensitive-content rules.

When this mode is selected, read
`references/celebrity-explainer-series.md` and use
`assets/celebrity-explainer-card.md`.

After choosing the mode, identify the topic family and read
`references/topic-style-playbooks.md`. Use its playbook to set the tone,
opening style, pacing, evidence density, CTA, and visual language.

Do not force one voice across every topic. A breaking-news script, celebrity
gossip story, sports analysis, and food video should feel different even when
they use the same Hook and S.T.O.R.M. principles.

If the user explicitly asks for only a script or a compact response, output
Hook, Script, and the Chinese translation of both. Do not add a storyboard,
cover, or engagement section unless requested. For social news, always retain
the Fact and Risk Notes and Sources sections because they carry legal and
factual limits.

## Core Rules

- Hook: use the first 0-3 seconds for one core idea. The spoken hook is
  normally 8-12 words, not a hard five-word limit. A visual, evidence, or
  result hook can lead instead of spoken text.
- Answer axis: by 0:05, reveal the direction of the answer in one clear
  sentence. Say what the real issue is, what changed, or what the evidence
  contradicts. Do not hide the entire premise behind "here's why" or "it gets
  complicated."
- Duration: use one length standard across the skill.

| Mode | Default | Supported |
| --- | --- | --- |
| General | 80 seconds, about 190-210 spoken words | 15, 30, 45, 60, or 80 seconds |
| Commentary | 80 seconds, about 190-210 spoken words | 15-30 seconds only on request; otherwise 45-90 seconds |
| Social news | 60-80 seconds | 30, 60, or 80 seconds |
| Celebrity explainer series | 60-80 seconds, about 160-210 spoken words | 30, 60, or 80 seconds |

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

For topics built around a choice, public-figure decision, two people or
brands, expected versus actual behavior, before versus after, or a status
gap, read `references/comparison-hook-patterns.md`. Build the contrast matrix
and choose one supported question hook when it fits. Before drafting, define
the answer axis that must land by 0:05. Do not invent a comparison, motive,
relationship, or decision that the source does not support.

### 3. Script Body

Use the duration standard in Core Rules. Build meaningful tension and deliver
the payoff without filler. End with a CTA that fits the content rather than
forcing controversy. After the hook, use the answer-axis sentence to tell the
viewer what distinction, tradeoff, or consequence the rest of the script will
explain.

For `Celebrity explainer series`, use the fixed six beats from
`references/celebrity-explainer-series.md`: question hook, answer axis, three
contrast layers, receipts or qualifiers, judgment, and decision CTA. Do not
replace the series structure with a chronological biography or press recap.

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
2. Does the answer axis land by 0:05 and is it supported by the source?
3. Has news-release language been replaced with natural spoken English without
   damaging accuracy or attribution?
4. Does the pacing create a visual or audio cut every 2-3 seconds?
5. Does the CTA create a useful decision, prediction, debate, or identity
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

### 13. Aggregated Word Document Deliverables

When the user asks to compile multiple scripts into a Word document, read
`references/aggregated-document-deliverables.md`.

For each script in the document, preserve:

- English script with no timecodes
- Chinese translation with timecodes
- Storyboard with Chinese headers and Chinese cell content
- Title and cover copy in English and Chinese
- Caption, first line, search keywords, and hashtags
- CTA in English and Chinese
- Fact and Risk Notes in English and Chinese
- Sources

Keep separate iterations such as v1.0 and v1.1 as distinct numbered entries
when the user asks for all generated versions.

### 14. Creator Voice and Final Quality Review

When a creator supplies writing samples, approved scripts, previous captions,
or explicit voice preferences, read `references/creator-voice-profile.md` and
use `assets/creator-voice-profile-template.md`.

Record:

- Primary viewer
- Signature and banned phrases
- Sentence length and pacing
- Humor and emotional range
- Authority and skepticism level
- Topic-specific tone changes
- CTA style
- Visual and caption patterns
- Legal, privacy, and brand-safety boundaries

Never imitate another living creator's signature style without permission.
The voice profile should capture the user's own approved patterns.

Before final delivery, run `references/quality-scorecard.md` when the task is
substantial, high-risk, or requested as an optimization pass. A high score
does not override factual accuracy, legal limits, privacy, or platform policy.

### 15. Topic-Style Routing

For topic-specific tone and structure, read
`references/topic-style-playbooks.md` and use
`assets/topic-style-card.md` when the user wants a repeatable format.

Select one controlling playbook:

- Breaking news / public safety
- True crime / courts
- Celebrity / creator gossip
- Music / hip-hop news
- Sports
- Film / TV / entertainment commentary
- Technology / product explainers
- Business / entrepreneurship
- Health / mental health
- Fashion / beauty / lifestyle
- Food / travel / local stories
- Viral internet / memes / wholesome stories
- Politics / high-sensitivity public issues

If a story spans multiple topics, use the highest-risk playbook for factual
limits and add another playbook only as a tonal layer.

## Output Format

Use this order for a full deliverable:

```markdown
## Hook
[English hook] - [hook type]
Answer axis: [one sentence that lands the direction of the answer by 0:05]

## Script
[Spoken English only. No camera angles, action notes, or timecodes.]

## Series Beat Map (celebrity explainer series only)
[Question hook / answer axis / three contrast layers / receipts or qualifiers /
judgment / decision CTA]

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
- `references/comparison-hook-patterns.md`: question-first hooks, contrast
  matrices, answer-axis rules, and safe comparison templates.
- `references/celebrity-explainer-series.md`: automatic routing, six-beat
  series structure, motive-safe phrasing, and subtype CTA patterns.
- `references/viral-copy-review.md`: four-check diagnostic, S.T.O.R.M.
  rewriting structure, visual pacing guidance, and safe engagement triggers.
- `references/production-and-publishing.md`: caption and discovery, sound-off
  accessibility, delivery notes, testing, analytics reviews, corrections, and
  recurring-series design.
- `references/aggregated-document-deliverables.md`: required structure for
  multi-script Word files and Chinese storyboard translation.
- `references/creator-voice-profile.md`: account voice, audience, signature
  language, banned phrasing, and topic-specific tone.
- `references/quality-scorecard.md`: final 100-point review across retention,
  clarity, evidence, safety, bilingual fidelity, and production readiness.
- `references/topic-style-playbooks.md`: topic-specific hooks, tone, pacing,
  evidence density, CTA, visual language, and common mistakes.
- `references/default-american-commentary-style.md`: default US commentary
  voice, personal-stance rules, controlled exaggeration, and news-to-commentary
  conversion.
- `assets/script-template.md`: general script package.
- `assets/storyboard-template.md`: general shot planning.
- `assets/commentary-script-template.md`: commentary package.
- `assets/social-news-script-template.md`: sourced news package.
- `assets/creator-voice-profile-template.md`: repeatable account voice profile.
- `assets/quality-review-scorecard.md`: fillable final QA checklist.
- `assets/topic-style-card.md`: reusable topic-specific style configuration.
- `assets/celebrity-explainer-card.md`: fillable celebrity series episode card.
- `scripts/generate-ideas.py`: optional seed generation for a requested niche.

## Triggers

Use this skill when the user mentions TikTok, short-form video, English script,
US audience, storyboard, hook, Chinese translation, 二创, 解说, commentary,
film/TV/sports commentary, mashup, clip commentary, breaking news, social news,
true crime, police report, court records, public safety, surveillance footage,
or viral incident commentary.

Also use this skill when the supplied source is primarily about a celebrity,
influencer, streamer, actor, singer, athlete, royal, creator, entertainment
figure, or public personality, even if the user only provides the source and
asks for a script. Apply the automatic celebrity explainer routing unless a
higher-risk mode or explicit user format takes precedence.

Also use this skill when the user asks for S.T.O.R.M. copy, a viral-style
rewrite, stronger retention hooks, or diagnostic feedback on a TikTok script.
