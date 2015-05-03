#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:       Ivan Fontarensky
@license:      GNU General Public License 3.0
@contact:      ivan.fontarensky_at_gmail.com
"""


__docformat__ = 'restructuredtext'
__author__ = 'ifontarensky'

try:
    import qdarkstyle
    stylesheet_darkstyle = qdarkstyle.load_stylesheet(pyside=False)
except:
    stylesheet_darkstyle = None

stylesheet_xmas = """

/*
    qmc2-xmas: v0.5, 11-JAN-2011, rene.reucher@batcom-it.net

    Qt style sheet compatible with QMC2 0.2.b10+

    http://qmc2.arcadehits.net/wordpress/style-sheets/

    Changes:

    v0.5 - updated to 0.2.b19
    v0.4 - updated to 0.2.b17
    v0.3 - updated to 0.2.b15
    v0.2 - solid black logo backround (about dialog)
    v0.1 - initial version
*/

QWidget {
    color: lightgrey;
    background-color: rgba(0, 0, 22, 128);
}

QDialog,
Options,
QSplitter,
QScrollArea,
QScrollArea *,
Preview,
Flyer,
Cabinet,
Title,
Marquee,
Controller,
PCB {
    background-image: url(main-bg.png);
    background-position: top left;
    background-origin: content;
}

QTabWidget {
    background-color: rgba(0, 34, 255, 128);
    border: 0px solid gray;
    padding: 0px;
    border-radius: 0px;
}

QTabBar {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 34, 255, 128), stop:1 rgba(255, 255, 255, 128));
}

QLabel {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 34, 255, 128), stop:1 rgba(255, 255, 255, 128));
}

QLabel#labelGameStatus {
    background: none;
}

QLabel#labelGamelistStatus {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 34, 255, 128), stop:1 rgba(255, 255, 255, 128));
}

QLabel#labelProjectInfo {
   color: rgba(255, 255, 255, 128);
   background-image: url(about-bg.png);
   background-repeat: no-repeat;
   background-position: center;
   min-width: 600;
   max-width: 600;
   min-height: 439;
   max-height: 439;
}

QLabel#labelLogoPixmap {
    background: black;
}

QListWidget#listWidgetFavorites,
QListWidget#listWidgetPlayed,
QListWidget#listWidgetSearch,
QTreeWidget#treeWidgetCategoryView,
QTreeWidget#treeWidgetVersionView,
QTreeWidget#treeWidgetGamelist,
QTreeWidget#treeWidgetHierarchy {
    border-image: url(gamelist-bg.png) repeat;
    background-color: rgba(0, 34, 255, 128);
}

QLabel#labelLoadingGamelist,
QLabel#labelLoadingHierarchy,
QLabel#labelCreatingCategoryView,
QLabel#labelCreatingVersionView {
    border-image: url(gamelist-bg.png) repeat;
    background-color: rgba(0, 34, 255, 64);
}

QTreeView,
QListView,
QPlainTextEdit,
QTextBrowser {
    selection-color: darkblue;
    selection-background-color: white;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 34, 255, 128), stop:1 rgba(255, 255, 255, 128));
    min-width: 14px;
    min-height: 14px;
    border: 1px solid gray;
    padding: 2px;
    border-radius: 3px;
}

QMenu,
QComboBox,
QComboBox::drop-down {
    color: darkblue;
    selection-color: darkblue;
    selection-background-color: white;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0, 34, 255), stop:1 rgb(255, 255, 255));
    min-width: 14px;
    min-height: 14px;
    border: 1px solid gray;
    padding: 2px;
    border-radius: 3px;
}

QComboBox::down-arrow {
    image: url(down-arrow.png);
}

QComboBox::down-arrow:on { /* shift the arrow when popup is open */
    top: 1px;
    left: 1px;
}

QComboBox:on { /* shift the text when the popup opens */
    padding-top: 3px;
    padding-left: 4px;
}

