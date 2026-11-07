# 🎯 Nitro Finder

> ⚡ A brute-force Discord Nitro link finder — automatically generates and checks gift links at scale.

---

## ⚠️ Disclaimer

> This project is for **educational purposes only**. Use responsibly and at your own risk.

---

## 🚀 Getting Started

### Step 1 — Fork this Repo

Click the **Fork** button at the top-right of this page to copy the repo to your GitHub account.

```
👆 Fork → Your GitHub → Done
```

---

### Step 2 — Open Railway

Go to 👉 [railway.app](https://railway.app) and **log in with GitHub**.

```
🔗 railway.app → Login → Continue with GitHub
```

---

### Step 3 — Create a New Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose your **forked repo** from the list
4. Railway will automatically detect and deploy it 🎉

---

### Step 4 — Set Environment Variables *(if needed)*

In your Railway project dashboard:

```
⚙️ Variables → Add any required env vars here
```

---

### Step 5 — Deploy & Watch It Run 🔥

Railway will build and launch Nitro Finder automatically.

```
✅ Build → ✅ Deploy → 🚀 Running
```

---

## 🛠️ How It Works

```
🎲 Generate random gift code
     ↓
🌐 Check discord.com/gifts/{code}
     ↓
✅ Valid? → Log it!
❌ Invalid? → Try again
```

Nitro Finder brute-forces Discord gift link URLs by generating random alphanumeric strings and checking if they resolve to a valid Nitro gift. It runs continuously on Railway's free-tier infrastructure.

---

## 📦 Stack

| Tool | Purpose |
|------|---------|
| 🚂 Railway | Cloud hosting & deployment |
| 🐍 Python / Node | Core runtime |
| 🌐 HTTP requests | Link checking |
| 🎰 Random generator | Code generation |

---

## 🌟 Features

- 🔄 Continuous brute-force loop
- 📋 Logs valid codes when found
- ☁️ Runs 24/7 on Railway for free
- ⚡ Fast async HTTP requests
- 🛡️ No local setup required

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue or submit a PR.

1. 🍴 Fork the repo
2. 🌿 Create a new branch (`git checkout -b feature/my-feature`)
3. 💾 Commit your changes (`git commit -m 'Add my feature'`)
4. 📤 Push to the branch (`git push origin feature/my-feature`)
5. 🔁 Open a Pull Request

---

## ⭐ Show Some Love

If this project helped you, **leave a star** ⭐ — it means a lot!

---

> Made with ❤️ and ☕ — happy hunting 🎯
