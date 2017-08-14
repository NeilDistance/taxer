from __future__ import absolute_import

from compute import tax, overtime_pay_weekend
from PyQt5 import QtWidgets

salary = 15000
start_line = 3500
insure = 3060

total = salary+overtime_pay_weekend(salary, 22.6)
print "total:{:.0f}".format(total)

income2tax = total - start_line - insure
print "income2tax:{:.0f}".format(income2tax)

taxed = tax(income2tax)
print "taxed:{:.0f}".format(taxed)

inhand = total - insure - taxed
print "inhand:{:.0f}".format(inhand)