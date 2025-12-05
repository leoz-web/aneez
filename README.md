 # انيز — لغة وصف عربية (Aneez v1)

[![CI](https://github.com/leoz-web/aneez/actions/workflows/python.yml/badge.svg)](https://github.com/leoz-web/aneez/actions/workflows/python.yml)
[![PyPI](https://img.shields.io/pypi/v/aneez.svg)](https://pypi.org/project/aneez) <!-- حدّث الرابط عند النشر -->
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

إصدار v1 — ملخّص
----------------
هذا المستودع يصدُر الآن كـ "v1.0.0" — إصدار مُستقر مخصّص للاستخدام الإنتاجي والبدء بتبني API الأساسية. في هذا الإصدار، تركّز انيز على توفير محرك تحويل مستقر (Lexer → Parser → AST → Renderer)، عناصر واجهة افتراضية، واجهة سطر أوامر، وحزمة قابلة للتوزيع عبر PyPI/GitHub Packages.

ما الجديد في v1.0.0
-------------------
- إطلاق أول إصدار مستقر (v1.0.0).
- واجهة CLI: `python -m aneez.cli render <input> <output>`.
- محرك رئيسي: lexer.py, parser.py, ast.py, renderer.py.
- عناصر افتراضية: رأس، قائمة، بطاقة، زر، نموذج، صورة، قسم، تذييل.
- أمثلة في `examples/`، واختبارات بسيطة في `tests/`.
- ملف pyproject.toml / setup.cfg مُعدّ لبناء الحزمة.

أهداف هذا الملف
---------------
- وصف طريقة إصدار v1 وتوزيع الحزمة.
- توضيح اسم الحزمة، نسخها، وكيفية بناء / نشر / تثبيت الحزمة.
- تعليمات واضحة للمساهمة في دورة إصدار (release flow).

معلومات الحزمة والإصدار
----------------------
- اسم الحزمة المقترح على PyPI: `aneez`
- إصدار البداية: `1.0.0` (Semantic Versioning)
  - تنسيق: MAJOR.MINOR.PATCH
  - تغييرات رئيسية وغير متوافقة: زيادة MAJOR
  - إضافة ميزات دون كسر التوافق: زيادة MINOR
  - إصلاحات صغيرة/باكشافات: زيادة PATCH

مكان تخزين رقم الإصدار:
- أنسب مكان لتتبع الإصدار هو في `aneez/__init__.py` كسطر وحيد:
  ```py
  __version__ = "1.0.0"
  ```
- ومن المستحسن أيضاً مزامنته مع `pyproject.toml` أو `setup.cfg` إن وُجد الحقل `version=` لضمان اتساق البنيات.

متطلبات الحزمة
--------------
- Python >= 3.8
- تبعيات (إن وُجدت) تُحدد في `pyproject.toml` أو `setup.cfg` تحت `install_requires`
  - مثال افتراضي (إن لم توجد تبعيات): لا توجد تبعيات خارجية إلزامية.

بناء الحزمة (Local build)
-------------------------
1. إنشاء بيئة معزولة وتفعيلها:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   pip install --upgrade build twine
   ```

2. بناء sdist و wheel:
   ```bash
   python -m build
   ```
   الناتج سيكون داخل `dist/` (*.tar.gz, *.whl).

نشر الحزمة إلى TestPyPI (اختباري)
--------------------------------
1. إنشاء حساب على https://test.pypi.org/ (إن لم يكن لديك).
2. رفع الحزمة لاختبار الرفع:
   ```bash
   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```
3. تثبيت واختبار النسخة من TestPyPI:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --no-deps aneez==1.0.0
   ```

نشر الحزمة إلى PyPI (Production)
---------------------------------
1. تأكّد من أن لديك حساب PyPI وأن ملف `~/.pypirc` مُعدّ إن رغبت.
2. رفع الحزمة:
   ```bash
   twine upload dist/*
   ```

استراتيجية إصدار على GitHub
---------------------------
نقترح اتباع الخطوات التالية لإطلاق إصدار v1.0.0 عبر Git/GitHub:

1. تحديد التغييرات النهائية وكتابة ملاحظة إصدار (release notes) في ملف CHANGELOG.md.
2. تحديث رقم الإصدار في:
   - `aneez/__init__.py` (`__version__ = "1.0.0"`)
   - إن وُجد، `pyproject.toml` أو `setup.cfg`
3. التزام (commit) التغييرات:
   ```bash
   git add aneez/__init__.py pyproject.toml CHANGELOG.md
   git commit -m "chore(release): v1.0.0"
   ```
4. إنشاء الوسم (tag) ودفعه:
   ```bash
   git tag -a v1.0.0 -m "Release v1.0.0"
   git push origin main --tags
   ```
5. فتح Release جديد على GitHub (يمكن أوتوماتيكيًا من خلال وسم tag) وإضافة ملاحظات الإصدار وروابط artifact إن وُجدت.

نموذج CHANGELOG (موجز)
----------------------
CHANGELOG.md
- 1.0.0 — YYYY-MM-DD
  - إصدار أول مستقر: محرك تحويل أساسي، CLI، عناصر افتراضية، أمثلة، واختبارات.

نصائح عملية قبل الإصدار
------------------------
- تأكد من أن جميع الاختبارات في CI تمر بنجاح.
- ارفع نسخة تجريبية إلى TestPyPI وجرّب التثبيت والتشغيل.
- تحقق من أن ملفات التوزيع تحتوي على:
  - README.md متضمّن في الحزمة (long_description).
  - LICENSE.
  - الملفات المصدرية الرئيسية داخل الحزمة `aneez/`.
- ضع ملف MANIFEST.in إن احتجت لتضمين ملفات غير بايثونية في الحَزمة.

تثبيت الإصدار المستقر
----------------------
بعد نشر v1.0.0 على PyPI، يمكن التثبيت مباشرة:
```bash
pip install aneez==1.0.0
```
أو تثبيت مباشرة من Git tag:
```bash
pip install git+https://github.com/leoz-web/aneez.git@v1.0.0
```

ماذا عن الحزم المتعدّدة (Extras) أو التوزيع على GitHub Packages؟
---------------------------------------------------------------
- Extras: يمكنك تعريف extras في `pyproject.toml` / `setup.cfg` مثل `aneez[dev]` يضيف تبعيات التطوير أو `aneez[full]` يضيف إمكانيات إضافية.
- GitHub Packages: اتبع توثيق GitHub Packages لرفع الحزمة كـ registry بديل، ثم ربط CI لنشر تلقائي عند إصدار tag.

قائمة فحص لإطلاق إصدار (Release checklist)
-----------------------------------------
- [ ] تحديث __version__
- [ ] تحديث CHANGELOG.md وملخص التغييرات
- [ ] اجتياز جميع اختبارات CI
- [ ] بناء الحزم محليًا وتجريب تثبيتها
- [ ] رفع للحزمة إلى TestPyPI للتجارب
- [ ] إنشاء Tag ودفعه إلى GitHub وفتح Release
- [ ] رفع الحزم إلى PyPI (أو GitHub Packages)
- [ ] نشر إشعار (Release notes) وروابط التنزيل

ملاحظات للمطورين والمساهمين
---------------------------
- للحفاظ على استقرار v1، أي تغييرات قد تكسر التوافق يجب أن تُقترح عبر Issue ومناقشتها قبل رفعها إلى الفرع الرئيسي.
- اقتراح الميزات غير المتوافقة يجب أن يُؤجل لإصدار v2 أو يتم تقديمها كخيار قابل للتفعيل عبر إعدادات أو Flags.


---
