from gtts import gTTS
from playsound import playsound
import os

# Skincare Chatbot - With Voice Output
print("🧴 Welcome to the Skincare Chatbot!")
print("I'm here to help you with skincare tips based on your skin type.\n")

# Data for chatbot
skincare_data = {
    "oily": {
        "acne": "Use products with salicylic acid or niacinamide. Avoid heavy moisturizers.Here 741 hz for regenerate skin tissue,help to fade acne marks",
        "glow": "Try exfoliation 2-3 times/week and use Vitamin C serum.Here 528 hz for “Cell repair,” “DNA harmonizing,” promotes healing & glow.",
        "dark spots": "Niacinamide and gentle chemical exfoliation (AHA/BHA) help reduce spots.Here 741 hz used to clear impurities."
    },
    "dry": {
        "flakiness": "Use a rich moisturizer with hyaluronic acid and ceramides.Here 285 hz for Regenerates damaged skin cells and promotes hydration retention",
        "glow": "Use facial oils (like rosehip) and stay hydrated. Avoid alcohol-based toners.Here 528 hz for “Cell repair,” “DNA harmonizing,” promotes healing & glow.",
        "redness": "Use calming ingredients like oat extract or aloe vera.Here 285 hz to Heals damaged tissues and calms redness."
    },
    "sensitive": {
        "irritation": "Use fragrance-free and alcohol-free products. Patch test always.Here 285 hz for Regenerates damaged skin tissues, supports skin repair.",
        "acne": "Use minimal ingredients like azelaic acid and gentle cleansers.Here 528 hz to Repairs skin at the cellular level, reduces inflammation and bacterial activity",
        "glow": "Stick to barrier-friendly ingredients like squalane and niacinamide.Here 528 hz for “Cell repair,” “DNA harmonizing,” promotes healing & glow."
    },
    "combination": {
        "acne": "Use a balanced routine - salicylic acid for T-zone, gentle cream for dry areas.Here 741 hz to Clears pores and helps prevent breakouts.",
        "glow": "Use gel moisturizers and Vitamin C serums sparingly.Here 528 hz to Boosts skin glow by supporting DNA repair and cellular energy.",
        "blackheads": "Try clay masks on oily areas and gentle scrubs.Here 741 hz to Clears pores and helps prevent breakouts."
    },
    "normal": {
        "maintenance": "Stick with a balanced routine: Cleanser + Moisturizer + Sunscreen.Here 528 hz to Rejuvenates skin at a DNA level.",
        "glow": "Use AHA serum once a week and Vitamin C in the morning.Here 528 hz to Restores natural glow and energy to the skin.",
        "hydration": "Gel or cream moisturizers work well. Avoid harsh exfoliants.Here 285 hz to Regenerates tissues, helps skin retain moisture"
    }
}

# Step 1: Choose skin type
skin_types = list(skincare_data.keys())
print("Please choose your skin type:")
for i, s in enumerate(skin_types, 1):
    print(f"{i}. {s.capitalize()}")

while True:
    try:
        skin_choice = int(input("Enter the number of your skin type: "))
        if 1 <= skin_choice <= len(skin_types):
            skin_type = skin_types[skin_choice - 1]
            break
        else:
            print("❌ Invalid input. Try again.")
    except ValueError:
        print("❌ Please enter a number.")

# Step 2: Choose concern
print(f"\nGreat! You selected: {skin_type.upper()} skin.")
concerns = list(skincare_data[skin_type].keys())
print("Now choose your skincare concern:")
for i, c in enumerate(concerns, 1):
    print(f"{i}. {c.capitalize()}")

while True:
    try:
        concern_choice = int(input("Enter the number of your concern: "))
        if 1 <= concern_choice <= len(concerns):
            concern = concerns[concern_choice - 1]
            break
        else:
            print("❌ Invalid input. Try again.")
    except ValueError:
        print("❌ Please enter a number.")

# Final Result
result = skincare_data[skin_type][concern]
print("\n💡 Skincare Tip for You:")
print(result)

# Step 3: Speak the Output using gTTS
tts = gTTS(result, lang='en')
tts.save("skincare_tip.mp3")
playsound("skincare_tip.mp3")

# Optional: Remove audio file after playing
# os.remove("skincare_tip.mp3")

# End
print("\n🧴 Thank you for using the Skincare Chatbot! Stay glowing! ✨")
