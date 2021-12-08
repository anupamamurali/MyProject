import base64
import io
from odoo import models


class ReportPatientXls(models.AbstractModel):
    _name = 'report.hospital.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        sheet = workbook.add_worksheet('op')
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '14px'})
        col_head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '12px'})
        bold = workbook.add_format({'bold': True})
        sheet.set_column('A:A', 6)
        sheet.set_column('B:B', 13)
        sheet.set_column('C:C', 26)
        sheet.set_column('D:D', 12)
        sheet.set_column('E:E', 22)
        sheet.set_column('F:F', 12)
        sheet.set_column('G:G', 15)
        sheet.merge_range('D1:E1', 'MEDICAL REPORT', head)
        form_data = data['form_data']
        if form_data['patient_card_id'] and form_data['patient_name_id']:
            patient_id = form_data['patient_card_id'][1]
            patient_name = form_data['patient_name_id'][1]
            patient_reference = patient_id + '  ' + patient_name
        else:
            patient_reference = ' ' + '  ' + ' '
        sheet.merge_range('C3:E3', patient_reference, bold)
        if form_data['doctor_id']:
            doctor = 'Doctor : ' + form_data['doctor_id'][1]
        else:
            doctor = 'Doctor : ' + ' '
        sheet.merge_range('C5:E5', doctor)
        if form_data['date_from']:
            date_from = 'Date From : ' + form_data['date_from']
        else:
            date_from = 'Date From : ' + ' '
        sheet.merge_range('C6:D6', date_from)
        if form_data['date_to']:
            date_to = 'Date To : ' + form_data['date_to']
        else:
            date_to = 'Date To : ' + ' '
        sheet.merge_range('C7:D7', date_to)
        row = 8
        col = 0
        sheet.write(row, col, 'SL.No', col_head)
        sheet.write(row, col + 1, 'OP Reference', col_head)
        sheet.write(row, col + 2, 'Patient name', col_head)
        sheet.write(row, col + 3, 'Date', col_head)
        sheet.write(row, col + 4, 'Doctor', col_head)
        sheet.write(row, col + 5, 'Department', col_head)
        sheet.write(row, col + 6, 'Disease', col_head)
        count = 0
        for op in data['op']:
            row += 1
            count += 1
            sheet.write(row, col, count)
            sheet.write(row, col + 1, op['op'])
            sheet.write(row, col + 2, op['patient_name'])
            sheet.write(row, col + 3, op['date'])
            sheet.write(row, col + 4, op['doctor'])
            sheet.write(row, col + 5, op['department'])
            sheet.write(row, col + 6, op['disease'])
