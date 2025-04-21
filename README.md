# 🎣 SoPhish v1.2 - Advanced Phishing Tool

**SoPhish** is a powerful and advanced phishing tool built with **Flask**, offering modern phishing capabilities combined with clean UI and automation. It allows you to generate phishing pages, track device info and geolocation, mask malicious URLs to make them look legitimate, and forward captured data instantly to a **Discord webhook**.

> ⚠️ This tool is intended for **educational and authorized testing purposes only**. Do not use it for illegal activities.

---

## 🚀 Features

- 🌐 **URL Masking** (with custom domains and phishing keywords)
- 📍 **Live Location Tracking** (via GPS API and IP fallback)
- 🧠 **Device Fingerprinting** (IP address, browser, OS, ISP)
- 📷 **Webcam Access & Snapshot Capture**
- 🛠️ **Serveo/Cloudflare Port Forwarding**
- 🔔 **Discord Webhook Integration** (instant alert and data forwarding)
- 🧩 **Modular Design** - Easy to add or customize templates

---

## 📸 Demo Screenshot

![image](https://github.com/user-attachments/assets/ce6a96ef-72b1-4792-947a-3885bb99be58)


---

## 🔧 Setup Instructions

### 📥 Clone the Repository

```bash
git clone https://github.com/letchupkt/sophish.git
cd sophish
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ⚙️ Configure Discord Webhook

Edit the `config.json` file and add your webhook URL:

```json
{
  "webhook_url": "https://discord.com/api/webhooks/your_webhook_here"
}
```

---

## 🧪 Usage

### ▶️ Run the Tool

```bash
python3 main.py
```

### 🔗 What You Can Do

- Choose between Cloudflare or Serveo for port forwarding
- Automatically mask phishing links using multiple shorteners
- Choose a phishing page template
- Share masked phishing URL with target
- Receive live updates on Discord when a target opens the link

---

## 📦 Output Example

Once the victim opens the phishing link:

- 🔍 IP Address, ISP, Country, OS, Browser info collected
- 🌍 Location coordinates retrieved (with fallback)
- 📷 Webcam snapshot (if allowed by the target)
- 📤 All data is logged and sent to your **Discord webhook**

---

## 🛠 Built With

- **Python 3**
- **Flask** – Backend Server
- **pyshorteners** – URL Shortening
- **JavaScript** – Webcam & device data
- **IPinfo / GPS APIs** – For geolocation

---

## ⚠️ Legal Disclaimer

This tool is created for **educational purposes only**. Use it only in environments where you have **explicit permission** (e.g., your own devices, test labs, or authorized engagements).

**The developer is not responsible for any misuse.**

---

## 📫 Contact

Built with ❤️ by **@letchu_pkt**

If you find this project useful, feel free to ⭐ star this repo and share it with fellow security enthusiasts!
