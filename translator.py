from textblob import TextBlob

text_entered = TextBlob(input("Enter text :\n"))
lang_detected = text_entered.detect_language()

language_dictonary = {
    'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'eu': 'Basque', 'be': 'Belarusian',
    'bg': 'Bulgarian', 'ca': 'Catalan', 'zh': 'Chinese', 'hr': 'Croatian', 'cs': 'Czech',
    'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'et': 'Estonian', 'fo': 'Faeroese', 'fa': 'Farsi',
    'fi': 'Finnish', 'fr': 'French', 'gd': 'Gaelic', 'de': 'German', 'el': 'Greek', 'he': 'Hebrew',
    'hi': 'Hindi', 'hu': 'Hungarian', 'is': 'Icelandic', 'id': 'Indonesian', 'ga': 'Irish',
    'it': 'Italian', 'ja': 'Japanese', 'ko': 'Korean', 'ku': 'Kurdish', 'lv': 'Latvian',
    'lt': 'Lithuanian', 'mk': 'Macedonian', 'ml': 'Malayalam', 'ms': 'Malaysian', 'mt': 'Maltese',
    'no': 'Norwegian', 'nb': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi',
    'rm': 'Rhaeto', 'ro': 'Romanian', 'ru': 'Russian', 'sr': 'Serbian', 'sk': 'Slovak',
    'sl': 'Slovenian', 'sb': 'Sorbian', 'es': 'Spanish', 'sv': 'Swedish', 'th': 'Thai',
    'ts': 'Tsonga', 'tn': 'Tswana', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 've': 'Venda',
    'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa', 'ji': 'Yiddish', 'zu': 'Zulu'
}

for key in language_dictonary:
    if key == lang_detected:
        print(language_dictonary[key], "language Detected")

lang = TextBlob(input('Enter the language code you want to translate the text into \n'))
print(text_entered.translate(to=str(lang)))