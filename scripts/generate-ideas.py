#!/usr/bin/env python3
"""
TikTok topic idea generator.
Generates 5 trending topic ideas plus P0 comparison-question seeds and
answer-axis starters for a given niche and US audience. Profile, resume, bio,
and CV inputs route to the person profile introduction mode.
"""
import json
import sys

NICHE_ANGLES = {
    "fitness": [
        "The exercise EVERYONE does wrong",
        "Why you're not seeing results (it's not your diet)",
        "The 30-second fix for [common problem]",
        "I tried [popular trend] for 30 days and here's what happened",
        "Stop [common mistake] if you want [goal]"
    ],
    "finance": [
        "How I made $X doing [simple thing]",
        "The habit keeping you broke",
        "Why [common advice] is actually terrible advice",
        "3 things wealthy people never tell you",
        "The math behind [popular financial product]"
    ],
    "dating": [
        "The [gender] truth nobody wants to admit",
        "3 red flags you're ignoring",
        "Why [popular dating advice] is ruining your love life",
        "The real reason you're still single",
        "POV: You're dating a [personality type]"
    ],
    "productivity": [
        "The one hack that actually works (and it's free)",
        "Why busy people get NOTHING done",
        "The 5-second rule that changed my life",
        "Stop doing these 3 things in the morning",
        "How I get 8 hours of work done in 2 hours"
    ],
    "food": [
        "The [dish] that chefs won't admit is this easy",
        "I perfected [popular recipe] and here's the secret",
        "Taste test: [popular item] vs homemade",
        "The ingredient that changes everything",
        "[Number] ways to make [cheap ingredient] taste expensive"
    ],
    "comedy": [
        "POV: You're the only one who [relatable situation]",
        "Nobody talks about how [common struggle]",
        "The most American thing happened to me today",
        "Things [group] say vs what they actually mean",
        "I tried to be [adjective] for 24 hours"
    ],
    "celebrity": [
        "Why did [celebrity] make this career decision?",
        "Everyone focused on the headline. The real shift is [X].",
        "What changed after [public turning point]?",
        "The deal looked standard until [new detail] changed the frame",
        "Why fans are split over [public decision]"
    ],
    "influencer": [
        "Why did [creator] change [platform / brand / format]?",
        "The real issue isn't the post. It's [business or audience stake].",
        "Was this an audience decision or a brand move?",
        "What changed after [creator] built this audience?",
        "The messy timeline behind [public creator decision]"
    ],
    "entertainment": [
        "Why did [star] choose [project or strategy] over [alternative]?",
        "The headline says [X]. The career logic says [Y].",
        "What does [career move] change for [star]?",
        "Was this image control, business strategy, or both?",
        "The real question isn't [rumor]. It's what the record can prove."
    ],
    "profile": [
        "The career throughline behind [person]",
        "How [person] built expertise in [field]",
        "From [early background] to [current position]",
        "Three turning points that shaped [person]'s work",
        "What [person] brings to [current mission]"
    ]
}

COMPARISON_QUESTIONS = {
    "fitness": [
        "Why does [approach A] work better than [approach B]?",
        "The real issue isn't [exercise]. It's [recovery / consistency / load].",
        "This looks like a diet problem. The evidence points to [other factor]."
    ],
    "finance": [
        "Why did [person or brand] choose [option A] over [option B]?",
        "The real issue isn't income. It's [cash flow / debt / risk].",
        "[Person or brand] didn't just [save / invest]. They chose [strategy]."
    ],
    "dating": [
        "Why do people choose [behavior A] over [behavior B]?",
        "The real issue isn't [surface trait]. It's [communication / trust / values].",
        "Was this [interpretation A], [interpretation B], or both?"
    ],
    "productivity": [
        "Why do busy people get less done than [comparison group]?",
        "The real issue isn't time. It's [attention / priority / system].",
        "This looks like a motivation problem. The evidence points to [other cause]."
    ],
    "food": [
        "Why does [food A] taste better than [food B]?",
        "The real issue isn't the ingredient. It's [technique / temperature / timing].",
        "This wasn't just [recipe A]. It was [method B]."
    ],
    "comedy": [
        "Which is worse: [relatable option A] or [relatable option B]?",
        "The real issue isn't [surface problem]. It's [shared relatable truth].",
        "Was this [behavior A], [behavior B], or both?"
    ],
    "celebrity": [
        "Why did [celebrity] choose [option A] over [option B]?",
        "The real issue isn't [headline]. It's [career / money / image / legal stake].",
        "Was this a personal decision, a strategic decision, or both?"
    ],
    "influencer": [
        "Why did [creator] choose [platform or brand move] over [alternative]?",
        "The real issue isn't [audience reaction]. It's [ownership / control / monetization].",
        "What evidence supports the business explanation rather than the drama explanation?"
    ],
    "entertainment": [
        "Why did [star] turn down or choose [project / deal / strategy]?",
        "The early story looked like [X]. The career record points to [Y].",
        "Was this a career move, an image reset, or both?"
    ],
    "profile": [
        "What single throughline connects [person]'s career?",
        "Which turning point best explains [person]'s current work?",
        "What makes [person]'s path distinct in [field]?"
    ]
}

