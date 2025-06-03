import streamlit as st
import random
from pymongo import MongoClient
from datetime import datetime

# --------------------------- CONFIG ---------------------------
st.set_page_config(page_title="Rock Paper Scissors Game 🎮", page_icon="🕹️")
st.title("🎮 Rock - Paper - Scissors Game")
st.markdown("Choose one to play against the computer!")

# --------------------------- MONGODB ---------------------------
MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB Atlas URI
client = MongoClient(MONGO_URI)
db = client["rps_game"]
leaderboard = db["scores"]

# --------------------------- RULES & EMOJIS ---------------------------
emojis = {
    "Rock": "✊",
    "Paper": "📄",
    "Scissors": "✂️"
}

rules = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

# --------------------------- SESSION STATE INIT ---------------------------
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

# --------------------------- FUNCTIONS ---------------------------
def play_sound(file_path):
    """Play an audio file (mp3 or wav) using Streamlit."""
    with open(file_path, "rb") as sound_file:
        sound_bytes = sound_file.read()
        fmt = "audio/wav"
        if file_path.lower().endswith(".mp3"):
            fmt = "audio/mp3"
        st.audio(sound_bytes, format=fmt)

def save_score(player_name, score):
    """Save player score in MongoDB leaderboard."""
    if player_name.strip() == "":
        return
    entry = {
        "name": player_name.strip(),
        "score": score,
        "timestamp": datetime.utcnow()
    }
    leaderboard.insert_one(entry)

def show_leaderboard():
    """Show top 5 scores from leaderboard."""
    st.subheader("🏆 Leaderboard (Top 5)")
    top_players = list(leaderboard.find().sort("score", -1).limit(5))
    if len(top_players) == 0:
        st.write("No scores yet. Be the first to play!")
    else:
        for idx, player in enumerate(top_players, start=1):
            st.write(f"{idx}. {player['name']} - {player['score']} points")

# --------------------------- UI ---------------------------
player_name = st.text_input("Enter your name:", value="Player")
user_choice = st.radio("Your Choice:", ["Rock", "Paper", "Scissors"], horizontal=True)

if st.button("Play"):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    st.write(f"🧍 You chose: **{user_choice}** {emojis[user_choice]}")
    st.write(f"💻 Computer chose: **{computer_choice}** {emojis[computer_choice]}")

    if user_choice == computer_choice:
        st.info("🤝 It's a tie!")
        play_sound("sounds/game-explosion-321700.mp3")  # Tie sound
    elif rules[user_choice] == computer_choice:
        st.success("✅ You win!")
        st.session_state.player_score += 1
        save_score(player_name, st.session_state.player_score)
        play_sound("sounds/win-176035.mp3")             # Win sound
    else:
        st.error("❌ You lose!")
        st.session_state.computer_score += 1
        play_sound("sounds/game-over-kid-voice-clip-352738.mp3")  # Lose sound

    # Show scoreboard
    st.subheader("📊 Scoreboard")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Your Score", st.session_state.player_score)
    with col2:
        st.metric("Computer Score", st.session_state.computer_score)

    # Show leaderboard
    show_leaderboard()

if st.button("🔄 Reset Scores"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.success("Scores reset successfully!")
