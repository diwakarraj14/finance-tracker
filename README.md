# 💰 Personal Finance Tracker

A full-stack web application to manage daily income and expenses with secure user authentication and an interactive dashboard.

---

## 🌐 Live Demo

🔗 https://finance-tracker-1ros.onrender.com

---

## ✨ Features

* 🔐 User Signup & Login (Password Protected)
* 💰 Add Income & Expense Transactions
* 📊 Automatic Balance Calculation
* 📈 Pie Chart (Income vs Expense)
* 👤 User-wise Data (Each user sees their own data)
* ❌ Delete Transactions
* 📱 Responsive UI (Mobile Friendly)

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Deployment:** Render

---

## 📂 Project Structure

```id="ps1"
finance-tracker/
│
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── login.html
│   └── signup.html
├── static/
│   └── style.css
└── instance/
    └── finance.db
```

---

## ⚙️ Installation & Setup

```bash id="setup1"
git clone https://github.com/yourusername/finance-tracker.git
cd finance-tracker
pip install -r requirements.txt
python app.py
```

---

## 🧠 How It Works

1. User signs up and logs in
2. Session is created
3. User adds transactions (income/expense)
4. Data is stored in database
5. Dashboard displays:

   * Total Income
   * Total Expense
   * Balance
   * Chart visualization

---

## 🔐 Security

* Password hashing used
* Session-based authentication
* User-specific data filtering

---

## 📸 Screenshots

```id="ss1"
![Dashboard](screenshots/dashboard.png)
![Login](screenshots/login.png)
![Add](screenshots/add.png)
```

---

## 🚀 Future Improvements

* 📊 Advanced charts
* 🌙 Dark mode
* 📄 Export data (PDF/Excel)
* 👤 Profile management

---

## 👨‍💻 Author

**Diwakar Raj**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
