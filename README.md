# 🎮 Rock-Paper-Scissors Game with Streamlit

A fun and interactive Rock-Paper-Scissors game built using **Python** and **Streamlit**, complete with local sound effects and a leaderboard powered by **MongoDB**.

---

## 📝 How to Play
- Enter your name.

- Choose Rock, Paper, or Scissors.

- Click Play.

- Hear a sound based on the outcome!

- See your score and the leaderboard.

---

## ✨ Features

- ✅ Play Rock, Paper, or Scissors against the computer.
- 🔊 Outcome-based sound effects (Win, Tie, Game Over).
- 📊 Scoreboard that updates live.
- 🏆 Leaderboard (top 5 players) stored in MongoDB.
- 🧼 Reset option to clear your scores.

---

## ⚠️ Important Notes on Sound Playback

- This app uses `.mp3` audio files stored **locally in a `sounds/` folder**.
- Due to browser and Streamlit security restrictions:
  - **Sounds do not play automatically.**
  - Users must **click the "play" button** for the audio to be heard.
- This is a known limitation in Streamlit, as it does **not support autoplay for audio files**.

---

## 🎧 Sound Effects Used

| Game Outcome | File Name                             | Folder     |
|--------------|----------------------------------------|------------|
| Win          | `win-176035.mp3`                      | `/sounds`  |
| Tie          | `game-explosion-321700.mp3`           | `/sounds`  |
| Game Over    | `game-over-kid-voice-clip-352738.mp3` | `/sounds`  |

All sound files are in a folder named `sounds` within the project directory.

---

## 🛠️ Technologies Used

- **Streamlit** for UI and interactivity
- **Python** for game logic and backend
- **MongoDB** (local or Atlas) for storing leaderboard scores

---
Run using the command:-streamlit run Game.py


![image](https://github.com/user-attachments/assets/d8bd4e1b-4b87-4d13-856c-a39a1d8b9455)


![image](https://github.com/user-attachments/assets/01a789f9-79be-4b6f-96a2-9761cd31d39e)



