📝 Extractive Text Summarization (NLP + Django)
This project is an Extractive Text Summarizer that condenses long text into a concise summary by selecting the most important sentences — built using Python, Django, and pure CSS.

## 🌐 Live Demo

🔗 [Check it out here](https://django-text-summarizer-production.up.railway.app/)

🚀 Features
Automatically summarizes large text inputs

Clean and responsive UI using vanilla CSS

Built-in Django form to process and display summaries

Deployed and publicly accessible

🛠 Tech Stack
Python 3

Django (for backend + frontend rendering)

NLTK (for NLP processing)

HTML + CSS (for UI styling)

Railway (for deployment)

📦 Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python manage.py migrate
python manage.py runserver
Then go to http://127.0.0.1:8000 in your browser.

🧠 How It Works
Text Preprocessing:

Tokenizes the input into words and sentences

Filters out stopwords and punctuation

Sentence Scoring:

Scores each sentence based on word frequency

Summary Generation:

Picks top-scoring sentences to form the final summary

📁 Project Structure
summarizer/
├── summarizer/             # Django app with views, templates
│   ├── templates/
│   ├── static/             # Custom CSS styles
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
✨ Example
Input:

Artificial Intelligence (AI) is transforming industries with applications like image recognition, voice assistants, and more. It uses algorithms and massive data to replicate human-like thinking and decision-making...

Summary Output:

Artificial Intelligence (AI) is transforming industries with applications like image recognition, voice assistants, and more.

✅ Future Ideas
Upload .txt or .pdf for summarization

Add summary length control

Add abstractive summarization (e.g., using BERT or T5)


🙋‍♂️ Author
Samarth Shetty
🎓 Final Year CSE (Data Science)
🔗 [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samarthshetty1/)


