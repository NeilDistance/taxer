# author: Neil Feng
from __future__ import absolute_import

from .config import tax_table

def overtime_pay(salary, overtime, ratio):
    daytime_salary = salary / 21.75
    hourtime_salary = daytime_salary / 8
    return hourtime_salary * ratio * overtime

def overtime_pay_weekend(salary, overtime):
    return overtime_pay(salary, overtime, ratio=2)

def overtime_pay_workday(salary, overtime):
    return overtime_pay(salary, overtime, ratio=1.5)

def overtime_pay_holiday(salary, overtime):
    return overtime_pay(salary, overtime, ratio=3)

def tax(income2tax):
    assert income2tax >= 0
    for range, value in tax_table.iteritems():
        if range[0] <= income2tax <= range[1]:
            return income2tax*value["ratio"] - value["fast"]
    return 0

