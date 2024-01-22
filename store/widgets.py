from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    input_text = _('')
    template_name = 'store/custom_widget_templates/custom_clearable_file_input.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        # Determine the number of images based on the form instance
        num_images = 2 if 'image_two' in context['widget']['name'] else 1


        # Customize initial_text based on the number of images
        if num_images == 1:
            context['widget']['initial_text'] = _('Current Image')
        elif num_images == 2:
            if name == 'image_one':
                context['widget']['initial_text'] = _('Current Main Image')
            elif name == 'image_two':
                context['widget']['initial_text'] = _('Current Flip Image')

        return context