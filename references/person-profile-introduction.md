# Person Profile Introduction

Use this P2 mode automatically when the user supplies a resume, CV, bio,
speaker profile, LinkedIn-style summary, company bio, or structured facts
about a person and asks for an introduction, profile, biography explainer, or
60-80 second English script.

This mode creates a separate person introduction direction. It must not reuse
the celebrity explainer question-contrast-judgment structure.

## Automatic Profile Trigger

Select this mode when:

- The source is structured career, education, skill, project, or achievement
  material.
- The user asks for a person introduction, profile script, biography
  explainer, speaker introduction, or 60-80 second introduction.
- The desired direction is factual, informative, and forward-looking rather
  than gossip, debate, controversy, or judgment.

This mode takes precedence over `Celebrity explainer series` when the request
is to introduce who the person is. It does not take precedence over death,
abuse, health, minors, criminal allegations, or active legal proceedings that
materially control the source.

If the source contains only a name or unverified claims, do not invent the
person's background, education, achievements, motives, or current goals. Use
placeholders and identify the missing facts.

## Six-Beat Profile Structure

Use these six beats in order. The target is 60-80 seconds, usually about
160-210 spoken English words.

| Beat | 80s Guide | Purpose |
|------|-----------|---------|
| 1. Position | 0:00-0:05 | Lead with the person's role and strongest verified credential |
| 2. Core thesis | 0:05-0:12 | State the throughline that connects the career |
| 3. Foundations | 0:12-0:25 | Cover origin, education, training, or early career |
| 4. Turning points | 0:25-0:47 | Explain two or three career-defining milestones |
| 5. Expertise and impact | 0:47-0:65 | Show skills, projects, outcomes, or recognition |
| 6. Forward outlook | 0:65-0:80 | Close with current mission and future contribution |

For a 60-second version, compress the foundations and expertise beats first.
Keep the position, core thesis, one or two turning points, impact, and future
outlook.

## Resume-to-Story Rules

Do not read the resume in order. Convert it into a narrative:

1. Find the clearest career throughline.
2. Choose the strongest verified credential for the opening.
3. Select two or three turning points that explain how the person arrived at
   their current position.
4. Group skills into capabilities instead of listing every tool or keyword.
5. Connect expertise to a project, result, audience, or mission.
6. End with what the person is building, solving, leading, or contributing
   next when the source supports it.

Prefer concrete language:

- "has led"
- "built"
- "worked across"
- "specializes in"
- "is known for"
- "developed"
- "helped grow"

Do not add:

- Unverified awards, titles, clients, or results
- Private family, health, relationship, or financial details
- Speculative motives
- Inflated claims such as "world-class" unless the source supports them
- Invented quotes or a fake first-person voice

## Differentiation from Celebrity Explainer

| Celebrity explainer | Person profile introduction |
|---------------------|-----------------------------|
| Starts with a public decision, controversy, or timeline | Starts with role, credential, and career thesis |
| Uses question-contrast-judgment beats | Uses foundation-turning point-impact beats |
| Ends with a debate or value judgment | Ends with a forward-looking positioning statement |
| Allows controlled skepticism | Stays factual, informative, and respectful |
| Focuses on a public event | Explains the whole person and career arc |
| Uses evidence to test a claim | Uses evidence to support a profile |

Never reuse the celebrity mode's gossip framing, binary CTA, private-motive
language, or "what is the real reason" hook for a resume-based introduction.

## English-Only Output

When the user explicitly requests an English script, output the English hook
and spoken script only. Do not append the Chinese translation unless the user
requests it.

When the user requests a full bilingual package, provide the normal complete
Chinese translation after the English sections.

## Profile Quality Checks

- The script sounds like a short documentary introduction, not a resume read
  aloud.
- The first five seconds establish position and credibility.
- One clear thesis connects the career.
- Two or three turning points carry the middle.
- Skills become capabilities and evidence.
- The ending looks forward without inventing future plans.
- Every material fact comes from the supplied profile or a verified source.
- The direction remains visibly separate from the celebrity explainer series.
