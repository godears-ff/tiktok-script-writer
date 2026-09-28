#!/usr/bin/env python3
"""
TikTok topic idea generator.
Generates 5 trending video topic ideas for a given niche and US audience.
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
    ]
}

def main():
    niche = sys.argv[1].lower() if len(sys.argv) > 1 else "general"
    if niche in NICHE_ANGLES:
        ideas = NICHE_ANGLES[niche]
    else:
        ideas = [
            f"The truth about {niche} nobody wants to hear",
            f"Why your {niche} approach is completely wrong",
            f"The {niche} hack that changed everything",
            f"Stop doing this if you care about {niche}",
            f"I tried [popular {niche} trend] so you don't have to"
        ]
    output = {"niche": niche, "ideas": ideas}
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
