from translate import Translator

try:
    translator = Translator(to_lang="zh")
    text_to_translate = "This is a pen."
    translation = translator.translate(text_to_translate)
    print(f"Original: {text_to_translate}")
    print(f"Translation to Chinese: {translation}")

except Exception as e:
    print(f"An error occurred during translation: {e}")
    print("Please ensure you have an internet connection and the 'translate' library is installed correctly.")

print("-" * 20) # Separator

try:
    # Assuming test.txt is in the same directory as script2.py (c:\Users\hoang\src\Python\File IO\)
    # This file is created by script.py in 'File IO/test.txt'
    file_path = './test.txt'
    with open(file_path, "r") as my_file:
        print(f"\nContent of '{file_path}':")
        print(my_file.read())
        translator = Translator(to_lang="ja")
        translation = translator.translate(my_file.read())
        print(translation)
        with open(file_path, "w") as my_file_w:
            my_file_w.write(translation)
        my_file.close()
        print(f"File '{file_path}' has been updated with the translation.")
       
except FileNotFoundError:
    print(f"File '{file_path}' not found. Please check the path and ensure it exists.")
except Exception as e:
    print(f"An error occurred while reading the file '{file_path}': {e}")

