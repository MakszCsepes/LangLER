from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QGridLayout, QSizePolicy

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
    _dir_to_use = ""  # dir with dictionaries selected by user
    _dir_files = []  # list of files in the dir

    _b_opened_new_dict = False
    _file_to_work_name = ""  # text3.txt.txt
    _file_to_work_full_name = ""  # dir/.../text3.txt.txt

    _file_lines = []  # list of lines in file
    _file_lines_meta = {}  # metadata for lines in file
    _file_lines_index = INITIAL_INDEX
    _cur_line = ""  # current line in progress
    _lines_on_top = []  # lines to drop on the very top of the dict so they will appear again FIRST next time
    _lines_to_save = []  # lines to save so they will appear again next time but after `_lines_on_top`

    _progress = 0  # total progress in percentage
    _progress_step = 0

    # dropbox with files in the dir
    _comboBox_ToLearn_current_index = 0

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
        self.ui.pushButton_save.clicked.connect(self.push_to_save_line)

        # Button groups organized
        self.ui.buttonGroup_writeMode.buttonClicked.connect(self.change_text_in_write_page)
        self.ui.radioOneWord_towrite.setChecked(True)

        # ComboBox organized
        self.ui.comboBox_ToLearn.currentIndexChanged.connect(self.change_apply_button)

        # Set an Image
        self.set_image("resources/asset.jpg")

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
        self._dir_files.clear()

        # select new dir
        dir_to_use = QFileDialog.getExistingDirectory(self, "select directory")

        if dir_to_use:
            self.ui.comboBox_ToLearn.clear()
            self._dir_to_use = dir_to_use

            # display directory name on label
            dir_path_list = self._dir_to_use.split('/')
            self.ui.label_dirname.setText(str(dir_path_list[-1]))

            # generate list of files in directory
            for filename in os.listdir(dir_to_use):
                self._dir_files.append(filename)

                filename = filename.split(".")
                self.ui.comboBox_ToLearn.addItem(filename[0])

    def apply(self):
        self.change_dict(self._dir_files[self.ui.comboBox_ToLearn.currentIndex()])

        # disable apply button
        self.ui.pushButton_apply.setEnabled(False)

    # clears class variables such as lists, strings, arrays
    # to get ready for new dict data
    def clear_dict_variables(self):
        self._file_lines.clear()
        self._file_lines_meta.clear()
        self._file_lines_index = INITIAL_INDEX
        self._cur_line = ""
        self._lines_on_top.clear()
        self._lines_to_save.clear()

        self._progress = 0
        self._progress_step = 0

    def define_progress(self):
        # set progressBar to zero
        self._progress_step = 0
        self._progress = 0
        self.ui.progressBar.setValue(self._progress)

        file_lines_length = len(self._file_lines)
        if file_lines_length != 0:
            self._progress_step = 100 / file_lines_length

        if self._file_lines_index != INITIAL_INDEX:
            self._progress = self._progress_step * (self._file_lines_index + 1)
            self.ui.progressBar.setValue(self._progress)

    def change_dict(self, filename):
        if self._b_opened_new_dict:
            self.save_current_dict(self._file_to_work_full_name)

        self._file_to_work_name = filename
        self._file_to_work_full_name = self._dir_to_use + "/" + self._file_to_work_name

        self.open_new_dict(self._file_to_work_full_name)

        # display number of elements in the file
        self.ui.label_words_number.setText(str(len(self._file_lines)))

        # display the last position
        label_text = self.ui.label_last_position.text()
        label_text += str(self._file_lines_meta[DICT_LAST_LINE_i])
        self.ui.label_last_position.setText(label_text)

        # display word and a relevant translation
        self._cur_line = self._file_lines[self._file_lines_index]
        self.display_word_line()

        self.define_progress()

    def open_new_dict(self, filename):
        with open(filename, "r", encoding="utf-8") as file_to_use_:
            self._file_lines_index = INITIAL_INDEX
            self._file_lines = file_to_use_.readlines()

            self.get_dict_metadata()
            self._file_lines_index = self._file_lines_meta[DICT_LAST_LINE_i]

            self.remove_elements_from_list()

            self._b_opened_new_dict = True

    def save_current_dict(self, filename):
        # in order not to get duplicates

        # cut off `to-save` elements from `on_top` list
        cut_off_list_from_list(self._lines_to_save, self._lines_on_top)
        # cut off `to-save` elements from the main list
        cut_off_list_from_list(self._file_lines, self._lines_to_save)
        # cut off `on_top` elements from the main list
        cut_off_list_from_list(self._file_lines, self._lines_on_top)

        self.write_saved_elements()
        self.write_on_top_elements()

        # place metadata (e.g a dictname, a separator, current position e.t.c)
        # onto the very first line of the file
        self.save_dict_metadata()

        with open(filename, "w", encoding="utf-8") as file_to_use_:
            file_to_use_.writelines(self._file_lines)

        self._b_opened_new_dict = False
        self.clear_dict_variables()

    def get_dict_metadata(self):
        line = self._file_lines[0]
        splitted_line = line.split()

        for i in FILE_METADATA_ELEMENTS:
            if i == DICT_NAME_i:
                self._file_lines_meta[DICT_NAME_i] = splitted_line[i]
            elif i == DICT_LAST_LINE_i and splitted_line[i].isdigit():
                self._file_lines_meta[DICT_LAST_LINE_i] = int(splitted_line[i])
            elif i == DICT_SEPARATOR_i:
                self._file_lines_meta[DICT_SEPARATOR_i] = splitted_line[i]
            elif i == DICT_META_POINTER_i:
                self._file_lines_meta[DICT_META_POINTER_i] = splitted_line[i]

    def save_dict_metadata(self):
        # save last (current) position in dict
        self._file_lines_meta[DICT_LAST_LINE_i] = self._file_lines_index

        # generate string with metadata
        metadata_str = str(self._file_lines_meta[DICT_META_POINTER_i])
        for i in self._file_lines_meta:
            if str(self._file_lines_meta[i]) != str(self._file_lines_meta[DICT_META_POINTER_i]):
                metadata_str += ' ' + str(self._file_lines_meta[i])
        metadata_str += '\n'

        # push the string onto the top of the list (that is aka dict)
        self._file_lines.insert(0, metadata_str)

    def write_saved_elements(self):
        cur_line = self._cur_line

        # there is no need to save the very last line
        # because it will definitely be the first line to appear next time
        # so it's implicitly saved
        if cur_line in self._lines_to_save:
            self._lines_to_save.remove(cur_line)

        cur_line_index = self._file_lines.index(cur_line)

        # push each `to-save` element onto the beginning of the list (aka dict)
        for elem_to_save in self._lines_to_save:
            self._file_lines.insert(cur_line_index + 1, elem_to_save)

        self._file_lines_index = cur_line_index

    def write_on_top_elements(self):
        cur_line_index = self._file_lines_index
        # push each on_top element onto the beginning of the list (aka dict)
        for on_top_elem in self._lines_on_top:
            self._file_lines.insert(cur_line_index + 1, on_top_elem)

        self._file_lines_index = cur_line_index

    def push_on_top(self):
        if self._cur_line not in self._lines_on_top:
            self._lines_on_top.insert(0, self._cur_line)

    # add current line to `saved lines`
    def push_to_save_line(self):
        if self._cur_line not in self._lines_to_save:
            self._lines_to_save.insert(0, self._cur_line)

    def remove_elements_from_list(self):
        for line in self._file_lines:
            if '#' in line:
                self._file_lines.remove(line)

    # button groups
    def change_text_in_write_page(self):
        if self.ui.radioOneWord_towrite.isChecked():
            self.ui.pushButton_write.setText("Записать одно слово")
        else:
            self.ui.pushButton_write.setText("Записать слова")

    def select_beginning_position(self):
        if self.ui.radio_from_the_beginning.isChecked():
            self._file_lines_index = INITIAL_INDEX
        elif self.ui.radio_from_saved_position.isChecked():
            self._file_lines_index = self._file_lines_meta[DICT_LAST_LINE_i]

        self.update_word_display()
        self.define_progress()

    def change_apply_button(self):
        if self._comboBox_ToLearn_current_index == self.ui.comboBox_ToLearn.currentIndex():
            self.ui.pushButton_apply.setEnabled(False)
        else:
            self.ui.pushButton_apply.setEnabled(True)

    def write_word(self):
        file_to_write_into = open("languages/" + self._file_to_work_name.lower() + ".txt", 'a', encoding="utf-8")

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

    def set_image(self, image_filename):
        self.ui.label_Image.setPixmap(QtGui.QPixmap(image_filename))
        self.ui.label_Image.setScaledContents(True)

    # display current word and translation
    # according to checkBox
    def display_word_line(self):
        if self.ui.checkBox_Translation.isChecked():
            self.get_translation_btn()
        if self.ui.checkBox_Word.isChecked():
            self.get_word_btn()

        self.get_image()

        self.ui.label_current_index.setText(str(self._file_lines_index + 1))

    # according to lines_index display appropriate/relevant word
    def update_word_display(self):
        # clear word and translation lineEdits
        self.ui.lineEdit_word.clear()
        self.ui.lineEdit_translation.clear()

        line = self._file_lines[self._file_lines_index]

        if line is not None and len(line) != 0:
            self._cur_line = line

        self.display_word_line()

    def get_new_word_btn(self):
        # clear word and translation lineEdits
        self.ui.lineEdit_word.clear()
        self.ui.lineEdit_translation.clear()

        # go back on top if index is out of the list range
        if self._file_lines_index + 1 >= len(self._file_lines):
            self._file_lines_index = -1

        line = self._file_lines[self._file_lines_index + 1]

        if line is not None and len(line) != 0:
            self._cur_line = line
            self._file_lines_index += 1

            self.display_word_line()

        # increase value of progress bar
        self._progress += self._progress_step
        self.ui.progressBar.setValue(self._progress)

    def get_prev_word(self):
        # clear word and translation lineEdits
        self.ui.lineEdit_word.clear()
        self.ui.lineEdit_translation.clear()

        # get out if index is out of the list range
        if self._file_lines_index - 1 < 0:
            return

        line = self._file_lines[self._file_lines_index - 1]

        if line is not None and len(line) != 0:
            self._cur_line = line
            self._file_lines_index -= 1

            self.display_word_line()

        # decrease value of progress bar
        self._progress -= self._progress_step
        self.ui.progressBar.setValue(self._progress)

    def get_word_btn(self):
        if len(self._cur_line) != 0:
            origin_word = get_word_from_line(self._cur_line)

            self.ui.lineEdit_word.setText(origin_word)

    def get_translation_btn(self):
        if len(self._cur_line) != 0:
            translation = get_translation_from_line(self._cur_line, [self._file_lines_meta[DICT_SEPARATOR_i]])

            self.ui.lineEdit_translation.setText(translation)

    def get_image(self):
        if len(self._cur_line) != 0:
            image = get_image_from_line(self._cur_line, [self._file_lines_meta[DICT_SEPARATOR_i], '\n'])

            if len(image) != 0:
                self.ui.label_Image.setPixmap(QtGui.QPixmap("resources/" + image))
                self.ui.label_Image.setScaledContents(True)

    def exit(self):
        self.save_current_dict(self._file_to_work_full_name)
        sys.exit()


def main():
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())


main()

