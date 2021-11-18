import base64
import io
from odoo import models


class ReportPatientXls(models.AbstractModel):
    _name = 'report.hospital.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        sheet = workbook.add_worksheet('op')
        bold = workbook.add_format({'bold': True})
        sheet.set_column('A:A', 6)
        sheet.set_column('B:B', 13)
        sheet.set_column('C:C', 26)
        sheet.set_column('D:D', 12)
        sheet.set_column('E:E', 22)
        sheet.set_column('F:F', 12)
        sheet.set_column('G:G', 15)
        sheet.merge_range('D1:E1', 'MEDICAL REPORT', bold)
        form_data = data['form_data']
        patient_id = form_data['patient_card'][1]
        patient_name = form_data['patient_name'][1]
        patient_reference = patient_id + patient_name
        sheet.merge_range('C3:E3', patient_reference, bold)
        doctor = 'Doctor : ' + form_data['doctor'][1]
        sheet.merge_range('C5:E5', doctor)
        date_from = 'Date From : ' + form_data['date_from']
        date_to = 'Date To :' + form_data['date_to']
        date = date_from + '          ' + date_to
        sheet.merge_range('C6:E6', date)
        row = 8
        col = 0
        sheet.write(row, col, 'SL.No', bold)
        sheet.write(row, col+1, 'OP Reference', bold)
        sheet.write(row, col+2, 'Patient name', bold)
        sheet.write(row, col+3, 'Date', bold)
        sheet.write(row, col+4, 'Doctor', bold)
        sheet.write(row, col+5, 'Department', bold)
        sheet.write(row, col+6, 'Disease', bold)
        count = 0
        for op in data['op']:
            row += 1
            count += 1
            sheet.write(row, col, count)
            sheet.write(row, col + 1, op['name'])
            sheet.write(row, col + 2, op['patient_name'][1])
            sheet.write(row, col + 3, op['date'])
            sheet.write(row, col + 4, op['doctor'][1])
            sheet.write(row, col + 5, op['department'][1])
            sheet.write(row, col + 6, op['disease'][1])