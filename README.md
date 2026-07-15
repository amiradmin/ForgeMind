# 🚀 ForgeMind

> **Enterprise Industrial AI Platform for Predictive Maintenance, Energy Monitoring, and CMMS**

ForgeMind is an open-source enterprise platform designed for heavy industries such as steel plants, mining, cement, power generation, and manufacturing.

The project combines Industrial IoT, Predictive Maintenance, Computerized Maintenance Management (CMMS), Energy Management, and Artificial Intelligence into a single modular platform.

This repository documents the complete engineering journey of building ForgeMind using professional software engineering practices, including GitHub Issues, Pull Requests, CI-ready architecture, Docker, and sprint-based development.

---

# 🌍 Vision

Modern industrial companies often use multiple disconnected systems for maintenance, energy monitoring, asset management, and production analytics.

ForgeMind aims to unify these capabilities into a single intelligent platform capable of:

* Predictive Maintenance (PdM)
* Energy Monitoring
* CMMS
* Asset Management
* AI-assisted Decision Support
* Digital Twin Integration
* Industrial Analytics

---

# ✨ Current Features

## Infrastructure

* Docker Development Environment
* PostgreSQL Database
* Redis
* Environment-based Configuration
* Modular Django Settings
* Health Check Endpoint

## Authentication

* Custom User Model
* JWT Authentication
* Login API
* Refresh Token API
* User Profile API

---

# 🏭 Planned Modules

* Organization Management
* Plant Management
* Production Areas
* Asset Registry
* CMMS
* Preventive Maintenance
* Work Orders
* Spare Parts Inventory
* Energy Monitoring
* Energy Forecasting
* Predictive Maintenance
* Remaining Useful Life (RUL)
* Failure Prediction
* AI Assistant
* Computer Vision
* Conveyor Monitoring
* Digital Twin
* Sustainability Dashboard

---

# 🏗 Architecture

```text
                 React Frontend
                        │
                        │ REST API
                        ▼
               Django REST Framework
                        │
     ┌──────────────────┼──────────────────┐
     │                  │                  │
     ▼                  ▼                  ▼
 Authentication      CMMS           Energy Module
     │                  │                  │
     └──────────────┬───┴──────────────────┘
                    ▼
              AI Services Layer
                    │
     ┌──────────────┼───────────────┐
     ▼              ▼               ▼
 Predictive     Computer Vision   Analytics
 Maintenance
                    │
                    ▼
               PostgreSQL
                    │
                 Redis/Celery
```

---

# 🛠 Technology Stack

## Backend

* Python 3.12
* Django 5
* Django REST Framework
* SimpleJWT

## Database

* PostgreSQL
* Redis

## Frontend

* React
* TypeScript (planned)

## AI

* PyTorch
* YOLOv8
* OpenCV
* Scikit-learn

## DevOps

* Docker
* Docker Compose
* GitHub
* Ruff
* Black
* isort

---

# 📂 Repository Structure

```
ForgeMind/

backend/
frontend/
services/
docs/
infrastructure/
scripts/

```

---

# 🚧 Current Development Status

| Sprint                             | Status         |
| ---------------------------------- | -------------- |
| Sprint 1 – Project Foundation      | ✅ Completed    |
| Sprint 2 – Docker & Infrastructure | ✅ Completed    |
| Sprint 3 – Authentication          | ✅ Completed    |
| Sprint 4 – Organization & Assets   | 🚧 In Progress |
| Sprint 5 – CMMS                    | ⏳ Planned      |
| Sprint 6 – Energy Monitoring       | ⏳ Planned      |
| Sprint 7 – AI Services             | ⏳ Planned      |

---

# 🎯 Project Goals

* Enterprise-grade architecture
* Production-ready backend
* Modular design
* Industrial scalability
* AI-first platform
* Cloud-ready deployment

---

# 🤝 Contributing

Contributions, suggestions, and discussions are welcome.

Please open an Issue before submitting large Pull Requests.

---

# 📜 License

This project is released under the MIT License.

---

# 👨‍💻 Author

**Amir Behvandi**

Software Engineer

Industrial AI • Django • Computer Vision • Predictive Maintenance

GitHub:
https://github.com/amiradmin

---

⭐ If you find this project interesting, consider giving it a Star.



Copyright 2026 Amir Behvandi

Licensed under the Apache License, Version 2.0