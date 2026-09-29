# TikTok Script Writer

![Validate Skill](https://github.com/godears-ff/tiktok-script-writer/actions/workflows/validate.yml/badge.svg)

An agent skill for writing US-audience TikTok and short-form video scripts in
English with a complete Chinese translation.

Current release: **v1.1.0**

## Features

- General TikTok scripts with hooks, scripts, storyboards, titles, covers,
  CTAs, and image-generation prompts.
- English-first output with a complete Chinese translation below each
  deliverable.
- Commentary workflows for film, TV, sports, and mashup 二创 content.
- Fact-grounded social-news and true-crime workflows with fact ledgers,
  sourcing, legal-language checks, and sensitive-content rules.
- Viral-copy review using the four-check diagnostic and S.T.O.R.M. structure.
- De-newsroom and de-Wikipedia rewriting for natural US TikTok voice.
- Topic-specific tone calibration for news, entertainment, sports, technology,
  film, music, health, and minor-related content.
- Primary-viewer positioning, single-promise structure, testable hooks, and
  share/save reasoning.
- Production guidance for captions, search terms, sound-off readability,
  voiceover delivery, A/B testing, analytics review, and recurring series.
- Correction, community-moderation, sponsorship, rights, and disclosure
  workflows.
- Freshness gates that prevent stale trends, slang, statistics, and
  time-sensitive claims from being presented as current.
- Rights, platform-policy, AI-disclosure, and pre-publish checks.

## Compatibility

This repository follows the agent skills format and works with Codex skill
loading. Compatible environments should read `SKILL.md` and load supporting
files from `references/`, `assets/`, and `scripts/` as needed.

## Install

### Codex user skills

Clone the repository into your user skills directory:

```powershell
git clone https://github.com/godears-ff/tiktok-script-writer.git "$HOME\.agents\skills\tiktok-script-writer"
```

If you use an environment that loads skills from `~/.codex/skills`, clone or
copy the repository there instead:

```powershell
git clone https://github.com/godears-ff/tiktok-script-writer.git "$HOME\.codex\skills\tiktok-script-writer"
```

Restart Codex if the skill does not appear automatically.

### Manual install

1. Download the repository ZIP or the latest GitHub Release.
2. Extract the `tiktok-script-writer` folder into your user skills directory.
3. Confirm that `SKILL.md` is directly inside the installed
   `tiktok-script-writer` folder.

## Usage

Explicitly invoke the skill:

```text
$tiktok-script-writer Write a TikTok script for a US audience about...
```

You can also ask naturally for a TikTok script, English short-form copy,
二创解说, or a sourced social-news script.

## Output Modes

- **General:** Full script package or compact Hook + Script response.
- **Commentary:** Film, TV, sports, or mashup commentary with rights checks.
- **Social news / true crime:** Fact ledger, `As of` date, sources, legal-stage
  checks, and complete bilingual output.

## Repository Structure

```text
tiktok-script-writer/
|-- .github/
|   `-- workflows/
|       `-- validate.yml
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- assets/
|-- references/
|-- scripts/
|   |-- generate-ideas.py
|   `-- validate_skill.py
|-- LICENSE
`-- README.md
```

## Versioning

Releases use Git tags and GitHub Releases. See the
[Releases](https://github.com/godears-ff/tiktok-script-writer/releases) page for
the latest version and [CHANGELOG.md](CHANGELOG.md) for release notes.

## Validation

Run the repository validation script:

```text
python scripts/validate_skill.py
```

GitHub Actions runs the same validation on pushes to `main` and pull requests.

## License

MIT License. See [LICENSE](LICENSE).
