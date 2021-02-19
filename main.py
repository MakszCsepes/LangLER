from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from interface import Ui_MainWindow
import sys
import os
from file_lines import *

window_width = 1000
window_height = 650

INITIAL_INDEX = 0


DICT_META_POINTER_i = 0
DICT_NAME_i = 1
DICT_LAST_LINE_i = 2
DICT_SEPARATOR_i = 3
FILE_METADATA_ELEMENTS = [DICT_META_POINTER_i, DICT_NAME_i, DICT_LAST_LINE_i, DICT_SEPARATOR_i]


class MyWindow(QtWidgets.QMainWindow):
    dir_to_use_ = ""  # dir with dictionaries selected by user
    dir_files_ = []  # list of files in the dir

    opened_new_dict_ = False
    file_to_work_name_ = ""  # text3.txt.txt
    file_to_work_full_name_ = ""  # dir/.../text3.txt.txt

    file_lines_ = []  # list of lines in file
    file_lines_meta_ = {}  # metadata for lines in file
    file_lines_index_ = INITIAL_INDEX
    cur_line_ = ""  # current line in progress
    lines_on_top_ = []  # lines to drop on top of the dict

    progress_ = 0  # total progress in percentage
    progress_step_ = 0

    # dropbox with files in the dir
    comboBox_ToLearn_current_index_ = 0

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("LangLER")
        self.setGeometry(400, 50, window_width, window_height)

        self.ui.tabWidget.setFixedWidth(window_width - (window_width/100*5))

        # Connection to buttons
        self.ui.pushButton_get_word.clicked.connect(self.get_word_btn)
        self.ui.pushButton_clear_word.clicked.connect(self.ui.lineEdit_word.clear)
        self.ui.pushButton_get_translation.clicked.connect(self.get_translation_btn)
        self.ui.pushButton_clear_translation.clicked.connect(self.ui.lineEdit_translation.clear)
        self.ui.pushButton_get_new_word.clicked.connect(self.get_new_word_btn)
        self.ui.pushButton_exit.clicked.connect(self.exit)
        self.ui.pushButton_write.clicked.connect(self.write_word)
        self.ui.pushButton_prev_word.clicked.connect(self.get_prev_word)
        self.ui.pushButton_apply.clicked.connect(self.apply)
        self.ui.pushButton_browse.clicked.connect(self.browse)
        self.ui.pushButton_browse.clicked.connect(self.apply)
        self.ui.pushButton_on_top.clicked.connect(self.push_on_top)

        # Button groups organized
        self.ui.buttonGroup_writeMode.buttonClicked.connect(self.change_text_in_write_page)
        self.ui.radioOneWord_towrite.setChecked(True)
        self.ui.buttonGroup_select_position.buttonClicked.connect(self.select_beginning_position)

        # ComboBox organized
        self.ui.comboBox_ToLearn.currentIndexChanged.connect(self.change_apply_button)

        self.ui.pushButton_apply.setEnabled(False)
        self.ui.pushButton_apply.setToolTip("changes the file to read")
        self.ui.Text_towrite.hide()
        self.ui.label_writeTip.hide()

        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setMaximum(100)

        self.browse()
        self.apply()

    def browse(self):
        # clear list of files in directory
        self.dir_files_.clear()

        # select new dir
        dir_to_use = QFileDialog.getExistingDirectory(self, "select directory")

        if dir_to_use:
            self.ui.comboBox_ToLearn.clear()
            self.dir_to_use_ = dir_to_use

            # display directory name on label
            dir_path_list = self.dir_to_use_.split('/')
            self.ui.label_dirname.setText(str(dir_path_list[-1]))

            # generate list of files in directory
            for filename in os.listdir(dir_to_use):
                self.dir_files_.append(filename)

                filename = filename.split(".")
                self.ui.comboBox_ToLearn.addItem(filename[0])

    def apply(self):
        self.comboBox_ToLearn_current_index_ = self.ui.comboBox_ToLearn.currentIndex()

        self.change_dict(self.dir_files_[self.comboBox_ToLearn_current_index_])

        # disable apply button
        self.ui.pushButton_apply.setEnabled(False)

    # clears class variables such as lists, strings, arrays
    # to get ready for new dict data
    def clear_dict_variables(self):
        self.file_lines_.clear()
        self.file_lines_meta_.clear()
        self.file_lines_index_ = INITIAL_INDEX
        self.cur_line_ = ""
        self.lines_on_top_.clear()

        self.progress_ = 0
        self.progress_step_ = 0

    def define_progress(self):
        # set progressBar to zero
        self.progress_step_ = 0
        self.progress_ = 0
        self.ui.progressBar.setValue(self.progress_)

        file_lines_length = len(self.file_lines_)
        if file_lines_length != 0:
            self.progress_step_ = 100 / file_lines_length

        if self.file_lines_index_ != INITIAL_INDEX:
            self.progress_ = self.progress_step_*(self.file_lines_index_ + 1)
            self.ui.progressBar.setValue(self.progress_)

    def change_dict(self, filename):
        if self.opened_new_dict_:
            self.save_current_dict(self.file_to_work_full_name_)

        self.file_to_work_name_ = filename
        self.file_to_work_full_name_ = self.dir_to_use_ + "/" + self.file_to_work_name_

        self.open_new_dict(self.file_to_work_full_name_)

        # display number of elements in the file
        self.ui.label_words_number.setText(str(len(self.file_lines_)))

        # display the last position
        label_text = self.ui.label_last_position.text()
        label_text += str(self.file_lines_meta_[DICT_LAST_LINE_i])
        self.ui.label_last_position.setText(label_text)

        # display word and a relevant translation
        self.cur_line_ = self.file_lines_[self.file_lines_index_]
        self.display_word_line()

        self.define_progress()

    def open_new_dict(self, filename):
        with open(filename, "r", encoding="utf-8") as file_to_use_:
            self.file_lines_index_ = INITIAL_INDEX
            self.file_lines_ = file_to_use_.readlines()

            self.get_dict_metadata()
            self.file_lines_index_ = self.file_lines_meta_[DICT_LAST_LINE_i]

            self.remove_elements_from_list()

            self.opened_new_dict_ = True

    def save_current_dict(self, filename):
        self.save_on_top_elements()

        self.save_dict_metadata()

        with open(filename, "w", encoding="utf-8") as file_to_use_:
            file_to_use_.writelines(self.file_lines_)

        self.opened_new_dict_ = False
        self.clear_dict_variables()

    def get_dict_metadata(self):
        line = self.file_lines_[0]
        splitted_line = line.split()

        for i in FILE_METADATA_ELEMENTS:
            if i == DICT_NAME_i:
                self.file_lines_meta_[DICT_NAME_i] = splitted_line[i]
            elif i == DICT_LAST_LINE_i and splitted_line[i].isdigit():
                self.file_lines_meta_[DICT_LAST_LINE_i] = int(splitted_line[i])
            elif i == DICT_SEPARATOR_i:
                self.file_lines_meta_[DICT_SEPARATOR_i] = splitted_line[i]
            elif i == DICT_META_POINTER_i:
                self.file_lines_meta_[DICT_META_POINTER_i] = splitted_line[i]

    def save_dict_metadata(self):
        # save last (current) position in dict
        self.file_lines_meta_[DICT_LAST_LINE_i] = self.file_lines_index_

        # generate string with metadata
        metadata_str = str(self.file_lines_meta_[DICT_META_POINTER_i])
        for i in self.file_lines_meta_:
            if str(self.file_lines_meta_[i]) != str(self.file_lines_meta_[DICT_META_POINTER_i]):
                metadata_str += ' ' + str(self.file_lines_meta_[i])
        metadata_str += '\n'

        # push the string onto the top of the list (that is aka dict)
        self.file_lines_.insert(0, metadata_str)

    def save_on_top_elements(self):
        # push each on_top element onto the beginning of the list (that is aka dict)
        for on_top_elem in self.lines_on_top_:
            self.file_lines_.remove(on_top_elem)
            self.file_lines_.insert(0, on_top_elem)

    def push_on_top(self):
        self.lines_on_top_.insert(0, self.cur_line_)

    def remove_elements_from_list(self):
        for line in self.file_lines_:
            if '#' in line:
                self.file_lines_.remove(line)

    # button groups
    def change_text_in_write_page(self):
        if self.ui.radioOneWord_towrite.isChecked():
            self.ui.pushButton_write.setText("Записать одно слово")
        else:
            self.ui.pushButton_write.setText("Записать слова")

    def select_beginning_position(self):
        if self.ui.radio_from_the_beginning.isChecked():
            self.file_lines_index_ = INITIAL_INDEX
        elif self.ui.radio_from_saved_position.isChecked():
            self.file_lines_index_ = self.file_lines_meta_[DICT_LAST_LINE_i]

        self.update_word_display()
        self.define_progress()

    def change_apply_button(self):
        if self.comboBox_ToLearn_current_index_ == self.ui.comboBox_ToLearn.currentIndex():
            self.ui.pushButton_apply.setEnabled(False)
        else:
            self.ui.pushButton_apply.setEnabled(True)

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

    # display current word and translation
    # according to checkBox
    def display_word_line(self):
        if self.ui.checkBox_Translation.isChecked():
            self.get_translation_btn()
        if self.ui.checkBox_Word.isChecked():
            self.get_word_btn()

        self.ui.label_current_index.setText(str(self.file_lines_index_ + 1))

    # according to lines_index display appropriate/relevant word
    def update_word_display(self):
        # clear word and translation lineEdits
        self.ui.lineEdit_word.clear()
        self.ui.lineEdit_translation.clear()

        line = self.file_lines_[self.file_lines_index_]

        if line is not None and len(line) != 0:
            self.cur_line_ = line

        self.display_word_line()

    def get_new_word_btn(self):
        # clear word and translation lineEdits
        self.ui.lineEdit_word.clear()
        self.ui.lineEdit_translation.clear()

        # get out if index is out of the list range
        if self.file_lines_index_ + 1 > len(self.file_lines_):
            return

        line = self.file_lines_[self.file_lines_index_ + 1]

        if line is not None and len(line) != 0:
            self.cur_line_ = line
            self.file_lines_index_ += 1

            self.display_word_line()

        # increase value of progress bar
        self.progress_ += self.progress_step_
        self.ui.progressBar.setValue(self.progress_)

    def get_prev_word(self):
        # clear word and translation lineEdits
        self.ui.lineEdit_word.clear()
        self.ui.lineEdit_translation.clear()

        # get out if index is out of the list range
        if self.file_lines_index_ - 1 < 0:
            return

        line = self.file_lines_[self.file_lines_index_ - 1]

        if line is not None and len(line) != 0:
            self.cur_line_ = line
            self.file_lines_index_ -= 1

            self.display_word_line()

        # decrease value of progress bar
        self.progress_ -= self.progress_step_
        self.ui.progressBar.setValue(self.progress_)

    def get_word_btn(self):
        if len(self.cur_line_) != 0:
            origin_word = get_word_from_line(self.cur_line_)

            self.ui.lineEdit_word.setText(origin_word)

    def get_translation_btn(self):
        if len(self.cur_line_) != 0:
            translation = get_translation_from_line(self.cur_line_, [self.file_lines_meta_[DICT_SEPARATOR_i]])

            self.ui.lineEdit_translation.setText(translation)

    def exit(self):
        self.save_current_dict(self.file_to_work_full_name_)
        sys.exit()


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())

