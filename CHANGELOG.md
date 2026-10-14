# Changelog

All notable changes to this skill are documented here.

## [1.7.0] - 2026-10-14

### Added

- Automatic `Person profile introduction` routing for resumes, CVs, bios,
  LinkedIn-style summaries, speaker profiles, company bios, and structured
  person facts.
- A six-beat profile structure: position, core thesis, foundations, turning
  points, expertise and impact, and forward outlook.
- Resume-to-story rules, English-only output support, and a dedicated profile
  introduction card.
- A differentiation contract that keeps profile introductions separate from
  the celebrity explainer series.

### Changed

- Profile introductions default to a 60-80 second English script when the user
  explicitly requests English only.
- Topic playbooks, script templates, quality scorecards, and the idea
  generator now support the profile introduction route.
- High-risk facts still follow social-news and legally safe mode precedence.

## [1.6.0] - 2026-10-08

### Added

- Automatic `Celebrity explainer series` routing for celebrity, influencer,
  streamer, actor, singer, athlete, royal, creator, entertainment-person, and
  public-figure sources.
- A fixed six-beat series structure: question hook, answer axis, three
  contrast layers, receipts or qualifiers, judgment, and decision CTA.
- Motive-safe phrasing rules and subtype-specific CTA patterns.
- A fillable `assets/celebrity-explainer-card.md` episode card.

### Changed

- High-risk social-news, legal, death, abuse, health, and minor-related modes
  override celebrity series routing.
- Celebrity topic playbooks, script templates, viral review, and quality
  scorecards now reference the P1 series mode.
- The idea generator now recommends the auto route for celebrity, influencer,
  and entertainment niches.

## [1.5.0] - 2026-10-08

### Added

- P0 question-hook patterns for supported choice, decision, comparison,
  before-versus-after, expected-versus-actual, and status-gap topics.
- A contrast-matrix workflow that requires source or qualifier coverage for
  every material comparison.
- A mandatory answer-axis rule: the script must reveal the direction of the
  answer by 0:05 without overstating the evidence.
- New comparison guidance in the script template, topic-style card, viral
  review, and quality scorecards.
- The topic idea generator now emits P0 comparison-question seeds and
  answer-axis starters.

### Changed

- Viral-copy review now checks the hook, answer axis, contrast quality,
  language, pacing, fact risk, and CTA.
- Full script output now includes an `Answer axis` line under the hook.
- Updated validation coverage for the new P0 reference contract.

## [1.4.0] - 2026-10-02

### Added

- Default US commentary/explainer voice for all new scripts unless another
  format is explicitly requested.
- Personal-stance rules for opinions, reactions, humor, curiosity, and
  discussion-driven narration.
- News-to-commentary conversion rules that retain facts and legal limits.
- Controlled-exaggeration guidance that protects numbers, quotes, injuries,
  charges, and source certainty.
- Sensitive-topic exceptions for death, abuse, health, minors, and active
  legal cases.

### Changed

- Made commentary style the default even when the source material is a news
  article or headline.
- Updated release version and README feature coverage.

## [1.3.0] - 2026-10-02

### Added

- Topic-style playbooks for news, true crime, celebrity gossip, music,
  sports, film/TV, technology, business, health, fashion, food, viral stories,
  and political or high-sensitivity stories.
- Topic routing rules that select tone, hook style, pacing, evidence density,
  CTA, and visual language before drafting.
- Reusable topic-style card asset.

### Changed

- Established one controlling playbook per script, with optional tonal layers
  for crossover stories.
- Updated release version and README feature coverage.

## [1.2.0] - 2026-10-02

### Added

- Aggregated Word document deliverable rules.
- Required Chinese translation for storyboard headers and cell content.
- Required Caption, search keywords, hashtags, CTA, and risk sections in
  multi-script documents.
- Creator voice profile reference and fillable template.
- 100-point final quality review scorecard.
- Voice-specific rules for tone, banned phrasing, humor, CTA style, and
  topic-based tone changes.
- Critical-fail safeguards that override optimization scores.

### Changed

- Expanded the main workflow with creator voice and final quality review.
- Updated README feature coverage and release version.

## [1.1.0] - 2026-09-29

### Added

- Four-check diagnostic for hooks, spoken language, pacing, and engagement.
- S.T.O.R.M. editing structure and S.T.O.R.M. labels in the general script
  template.
- Viral-copy review reference with safe rewrite rules and topic-specific voice
  calibration.
- De-newsroom and de-Wikipedia rewrite guidance for natural US TikTok voice.
- Production and publishing workflow covering captions, discovery, sound-off
  readability, voiceover delivery, A/B testing, analytics, series design,
  corrections, moderation, disclosure, and rights.
- Primary-viewer and single-promise requirements.
- Hook-variant testing and share/save reasoning.
- Caption and search-text output fields.
- Delivery notes for pace, pronunciation, pauses, emphasis, and tone.
- Test and review plan fields in the general script template.

### Changed

- Expanded US audience guidance with TikTok-specific voice calibration by
  content type.
- Expanded the main workflow with production, publishing, and learning rules.
- Preserved strict fact, legal, privacy, minor-protection, and sensitive-content
  limits across viral optimization.

### Validation

- Skill frontmatter and references validated successfully.
