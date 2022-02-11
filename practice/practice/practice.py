from jinja2 import Environment

template = open("email.j2", "r").read()
templated = Environment().from_string(template).render(noobAccount='nora.yang.a00814',Password='Today@0214',Email='nora.yang.a00814@oppo-aed.tw',printer='345621')
open("nora.yang.a00814.html", "w").write(templated)