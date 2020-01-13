from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

def set_if_not_none(parameters, key, value):
	if value:
		parameters[key] = value

# DEVICE MODEL
DEVICE_APP_CHOICES = (
	(1, "Εργασίες"),
	(2, "Τεχνικές Εκθέσεις")
)

# TASK MODEL
TASK_STATUS_CHOICES = (
	(1, "Σε εκκρεμότητα"),
	(2, "Σε επισκευή"),
	(3, "Ολοκληρωμένες")
)

# EVENT MODEL
EVENT_STATUS_CHOICES = (
	(1, "Σε εκκρεμότητα"),
	(2, "Ολοκληρωμένη")
)