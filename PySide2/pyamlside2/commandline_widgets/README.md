# commandline-widgets

The best technique for GUIing variables in shell scripts is to use command_line_widgets.
You can receive a string as a return value by installing it with pypi or invoking the corresponding script with a relative path.

<br>

## messagebox.py

![](../../images_for_readme/q_yn.png)

- `--title`: Question for lineedit.
- `--type`: icon type (Default: `information`)
  - `information`: Set widget as information.
  - `warning`: Set widget as warning.
  - `critical`: Set widget as critical.
  - `question`: Set widget as question. (return "Yes" or "No" as string)


```bash
ANS=`python messagebox.py --title Y/N --type question`
echo $ANS
```

<br>

## question_lineedit.py

![](../../images_for_readme/q_lineedit.png)

- `--title`: Question for lineedit.
- `--default`: Default input text. (Default: None)

```bash
ANS=`python question_lineedit.py --title "enter your text" --default sample-text`
echo $ANS
```

<br>

## question_select.py

![](../../images_for_readme/q_select.png)

- `--title`: Question for buttons.
- `--answer-list`: Buttons input (split by space)

```bash
ANS=`python question_select.py --title "select your answer" --answer-list ans1 "ans 2" ans3 ans4`
echo $ANS
```

<br>

## select_folder_file_dialog.py

- `--title`: Question for buttons.
- `--path`: Entry point for search.
- `--file`: Using file mode. (If not used, only folder can be select.)
  - `--ext`:  (split by space)

### select file mode (filter using extension)

![](../../images_for_readme/q_select_file.png)



```bash
ANS=`python select_folder_file_dialog.py --title "select your file" --file --path ./ --ext "*.md"`
echo $ANS
```

### select folder mode

![](../../images_for_readme/q_select_folder.png)

```bash
ANS=`python select_folder_file_dialog.py --title "select your file" --path ./`
echo $AWS
```

<br>

## Call from python

commandline_widgets also can be called from python. 

```python
from pyamlside2.commandline_tools.simple_widget import *

print("-----")
print(exec_select_folder_file_dialog('title', './', False))
print("-----")
print(exec_messagebox('title', 'information'))
print("-----")
print(exec_question_lineedit('title', 'default'))
print("-----")
print(exec_question_select('title', ['a', 'b', 'c']))
```