QSpinBox,
QDoubleSpinBox,
QLineEdit {
    color: darkblue;
    selection-color: darkblue;
    selection-background-color: white;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0, 34, 255), stop:1 rgb(255, 255, 255));
    min-width: 14px;
    min-height: 14px;
    border: 1px solid gray;
    padding: 2px;
    border-radius: 3px;
}

QMenuBar {
    background-color: rgba(0, 0, 22, 128);
}

QMenuBar::item {
    color: white;
    selection-color: white;
    selection-background-color: darkblue;
    background-color: rgba(0, 34, 255, 128);
    border: 1px solid gray;
    border-radius: 3px;
    spacing: 3px;
    padding: 3px;
}

QMenuBar::item:selected {
    background-color: white;
    color: darkblue;
}

QPushButton,
QToolButton {
    color: white;
    selection-color: darkblue;
    selection-background-color: white;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0, 34, 255), stop:1 rgb(255, 255, 255));
    border: 1px solid gray;
    padding: 2px;
    border-radius: 3px;
}

QPushButton:hover,
QToolButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(255, 255, 255), stop:1 rgb(0, 34, 255));
}

QPushButton:pressed,
QToolButton:pressed,
QPushButton:on,
QToolButton:on {
    background: darkblue;
}

QToolButton::menu-arrow {
    image: url(down-arrow.png);
}

QCheckBox {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 34, 255, 128), stop:1 rgba(255, 255, 255, 128));
}

QGroupBox::indicator,
QCheckBox::indicator {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 34, 255, 128), stop:1 rgba(255, 255, 255, 128));
    width: 14px;
    height: 14px;
    border: 1px solid gray;
    padding: 1px;
    border-radius: 3px;
}

QGroupBox::indicator:checked,
QCheckBox::indicator:checked {
    image: url(ok.png);
}

QRadioButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 34, 255, 128), stop:1 rgba(255, 255, 255, 128));
}

QRadioButton::indicator {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 34, 255), stop:1 rgb(255, 255, 255));
    width: 7px;
    height: 7px;
    border: 1px solid gray;
    padding: 1px;
    border-radius: 5px;
}

QRadioButton::indicator:checked {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 34, 255), stop:1 black);
    width: 7px;
    height: 7px;
    border: 1px solid gray;
    padding: 1px;
    border-radius: 5px;
}

QGroupBox::title {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 34, 255, 64), stop:1 rgba(255, 255, 255, 64));
    color: white;
}

QTreeView::item:hover,
QListView::item:hover,
QMenu::item:selected,
QMenu::item:hover,
QProgressBar {
    background-color: darkblue;
    color: white;
}

QTreeWidget#treeWidgetCategoryView::item:hover,
QTreeWidget#treeWidgetVersionView::item:hover,
QTreeWidget#treeWidgetGamelist::item:hover,
QTreeWidget#treeWidgetHierarchy::item:hover {
    background-color: darkblue;
    color: white;
    show-decoration-selected: 1;
    padding-left: 30px;
    margin-left: -25px;
}

QTreeWidget#treeWidgetCategoryView::item:selected,
QTreeWidget#treeWidgetVersionView::item:selected,
QTreeWidget#treeWidgetGamelist::item:selected,
QTreeWidget#treeWidgetHierarchy::item:selected {
    background-color: white;
    color: darkblue;
    show-decoration-selected: 1;
    padding-left: 30px;
    margin-left: -25px;
}

QHeaderView {
    background: rgb(0, 34, 255);
}

QRadioButton:hover,
QCheckBox:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 34, 255), stop:1 rgb(255, 255, 255));
}

QToolTip {
    color: white;
    background: darkblue;
    border: 1px solid gray;
    padding: 2px;
    border-radius: 3px;
}

QSplitter::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 darkblue, stop:1 white);
    border: 1px solid rgb(50, 50, 50);
    width: 2px;
    height: 2px;
    border-radius: 1px;
}

