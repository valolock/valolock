import logging
import threading
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QComboBox, QLabel, QSpacerItem, QSizePolicy, QMenuBar, QMessageBox
from PyQt5.QtGui import QIcon
import cv2
import numpy as np
import pyautogui
import keyboard

from config.config import Config

class AgentSelector(QWidget):
    isRunning = False
    
    def __init__(self):
        super().__init__()
        self.initUI()
        keyboard.add_hotkey('f5', self.toggle_selection)

    
    def initUI(self):
        self.create_message_box(QMessageBox.Information, "REMINDER!", "This program does NOT work in fullscreen mode! Please make sure that Valorant is in windowed mode, when loading into agent select. This can be done quickly with ctrl-enter(but make sure you maximize the window afterwards) or in the Valorant settings.", "REMINDER!")
        Config.increment_opened_the_program_count()
        self.setWindowTitle('valolock - instalocker ' + Config.read_version_from_file('version.txt'))
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon('assets/jettlogo.PNG'))

        self.setStyleSheet("""
            QWidget {background-color: #2C2F33; color: #FFFFFF;}
            QPushButton {background-color: #7289DA; border-radius: 5px; padding: 5px;}
            QPushButton:hover {background-color: #5B6EAE;}
            QComboBox {background-color: #23272A; border-radius: 5px; padding: 5px; color: #FFFFFF;}
            QLabel {font-weight: bold;}
        """)

        layout = QVBoxLayout()
        layout.setSpacing(10)

        self.agent_dropdown = self.create_agent_dropdown()
        self.start_button = self.create_button('Start', self.start_selection)
        self.stop_button = self.create_button('Stop', self.stop_selection, True)
        self.status_label = self.create_label('Status: Idle', False)
        
        layout.addWidget(self.agent_dropdown)
        layout.addWidget(self.start_button)
        layout.addWidget(self.status_label)
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

    def create_agent_dropdown(self):
        dropdown = QComboBox()
        dropdown.addItems(Config.agents_df['Agent'])
        return dropdown

    def create_button(self, text, callback, hide=False):
        button = QPushButton(text)
        button.clicked.connect(callback)
        button.setVisible(not hide)
        return button

    def create_label(self, text, hide=False):
        label = QLabel(text)
        label.setVisible(not hide)
        return label
    
    def create_config_menubar(self, text):
        qMenuBar = QMenuBar(self)
        qMenuBar.addMenu(text)
        return qMenuBar
    
    def create_message_box(self, icon, text, informative_text, title):
        if Config.opened_the_program_count == 0:
            msg = QMessageBox()
            msg.setIcon(icon)
            msg.setText(text)
            msg.setInformativeText(informative_text)
            msg.setWindowTitle(title)
            msg.exec_()
            return msg
        
    def start_selection(self):
        AgentSelector.isRunning = True
        logging.info('Started instalocker. Waiting for agent selection screen.')
        selected_agent = self.agent_dropdown.currentText()
        self.status_label.setText(f'Status: Running \nLocking: {selected_agent}')
        position = Config.agents_df[Config.agents_df['Agent'] == selected_agent]['Position'].iloc[0]
        threading.Thread(target=self.select_agent, args=(position,)).start()
        self.toggle_ui(True)
    
    def stop_selection(self):
        AgentSelector.isRunning = False
        logging.info('Stopped instalocker.')
        self.status_label.setText('Status: Idle')
        self.toggle_ui(False)
    
    def toggle_selection(self):
        if self.isRunning:
            self.stop_selection()
        else:
            self.start_selection()
    
    def toggle_ui(self, isRunning):
        self.stop_button.setVisible(isRunning)
        self.start_button.setVisible(not isRunning)
        self.agent_dropdown.setVisible(not isRunning)
    
    def closeEvent(self, event):
        self.stop_selection()
        super().closeEvent(event)
    
    def select_agent(self, position):
        detect_screen_and_select_agent(position, 'assets/lockInButton.PNG')
        self.stop_selection()
        

def detect_screen_and_select_agent(agent_position, reference_image_path):
    reference_image = cv2.imread(reference_image_path, cv2.IMREAD_GRAYSCALE)
    threshold = 0.9  
    while AgentSelector.isRunning:
        screen = pyautogui.screenshot()
        screen_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(screen_gray, reference_image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)
        
        if max_val >= threshold:
            logging.info("Agent selection found. Locking agent.")
            pyautogui.click(agent_position)
            pyautogui.moveTo(Config.lock_in_button_position)
            pyautogui.mouseDown()
            pyautogui.sleep(0.1)
            pyautogui.mouseUp()
            AgentSelector.isRunning = False
            break