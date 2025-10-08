import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Streak & Spark — 10-day Tracker", layout="wide")

st.title("✨ Streak & Spark — 10 Day Challenge")
st.markdown("_Enter the secret code for today's streak to unlock a micro-boost and move closer to your reward!_")

# --- session state ---
if "valid_code" not in st.session_state:
    st.session_state.valid_code = False
if "last_unlocked" not in st.session_state:
    st.session_state.last_unlocked = None

# --- input ---
num = st.text_input("Enter today's code", placeholder="e.g. X101").strip()

codes = {
    'X101': ("Day 1", 9),
    'A2B2': ("Day 2", 8),
    'C3D3': ("Day 3", 7),
    'D4E4': ("Day 4", 6),
    'E5F5': ("Day 5", 5),
    'F6G6': ("Day 6", 4),
    'G7H7': ("Day 7", 3),
    'H8I8': ("Day 8", 2),
    'I9J9': ("Day 9", 1),
    'J10K': ("Day 10", 0),
}

quotes = {
    "Day 1": "Starting is the hardest part — everyone notices the results, few remember the morning you showed up.",
    "Day 2": "Progress is messy. You’ll fail more times than you win; that’s the only path to getting better.",
    "Day 3": "Most people quit right before their breakthrough. Keep showing up when it hurts.",
    "Day 4": "Pain is honest — it points to what needs fixing. Don’t avoid it; learn from it.",
    "Day 5": "Halfway means you’ve invested enough to refuse giving up. Keep clearing the debt of effort.",
    "Day 6": "Comfort steals potential. Discomfort is the currency that buys a new life.",
    "Day 7": "Real work is lonely at times. Let the silence sharpen you, not stop you.",
    "Day 8": "No one owes you ease. Build what you want by choosing hard things and finishing them.",
    "Day 9": "Doubt gets loudest when success is closest. Move anyway — action drowns the noise.",
    "Day 10": "Finishing proves this truth: discipline outlasts feeling. Rewards follow those who endure."
}

# --- main logic ---
if st.button("Check Code"):
    if not num:
        st.error("Please enter a code first.")
    elif num in codes:
        day, days_left = codes[num]
        st.session_state.valid_code = (days_left == 0)
        st.session_state.last_unlocked = {"day": day, "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

        # header area
        left, right = st.columns([3,2])
        with left:
            st.success(f"{day} Completed — Well done! 🌟")
            st.write(quotes.get(day, "Nice work — keep the streak alive!"))
            # fun progress display
            progress_value = int((int(day.split()[-1]) / 10) * 100)
            st.progress(progress_value / 100.0, text=f"{progress_value}% — {day} of 10")

        with right:
            st.metric("Days left to reward", f"{days_left}")
            st.write("**Last Completed:**")
            st.write(f"{st.session_state.last_unlocked['time']}")

        # subtle encouragement
        if days_left > 5:
            st.info("Nice start — keep the rhythm going! 🔥")
        elif days_left > 1:
            st.info("Sweet — you're in the sprint now. Finish strong! 💪")
        elif days_left == 1:
            st.info("One more day to claim your reward — don't stop! 🏁")
        else:
            st.balloons()
            st.success("Amazing! You've completed 10 days — claim your reward below 🎁")

    else:
        st.error("❌ Invalid code. Double-check and try again.")
        st.session_state.valid_code = False

# show claim UI if reward is ready
st.divider()
if st.session_state.valid_code:
    st.markdown("### 🎉 Ready to claim your reward")
    if st.button("Claim Reward"):
        st.success("Claim received — send '🥳' on WhatsApp to confirm claim")
        st.balloons()
        st.session_state.valid_code = False
# else:
    # st.info("Tip: ")

# footer: show tracker overview
st.divider()
cols = st.columns(5)
for i, (code_key, (day_label, days_left)) in enumerate(codes.items()):
    idx = i % 5
    with cols[idx]:
        unlocked = (st.session_state.last_unlocked and st.session_state.last_unlocked['day'] == day_label)
        emoji = "✅" if unlocked else "◻️"
        st.write(f"{emoji} **{day_label}**")
        # st.caption(f"code: `{code_key}`")

# st.markdown("_Made with 🙊_")