QSplitter::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 darkblue, stop:1 white);
}

QProgressBar:horizontal {
    border: 1px solid gray;
    border-radius: 3px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 darkblue, stop:1 rgba(0, 34, 255, 128));
    padding: 0px;
    text-align: center;
}

QProgressBar:vertical {
    border: 1px solid gray;
    border-radius: 3px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 darkblue, stop:1 rgba(0, 34, 255, 128));
    padding: 0px;
    text-align: center;
}

QProgressBar::chunk:horizontal {
    background-color: rgb(0, 34, 255);
    width: 1px;
}

QProgressBar::chunk:vertical {
    background-color: rgb(0, 34, 255);
    height: 1px;
}

QProgressBar:disabled {
    color: white;
}

QHeaderView::down-arrow {
    image: url(down-arrow.png);
}

QHeaderView::up-arrow {
    image: url(up-arrow.png);
}

QTreeView {
    alternate-background-color: rgba(0, 34, 255, 64);
    paint-alternating-row-colors-for-empty-area: true;
    show-decoration-selected: 0;
}

QTreeView::branch:has-siblings:!adjoins-item {
    border-image: url(vline.png) 0;
}

QTreeView::branch:has-siblings:adjoins-item {
    border-image: url(branch-more.png) 0;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url(branch-end.png) 0;
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    border-image: none;
    image: url(branch-closed.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings {
    border-image: none;
    image: url(branch-open.png);
}

QSlider::groove:horizontal {
    border: 1px solid #999999;
    height: 8px;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 white, stop:1 rgba(0, 34, 255, 64));
    margin: 2px 0;
}

QSlider::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 34, 255), stop:1 white);
    border: 1px solid #5c5c5c;
    width: 20px;
    margin: -2px 0;
    border-radius: 3px;
}

QMessageBox {
    messagebox-text-interaction-flags: 5 /* text can be selected and copied to clipboard */
}

QScrollBar:horizontal {
    border: 1px solid lightgrey;
    background: darkblue;
    height: 15px;
    margin: 0px 21px 0px 21px;
}

QScrollBar::handle:horizontal {
    background: white;
    min-width: 20px;
}

QScrollBar::add-line:horizontal {
    border: 1px solid lightgrey;
    background: darkblue;
    width: 20px;
    subcontrol-position: top right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
    border: 1px solid lightgrey;
    background: darkblue;
    width: 20px;
    subcontrol-position: top left;
    subcontrol-origin: margin;
}

QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
    border: 1px solid lightgrey;
    width: 3px;
    height: 3px;
    background: white;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

QScrollBar:vertical {
    border: 1px solid lightgrey;
    background: darkblue;
    width: 15px;
    margin: 21px 0px 21px 0px;
}

QScrollBar::handle:vertical {
    background: white;
    min-height: 20px;
}

QScrollBar::add-line:vertical {
    border: 1px solid lightgrey;
    background: darkblue;
    height: 20px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical {
    border: 1px solid lightgrey;
    background: darkblue;
    height: 20px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
    border: 1px solid lightgrey;
    width: 3px;
    height: 3px;
    background: white;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

"""

stylesheet_darkorange = """
QToolTip
{
     border: 1px solid black;
     background-color: #ffa02f;
     padding: 1px;
     border-radius: 3px;
     opacity: 100;
}

QWidget
{
    color: #b1b1b1;
    background-color: #323232;
}

QWidget:item:hover
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);
    color: #000000;
}

QWidget:item:selected
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 1px solid #ffaa00;
}

QMenuBar::item:pressed
{
    background: #444;
    border: 1px solid #000;
    background-color: QLinearGradient(
        x1:0, y1:0,
        x2:0, y2:1,
        stop:1 #212121,
        stop:0.4 #343434/*,
        stop:0.2 #343434,
        stop:0.1 #ffaa00*/
    );
    margin-bottom:-1px;
    padding-bottom:1px;
}

