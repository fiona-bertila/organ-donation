# 🚑 Optimized Organ Matching and Donation System (Beginner Version)

This is my **first Python project**, built as a beginner-friendly simulation of an organ matching and donation system. It uses a **weighted scoring algorithm** to find the best matches between donors and recipients and includes a basic **real-time notification system** to alert when a match is found.

> ⚠️ Note: This project is a standalone simulation. It is **not connected to any hospital systems**, but it is designed in a way that can be extended into a full-fledged application in the future.

---

## 🧠 Key Features

- ✅ **Weighted Scoring Algorithm** for optimal donor-recipient matching  
- ✅ **Real-Time Notifications** (via SMS or pop-up messages)  
- ✅ Prioritizes based on **blood type, HLA match, urgency level, and proximity**  
- ✅ Simple and modular Python code  
- ✅ Easily extendable for real-world applications

---

## 🎯 Objective

The goal of this project is to create a system that simulates how organ matching can be optimized using scoring logic and real-time updates. It serves as a proof-of-concept or a learning tool for developers, researchers, or students.

---

## 🧱 Project Structure

```

├── data/
│   ├── donors.csv
│   └── recipients.csv
├── organ\_matcher.py
├── notifier.py
├── utils.py
└── README.md

````

- `organ_matcher.py`: Main logic for matching using weighted scores  
- `notifier.py`: Simulated real-time notification system  
- `utils.py`: Helper functions for scoring, loading data, etc.  
- `data/`: Sample datasets for donors and recipients

---

## ⚙️ How It Works

1. The system reads sample donor and recipient data.
2. It calculates a **match score** for each donor-recipient pair based on:
   - Blood type match
   - HLA compatibility
   - Urgency level (medical need)
   - Geographical proximity
3. It selects the best match and sends a notification.

---

## 🖥️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/organ-matching-system.git
   cd organ-matching-system
````

2. Install dependencies (if any):

   ```bash
   pip install pandas twilio
   ```

3. Run the program:

   ```bash
   python organ_matcher.py
   ```

---

## 📊 Sample Output

```
Best Match Found: Recipient R004 matched with Donor D002
Match Score: 87.5%
Notification Sent: "You have a matching organ available!"
```

---

## 🚀 Future Enhancements

* Integrate with real-time hospital or transplant databases
* Add GUI for better visualization
* Use AI/ML to predict post-transplant outcomes
* Implement blockchain for secure and transparent data logging

---

## 🙋‍♂️ Contributing

Pull requests are welcome! If you'd like to improve or expand this system, feel free to fork the repo and submit a PR.

---


