from pathlib import Path


# path = Path('my_name.txt')
# contents = path.read_text()

# new_path = Path("new_file.txt")
# new_path.write_text("Today was a day that was being a day.")


from pathlib import Path

# Use an absolute path
new_path = Path("c:/Users/rouss/OneDrive/Desktop/code-college/python/my-code/chapter_10/new_file.txt")

file_text = "Today was a day that was being a day.\n"
file_text += "We learnt how to open .txt files in python"

new_path.write_text(file_text)