# Secure-Payroll-System

A Python-based payroll application demonstrating secure authentication, Role-Based Access Control, and DevSecOps practices. Includes a self-directed security audit with five findings documented against NIST 800-63B standards.

---

### Core Security Features

* **Cryptographic Password Hashing:** Implements `bcrypt` with salting to protect stored credentials against brute force and rainbow table attacks. Upgraded from SHA-256 after demonstrating its vulnerability using John the Ripper.
* **Role-Based Access Control (RBAC):** A logic-driven permission system that differentiates between **Admin** (Full Access) and **User** (View Only) roles.
* **Security Audit:** A self-directed audit identifying five findings including account lockout policy, MFA, and password complexity recommendations, all aligned to NIST 800-63B. See `SECURITY_AUDIT.md`.
* **Containerization:** Dockerized with a non-root user configuration to reduce container attack surface, demonstrating secure DevSecOps practices.

---

### Repository Structure

* `payroll_security.py`: Main application handling authentication and payroll logic.
* `Dockerfile`: Secure container configuration running as non-root user.
* `SECURITY_AUDIT.md`: Full security audit with findings, evidence, and NIST-aligned recommendations.
* `.gitignore`: Prevents sensitive local data from being uploaded to the public repository.
* `audit_evidence/`: Screenshots and evidence supporting security audit findings.
* `LICENSE`: MIT License.

---

### Technical Skills Demonstrated

* **Python Programming** (Data Structures, File I/O, Authentication Logic)
* **Cybersecurity** (Password Hashing, Salting, RBAC, Vulnerability Assessment)
* **Security Auditing** (NIST 800-63B, John the Ripper, Findings Documentation)
* **DevSecOps** (Docker, Non-Root Container Configuration, Git/GitHub)
* **Secure Coding Practices** (PII Protection, Least Privilege, Defense in Depth)