import streamlit as st

st.title("📚 Streak and Reward Manager")

# initialize session state
if "valid_code" not in st.session_state:
    st.session_state.valid_code = False

num = st.text_input("Enter Latest code").strip().lower()

if st.button("Check"):
    rewards = {
        '1010': ("Day 1", 14),
        '1100': ("Day 2", 13),
        '1110': ("Day 3", 12),
        '20101': ("Day 4", 11),
        '10210': ("Day 5", 10),
        '10140': ("Day 6", 9),
        '13010': ("Day 7", 8),
        '10160': ("Day 8", 7),
        '10510': ("Day 9", 6),
        '10410': ("Day 10", 5),
        '10710': ("Day 11", 4),
        '1410': ("Day 12", 3),
        '10180': ("Day 13", 2),
       '10519': ("Day 14", 1),
        '1015550': ("Day 15", 0)
    }

    if num in rewards:
        day, days_left = rewards[num]
        st.success(f"{day} Completed, Well done ({days_left} more days to claim your 1st reward!)")

        # Progress bar with label and conditional styling
        progress = (15 - days_left) / 15
        # st.markdown(f"**Day {15 - days_left} of 15**")
        st.progress(progress, text=f"Progress: {15 - days_left} / 15 days")
        if progress < 0.5:
            st.warning(f"Keep going! You're {(progress*100):.0f}% done.")
        else:
            st.info(f"Great job! You're {(progress*100):.0f}% done.")
        # store valid code in session
        st.session_state.valid_code = (days_left == 0)
    else:
        st.error("❌ Sorry, the code is not valid")
        st.session_state.valid_code = False

# Show claim reward button if last code was valid
if st.session_state.valid_code:
    if st.button("🎁 Claim Reward"):
        st.success("send '🥳' this on whatsapp to know more abt Sarparaijj")
        st.session_state.valid_code = False  # reset after claiming