import json
import pathlib
import sys

import ollama

MODEL = "llama3.2"
DATA = pathlib.Path(__file__).with_name("schemes.json")
LOW = ("Below 1 lakh", "1-3 lakh")

# Eligibility rules. Schemes without a rule here are always included.
RULES = {
    "PM-KISAN": lambda f: f["occupation"] == "Farmer"
    or ("land" in f["extra"].lower() and "no land" not in f["extra"].lower()),
    "Ayushman Bharat PM-JAY": lambda f: f["income"] in LOW or f["age"] >= 70,
    "PM Ujjwala Yojana": lambda f: f["gender"] == "Female" and f["income"] in LOW,
    "Atal Pension Yojana": lambda f: 18 <= f["age"] <= 40 and f["income"] != "Above 8 lakh",
    "PM Awas Yojana": lambda f: f["income"] != "Above 8 lakh",
    "National Scholarship Portal": lambda f: f["occupation"] == "Student" and f["income"] != "Above 8 lakh",
}

SYSTEM = """You help people understand government schemes.
The schemes below already passed an eligibility check. For each one give: name,
one short line on why it may suit the user, the benefit, documents needed, and link.
Use ONLY facts from the JSON. Do NOT add income limits, age limits or conditions
that are not in the JSON. Reply in the same language the user writes in, in simple
words. End with: 'Please verify on the official site.'

SCHEMES:
{schemes}
"""


def find_schemes(profile, facts=None):
    schemes = json.loads(DATA.read_text(encoding="utf-8"))
    if facts:
        schemes = [s for s in schemes if RULES.get(s["name"], lambda f: True)(facts)]
    if not schemes:
        return "No matching schemes found in our list. Please visit your nearest CSC or government office."
    response = ollama.chat(
        model=MODEL,
        options={"temperature": 0},
        messages=[
            {"role": "system", "content": SYSTEM.format(schemes=json.dumps(schemes, ensure_ascii=False))},
            {"role": "user", "content": profile},
        ],
    )
    return response["message"]["content"]


if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) or input("Describe yourself: ")
    print("\n" + find_schemes(text))
