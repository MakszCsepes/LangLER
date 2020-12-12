from PyQt5 import QtWidgets, QtCore
from interface import Ui_MainWindow
import sys
from subprocess import call
import time
import linecache
import json

js_data = ''' [{"CompName": "Ubisoft", "EmployeeName": "Maxim"},
    {"CompName": "Ubisoft", "EmployeeName": "Misha"},
    {"CompName": "Grand", "EmployeeName": "Dima"},
    {"CompName": "Ubisoft", "EmployeeName": "Alex"},
    {"CompName": "Ubisoft", "EmployeeName": "Beci"},
    {"CompName": "Grand", "EmployeeName": "Kolya"},
    {"CompName": "Spar", "EmployeeName": "Alexander"}]'''
data = json.loads(js_data)

# print(type(data))

# d = {
#     'words': {
#         'to trust': 'доверять',
#         'occasionally': 'по случаю',
#         'a stuntman': 'каскадер'
#     },
#     'expressions/phrases': {
#         'Be thrilled about': 'быть в восторге от',
#         'not to mention': 'не говоря уже о;'
#     }
# }
# 
# json_obj = json.dumps(d, indent=2, ensure_ascii=False).encode('utf-8')
# print(json_obj.decode('utf-8'))
# 
# with open('sample.json', 'w') as outfile:
#     json.dump(d, outfile, indent=2, ensure_ascii=False)


window_width = 900
window_height = 650


def get_specific_line_from_file(filename, line_number, lines_to_elude=[]):
    with open(filename) as file:
        lines_list = file.readlines()

        if len(lines_to_elude) != 0:
            if line_number in lines_to_elude:
                return

        if line_number < 1:
            print(line_number)
            return

        # because of a list starts with "0" and
        # we're trying literally to take a line
        # there should be -1
        return lines_list[line_number - 1]


def test_insert_into_file(line_number, text):
    with open('text.txt', 'r+', encoding="utf-8") as fh:
        lines = fh.readlines()
        fh.seek(0)
        lines.insert(line_number - 1, text + '\n')
        fh.writelines(lines)


# test_insert_into_file(5, "loh")


def write_into_file(filename, index, data):
    f = open(filename, "r", encoding="utf-8")
    contents = f.readlines()
    f.close()

    contents.insert(index - 1, data + "\n")

    f = open(filename, "w", encoding="utf-8")
    f.writelines(contents)
    f.close()


# write_into_file(filename, index, "hello")


def get_word_from_line(line):
    word = ""

    for char in line:
        if char == "-" or char == '\n':
            break
        else:
            word += char
    return word


def get_number_of_lines_in_file(filename):
    return call("bash-scripts/get_lines_number.sh " + "languages/" + filename + ".txt", shell=True)


def get_translation_from_line(line):
    start_index = line.index("-")
    start_index += 1

    translation = ""
    while line[start_index] != ';':
        translation += line[start_index]
        start_index += 1

    return translation


def get_word(cur_line):
    if len(cur_line) != 0:
        origin_word = get_word_from_line(cur_line)

        return origin_word