QMenu
{
    border: 1px solid #000;
}

QMenu::item
{
    padding: 2px 20px 2px 20px;
}

QMenu::item:selected
{
    color: #000000;
}

QWidget:disabled
{
    color: #404040;
    background-color: #323232;
}

QAbstractItemView
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);
}

QWidget:focus
{
    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/
}

QLineEdit
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);
    padding: 1px;
    border-style: solid;
    border: 1px solid #1e1e1e;
    border-radius: 5;
}

QPushButton
{
    color: #b1b1b1;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-width: 1px;
    border-color: #1e1e1e;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 12px;
    padding-left: 5px;
    padding-right: 5px;
}

QPushButton:pressed
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
}

QComboBox
{
    selection-background-color: #ffaa00;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-style: solid;
    border: 1px solid #1e1e1e;
    border-radius: 5;
}

QComboBox:hover,QPushButton:hover
{
    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}


QComboBox:on
{
    padding-top: 3px;
    padding-left: 4px;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
    selection-background-color: #ffaa00;
}

QComboBox QAbstractItemView
{
    border: 2px solid darkgray;
    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QComboBox::drop-down
{
     subcontrol-origin: padding;
     subcontrol-position: top right;
     width: 15px;

     border-left-width: 0px;
     border-left-color: darkgray;
     border-left-style: solid; /* just a single line */
     border-top-right-radius: 3px; /* same radius as the QComboBox */
     border-bottom-right-radius: 3px;
 }

QComboBox::down-arrow
{
     image: url(:/down_arrow.png);
}

QGroupBox:focus
{
border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QTextEdit:focus
{
    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QScrollBar:horizontal {
     border: 1px solid #222222;
     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
     height: 7px;
     margin: 0px 16px 0 16px;
}

QScrollBar::handle:horizontal
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);
      min-height: 20px;
      border-radius: 2px;
}

QScrollBar::add-line:horizontal {
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);
      width: 14px;
      subcontrol-position: right;
      subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);
      width: 14px;
     subcontrol-position: left;
     subcontrol-origin: margin;
}

QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal
{
      border: 1px solid black;
      width: 1px;
      height: 1px;
      background: white;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
      background: none;
}

QScrollBar:vertical
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
      width: 7px;
      margin: 16px 0 16px 0;
      border: 1px solid #222222;
}

QScrollBar::handle:vertical
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);
      min-height: 20px;
      border-radius: 2px;
}

QScrollBar::add-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
      height: 14px;
      subcontrol-position: bottom;
      subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);
      height: 14px;
      subcontrol-position: top;
      subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
      border: 1px solid black;
      width: 1px;
      height: 1px;
      background: white;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
      background: none;
}

QTextEdit
{
    background-color: #242424;
}

QPlainTextEdit
{
    background-color: #242424;
}

QHeaderView::section
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
}

QCheckBox:disabled
{
color: #414141;
}

QDockWidget::title
{
    text-align: center;
    spacing: 3px; /* spacing between items in the tool bar */
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);
}

QDockWidget::close-button, QDockWidget::float-button
{
    text-align: center;
    spacing: 1px; /* spacing between items in the tool bar */
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover
{
    background: #242424;
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed
{
    padding: 1px -1px -1px 1px;
}

QMainWindow::separator
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    border: 1px solid #4c4c4c;
    spacing: 3px; /* spacing between items in the tool bar */
}

QMainWindow::separator:hover
{

    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
    spacing: 3px; /* spacing between items in the tool bar */
}

QToolBar::handle
{
     spacing: 3px; /* spacing between items in the tool bar */
     background: url(:/images/handle.png);
}

QMenu::separator
{
    height: 2px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;
}

QProgressBar
{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk
{
    background-color: #d7801a;
    width: 2.15px;
    margin: 0.5px;
}

QTabBar::tab {
    color: #b1b1b1;
    border: 1px solid #444;
    border-bottom-style: none;
    background-color: #323232;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 3px;
    padding-bottom: 2px;
    margin-right: -1px;
}

QTabWidget::pane {
    border: 1px solid #444;
    top: 1px;
}

QTabBar::tab:last
{
    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
    border-top-right-radius: 3px;
}

QTabBar::tab:first:!selected
{
 margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */


    border-top-left-radius: 3px;
}

QTabBar::tab:!selected
{
    color: #b1b1b1;
    border-bottom-style: solid;
    margin-top: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);
}

QTabBar::tab:selected
{
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    margin-bottom: 0px;
}

QTabBar::tab:!selected:hover
{
    /*border-top: 2px solid #ffaa00;
    padding-bottom: 3px;*/
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);
}

QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{
    color: #b1b1b1;
    background-color: #323232;
    border: 1px solid #b1b1b1;
    border-radius: 6px;
}

QRadioButton::indicator:checked
{
    background-color: qradialgradient(
        cx: 0.5, cy: 0.5,
        fx: 0.5, fy: 0.5,
        radius: 1.0,
        stop: 0.25 #ffaa00,
        stop: 0.3 #323232
    );
}

QCheckBox::indicator{
    color: #b1b1b1;
    background-color: #323232;
    border: 1px solid #b1b1b1;
    width: 9px;
    height: 9px;
}

QRadioButton::indicator
{
    border-radius: 6px;
}

QRadioButton::indicator:hover, QCheckBox::indicator:hover
{
    border: 1px solid #ffaa00;
}

QCheckBox::indicator:checked
{
    image:url(:/images/checkbox.png);
}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled
{
    border: 1px solid #444;
}


"""

stylesheet_metal = """
/*
    qmc2-metal: v0.9, 11-JAN-2011, rene.reucher@batcom-it.net

    Qt style sheet compatible with QMC2 0.2.b10+

    http://qmc2.arcadehits.net/wordpress/style-sheets/

    Changes:

    v0.9 - updated to 0.2.b19
    v0.8 - updated to 0.2.b17
    v0.7 - updated to 0.2.b15
    v0.6 - updated to 0.2.b12
    v0.5 - updated to 0.2.b11
    v0.4 - corrected button resize issues
    v0.3 - added PCB class and button on/pressed states
    v0.2 - added border image for game/machine lists
    v0.1 - initial version
*/

QDialog,
QTabWidget,
QTabBar,
QMenuBar,
QWebView,
QMainWindow,
Options,
QSplitter,
QScrollArea,
QScrollArea *,
Preview,
Flyer,
Cabinet,
Title,
Marquee,
Controller,
PCB {
    background-color: rgb(222, 222, 222);
    background-image: url(main-bg.png);
    background-position: top left;
    background-origin: content;
}

QLabel#labelLoadingGamelist,
QLabel#labelLoadingHierarchy,
QLabel#labelCreatingCategoryView,
QLabel#labelCreatingVersionView,
QListWidget#listWidgetFavorites,
QListWidget#listWidgetPlayed,
QListWidget#listWidgetSearch,
QTreeWidget#treeWidgetCategoryView,
QTreeWidget#treeWidgetVersionView,
QTreeWidget#treeWidgetGamelist,
QTreeWidget#treeWidgetHierarchy {
    border-image: url(gamelist-bg.png) repeat;
}

QTreeView,
QListView,
QLineEdit,
QTextBrowser,
QPlainTextEdit,
QSpinBox,
QDoubleSpinBox,
QComboBox,
QMenu {
    selection-color: black;
    selection-background-color: rgb(162, 162, 162);
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222, 222, 222), stop:1 white);
    min-width: 14px;
    min-height: 14px;
    border: 1px solid gray;
    padding: 2px;
    border-radius: 3px;
}

QPushButton,
QToolButton {
    selection-color: black;
    selection-background-color: rgb(162, 162, 162);
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222, 222, 222), stop:1 white);
    border: 1px solid gray;
    padding: 2px;
    border-radius: 3px;
}

