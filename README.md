# Secure-Payroll-System
Python-based payroll application demonstrating Role-Based Access Control (RBAC) and SHA-256 password hashing.

# Secure Payroll & Authentication Lab
This repository contains a professional security demonstration of a **Python-based Payroll System**. It focuses on protecting sensitive employee data through modern cryptographic standards and access control.

---

### Core Security Features
* **Cryptographic Password Hashing:** Implements `SHA-256` hashing (via Python's `hashlib`) to ensure that even if the database is compromised, user credentials remain encrypted.
* **Role-Based Access Control (RBAC):** A logic-driven permission system that differentiates between **Admin** (Full Access) and **User** (View Only) roles.
* **Security Auditing (Brute-Force Simulation):** Includes a standalone script (`cracker.py`) that demonstrates a dictionary attack, used to validate the strength of the system's hashing implementation.
* **Containerization:** Fully Dockerized for secure, isolated deployment in a DevSecOps pipeline.

---

### Repository Structure
* `payroll_security.py`: The main application handling authentication and payroll logic.
* `cracker.py`: The security auditing tool used for vulnerability testing.
* `Dockerfile`: Configuration for building the secure container environment.
* `.gitignore`: Prevents sensitive local data (like `user_data.txt`) from being uploaded to the public cloud.

---

### Technical Skills Demonstrated
* **Python Programming** (Data Structures, File I/O, Logic)
* **Cybersecurity Fundamentals** (Hashing, RBAC)
* **DevOps Tools** (Docker, Git/GitHub)
* **Secure Coding Practices** (PII Protection, Data Minimization)
