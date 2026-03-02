from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException

language_dictionary = {
    'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'bg': 'Bulgarian',
    'bn': 'Bengali', 'ca': 'Catalan', 'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)', 'cs': 'Czech', 'da': 'Danish',
    'nl': 'Dutch', 'en': 'English', 'et': 'Estonian', 'fi': 'Finnish',
    'fr': 'French', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati',
    'he': 'Hebrew', 'hi': 'Hindi', 'hu': 'Hungarian', 'id': 'Indonesian',
    'it': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada', 'ko': 'Korean',
    'ml': 'Malayalam', 'mr': 'Marathi', 'ne': 'Nepali', 'no': 'Norwegian',
    'pa': 'Punjabi', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian',
    'ru': 'Russian', 'es': 'Spanish', 'sv': 'Swedish', 'ta': 'Tamil',
    'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian',
    'ur': 'Urdu', 'vi': 'Vietnamese'
}

def detect_language(text):
    try:
        detected_code = detect(text)
        language_name = language_dictionary.get(detected_code, detected_code)
        return detected_code, language_name
    except LangDetectException:
        return None, "Could not detect language"


def translate_text(text, target_lang):
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Translation Error: {e}"


def main():

    input_text = input("Enter text: ").strip()

    if not input_text:
        print("No text entered.")
        return

    code, language = detect_language(input_text)
    if code:
        print(f"\nDetected Language: {language} ({code})")
    else:
        print(language)
        return

    target_lang = input("\nEnter target language code (e.g., en, hi, fr, de, es): ").strip()

    translated = translate_text(input_text, target_lang)

    print("\nTranslated Text:")
    print(translated)

if __name__ == "__main__":
    main()
