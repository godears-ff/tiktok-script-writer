# Commentary / 二创 Scripts (Film, TV, Sports, Mashups)

Commentary scripts for second-creation content built from existing footage:
movies, TV shows, variety shows, sports, and mashup clips. Targets TikTok
(US) and YouTube. Always deliver an English script and a complete Chinese
translation in the final response.

Use the 80-second format as the default. If the user requests a short version,
use 15-30 seconds. Other supported durations are 45, 60, and 90 seconds.

## Workflow

1. Collect the variable table below from the user. The more specific the
   info, the less template-like the script becomes.
2. Pick the prompt version that fits the primary delivery: the English main
   prompt for US delivery or the Chinese main prompt for CN delivery. The
   final response must still include both languages.
3. Generate a draft, then run the human rewrite checklist.
4. Run the pre-publish checklist before dubbing and editing.

## Variable Table

| Variable | What it asks | Example |
| --- | --- | --- |
| Topic | What this video is about | Why this movie's ending hurts |
| Source clips | Title and exact clip timestamps | Movie X, 1:02:00-1:02:20 staircase shot |
| Platform | TikTok / YouTube | TikTok |
| Duration | Video length | 45 seconds |
| Target audience | Who watches this | Horror fans who have seen the film |
| Key details to highlight | What matters most | Lighting, dialogue, music, facial expression |
| My take | The creator's real opinion | I think it's not revenge, it's a choice |
| My angle | Experience / job / taste | I edit videos, so I notice transitions |

## Main Prompt (Chinese)

```text
你是一名资深短视频内容编辑，专门为影视、综艺、体育二创写解说文案。
你的目标是写出像真人聊天一样自然、有明确个人观点、且不容易和别人类似的文案。

请根据我提供的信息，写一条【目标时长】的解说文案。

【素材信息】
- 选题：
- 素材来源和引用片段：
- 平台：
- 目标受众：
- 我最想讲的看点：
- 我的个人观点：
- 我的经历/职业/审美角度：

【硬性要求】
1. 口语化：短句为主，像真人说话，可以有停顿、语气词和反问，不要书面腔。
2. 前 3 秒必须有钩子：悬念、冲突、反常识、具体细节都行，禁止“今天给大家介绍”。
3. 结构固定：钩子 → 背景 → 冲突/看点 → 我的观点 → 结尾引导互动。
4. 观点必须具体：至少包含“我觉得 / 我印象最深的是 / 如果是我”式个人判断，禁止中立总结。
5. 去 AI 味：禁止“首先、其次、最后、总而言之、值得注意的是、在这个快节奏的时代、电影教会我们、绝绝子、YYDS、天花板、不容错过、众所周知”等套话。
6. 去重：不要逐句复述画面或原片台词，不要写成素材简介；引用片段只作为论据，解说词要有自己的解读角度。
7. 差异化：给我 2~3 个不同切入角度，每个角度用一句话说明和常见解说的区别。
8. 输出分镜脚本：时间轴 | 画面提示 | 解说词 | 字幕 | BGM/音效。
9. 字幕文案必须是你重写的，不能和源片字幕相同。
10. 结尾附“发布前检查清单”：短引用、版权与平台政策、原声占比、字幕重写、观点强度、AI 标识。

如果信息不全，按合理假设输出，并在开头列出你做了哪些假设。
```

## Short Prompt (Chinese, 15-30s)

```text
用上面同样的素材信息，写一条 20 秒的短解说。

要求：
1. 前 3 秒直接抛结论或冲突，不许铺垫。
2. 总字数控制在 80~130 字。
3. 只用一句讲背景，重点讲观点。
4. 结尾必须是互动句，引导评论或收藏。
5. 保持口语化，保留一个只有我会说的细节。
```

## Main Prompt (English, US Audience)

