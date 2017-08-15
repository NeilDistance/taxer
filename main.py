from __future__ import absolute_import

import sys
from compute import tax, overtime_pay_weekend, overtime_pay_workday, overtime_pay_statutory
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi

def changEnable(widget, state):
    if widget.isEnabled():
        widget.clear()
        widget.setEnabled(False)
    else:
        widget.setEnabled(True)

app = QApplication(sys.argv)
ui = loadUi("taxer.ui")

def calc(ui):
    salary = float(ui.salary.text())
    start_line = float(ui.start_line.text())
    insure_fund = float(ui.insure_fund.text())

    weekend_overtime_str = ui.weekend_overtime.text()
    workday_overtime_str = ui.workday_overtime.text()
    statutory_overtime_str = ui.statutory_overtime.text()
    bonus = 0.0
    if weekend_overtime_str:
        weekend_overtime = float(weekend_overtime_str)
        bonus += overtime_pay_weekend(salary, weekend_overtime)

    if workday_overtime_str:
        workday_overtime = float(workday_overtime_str)
        bonus += overtime_pay_workday(salary, workday_overtime)

    if statutory_overtime_str:
        statutory_overtime = float(statutory_overtime_str)
        bonus += overtime_pay_statutory(salary, statutory_overtime)

    salary += bonus
    salary2taxed = salary - start_line - insure_fund
    taxed_payment = tax(salary2taxed)
    net_pay = salary - taxed_payment -insure_fund

    ui.taxable_wages.setText("{:.1f}".format(salary2taxed))
    ui.taxation.setText("{:.1f}".format(taxed_payment))
    ui.net_pay.setText("{:.1f}".format(net_pay))

def reset(ui):
    for edit in ("insure_fund", "salary", "start_line", "statutory_overtime",
                 "weekend_overtime", "workday_overtime", "net_pay", "taxable_wages", "taxation"):
        getattr(ui, edit).clear()

#widget = QWidget()
#print dir(ui.weekend_check)
ui.weekend_check.stateChanged.connect(lambda state:changEnable(ui.weekend_overtime, state))
#print dir(ui.weekend_overtime)
ui.workday_check.stateChanged.connect(lambda state:changEnable(ui.workday_overtime, state))
ui.statutory_check.stateChanged.connect(lambda state:changEnable(ui.statutory_overtime, state))

ui.reset_btn.clicked.connect(lambda :reset(ui))

ui.calc_btn.clicked.connect(lambda :calc(ui))

ui.show()
sys.exit(app.exec_())