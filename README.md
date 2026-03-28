# AI Smart Study Planner 📚

AI Smart Study Planner is a web application that generates a personalised study schedule using artificial intelligence.
The planner prioritises the hardest chapters first and organises a daily study plan leading up to the exam date.

The application is built with Python and Streamlit and uses the Groq API to generate intelligent study plans.

## Features

* Generates AI-powered study schedules
* Prioritises the hardest chapters first
* Supports timezone selection (IST or EST)
* Uses the current date and time to start the plan
* Simple and clean Streamlit interface
* Fast responses using Groq Llama models

## Tech Stack

* Python
* Streamlit
* Groq API
* Llama 3.1 AI model
* pytz for timezone handling

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/ai-study-planner.git
```

Navigate to the project folder:

```
cd ai-study-planner
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## Environment Variables

Set your Groq API key as an environment variable.

Windows:

```
setx GROQ_API_KEY "your_api_key_here"
```

Mac / Linux:

```
export GROQ_API_KEY="your_api_key_here"
```

## Running the App

Start the Streamlit application:

```
streamlit run new_app.py
```

The app will open in your browser automatically.

## How It Works

1. Enter your subjects and chapters.
2. Specify which chapters are the hardest.
3. Select your timezone.
4. Enter your exam date and study hours per day.
5. The AI generates a day-by-day study plan prioritising difficult topics first.

## Future Improvements

* Study progress tracker
* Download study plan as PDF
* Auto chapter difficulty detection
* User accounts and saved plans
* Improved UI design

## License

This project is open source and available for learning and educational purposes.
