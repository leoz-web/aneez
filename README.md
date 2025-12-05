# انيز — لغة وصف عربية (Aneez v2)

**نبذة**
انيز (Aneez) هي لغة وصف DSL بالعربية تبسّط إنشاء صفحات واجهة ويب باستخدام وسوم عربية ومكائن جاهزة مثل قائمة، بطاقات، أزرار، نماذج، صورة، رأس وتذييل... يمكن تحويل ملفات `.aneez` إلى HTML جاهز للعرض.

**المحتويات**
- package: `aneez/` (الشفرة المصدرية)
  - lexer.py, parser.py, ast.py, renderer.py, elements.py, cli.py
- examples/: أمثلة قابلة للتحويل
- assets/: أيقونة SVG ولوجو صغير
- tests/: اختبارات بسيطة
- setup.cfg, setup.py, pyproject.toml, LICENSE, .gitignore
- .github/workflows/python.yml (CI: pytest)

**التثبيت**
```
unzip aneez_v2_lang.zip -d aneex_out
cd aneex_out/aneez_v2_lang
pip install -e .
```

**استخدام CLI**
```
python -m aneez.cli render examples/example.aneez output.html
```

**أمثلة**
راجع `examples/example.aneez` لرؤية كيفية استعمال العناصر الجديدة: <رأس>, <قائمة>, <بطاقة>, <زر>, <نموذج>, <صورة>, <قسم>, <تذييل>.

**تطوير**
- دعم سمات للوسوم (.attr(key="value"))
- توسيع محرك العناصر وإخراج CSS/JS مدمج
- دعم قوالب ديناميكية ومتغيرات

