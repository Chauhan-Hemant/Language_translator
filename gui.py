import tkinter as tk
from tkinter import *
from textblob import TextBlob

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


def getTextInput():
    """
    Function to take the input from the textbox and detect the language of the text
    """
    global language
    global result

    result = TextBlob(str(text.get('1.0', 'end')))
    lang_detected = result.detect_language()

    for key in language_dictonary:
        if key == lang_detected:
            language = language_dictonary[key]
    result_label = Label(result_frame, text=str(f"The above text is in {language} Language"))
    result_label.pack()


def translate():
    global language
    global result
    global dropdown
    global selected_lang

    text_getted = select.get()
    data = result.translate(to=str(text_getted))
    result_label = Label(result_frame, text=data)
    result_label.pack()


def clearText():
    """
    Function to clear the textbox and output section
    """
    text.delete('1.0', 'end')
    for widget in result_frame.winfo_children():
        widget.destroy()


def show():
    language = language_dictonary.get(select.get())
    selected_lang.config(text=language)


root = tk.Tk()
root.title("Text Translator")

Label(root, text="Enter Text to Translate", padx=25, pady=10, font=("", 15), fg='green').pack()

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

text = Text(root)
text.pack()

text.config(yscrollcommand=scroll.set)
scroll.config(command=text.yview)

submit_btn = Button(root, text='Detect Language', fg='green', command=getTextInput)
submit_btn.pack()

select = StringVar()
select.set('Select Language')
dropdown = OptionMenu(root, select, *language_dictonary)
dropdown.pack()

button = Button(root, text="Get Selected Language", command=show).pack()

selected_lang = Label(root, text='')
selected_lang.pack()

submit_btn = Button(root, text='Translate', fg='green', command=translate)
submit_btn.pack()

reset_button = Button(root, text="Clear", fg='red', command=clearText)
reset_button.pack()

result_frame = Frame(root, bg='white')
result_frame.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.7)

root.minsize(800, 850)
root.mainloop()
