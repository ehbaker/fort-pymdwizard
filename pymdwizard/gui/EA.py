#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
License:            Creative Commons Attribution 4.0 International (CC BY 4.0)
                    http://creativecommons.org/licenses/by/4.0/
PURPOSE
------------------------------------------------------------------------------
Provide a pyqt widget for a Metadata Date <timeperd> section
SCRIPT DEPENDENCIES
------------------------------------------------------------------------------
    None
U.S. GEOLOGICAL SURVEY DISCLAIMER
------------------------------------------------------------------------------
Any use of trade, product or firm names is for descriptive purposes only and
does not imply endorsement by the U.S. Geological Survey.
Although this information product, for the most part, is in the public domain,
it also contains copyrighted material as noted in the text. Permission to
reproduce copyrighted items for other than personal use must be secured from
the copyright owner.
Although these data have been processed successfully on a computer system at
the U.S. Geological Survey, no warranty, expressed or implied is made
regarding the display or utility of the data on any other system, or for
general or scientific purposes, nor shall the act of distribution constitute
any such warranty. The U.S. Geological Survey shall not be held liable for
improper or incorrect use of the data described and/or contained herein.
Although this program has been used by the U.S. Geological Survey (USGS), no
warranty, expressed or implied, is made by the USGS or the U.S. Government as
to the accuracy and functioning of the program and related program material
nor shall the fact of distribution constitute any such warranty, and no
responsibility is assumed by the USGS in connection therewith.
------------------------------------------------------------------------------
"""
import os
from lxml import etree

import pandas as pd

from PyQt5.QtGui import QPainter, QFont, QPalette, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QFileDialog
from PyQt5.QtWidgets import QWidget, QLineEdit, QSizePolicy, QComboBox, QTableView, QRadioButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPlainTextEdit, QStackedWidget, QTabWidget, QDateEdit, QListWidget
from PyQt5.QtWidgets import QStyleOptionHeader, QHeaderView, QStyle, QGridLayout, QScrollArea, QListWidgetItem, QAbstractItemView
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QSize, QRect, QPoint, QDate, QSettings

from pymdwizard.core import utils
from pymdwizard.core import xml_utils
from pymdwizard.core import data_io

from pymdwizard.gui.wiz_widget import WizardWidget
from pymdwizard.gui.ui_files import UI_EA
from pymdwizard.gui import detailed


class EA(WizardWidget):  #

    drag_label = "Entity and Attributes <eainfo>"

    def build_ui(self):
        """
        Build and modify this widget's GUI
        Returns
        -------
        None
        """
        self.ui = UI_EA.Ui_Form()
        self.ui.setupUi(self)

        self.detailed = detailed.Detailed()
        self.ui.detailed_frame.layout().addWidget(self.detailed)

        self.setup_dragdrop(self)

    def dragEnterEvent(self, e):
        """
        Only accept Dragged items that can be converted to an xml object with
        a root tag called 'timeperd'
        Parameters
        ----------
        e : qt event
        Returns
        -------
        """
        mime_data = e.mimeData()
        if e.mimeData().hasFormat('text/plain'):
            parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
            element = etree.fromstring(mime_data.text(), parser=parser)
            if element.tag == 'detailed':
                e.accept()
        else:
            e.ignore()

    def _to_xml(self):
        """
        encapsulates the QTabWidget text for Metadata Time in an element tag
        Returns
        -------
        timeperd element tag in xml tree
        """
        eainfo = xml_utils.xml_node('eainfo')

        #TODO add some logic to not include these when they haven't been used.
        detailed = self.detailed._to_xml()
        eainfo.append(detailed)

        overview = xml_utils.xml_node('overview')
        eaover = xml_utils.xml_node('eaover', text=self.ui.fgdc_eaover.toPlainText(), parent_node=overview)
        eadetcit = xml_utils.xml_node('eadetcit', text=self.ui.fgdc_eaover.toPlainText(), parent_node=overview)
        eainfo.append(overview)

        return eainfo

    def _from_xml(self, eainfo):
        """
        parses the xml code into the relevant timeperd elements
        Parameters
        ----------
        metadata_date - the xml element timeperd and its contents
        Returns
        -------
        None
        """
        try:
            if eainfo.tag == 'eainfo':
                detailed = eainfo.xpath('detailed')[0]
                self.detailed._from_xml(detailed)

                overview = eainfo.xpath('overview')
                if overview:
                    self.ui.fgdc_eaover.setText(eainfo.xpath('overview/eaover')[0].text)
                    self.ui.fgdc_eadetcit.setText(eainfo.xpath('overview/eadetcit')[0].text)
            else:
                print ("The tag is not udom")
        except KeyError:
            pass


if __name__ == "__main__":
    utils.launch_widget(EA,
                        "detailed testing")
