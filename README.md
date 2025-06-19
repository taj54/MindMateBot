# 🤖 MindMate Bot

**MindMate Bot** is a Telegram bot designed to support mental well-being through quick, private, and compassionate check-ins. It helps users reflect on their feelings, reduce stress, and access helpful resources.

---

## 🌟 Features

- **`/start`** – Welcomes the user and explains how to use the bot.  
- **`/checkin`** – A 3-step guided mental wellness check-in:
  1. Select your current mood using emojis.
  2. Share what's on your mind.
  3. Rate your stress level (scale 1–10).
- **`/tip`** – Get a random calming or self-care suggestion.
- **`/help`** – Access mental health resources and emergency helplines.
- **🛡 Privacy First** – No personal data is stored. Logs are anonymized and used only for bot improvement.

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python **3.10+**
- [Poetry](https://python-poetry.org/) for dependency management
- Telegram Bot Token from [BotFather](https://core.telegram.org/bots#botfather)

---

### 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone <repo-url>
   cd MindMateBot
   ```

2. **Install dependencies with Poetry:**

   ```bash
   poetry install
   ```

3. **Configure environment variables:**

   Copy `.env.example` to `.env`:

   ```bash
   cp .env.example .env
   ```

   Then, set your Telegram bot token in `.env`:

   ```env
   TELEGRAM_TOKEN=your-bot-token
   ```

4. **Run the bot:**

   ```bash
   poetry run python bot.py
   ```

   You should see: `🤖 Bot is running...`

---

## 📁 Project Structure

```
MindMateBot/
├── bot.py                   # Main bot entry point
├── handlers/                # Telegram command handlers
│   ├── checkin.py
│   ├── help.py
│   ├── messages.py
│   ├── start.py
│   └── tip.py
├── storage/
│   └── logs.json            # Anonymized logs (not personal data)
├── utils/                   # Utility modules
│   ├── constants.py
│   ├── logger.py
│   └── tips.py
├── .env                     # Environment config (not committed)
├── .env.example             # Sample environment config
├── pyproject.toml           # Poetry configuration
└── README.md                # Project documentation
```

---

## 💡 Usage

| Command      | Description                              |
|--------------|------------------------------------------|
| `/start`     | Start and get an introduction             |
| `/checkin`   | Begin the 3-step mood check-in            |
| `/tip`       | Get a calming self-care suggestion        |
| `/help`      | Access mental health resources            |

---

## 🔐 Privacy & Logging

- The bot **does not store any personal user data**.
- All interactions are anonymized.
- See `utils/logger.py` for logging implementation details.

---

## 🤝 Contributing

Contributions, suggestions, and pull requests are warmly welcomed!

---

## 📄 License

**MIT License** – Feel free to use and adapt.

---

## 👤 Author

**Taj**  
📧 [tajulislamj200@gmail.com](mailto:tajulislamj200@gmail.com)