```text
You are a senior short-form video writer who creates commentary scripts for TikTok (US) and YouTube.
Write like a real American creator talking to a friend, not like an AI or a translated Chinese article.

Create a commentary script for [target duration] using this info:

[VIDEO INFO]
- Topic:
- Source material and clip timestamps:
- Platform: TikTok (US) / YouTube
- Target audience:
- What I want viewers to notice:
- My personal take:
- My background / niche perspective:

[REQUIREMENTS]
1. Sound like spoken American English: short sentences, contractions, natural pauses, rhetorical questions. No essay language.
2. The first 3 seconds must hook: conflict, suspense, a surprising detail, or a strong opinion. No "Today we're going to talk about".
3. Structure: Hook -> Context -> Conflict/Key detail -> My take -> Ending call to action.
4. Your opinion must be specific: use "I think", "what gets me is", "if it were me", or "the detail nobody noticed is". No neutral summary.
5. Kill AI phrasing: avoid "In today's fast-paced world", "delve", "moreover", "it's worth noting", "unleash", "elevate", "game-changer", "dive into", "ultimately", "crucial". Use plain conversational language.
6. Don't recite the clip or copy its subtitles: the clip is evidence; the script must add interpretation and commentary.
7. Offer 2-3 different angles and explain how each differs from typical videos on this topic.
8. Output a shot list: timestamp | on-screen visual | narration | on-screen text | music/SFX.
9. Rewrite any subtitle text; do not reuse the source's subtitles.
10. At the end, add a pre-publish checklist: short clips, rights and platform policy, original audio mix, rewritten text, strong opinion, and AI disclosure.

If information is missing, make reasonable assumptions and list them at the start.
```

## Short Prompt (English, 15-30s)

```text
Use the same info and write a 20-second Shorts commentary.

Requirements:
1. Open with the opinion or conflict in the first 3 seconds. No setup.
2. Keep it around 80-130 words.
3. One sentence of context, then straight to your take.
4. End with an interaction question that makes people comment or save.
5. Keep it conversational and include one detail only you would notice.
```

## Translation Rules

- Translate the final script, title, on-screen text, CTA, and checklist.
- Keep the same level of uncertainty and attribution as the source material.
- Use natural Chinese for entertainment commentary, but do not introduce slang
  that makes an opinion sound like a confirmed fact.
- Do not reuse the source video's subtitles in either language.

## Anti-AI Phrasing

### English

| Avoid | Replace with |
| --- | --- |
| In today's fast-paced world | delete it |
| delve | dig into / get into |
| moreover | plus / honestly |
| it's worth noting | the thing is |
| unleash | let it do its thing |
| elevate | step it up / make it better |
| game-changer | changes everything |
| dive into | get into |
| ultimately | at the end of the day |
| crucial | actually matters |

### Chinese

| 避免 | 建议替换 |
| --- | --- |
| 首先 / 其次 / 最后 | 直接说内容，不要序号感 |
| 值得注意的是 | 真正有意思的是 |
| 总而言之 / 总的来说 | 说白了 |
| 在这个快节奏的时代 | 删掉 |
| 电影 / 剧集教会我们 | 我个人觉得 |
| 视觉盛宴、扣人心弦 | 换成具体画面和声音描述 |
| 绝绝子、YYDS、天花板 | 不用，或换成你自己的说法 |
| 不容错过 | 你一定要看第 3 分钟 |
| 众所周知 | 删掉 |

## Making Opinions Specific

1. Take a side: "If it were me, I wouldn't do that."
2. Compare: "Unlike similar films, this one..."
3. Details: which prop, shot, or line stands out.
4. Hypothetical: what if it was remade, recast, or given another ending.
5. Empathy: what would you choose as the protagonist.
6. Expertise: judge through your own profession or experience.

## Human Rewrite Checklist

- [ ] Turn AI-sounding sentences into words you would actually say
- [ ] Add one detail or experience only you know
- [ ] Delete every generic phrase
- [ ] Keep at least one "I think / I feel"
- [ ] Read it aloud; fix anything that doesn't flow

## Rights and Platform Check

- Do not state or imply that a clip automatically qualifies as fair use.
- Keep excerpts short and subordinate to the creator's commentary,
  transformation, and criticism.
- Assess whether the footage, music, logos, or broadcast audio may trigger
  platform copyright or content claims.
- Use licensed, platform-approved, or original audio whenever possible.
- Credit the source when useful, but do not treat attribution as a substitute
  for rights clearance.
- Remove clips when the user lacks a reasonable right or platform basis to use
  them.

## Pre-Publish Checklist

- [ ] Rights and platform policy reviewed; no fair-use guarantee implied
- [ ] AI-generated or materially altered realistic media is labeled when
  required by the platform
- [ ] Script text does not duplicate the source's subtitles
- [ ] Each version uses a different angle; no batch reuse of one template
- [ ] Clips are short, narrated, and serve as evidence for an opinion
- [ ] Title, cover, and script are not copied from the source
- [ ] English and Chinese preserve the same claims, uncertainty, and CTA
