# -*- coding: utf-8 -*-


def test_filter_autosources(app):
    app.project.open_project_page(project_id=6195)
    app.project.filter_source_contains(source_name=u"Яндекс Дир")
