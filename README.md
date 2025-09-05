# Typing Speed Test Web App

This is a simple web application built with Flask that allows users to test their typing speed and accuracy using randomly selected sentences or paragraphs.

## Features
- Choose between typing a single sentence or a full paragraph
- Real-time calculation of typing speed (WPM) and accuracy
- Stylish, retro-themed UI
- Results summary after each test

## How It Works
1. On the homepage, select either "Single Sentence" or "Paragraph".
2. Type the displayed text into the provided textarea.
3. Submit your typing to see your speed (words per minute), accuracy, and time taken.

## Project Structure
```
├── test1.py              # Main Flask application
├── static/
│   └── style.css         # Custom CSS for UI styling
├── templates/
│   └── index.html        # Main HTML template
```

## Getting Started
### Prerequisites
- Python 3.x
- Flask

### Installation
1. Clone or download this repository.
2. Install Flask:
   ```powershell
   pip install flask
   ```
3. Run the app:
   ```powershell
   python test1.py
   ```
4. Open your browser and go to `http://127.0.0.1:5000/`

## Customization
- You can add more sentences or paragraphs in `test1.py`.
- Modify `style.css` for different themes.

## License
This project is open source and free to use for educational purposes.
