import speech_recognition as sr
import os
import time
from datetime import datetime
import pyautogui
import webbrowser
import subprocess
from gtts import gTTS      
import pygame              


pygame.mixer.init()

def speak(text):
    print(f"Jarvis: {text}")
    try:
        
        if pygame.mixer.music.get_busy(): 
            pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        
       
        tts = gTTS(text=text, lang='ta') 
        audio_file = "jarvis_voice.mp3"
        tts.save(audio_file)
        
        
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        
        
        while pygame.mixer.music.get_busy(): 
            time.sleep(0.1)
            
        
        pygame.mixer.music.unload()
        if os.path.exists(audio_file):
            os.remove(audio_file)
            
    except Exception as e:
        print(f"Voice Error: {e}")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5) 
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='ta-IN')
        print(f"User said: {query}\n")
    except: return "None"
    return query.lower()

def close_app(app_name):
    speak(f"சரிங்க சார், {app_name} ஆப்பை மூடுகிறேன்.")
    apps = {
        "whatsapp": "WhatsApp*", "chrome": "chrome.exe", "notepad": "notepad.exe",
        "calc": "CalculatorApp.exe", "store": "WinStore.App.exe", "camera": "WindowsCamera.exe",
        "settings": "SystemSettings.exe", "excel": "excel.exe", "word": "winword.exe", "explorer": "explorer.exe"
    }
    target = apps.get(app_name.lower())
    if target:
        os.system(f"taskkill /f /im {target}")

def jarvis_backend():
    
    speak("வணக்கம் சார்! ஜார்விஸ் அட்வான்ஸ்டு கோர் சிஸ்டம் தயாராக உள்ளது. சொல்லுங்க சினேக் சார், நான் உங்களுக்கு என்ன செய்ய வேண்டும்?")
    
    while True:
        query = take_command()
        if query == "none": continue

       
        if 'உруவாக்கு' in query or 'யார் நீ' in query or 'who created you' in query or 'உருவாக்கினது' in query:
            speak("என்னை உருவாக்கினது சினேக் சார்!")
            continue
        elif 'சினேக்னா யாரு' in query or 'sinek' in query or 'ஸ்நேக்' in query or 'எஸ் ஐ என் இ கே' in query or 'மேக்னா யாரு' in query:
            speak("அவருதான் என்னோட பாஸ்!")
            continue

        
        elif 'open' in query or 'ஓபன்' in query or 'ஓப்பன்' in query:
            if 'யூடியூப்' in query or 'youtube' in query:
                speak("யூடியூப் ஓபன் செய்கிறேன் சார்.")
                webbrowser.open("https://www.youtube.com")
            elif 'குரோம்' in query or 'chrome' in query:
                speak("கூகுள் குரோம் ஓபன் செய்கிறேன் சார்.")
                os.startfile("chrome.exe")
            elif 'நோட்பேட்' in query or 'notepad' in query:
                speak("நோட்பேட் ஓபன் செய்கிறேன் சார்.")
                subprocess.Popen("notepad.exe")
            elif 'கால்குலேட்டர்' in query or 'calc' in query:
                speak("கால்குலேட்டர் ஓபன் செய்கிறேன் சார்.")
                subprocess.Popen("calc.exe")
            elif 'வாட்ஸ்அப்' in query or 'whatsapp' in query:
                speak("வாட்ஸ்அப் ஓபன் செய்கிறேன் சார்.")
                os.system("start whatsapp:")
            elif 'எக்ஸ்ப்ளோரர்' in query or 'explorer' in query or 'ஃபைல்' in query:
                speak("ஃபைல் எக்ஸ்ப்ளோரர் ஓபன் செய்கிறேன் சார்.")
                os.system("start explorer")
            elif 'ஸ்டோர்' in query or 'store' in query:
                speak("மைக்ரோசாஃப்ட் ஸ்டோர் ஓபன் செய்கிறேன் சார்.")
                os.system("start ms-windows-store:")
            elif 'கேமரா' in query or 'camera' in query:
                speak("கேமரா ஓபன் செய்கிறேன் சார்.")
                os.system("start microsoft.windows.camera:")
            elif 'செட்டிங்' in query or 'setting' in query:
                speak("சிஸ்டம் செட்டிங்ஸ் ஓபன் செய்கிறேன் சார்.")
                os.system("start ms-settings:")
            elif 'எக்செல்' in query or 'excel' in query:
                speak("எம் எஸ் எக்செல் ஓபன் செய்கிறேன் சார்.")
                os.system("start excel")
            elif 'வேர்ட்' in query or 'word' in query:
                speak("எம் எஸ் வேர்ட் ஓபன் செய்கிறேன் சார்.")
                os.system("start winword")
            continue

        
        elif 'மூடு' in query or 'க்ளோஸ்' in query or 'close' in query:
            if 'நோட்பேட்' in query: close_app("notepad")
            elif 'வாட்ஸ்அப்' in query: close_app("whatsapp")
            elif 'குரோம்' in query: close_app("chrome")
            elif 'கால்குலேட்டர்' in query: close_app("calc")
            elif 'ஸ்டோர்' in query: close_app("store")
            elif 'கேமரா' in query: close_app("camera")
            elif 'செட்டிங்' in query: close_app("settings")
            elif 'எக்செல்' in query: close_app("excel")
            elif 'வேர்ட்' in query: close_app("word")
            elif 'எக்ஸ்ப்ளோரர்' in query: close_app("explorer")
            continue
            
        
        elif 'நேரம்' in query or 'டைம்' in query:
            speak(f"இப்போ நேரம் {datetime.now().strftime('%I:%M %p')} சார்.")
        elif 'கூட்டு' in query or 'அதிகரி' in query:
            for _ in range(5): pyautogui.press("volumeup")
        elif 'குறை' in query:
            for _ in range(5): pyautogui.press("volumedown")
        elif 'எக்ஸிட்' in query or 'கிளம்பு' in query or 'exit' in query:
            speak("ஆட்டோமேஷன் சிஸ்டம் ஆஃப் செய்யப்படுகிறது. போயிட்டு வாரேன் சார்!")
            time.sleep(1)
            os.system('taskkill /f /fi "WINDOWTITLE eq Stark Industries Advanced HUD*"') 
            break

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, 'index.html')
    
    try:
        os.system('taskkill /f /fi "WINDOWTITLE eq Stark Industries Advanced HUD*" >nul 2>&1')
    except: pass
        
    time.sleep(0.5) 
    
    desktop_app_command = f'start msedge --app="file:///{html_path}"'
    subprocess.Popen(desktop_app_command, shell=True)
    
    
    jarvis_backend()