QPushButton:hover,
QToolButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 white, stop:1 rgb(222, 222, 222));
}

QPushButton:pressed,
QToolButton:pressed,
QPushButton:on,
QToolButton:on {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222, 222, 222), stop:1 black);
}

QToolButton[flat=true], QToolButton[flat=true]:hover {
    border: 0px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 white, stop:1 rgb(222, 222, 222));
}

QCheckBox::indicator {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222, 222, 222), stop:1 white);
    width: 14px;
    height: 14px;
    border: 1px solid gray;
    padding: 1px;
    border-radius: 3px;
}

QCheckBox::indicator:checked {
    image: url(ok.png);
}

QRadioButton::indicator {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222, 222, 222), stop:1 white);
    width: 7px;
    height: 7px;
    border: 1px solid gray;
    padding: 1px;
    border-radius: 5px;
}

QRadioButton::indicator:checked {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(170, 170, 170), stop:1 black);
    width: 7px;
    height: 7px;
    border: 1px solid gray;
    padding: 1px;
    border-radius: 5px;
}

QListView::item:hover,
QTreeView::item:hover,
QRadioButton:hover,
QCheckBox:hover,
QMenu::item:selected,
QHeaderView,
QScrollBar,
QProgressBar {
    background-color: rgb(202, 202, 202);
}

QToolTip {
    background-color: rgb(202, 202, 202);
    opacity: 128; /* with an active composition manager, this should look semi-transparent */
}

QSplitter::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(162, 162, 162), stop:1 rgb(222, 222, 222));
    border: 1px solid #5c5c5c;
    width: 2px;
    height: 2px;
    border-radius: 1px;
}

QSplitter::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(162, 162, 162), stop:1 rgb(222, 222, 222));
    border: 1px solid #5c5c5c;
    width: 2px;
    height: 2px;
    border-radius: 1px;
}

QProgressBar:horizontal {
    border: 1px solid gray;
    border-radius: 3px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 white, stop:1 rgb(222, 222, 222));
    padding: 0px;
    text-align: center;
}

QProgressBar::chunk:horizontal {
    background-color: rgb(162, 162, 162);
    width: 1px;
}

QProgressBar:vertical {
    border: 1px solid gray;
    border-radius: 3px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 white, stop:1 rgb(222, 222, 222));
    padding: 0px;
    text-align: center;
}

QProgressBar::chunk:vertical {
    background-color: rgb(162, 162, 162);
    height: 1px;
}

QProgressBar:disabled {
    color: white;
}

QHeaderView::down-arrow {
    image: url(down-arrow.png);
}

QHeaderView::up-arrow {
    image: url(up-arrow.png);
}

QTreeView {
    alternate-background-color: rgb(222, 222, 222);
    paint-alternating-row-colors-for-empty-area: true;
    show-decoration-selected: 0;
}

QTreeView::branch:has-siblings:!adjoins-item {
    border-image: url(vline.png) 0;
}

QTreeView::branch:has-siblings:adjoins-item {
    border-image: url(branch-more.png) 0;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url(branch-end.png) 0;
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    border-image: none;
    image: url(branch-closed.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings {
    border-image: none;
    image: url(branch-open.png);
}

QSlider::groove:horizontal {
    border: 1px solid #999999;
    height: 8px;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 white, stop:1 rgb(222, 222, 222));
    margin: 2px 0;
}

QSlider::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(162, 162, 162), stop:1 rgb(222, 222, 222));
    border: 1px solid #5c5c5c;
    width: 20px;
    margin: -2px 0;
    border-radius: 3px;
}

QMessageBox {
    messagebox-text-interaction-flags: 5 /* text can be selected and copied to clipboard */
}


"""

stylesheet_oxygen = """

QLabel#labelGamelistStatus {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 64), stop:1 rgba(255, 255, 255, 0));
}

"""