class MyWindow(QtWidgets.QMainWindow):
    file_to_work_name_ = "english"
    file_to_work_full_name_ = "languages/" + file_to_work_name_.lower() + ".txt"
    file_to_use_ = open(file_to_work_full_name_, "r", encoding="utf-8")
    file_index_ = 2
    cur_line_ = ""

    progress_ = 0
    progress_step_ = 0

    words_list_ = []
    lines_to_read_ = 10

    file_to_learn_name_ = ""
    file_to_learn_ = ""

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("LangLER")
        self.setGeometry(400, 50, window_width, window_height)

        # Omit the very first line in file, which contains hash #
        line = self.file_to_use_.readline()
        if '#' in line:
            self.cur_line_ = self.file_to_use_.readline()

        # Connection to buttons
        self.ui.pushButton_get_word.clicked.connect(self.get_word_btn)
        self.ui.pushButton_get_translation.clicked.connect(self.get_translation_btn)
        self.ui.pushButton_get_new_word.clicked.connect(self.get_new_word_btn)
        self.ui.pushButton_exit.clicked.connect(self.exit)
        self.ui.pushButton_write.clicked.connect(self.write_word)
        self.ui.pushButton_prev_word.clicked.connect(self.get_prev_word)

        self.ui.buttonGroup_Languages.buttonClicked.connect(self.but_grp)
        self.ui.radioEnglish.setChecked(True)
        self.ui.buttonGroup_writeMode.buttonClicked.connect(self.but_grp2)
        self.ui.radioOneWord_towrite.setChecked(True)

        self.ui.Text_towrite.hide()
        self.ui.label_writeTip.hide()

        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setMaximum(100)

        self.get_word_btn()
        self.get_translation_btn()

    def but_grp(self, button):
        if button.text() != self.file_to_work_name_:
            self.file_to_use_.close()

            self.file_to_work_name_ = button.text()
            self.file_to_work_full_name_ = "languages/" + self.file_to_work_name_.lower() + ".txt"
            self.file_to_use_ = open(self.file_to_work_full_name_, encoding="utf-8")
            self.file_to_use_.readline()
            self.get_new_word_btn()

            self.ui.label_words_number.setText(str(get_number_of_lines_in_file(self.file_to_work_name_.lower())))

            self.ui.progressBar.setValue(0)
            self.progress_ = 0
            number_of_lines_in_file = get_number_of_lines_in_file(self.file_to_work_name_.lower())
            if number_of_lines_in_file != 0:
                self.progress_step_ = 100 / number_of_lines_in_file

    def but_grp2(self, button):
        if (self.ui.radioOneWord_towrite.isChecked()):
            self.ui.pushButton_write.setText("Записать одно слово")
        else:
            self.ui.pushButton_write.setText("Записать слова")

    def but_grp_learn(self, button):
        if button.text() != self.file_to_work_name_:
            self.file_to_learn_.close()

            self.file_to_learn_name_ = button.text()
            self.file_to_learn_ = open("languages/" + self.file_to_work_name_.lower() + ".txt", encoding="utf-8")
            self.file_to_learn_.readline()
            self.get_new_word_btn()

            self.ui.label_words_number.setText(str(get_number_of_lines_in_file(self.file_to_work_name_.lower())))

            self.ui.progressBar.setValue(0)
            self.progress_ = 0
            number_of_lines_in_file = get_number_of_lines_in_file(self.file_to_work_name_.lower())
            if number_of_lines_in_file != 0:
                self.progress_step_ = 100 / number_of_lines_in_file

    def write_word(self):
        file_to_write_into = open("languages/" + self.file_to_work_name_.lower() + ".txt", 'a', encoding="utf-8")

        if self.ui.radioOneWord_towrite.isChecked():
            line_in_file = self.ui.lineEdit_word_towrite.text() + "-" + self.ui.lineEdit_translation_towrite.text() + ";\n"
            file_to_write_into.write(line_in_file)
        elif self.ui.radioText_towrite.isChecked():
            # splits input text by \n into array to have elements containing
            # each word corresponding to its translation
            word_list = self.ui.Text_towrite.toPlainText().split('\n')

            # appends each word (with its translation) to file having semicolon and '\n'
            # in the end
            for i in word_list:
                file_to_write_into.write(i)
                file_to_write_into.write(';\n')

        file_to_write_into.close()

    def get_new_word_btn(self):
        # clear word and translation lineEdits
        self.ui.lineEdit_word.clear()
        self.ui.lineEdit_translation.clear()

        line = get_specific_line_from_file(self.file_to_work_full_name_, self.file_index_ + 1, [1])

        if line is not None and len(line) != 0:
            self.cur_line_ = line

            if self.ui.checkBox_Translation.isChecked():
                self.get_translation_btn()
            if self.ui.checkBox_Word.isChecked():
                self.get_word_btn()

            self.file_index_ += 1

        # increase value of progress bar
        self.progress_ += self.progress_step_
        self.ui.progressBar.setValue(self.progress_)

    def get_word_btn(self):
        if len(self.cur_line_) != 0:
            origin_word = get_word_from_line(self.cur_line_)

            self.ui.lineEdit_word.setText(origin_word)

    def get_translation_btn(self):
        if len(self.cur_line_) != 0:
            translation = get_translation_from_line(self.cur_line_)
            self.ui.lineEdit_translation.setText(translation)

    def get_prev_word(self):
        # clear word and translation lineEdits
        self.ui.lineEdit_word.clear()
        self.ui.lineEdit_translation.clear()

        line = get_specific_line_from_file(self.file_to_work_full_name_, self.file_index_ - 1, [1])

        if line is not None and len(line) != 0:
            self.cur_line_ = line
            self.file_index_ -= 1

            if self.ui.checkBox_Translation.isChecked():
                self.get_translation_btn()
            if self.ui.checkBox_Word.isChecked():
                self.get_word_btn()

    def exit(self):
        self.file_to_use_.close()
        sys.exit()

app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
