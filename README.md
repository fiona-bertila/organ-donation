# 🚑 Optimized Organ Matching and Donation System (Beginner Version)

This is my first Python project, built as a beginner-friendly simulation of an organ matching and donation system. It uses a weighted scoring algorithm to find the best matches between donors and recipients and includes a basic real-time notification system to alert when a match is found.

> ⚠️ Note: This project is a standalone simulation. It is not connected to any hospital systems, but it is designed in a way that can be extended into a full-fledged application in the future.

---

# 🧠 Key Features

- ✅ Weighted Scoring Algorithm for optimal donor-recipient matching
- ✅ Real-Time Notifications (via SMS or pop-up messages)
- ✅ Prioritizes based on:
  - Blood type compatibility
  - HLA match
  - Urgency level
  - Geographical proximity
- ✅ Simple and modular Python code
- ✅ Easily extendable for real-world applications

---

# 🎯 Objective

The goal of this project is to create a system that simulates how organ matching can be optimized using scoring logic and real-time updates. It serves as a proof-of-concept or a learning tool for developers, researchers, or students.

---

# 🧱 Project Structure

```bash
organ-matching-system/
│
├── data/
│   ├── donors.csv
│   └── recipients.csv
│
├── organ_matcher.py
├── notifier.py
├── utils.py
└── README.md
