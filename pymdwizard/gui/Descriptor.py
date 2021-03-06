#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
License:            Creative Commons Attribution 4.0 International (CC BY 4.0)
                    http://creativecommons.org/licenses/by/4.0/

PURPOSE
------------------------------------------------------------------------------
Provide a pyqt widget for a Descriptor <descript> section


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

from lxml import etree

from PyQt5.QtGui import QPainter, QFont, QPalette, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from PyQt5.QtWidgets import QWidget, QLineEdit, QSizePolicy, QComboBox, QTableView
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPlainTextEdit
from PyQt5.QtWidgets import QStyleOptionHeader, QHeaderView, QStyle
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QSize, QRect, QPoint



from pymdwizard.core import utils
from pymdwizard.core import xml_utils

from pymdwizard.gui.wiz_widget import WizardWidget
from pymdwizard.gui.ui_files import UI_Descriptor #


class Descriptor(WizardWidget): #

    drag_label = "Descriptor <descript>"
    acceptable_tags = ['abstract']

    def build_ui(self):
        """
        Build and modify this widget's GUI

        Returns
        -------
        None
        """
        self.ui = UI_Descriptor.Ui_Form()#.Ui_USGSContactInfoWidgetMain()
        self.ui.setupUi(self)
        self.setup_dragdrop(self)



    def dragEnterEvent(self, e):
        """
        Only accept Dragged items that can be converted to an xml object with
        a root tag called 'descript'
        Parameters
        ----------
        e : qt event

        Returns
        -------

        None
        """
        print("pc drag enter")
        mime_data = e.mimeData()
        if e.mimeData().hasFormat('text/plain'):
            parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
            element = etree.fromstring(mime_data.text(), parser=parser)
            if element is not None and element.tag == 'descript':
                e.accept()
        else:
            e.ignore()


         
                
    def _to_xml(self):
        """
        encapsulates the QPlainTextEdit text in an element tag

        Returns
        -------
        descript element tag in xml tree
        """
        descript = etree.Element('descript')

        abstract = etree.Element("abstract")
        abstract.text = self.findChild(QPlainTextEdit, "fgdc_abstract").toPlainText()
        descript.append(abstract)

        purpose = etree.Element("purpose")
        purpose.text = self.findChild(QPlainTextEdit, "fgdc_purpose").toPlainText()
        descript.append(purpose)

        supplinf_str = self.ui.fgdc_supplinf.toPlainText()
        if supplinf_str:
            upplinf = xml_utils.xml_node('supplinf', text=supplinf_str,
                                         parent_node=descript)

        return descript

    def _from_xml(self, descriptors):
        """
        parses the xml code into the relevant descript elements

        Parameters
        ----------
        access_constraints - the xml element status and its contents

        Returns
        -------
        None
        """
        try:
            if descriptors.tag == 'descript':
                try:

                    abstract = descriptors[0]
                    abstract_text = abstract.text
                    abstract_box = self.findChild(QPlainTextEdit, "fgdc_abstract")
                    abstract_box.setPlainText(abstract.text)

                    purpose = descriptors[1]
                    purpose_text = purpose.text
                    purpose_box = self.findChild(QPlainTextEdit, "fgdc_purpose")
                    purpose_box.setPlainText(purpose.text)

                    supplinf = descriptors[2]
                    supplinf_text = supplinf.text
                    supplinf_box = self.findChild(QPlainTextEdit, "fgdc_supplinf")
                    supplinf_box.setPlainText(supplinf.text)
                except:
                    abstract = descriptors[0]
                    abstract_text = abstract.text
                    abstract_box = self.findChild(QPlainTextEdit, "fgdc_abstract")
                    abstract_box.setPlainText(abstract.text)

                    purpose = descriptors[1]
                    purpose_text = purpose.text
                    purpose_box = self.findChild(QPlainTextEdit, "fgdc_purpose")
                    purpose_box.setPlainText(purpose.text)
            else:
               print ("The tag is not descript")
        except KeyError:
            pass


if __name__ == "__main__":
    utils.launch_widget(Descriptor,
                        "Descriptor testing")

