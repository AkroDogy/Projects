import speech_recognition as sr
import os
from datetime import datetime

recognizer = sr.Recognizer()


def load_keywords():
    keywords = {}
    with open("keywords.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().lower()
            parts = line.split(":")
            if len(parts) == 2:
                keywords[parts[0].strip()] = parts[1].strip()
    return keywords


def microfon(recognizer, microphone, keywords):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("     >> Poti vorbi <<    ")
        recognized_text = ""
        while True:
            audio_data = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio_data, language='ro-RO')
                recognized_text += text + " "
                print(f"Text Neorganizat: {text}")
                for keyword, replacement in keywords.items():
                    if keyword in recognized_text.lower():
                        recognized_text = recognized_text.replace(f" {keyword}", f"{replacement}")
                if "stop" in recognized_text.lower() or "opreste" in recognized_text.lower() or "oprește" in recognized_text.lower():
                    recognized_text = recognized_text.replace("stop", "").replace("opreste", "").replace("oprește", "")
                    break
            except sr.UnknownValueError:
                print(f" >> Nu am inteles! Repetati, va rog! <<")
            except sr.RequestError as e:
                print(f" >> Eroare tehnica! Nu vă putem primi mesajul. << (Eroare: {e})")
                break

        words = recognized_text.split()
        filtered_words = [words[i] for i in range(len(words)) if i == 0 or words[i] != words[i - 1]]
        recognized_text = ' '.join(filtered_words)
        return recognized_text


def database(text):
    mode = 'a' if os.path.exists("db_speech_to_text.txt") else 'w'
    with open("db_speech_to_text.txt", mode, encoding='utf-8') as file:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"DB: ({current_time}) - {text}\n")


def main():
    keywords = load_keywords()
    microphone = sr.Microphone()
    recognized_text = microfon(recognizer, microphone, keywords)
    words = recognized_text.split()
    if words:
        words[0] = words[0].capitalize()
        recognized_text = ' '.join([words[0]] + [word.lower() for word in words[1:]])

    print("Text Organizat: ", recognized_text)
    database(recognized_text)

if __name__ == "__main__":
    main()