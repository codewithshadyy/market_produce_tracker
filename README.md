# 🌾 AgriPrice – Farm Produce Price Tracker API

AgriPrice is a RESTful API built with Django REST Framework (DRF) that enables farmers, administrators, and consumers to track and manage farm produce prices across different markets.

The system promotes transparency in agricultural markets and enforces secure role-based access control using JWT authentication.

---

## 🚀 Features Implemented

### 🔐 Authentication System (JWT-Based)

- User Registration
- Login (Access & Refresh Tokens)
- Token Refresh
- Logout (Refresh Token Blacklisting)
- Password Reset (Email-based)
- Role-Based Authorization (ADMIN, FARMER, CONSUMER)

Authentication is implemented using:

- Django REST Framework
- SimpleJWT

---

### 👤 Custom User Model

The system uses a custom user model extending `AbstractUser`.

**User Fields:**

- id
- username
- email (unique)
- password (hashed securely)
- role (ADMIN, FARMER, CONSUMER)
- is_verified
- date_joined

Authentication is email-based.

---

### 🏪 Market Management

Markets are managed strictly by ADMIN users.

**Market Fields:**

- id
- name
- location
- created_by (ForeignKey to User)
- created_at
- updated_at

**Permissions:**

| Role      | View | Create | Update | Delete |
|-----------|------|--------|--------|--------|
| ADMIN     | ✅   | ✅     | ✅     | ✅     |
| FARMER    | ✅   | ❌     | ❌     | ❌     |
| CONSUMER  | ✅   | ❌     | ❌     | ❌     |

---

### 🌽 Produce Management

Farmers and Admins can manage produce prices.

**Produce Fields:**

- id
- name
- market (ForeignKey to Market)
- price
- farmer (ForeignKey to User)
- description
- quantity_available
- date_added
- updated_at

**Permissions:**

| Role      | View | Add | Update | Delete |
|-----------|------|-----|--------|--------|
| ADMIN     | ✅   | ✅  | ✅     | ✅     |
| FARMER    | ✅   | ✅ (own only) | ✅ (own only) | ✅ (own only) |
| CONSUMER  | ✅   | ❌  | ❌     | ❌     |

Object-level permissions ensure farmers can only modify their own produce records.



---
### 🚨 Real-time Alerts
-  `alerts` app
- Alerts app has `PriceAlert` model
- Integrated Django signals to detect price updates
- Automatically evaluates:
  - Threshold-based alerts
  - General price increase/decrease subscriptions
- Sends email notifications to buyers




###  Analytics Endpoint

### 📊 Returns
- Average price
- Highest price
- Lowest price
- Total produce count

```
GET /api/produce/analytics/
```

### 🎯 Objective
Provide aggregated insights into produce pricing data.


### 🔎 Filtering, Search & Ordering

Produce endpoints support:

- Filter by market
- Filter by farmer
- Search by produce name
- Order by price
- Order by date_added

Implemented using:

- DjangoFilterBackend
- SearchFilter
- OrderingFilter

---

## 📡 API Endpoints

### 🔐 Authentication

```
POST   /api/auth/register/
POST   /api/auth/login/
POST   /api/auth/refresh/
POST   /api/auth/logout/
POST   /api/auth/password-reset/
POST   /api/auth/password-reset-confirm/<uid>/<token>/
```

---

### 🏪 Markets

```
GET    /api/markets/
POST   /api/markets/
GET    /api/markets/{id}/
PUT    /api/markets/{id}/
DELETE /api/markets/{id}/


```
### 🚨 Alerts
```
GET    /api/alerts/
POST   /api/alerts/
GET   /api/alerts/{id}/
PUT  /api/alerts/{id}/
DELETE /api/alerts/{id}/




```

---

### 🌽 Produce

```
GET    /api/produce/
POST   /api/produce/
GET    /api/produce/{id}/
PUT    /api/produce/{id}/
DELETE /api/produce/{id}/
```

Filtering :

```
/api/produce/?market=1
/api/produce/?farmer=3
/api/produce/?search=maize
/api/produce/?ordering=price
```

---





---





## 🛠 Tech Stack

- Python 3.12
- Django 6
- Django REST Framework
- SimpleJWT
- SQLite (Development)
- Console Email Backend (Development)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
cd market_produce_tracker
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Linux / Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run Development Server

```bash
python manage.py runserver
```

---

## 🔒 Security Features

- JWT Authentication
- Refresh Token Rotation
- Token Blacklisting
- Role-Based Permissions
- Object-Level Access Control
- Secure Password Reset Tokens
- Email Enumeration Protection

---

## 📂 Project Structure

```
market_produce_tracker/
│
├── users/
├── markets/
├── produces/
├── alerts/
├── manage.py
└── README.md
```

---

## 🧪 Development Email Configuration

During development, emails are printed to the console:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

This allows testing password reset functionality without SMTP configuration.

##  🧪 Production Email Configuration
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```

This allows:

✅ Clients to receive real-time email alerts

✅ Farmers to receive product-related notifications

✅ Threshold price change alerts



