from clientele.settings import BASE_DIR
from clientele.utils import render_to_pdf
from django.core.files.base import ContentFile

def GeneratePdf(instance):
	spare_parts = instance.spare_parts.split("\n")
	data = {
		'tech_report_id': instance.id,
		'last_name': instance.task_dty_id.client_id.last_name,
		'first_name': instance.task_dty_id.client_id.first_name,
		'task_dty_code_number': instance.task_dty_id.code_number,
		'task_dty_date': instance.task_dty_id.date,
		'spare_parts': spare_parts,
		'tech_date': instance.date,
		'text': instance.text,
		'BASE_DIR': BASE_DIR,
	}
	pdf = render_to_pdf('tech_report_pdf.html', data)
	file = ContentFile(b"%s" % pdf)
	instance.pdf.save('%s-%s.pdf' % (instance.id, instance.filename), file)