from django.test import TestCase

from django_settings_export import (
    UndefinedSettingError,
    UnexportedSettingError,
    ExportedSettings
)


class TestExportedSettings(TestCase):

    def test_exported_settings_wrapper(self):
        settings = ExportedSettings({'FOO': 'BAR'})
        self.assertEqual(settings.FOO, 'BAR')
        with self.assertRaises(UnexportedSettingError):
            # noinspection PyStatementEffect
            settings.XXX


class TestSettingsExportContextProcessor(TestCase):

    def test_export_ok(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'settings.FOO: foo')
        self.assertContains(r, 'settings.BAR: bar')

    def test_export_ok_with_renamed_variable(self):
        from django.conf import settings
        settings.SETTINGS_EXPORT_VARIABLE_NAME = 'django_settings'
        # This is a try/finally to make sure that a failure here doesn't break
        # the settings for other tests.
        try:
            r = self.client.get('/rename')
            self.assertEqual(r.status_code, 200)
            self.assertContains(r, 'django_settings.FOO: foo')
            self.assertContains(r, 'django_settings.BAR: bar')
        finally:
            del settings.SETTINGS_EXPORT_VARIABLE_NAME

    def test_unexported_setting(self):
        with self.assertRaises(UnexportedSettingError):
            self.client.get('/error')

    def test_undefined_setting(self):
        with self.assertRaises(UndefinedSettingError):
            with self.settings(SETTINGS_EXPORT=['UNDEFINED_SETTING']):
                self.client.get('/')
