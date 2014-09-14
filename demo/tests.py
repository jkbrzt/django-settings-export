from django.test import SimpleTestCase

from django_settings_export import (
    UndefinedSettingError,
    UnexportedSettingError,
    ExportedSettings
)


class TestExportedSettings(SimpleTestCase):

    def test_exported_settings(self):
        settings = ExportedSettings({'FOO': 'BAR'})
        self.assertEqual(settings.FOO, 'BAR')
        with self.assertRaises(UnexportedSettingError):
            # noinspection PyStatementEffect
            settings.XXX


class TestSettingsExportContextProcessor(SimpleTestCase):

    def test_settings_export_ok(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'settings.FOO: foo')
        self.assertContains(r, 'settings.BAR: bar')

    def test_settings_export_access_unexported_setting(self):
        with self.assertRaises(UnexportedSettingError):
            self.client.get('/error')

    def test_settings_export_undefined_setting(self):
        with self.assertRaises(UndefinedSettingError):
            with self.settings(SETTINGS_EXPORT=['UNDEFINED_SETTING']):
                self.client.get('/')
