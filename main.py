import sys
from PyQt5.QtWidgets import QApplication

from config.config import Config
from ui.agentselectorui import AgentSelector


if __name__ == '__main__':
    Config.configure_logging()
    app = QApplication(sys.argv)
    ex = AgentSelector()
    ex.show()
    sys.exit(app.exec_())