ANSWER_AXIS_STARTERS = [
    "The real issue isn't [X]. It's [Y].",
    "This wasn't just [X]. It was [Y].",
    "The early story looks like [X]. The evidence points to [Y].",
    "The question isn't what people believe. It's what the record can prove.",
    "One side risks [cost A]. The other risks [cost B]."
]
PROFILE_POSITIONING_STARTERS = [
    "[Person] built a career around [central theme].",
    "From [foundation] to [current role], [person] has focused on [impact].",
    "[Person]'s work connects [background] with [current mission].",
    "What stands out in [person]'s path is [verified strength].",
    "[Person] brings [capability] to [field or mission]."
]
CELEBRITY_NICHES = {"celebrity", "influencer", "entertainment"}
PROFILE_ALIASES = {"profile", "bio", "resume", "cv"}
PROFILE_NICHES = {"profile"}

def main():
    raw_niche = sys.argv[1].lower() if len(sys.argv) > 1 else "general"
    niche = "profile" if raw_niche in PROFILE_ALIASES else raw_niche
    if niche in NICHE_ANGLES:
        ideas = NICHE_ANGLES[niche]
        comparison_questions = COMPARISON_QUESTIONS[niche]
    else:
        ideas = [
            f"The truth about {niche} nobody wants to hear",
            f"Why your {niche} approach is completely wrong",
            f"The {niche} hack that changed everything",
            f"Stop doing this if you care about {niche}",
            f"I tried [popular {niche} trend] so you don't have to"
        ]
        comparison_questions = [
            f"Why did [person or brand] choose [A] over [B] in {niche}?",
            f"The real issue in {niche} isn't [X]. It's [Y].",
            f"This looks like [expected {niche} explanation]. The evidence says [other factor]."
        ]
    output = {
        "niche": niche,
        "auto_mode": (
            "person-profile-introduction"
            if niche in PROFILE_NICHES
            else "celebrity-explainer-series"
            if niche in CELEBRITY_NICHES
            else "topic-default"
        ),
        "auto_route_reason": (
            "Resume, CV, bio, or structured person profile source."
            if niche in PROFILE_NICHES
            else "Celebrity, influencer, or entertainment-person source."
            if niche in CELEBRITY_NICHES
            else "No automatic celebrity-series trigger detected."
        ),
        "target_duration_seconds": "60-80" if niche in PROFILE_NICHES else None,
        "default_output_language": "English" if niche in PROFILE_NICHES else None,
        "ideas": ideas,
        "comparison_questions": comparison_questions,
        "answer_axis_starters": (
            PROFILE_POSITIONING_STARTERS
            if niche in PROFILE_NICHES
            else ANSWER_AXIS_STARTERS
        ),
        "p0_note": (
            "Verify every premise, source, and qualifier before turning a seed "
            "into a script. Placeholders are not claims."
        ),
        "p1_note": (
            "Higher-risk social-news, legal, death, abuse, health, minor, or "
            "user-requested modes override the celebrity auto route."
        ),
        "p2_note": (
            "Person profile introductions use a distinct factual, "
            "career-arc structure and must not reuse the celebrity explainer "
            "question-contrast-judgment format."
        )
    }
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
