import re

with open("dzo.txt", "r", encoding="utf-8") as file:
    content = file.read()

  
cleaned_content = re.sub(r'[a-zA-Z0-9.,!?\'"()-_,]+', '',content)

with open("cleaned_file.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_content)

print("File cleaned successfully")