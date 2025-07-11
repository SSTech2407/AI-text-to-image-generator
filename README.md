# 🖼️ AI Text-to-Image Generator  
A powerful AI tool that transforms text into images using the **Clipdrop API** and **Flask**. Users can enter imaginative prompts and generate high-quality visuals instantly.
---
# 📌 Features
- Clipdrop Stable Diffusion API integration
- Text prompt to image generation
- Modern dark UI with Tailwind CSS
- Download option for generated images
- Loading animations and smooth transitions
- Privacy, Terms, Content Policy & Feedback pages

---

# ⚙️ Technologies Used

- Python
- Flask
- Clipdrop API
- HTML5 + Tailwind CSS
- JavaScript

---

## 📁 Project Structure

text-to-image-generator/
├── app.py # Flask backend
├── .env # Contains Clipdrop API key
├── requirements.txt # Python dependencies
├── Procfile # For deployment on Render
├── static/
│ ├── style.css # Custom CSS & animations
│ └── image1.png... # Sample preview images
├── templates/
│ ├── index.html # Main image generation page
│ ├── privacy.html
│ ├── term.html
│ ├── feedback.html
│ └── content.html
└── README.md # Project details

---

## ✨ How It Works

The user provides a **creative text prompt**, which is sent to the **Clipdrop API** via Flask. The API returns an image URL based on the prompt, which is then displayed and available for download.

---

## 🔧 How to Run Locally

1. Clone this repository.
    git clone (https://github.com/SSTech2407/text-to-image-generator)
    cd text-to-image-generator
   
2. Create virtual environment.
   python -m venv venv
   venv\Scripts\activate  # Windows
   
3. Install dependencies.
   pip install -r requirements.txt

4. Add your .env file in the root with this content.
   CLIPDROP_API_KEY=your_clipdrop_api_key

5. Run the app.
   python app.py

6. Open in browser:
   http://127.0.0.1:5000
---
🧠 API Info
 - Provider: Clipdrop by Stability AI
 - Model: Stable Diffusion
 - API Key: Required (free tier available)
 - Endpoint: https://clipdrop-api.co/text-to-image/v1

📸 Example Output
Prompt: "Futuristic cyberpunk city at night with glowing lights and flying cars"
→ Generated Image:

🌍 Live Demo
🔗 Click here to try the app

🧑‍💻 Author
Developed by Sparsh Sharma
GitHub: SSTech2407

📅 Final Release
This is the final version of the project completed on 9 July 2025, with full Clipdrop integration, responsive UI, animations, and deployment-ready structure.






   

