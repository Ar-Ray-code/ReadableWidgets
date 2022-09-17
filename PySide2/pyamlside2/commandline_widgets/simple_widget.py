import subprocess

def exec_messagebox(title: str, message_type: str):
    output_string = subprocess.check_output(['messagebox', '--title', title, '--type', message_type])

    return output_string.decode('utf-8').replace('\n','')

def exec_question_lineedit(title: str, default_input_txt: str='') -> str:
    output_string = subprocess.check_output(['question_lineedit', '--title', title, '--default', default_input_txt])

    return output_string.decode('utf-8').replace('\n','')

def exec_question_select(title: str, ans_list: list) -> str:
    exec_list = ['question_select', '--title', title, '--answer-list'] + ans_list
    output_string = subprocess.check_output(exec_list)

    return output_string.decode('utf-8').replace('\n','')

def exec_select_folder_file_dialog(title: str, entry_point_pass: str, file_mode: bool=False, exts_str: str="*") -> str:
    if file_mode:
        output_string = subprocess.check_output(['select_folder_file_dialog', '--title', title, '--file', '--path', entry_point_pass, '--exts', exts_str])
    output_string = subprocess.check_output(['select_folder_file_dialog', '--title', title, '--path', entry_point_pass])

    return output_string.decode('utf-8').replace('\n','')


if __name__ == '__main__':
    print("-----")
    print(exec_select_folder_file_dialog('title', './', False))
    print("-----")
    print(exec_messagebox('title', 'information'))
    print("-----")
    print(exec_question_lineedit('title', 'default'))
    print("-----")
    print(exec_question_select('title', ['a', 'b', 'c']))