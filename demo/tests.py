from django.test import TestCase

from django_settings_export import (
    UndefinedSettingError,
    UnexportedSettingError,
    ExportedSettings
)


# noinspection PyStatementEffect
class TestExportedSettings(TestCase):

    def setUp(self):
        self.settings = ExportedSettings(FOO='BAR')

    def test_attribute_access_ok(self):
        self.assertEqual(self.settings['FOO'], 'BAR')

    def test_attribute_access_unexported(self):
        with self.assertRaises(UnexportedSettingError):
            self.settings['XXX']

    def test_key_access_ok(self):
        self.assertEqual(self.settings.FOO, 'BAR')

    def test_key_access_unexported(self):
        with self.assertRaises(UnexportedSettingError):
            self.settings.XXX

    def test_dict_keys(self):
        self.assertListEqual(list(self.settings.keys()), ['FOO'])

    def test_dict_values(self):
        self.assertListEqual(list(self.settings.values()), ['BAR'])

    def test_dict_items(self):
        self.assertListEqual(list(self.settings.items()), [('FOO', 'BAR')])


class TestSettingsExportContextProcessor(TestCase):

    def test_export_ok(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'settings.FOO: foo')
        self.assertContains(r, 'settings.BAR: bar')

    def test_export_ok_with_renamed_variable(self):
        with self.settings(SETTINGS_EXPORT_VARIABLE_NAME='django_settings'):
            r = self.client.get('/rename')
            self.assertEqual(r.status_code, 200)
            self.assertContains(r, 'django_settings.FOO: foo')
            self.assertContains(r, 'django_settings.BAR: bar')

    def test_unexported_setting(self):
        with self.assertRaises(UnexportedSettingError):
            self.client.get('/error')

    def test_undefined_setting(self):
        with self.assertRaises(UndefinedSettingError):
            with self.settings(SETTINGS_EXPORT=['UNDEFINED_SETTING']):
                self.client.get('/')
