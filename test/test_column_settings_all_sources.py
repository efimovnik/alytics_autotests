# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def test_enable_shows_column_all_sources(app):
    app.project.open_project_page(project_id=6195)
    # Check precondition: no show column selected
    actual_text = (app.wd.find_elements_by_class_name("rt-th-header")[0].text.encode('utf-8'))
    expected_text = 'Показы'.encode('utf-8')
    if actual_text == expected_text:
        app.project.choose_shows_in_traffic_columns()
    # Test
    old_columns = app.project.get_column_count()
    app.project.choose_shows_in_traffic_columns()
    app.wd.refresh()
    new_colums = app.project.get_column_count()
    assert old_columns + 1 == new_colums
    # return the column settings
    app.project.choose_shows_in_traffic_columns()

def test_disable_shows_column_all_sources(app):
    app.project.open_project_page(project_id=6195)
    # Check precondition: no show column selected
    actual_text = (app.wd.find_elements_by_class_name("rt-th-header")[0].text.encode('utf-8'))
    expected_text = 'Показы'.encode('utf-8')
    if actual_text != expected_text:
        app.project.choose_shows_in_traffic_columns()
    # Test
    old_columns = app.project.get_column_count()
    app.project.choose_shows_in_traffic_columns()
    app.wd.refresh()
    new_colums = app.project.get_column_count()
    assert old_columns - 1 == new_colums
    # return the column settings
    app.project.choose_shows_in_traffic_columns()

