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

        quotes = {
            "Day 1": "🍥 'A lesson in chasing your dream: If you don't take risks, you can't create a future!' – Monkey D. Luffy",
            "Day 2": "🏴‍☠️ 'It’s not the face that makes someone a monster, it’s the choices they make with their lives.' – Naruto Uzumaki",
            "Day 3": "🔥 'Fear is not evil. It tells you what your weakness is, and once you know your weakness, you can become stronger as well as kinder.' – Gildarts (Fairy Tail)",
            "Day 4": "💡 'No matter how deep the night, it always turns to day.' – Brook (One Piece)",
            "Day 5": "🌟 'A lesson without pain is meaningless… That’s because you can’t gain something without sacrificing something in return.' – Edward Elric",
            "Day 6": "💪 'When you give up, your dreams and everything else, they’re gone.' – Naruto Uzumaki",
            "Day 7": "🎯 'A person becomes strong when they have someone they want to protect.' – Haku (Naruto)",
            "Day 8": "🌈 'When do you think people die? When they are forgotten.' – Dr. Hiriluk (One Piece)",
            "Day 9": "🔥 'To know sorrow is not terrifying. What is terrifying is to know you can’t go back to happiness you could have.' – Matsumoto Rangiku (Bleach)",
            "Day 10": "🌟 'Power comes in response to a need, not a desire. You have to create that need.' – Goku",
            "Day 11": "🚀 'You should enjoy the little detours. To the fullest. Because that’s where you’ll find the things more important than what you want.' – Ging Freecss",
            "Day 12": "💡 'A lesson without struggle teaches nothing. Embrace the challenge, and grow from it.' – Inspired by various anime",
            "Day 13": "🌱 'If you don’t take risks, you can’t create a future.' – Monkey D. Luffy",
            "Day 14": "🎉 'Hard work is worthless for those that don’t believe in themselves.' – Naruto Uzumaki",
            "Day 15": "🏆 'Inherited will, the swelling of the changing times, and the dreams of people… These are things that cannot be stopped.' – Gol D. Roger"
        }

        if day in quotes:
            st.info(quotes[day])

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