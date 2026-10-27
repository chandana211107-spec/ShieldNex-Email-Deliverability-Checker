# 🛡️ ShieldNex Email Deliverability Checker

> **A non-invasive web application that evaluates whether email addresses are likely to be deliverable using email-format validation and DNS MX record verification — without sending emails.**

---

## 🎯 Project Overview

**ShieldNex Email Deliverability Checker** is a Flask-based web application that allows users to check multiple email addresses at once.

The system performs two main checks:

**Email Format → Domain/MX Verification → Deliverability Classification**

It provides a clear status and reason for every email address.

### Results

- 🟢 **Likely to be delivered**
- 🔴 **Likely to bounce**
- 🟡 **Unknown**

---

## 🚨 Problem Statement

Applications and businesses often collect large numbers of email addresses, but some addresses may be incorrectly formatted or belong to domains that cannot receive email.

Sending test emails to verify every address is inefficient and may generate unnecessary bounces.

### Objective

Build a **non-invasive email validation system** that provides a preliminary deliverability assessment **without sending an email to the target address**.

---

## 👥 Target Users

The application is designed for:

- Developers building registration/contact systems
- Businesses performing basic email-list validation
- Data-quality teams
- Applications collecting user email addresses
- Students and developers learning DNS-based validation

---

# 💡 What I Built

I built a complete web application with a **Python/Flask backend** and a responsive **HTML/CSS/JavaScript frontend**.

### Core functionality

1. Accepts multiple email addresses.
2. Validates email syntax.
3. Extracts the email domain.
4. Performs a DNS MX-record lookup.
5. Applies rule-based classification.
6. Displays the result and reason.
7. Shows an overall result summary.

### Processing Flow

```text
User enters emails
        ↓
Format Validation
        ↓
Extract Domain
        ↓
DNS MX Lookup
        ↓
Rule-Based Analysis
        ↓
Status + Reason
```

---

# 🧠 Decision Logic

This project uses a **rule-based system**, not machine learning.

### Classification

| Check | Result |
|---|---|
| Invalid email format | 🔴 Likely to bounce |
| Valid format + no MX record | 🔴 Likely to bounce |
| Valid format + MX record found | 🟢 Likely to be delivered |
| Insufficient/uncertain information | 🟡 Unknown |

### Why MX Records?

An **MX (Mail Exchange) record** identifies mail servers associated with a domain.

For example:

```text
user@example.com
       ↓
    example.com
       ↓
   MX Record?
       ↓
Mail server information
```

This provides useful domain-level evidence without contacting the mailbox.

> **Important:** An MX record does not prove that a specific mailbox exists. Therefore, the application reports **"Likely"** rather than guaranteeing delivery.

---

# 🔍 Key Findings

### 1. Format validation quickly identifies obvious errors

Malformed addresses can be rejected before performing further checks.

### 2. MX verification provides useful domain-level evidence

A domain with an MX record has mail-server infrastructure configured for email reception.

### 3. Domain verification ≠ mailbox verification

An MX record cannot confirm that a particular mailbox exists.

### 4. Non-invasive validation is possible

Useful preliminary checks can be performed without sending emails.

### 5. Explainable results are important

Instead of returning only a status, the application provides a **reason** for each classification.

---

# 📊 Data Used

This project does **not require a machine-learning training dataset**.

It uses two sources of information:

### User Input

Email addresses entered by the user.

Example:

```text
user@gmail.com
hello@yahoo.com
invalid-email
test@nonexistentdomain.com
```

### DNS Information

The application performs an MX lookup on each email domain.

Therefore:

```text
Email Address
     ↓
Email Format
     ↓
Domain
     ↓
DNS MX Record
     ↓
Classification
```

---

# 🖥️ Application Features

### 📥 Bulk Email Input

Users can enter multiple email addresses, one per line.

### ⚡ Fast Batch Processing

All entered addresses are processed in one request.

### 📊 Result Dashboard

The interface provides counts for:

- 🟢 Likely Delivered
- 🔴 Likely Bounce
- 🟡 Unknown

### 📋 Detailed Results

Each result contains:

| Field | Description |
|---|---|
| Email | Address being checked |
| Status | Classification |
| Reason | Explanation for the classification |

### 🔐 Non-Invasive

The application does not send emails or require access to user mailboxes.

---

# 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Flask |
| DNS Verification | dnspython |
| Version Control | Git, GitHub |
| Deployment | Render |

---

# 📁 Project Structure

```text
ShieldNex-Email-Checker/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

# 🖼️ Screenshots

## Main Application

<img width="1898" height="870" alt="image" src="https://github.com/user-attachments/assets/60a5bb7b-dd47-4925-b348-ba70a8693109" />
<img width="1900" height="863" alt="image" src="https://github.com/user-attachments/assets/38db4862-2aa5-4c46-9751-db176591688b" />

## Results

Place your results screenshot in:
<img width="1897" height="867" alt="image" src="https://github.com/user-attachments/assets/4276dbdd-cb84-4660-a6cb-fda40878b52d" />
Email Verification Results:
<img width="1882" height="867" alt="image" src="https://github.com/user-attachments/assets/88cf0c23-4d49-40c9-aeea-f0b431c621b9" />

# ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/chandana211107-spec/ShieldNex-Email-Deliverability-Checker
```

### 2. Open the project

```bash
cd ShieldNex-Email-Deliverability-Checker
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```text
http://127.0.0.1:5000
```

---

# 🧪 Example

Input:

```text
user@gmail.com
hello@yahoo.com
invalid-email
test@nonexistentdomain123456.com
```

The application analyzes each address and returns:

```text
Email Address
Status
Reason
```

along with an overall summary.

---

# 🚀 Deployment

The application is designed for deployment using **Render**.

### Live Application

https://shieldnex-email-deliverability-checker.onrender.com


### GitHub Repository

https://github.com/chandana211107-spec/ShieldNex-Email-Deliverability-Checker

---

# 🔮 Future Enhancements

The current implementation focuses on format and MX-based validation.

Possible improvements:

- Disposable-email detection
- Role-based email detection
- Additional DNS checks
- Domain reputation analysis
- CSV bulk upload
- CSV result export
- Verification history
- Advanced analytics

---

# 🏆 Project Highlights

```text
✓ Full-stack web application
✓ Bulk email validation
✓ DNS MX record verification
✓ Rule-based decision engine
✓ Explainable results
✓ Responsive interface
✓ Non-invasive verification
✓ GitHub-ready project
✓ Cloud deployment ready
```

---

# 🎓 What I Learned

Through this project, I gained practical experience in:

- Python and Flask development
- Frontend-backend integration
- REST API development
- DNS and MX record handling
- Input validation
- Rule-based decision systems
- Error handling
- Git and GitHub
- Web application deployment

---

## ⚠️ Limitation

This application provides a **preliminary deliverability assessment**.

A valid MX record indicates that a domain has mail-server infrastructure, but it does **not guarantee that the specific mailbox exists or will accept an email**.

The results should therefore be interpreted as estimates rather than guaranteed delivery outcomes.

---

## 👩‍💻 Internship Project

**Built for the ShieldNex Software Development Internship Task.**

> **Validate smarter. Verify responsibly.**
