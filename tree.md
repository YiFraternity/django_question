.
├── data
│   ├── experimentProblemJson.json
│   ├── factorProblemJson.json
│   ├── outputProblemJson.json
│   ├── pigmentProblemJson.json
│   ├── rawoutputOfFunctionProblemJson.json
│   ├── rawoutputOfRelationProblemJson.json
│   ├── rawoutputOfWhatsProblemJson.json
│   └── rawProblemJson.json
├── dealJson
│   ├── encodeFileToJson.py
│   ├── experimentProblemToJson.py
│   ├── factorProblemToJson.py
│   ├── outputProblemToJson.py
│   ├── pigmentProblemToJson.py
│   ├── __pycache__
│   │   └── encodeFileToJson.cpython-36.pyc
│   ├── rawoutputOfFunctionProblemToJson.py
│   ├── rawoutputOfRelationProblemToJson.py
│   ├── rawoutputOfWhatsProblemToJson.py
│   ├── rawProblemToJson.py
│   └── test.json
├── django_question
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── question
│   ├── admin.py
│   ├── answer.py
│   ├── apps.py
│   ├── calculation.py
│   ├── config.py
│   ├── Dfile.py
│   ├── forms.py
│   ├── __init__.py
│   ├── lib
│   │   ├── const.py
│   │   └── __pycache__
│   │       └── const.cpython-36.pyc
│   ├── log
│   │   ├── difficulty-question.txt
│   │   ├── error.txt
│   │   └── synonyms-dict.txt
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20180514_0748.py
│   │   ├── 0003_auto_20180514_1449.py
│   │   ├── 0004_auto_20180515_1043.py
│   │   ├── 0005_question_img_location.py
│   │   ├── 0006_auto_20180521_0200.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-36.pyc
│   │       ├── 0002_auto_20180514_0748.cpython-36.pyc
│   │       ├── 0003_auto_20180514_1449.cpython-36.pyc
│   │       ├── 0004_auto_20180515_1043.cpython-36.pyc
│   │       ├── 0005_question_img_location.cpython-36.pyc
│   │       ├── 0006_auto_20180521_0200.cpython-36.pyc
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-36.pyc
│   │   ├── answer.cpython-36.pyc
│   │   ├── calculation.cpython-36.pyc
│   │   ├── config.cpython-36.pyc
│   │   ├── Dfile.cpython-36.pyc
│   │   ├── forms.cpython-36.pyc
│   │   ├── __init__.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── static
│   │   ├── css
│   │   │   ├── autocomplete.css
│   │   │   ├── base.css
│   │   │   ├── changelists.css
│   │   │   ├── dashboard.css
│   │   │   ├── fonts.css
│   │   │   ├── forms.css
│   │   │   ├── login.css
│   │   │   ├── responsive.css
│   │   │   ├── responsive_rtl.css
│   │   │   ├── rtl.css
│   │   │   ├── vendor
│   │   │   │   └── select2
│   │   │   │       ├── LICENSE-SELECT2.md
│   │   │   │       ├── select2.css
│   │   │   │       └── select2.min.css
│   │   │   └── widgets.css
│   │   ├── fonts
│   │   │   ├── LICENSE.txt
│   │   │   ├── README.txt
│   │   │   ├── Roboto-Bold-webfont.woff
│   │   │   ├── Roboto-Light-webfont.woff
│   │   │   └── Roboto-Regular-webfont.woff
│   │   ├── img
│   │   │   ├── calendar-icons.svg
│   │   │   ├── gis
│   │   │   │   ├── move_vertex_off.svg
│   │   │   │   └── move_vertex_on.svg
│   │   │   ├── icon-addlink.svg
│   │   │   ├── icon-alert.svg
│   │   │   ├── icon-calendar.svg
│   │   │   ├── icon-changelink.svg
│   │   │   ├── icon-clock.svg
│   │   │   ├── icon-deletelink.svg
│   │   │   ├── icon-no.svg
│   │   │   ├── icon-unknown-alt.svg
│   │   │   ├── icon-unknown.svg
│   │   │   ├── icon-yes.svg
│   │   │   ├── inline-delete.svg
│   │   │   ├── LICENSE
│   │   │   ├── logo.png
│   │   │   ├── README.txt
│   │   │   ├── search.svg
│   │   │   ├── selector-icons.svg
│   │   │   ├── sorting-icons.svg
│   │   │   ├── title16.png
│   │   │   ├── title18.png
│   │   │   ├── title19.png
│   │   │   ├── title20_1.gif
│   │   │   ├── title20_2.gif
│   │   │   ├── title20_3.gif
│   │   │   ├── title21.png
│   │   │   ├── title22.png
│   │   │   ├── title23.png
│   │   │   ├── title25.png
│   │   │   ├── title26.png
│   │   │   ├── title3.png
│   │   │   ├── tooltag-add.svg
│   │   │   └── tooltag-arrowright.svg
│   │   └── js
│   │       ├── actions.js
│   │       ├── actions.min.js
│   │       ├── admin
│   │       │   ├── DateTimeShortcuts.js
│   │       │   └── RelatedObjectLookups.js
│   │       ├── autocomplete.js
│   │       ├── calendar.js
│   │       ├── cancel.js
│   │       ├── change_form.js
│   │       ├── collapse.js
│   │       ├── collapse.min.js
│   │       ├── core.js
│   │       ├── inlines.js
│   │       ├── inlines.min.js
│   │       ├── jquery.init.js
│   │       ├── popup_response.js
│   │       ├── prepopulate_init.js
│   │       ├── prepopulate.js
│   │       ├── prepopulate.min.js
│   │       ├── SelectBox.js
│   │       ├── SelectFilter2.js
│   │       ├── timeparse.js
│   │       ├── urlify.js
│   │       └── vendor
│   │           ├── jquery
│   │           │   ├── jquery.js
│   │           │   ├── jquery.min.js
│   │           │   └── LICENSE-JQUERY.txt
│   │           ├── select2
│   │           │   ├── i18n
│   │           │   │   ├── ar.js
│   │           │   │   ├── az.js
│   │           │   │   ├── bg.js
│   │           │   │   ├── ca.js
│   │           │   │   ├── cs.js
│   │           │   │   ├── da.js
│   │           │   │   ├── de.js
│   │           │   │   ├── el.js
│   │           │   │   ├── en.js
│   │           │   │   ├── es.js
│   │           │   │   ├── et.js
│   │           │   │   ├── eu.js
│   │           │   │   ├── fa.js
│   │           │   │   ├── fi.js
│   │           │   │   ├── fr.js
│   │           │   │   ├── gl.js
│   │           │   │   ├── he.js
│   │           │   │   ├── hi.js
│   │           │   │   ├── hr.js
│   │           │   │   ├── hu.js
│   │           │   │   ├── id.js
│   │           │   │   ├── is.js
│   │           │   │   ├── it.js
│   │           │   │   ├── ja.js
│   │           │   │   ├── km.js
│   │           │   │   ├── ko.js
│   │           │   │   ├── lt.js
│   │           │   │   ├── lv.js
│   │           │   │   ├── mk.js
│   │           │   │   ├── ms.js
│   │           │   │   ├── nb.js
│   │           │   │   ├── nl.js
│   │           │   │   ├── pl.js
│   │           │   │   ├── pt-BR.js
│   │           │   │   ├── pt.js
│   │           │   │   ├── ro.js
│   │           │   │   ├── ru.js
│   │           │   │   ├── sk.js
│   │           │   │   ├── sr-Cyrl.js
│   │           │   │   ├── sr.js
│   │           │   │   ├── sv.js
│   │           │   │   ├── th.js
│   │           │   │   ├── tr.js
│   │           │   │   ├── uk.js
│   │           │   │   ├── vi.js
│   │           │   │   ├── zh-CN.js
│   │           │   │   └── zh-TW.js
│   │           │   ├── LICENSE-SELECT2.md
│   │           │   ├── select2.full.js
│   │           │   └── select2.full.min.js
│   │           └── xregexp
│   │               ├── LICENSE-XREGEXP.txt
│   │               ├── xregexp.js
│   │               └── xregexp.min.js
│   ├── templates
│   │   ├── base.html
│   │   ├── question
│   │   │   ├── answer.html
│   │   │   ├── ask-question.html
│   │   │   ├── base.html
│   │   │   ├── default.html
│   │   │   ├── each-quest.html
│   │   │   ├── index.html
│   │   │   ├── practice-answer-debug.html
│   │   │   ├── practice-answer-debug-strategy.html
│   │   │   ├── practice-answer.html
│   │   │   ├── practice-ask-question.html
│   │   │   ├── practice-each-quest.html
│   │   │   ├── practice-each-quest-img.html
│   │   │   ├── practice.html
│   │   │   ├── question.html
│   │   │   ├── question-type.html
│   │   │   ├── search-result.html
│   │   │   └── type.html
│   │   └── user
│   │       ├── login.html
│   │       └── register.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── tree.rd

29 directories, 221 files
