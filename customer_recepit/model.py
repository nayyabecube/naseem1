#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################
from openerp import models, fields, api
from num2words import num2words
import time


class SampleDevelopmentReport(models.AbstractModel):
    _name = 'report.customer_recepit.module_report'

    @api.model
    def render_html(self,docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('customer_recepit.module_report')
        records = self.env['customer.payment.bcube'].browse(docids)

        def number_to_word(attrb):
            word = num2words((attrb))
            word = word.title() + " " + "Only"
            return word

        def get_time():
            t0 = time.time()
            t1 = t0 + (60*60)*5 
            new = time.strftime("%I:%M",time.localtime(t1))

            return new


        docargs = {
            'doc_ids': docids,
            'doc_model': 'customer.payment.bcube',
            'docs': records,
            'data': data,
            'get_time': get_time,
            'number_to_word':number_to_word,

            }

        return report_obj.render('customer_recepit.module_report', docargs)