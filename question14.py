def add_tags(word,tag):
    html_with_tag = '<'+tag+'>' + word + '<'+tag+'/>'
    return html_with_tag

input_word = input("Enter the word : ")
tag = input("Enter the tag you want to add : ")

html_string = add_tags(input_word,tag)
print(html_string)