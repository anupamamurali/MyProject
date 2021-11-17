import base64
import io
from odoo import models


class ReportPatientXls(models.AbstractModel):
    _name = 'report.hospital.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        print("mmmmmmm", data['form_data'])