# MediReport-Voice

## Project Overview  
MediReport-Voice is a desktop application that enables doctors to create medical prescriptions using voice commands. It converts spoken words into a formatted prescription PDF that can be shared digitally with patients via email or messaging platforms. This eliminates the risks of losing or damaging physical prescriptions and streamlines the doctor-patient communication process.

---

## Features  
- Voice-driven input for patient data and prescription dictation.  
- Editable prescription entries via voice or manual input.  
- Preview generated prescriptions before saving or sending.  
- Generates prescription PDFs from customizable templates.  
- Automatically sends prescriptions to patients via email or SMS/WhatsApp.

---

## Technologies Used  
- Python  
- Speech Recognition (PyAudio, SpeechRecognition)  
- OpenCV (Image Manipulation)  
- Pillow (Image to PDF conversion)  
- Tkinter (GUI)  
- SMTPlib (Email sending)  
- gTTS (Google Text-to-Speech for feedback)

---

### Screenshot
![Screenshot (30)](https://github.com/user-attachments/assets/c576b7ba-377c-4f8d-9ad5-db6dae723fa4)

#### Template and Voice Feature
![image](https://github.com/user-attachments/assets/d12619b0-5ad8-4563-9e93-6618967314ee)


## Getting Started

### Clone the repository  
```bash
git clone https://github.com/your-username/MediReport-Voice.git
cd MediReport-Voice
```

### Install dependencies

Make sure you have Python 3 installed. Then install required packages:
```bash
pip install -r requirements.txt
```

### Setup Templates
```
    Unzip the template.zip folder into the project directory.

    Replace the prescription.jpg file inside the template folder with your preferred prescription template image (recommended size: 600x849 pixels).

    Ensure the program references the correct template file.
```
### Run the Application
```bash  
python main.py
```
### Usage

    Use voice commands to input patient details and dictate prescriptions.

    Edit or delete entries as needed.

    Preview the prescription in the app before finalizing.

    The prescription PDF will be saved locally and sent automatically via email.
  
