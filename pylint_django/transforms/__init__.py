"""Transforms."""
import os
import re
from pylint_django.transforms import foreignkey
from astroid import MANAGER
from astroid.builder import AstroidBuilder
from astroid import nodes


foreignkey.add_transform(MANAGER)


def _add_transform(package_name, *class_names):
    """Transform package's classes."""
    transforms_dir = os.path.join(os.path.dirname(__file__), 'transforms')
    fake_module_path = os.path.join(transforms_dir, '%s.py' % re.sub(r'\.', '_', package_name))

    with open(fake_module_path) as modulefile:
        fake_module = modulefile.read()

    fake = AstroidBuilder(MANAGER).string_build(fake_module)

    def set_fake_locals(module):
        """Set fake locals for package."""
        if module.name != package_name:
            return
        for class_name in class_names:
            module.locals[class_name] = fake.locals[class_name]

    MANAGER.register_transform(nodes.Module, set_fake_locals)


_add_transform('django.core.handlers.wsgi', 'WSGIRequest')
_add_transform('django.views.generic.base', 'View')
_add_transform('django.forms.fields',
               'BooleanField',
               'CharField',
               'ChoiceField',
               'DateField',
               'DateTimeField',
               'DecimalField',
               'EmailField',
               'FilePathField',
               'FloatField',
               'GenericIPAddressField',
               'IPAddressField',
               'IntegerField',
               'MultipleChoiceField',
               'NullBooleanField',
               'RegexField',
               'SlugField',
               'SplitDateTimeField',
               'TimeField',
               'TypedChoiceField',
               'TypedMultipleChoiceField',
               'URLField'
               )
_add_transform('django.forms', 'Form')
_add_transform('django.forms', 'ModelForm')
_add_transform('django.db.models', 'Model', 'Manager')
_add_transform('django.db.models.fields',
               'BigIntegerField',
               'BooleanField',
               'CharField',
               'CommaSeparatedIntegerField',
               'DateField',
               'DateTimeField',
               'DecimalField',
               'EmailField',
               'FilePathField',
               'FloatField',
               'GenericIPAddressField',
               'IPAddressField',
               'IntegerField',
               'NullBooleanField',
               'PositiveIntegerField',
               'PositiveSmallIntegerField',
               'SlugField',
               'SmallIntegerField',
               'TextField',
               'TimeField',
               'URLField'
               )
_add_transform('django.db.models.fields.files', 'FileField', 'ImageField')
_add_transform('django.db.models.fields.related', 'ManyToManyField')
_add_transform('django.utils.translation', 'ugettext_lazy')
