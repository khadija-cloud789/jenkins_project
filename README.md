Selenium Pytest CI/CD Pipeline:-

This repository contains a Python-based Selenium test framework integrated with Jenkins for Continuous Integration (CI).

Tech Stack:
*   **Language:** Python 3
*   **Testing:** Pytest, Selenium WebDriver
*   **CI/CD:** Jenkins
*   **Reporting:** Allure Reports

How to Run Locally:
1. Clone the repository:
   git clone https://github.com/khadija-cloud789/jenkins_project.git
2. Navigate to the directory:
   cd jenkins_project
3. Create and activate a virtual environment:
   python -m venv venv
   .\venv\Scripts\activate (Windows) OR source venv/bin/activate (Mac/Linux)
4. Install dependencies:
   pip install -r requirements.txt
5. Run the tests:
   pytest -v -s test_abd.py
