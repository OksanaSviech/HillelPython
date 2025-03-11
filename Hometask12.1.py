import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):

    with codecs.open(html_file, 'r', 'utf-8') as file:
         html = file.read()

    new_text = ""
    chars_inside = False

    for char in html:
        if char == "<":
            chars_inside = True
        elif char == ">":
            chars_inside = False
        elif not chars_inside:
            new_text += char

    cleaned_text = ""
    for line in new_text.splitlines():
        stripped_lines = line.strip()
        if line.strip():
            cleaned_text += stripped_lines + "\n"

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)

delete_html_tags('draft.html', 'cleaned.txt')
