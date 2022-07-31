from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        
        fields = ['title', 'text','price','capacity','photo', 'important', 'completed']
        error_messages = {
            'myfile': {
                'invalid_image': '請上傳正確格式的圖片！'
            }

        }