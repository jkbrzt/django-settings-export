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

    def test_key_access_ok(self):
        self.assertEqual(self.settings['FOO'], 'BAR')

    def test_key_access_UnexportedSettingError(self):
        with self.assertRaises(UnexportedSettingError):
            self.settings['XXX']

    def test_key_access_dict_method(self):
        """
        Since `items()` is an existing `dict` method, a KeyError needs to
        be raised instead of UnexportedSettingError, so that Django templates
        re-try with attribute access.

        Django first tries dict lookup and relies on specific exceptions being
        raised if the key is absent from the dict (specifically one of
        TypeError, AttributeError, KeyError, ValueError, IndexError).

        https://github.com/jakubroztocil/django-settings-export/pull/4

        """
        with self.assertRaises(KeyError):
            self.settings['items']

    def test_key_access_dict_can_assign(self):
        """"
        When there's is a setting name colliding with a `dict` method,
        things still should work. The ability to access `items() form
        templates, is lost though, which is acceptable.

        """
        self.settings['items'] = 'value'
        self.assertEqual(self.settings['items'], 'value')

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

    def test_list(self):
        r = self.client.get('/list')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'FOO: foo')
        self.assertContains(r, 'BAR: bar')
