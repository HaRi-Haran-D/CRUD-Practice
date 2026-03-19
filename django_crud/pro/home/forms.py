from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','para']
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        COMMON_CLASS = "w-full px-4 py-2 mt-4 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 focus:outline-none transition duration-200"

        self.fields['title'].widget.attrs['class'] = COMMON_CLASS
        self.fields['title'].widget.attrs['placeholder'] = 'Enter Your Post Title'
        self.fields['title'].label = ''
        self.fields['title'].help_text = ''

        self.fields['para'].widget.attrs['class'] = COMMON_CLASS + " h-32 resize-none"
        self.fields['para'].widget.attrs['placeholder'] = 'Enter Brief About Your Post'
        self.fields['para'].label = ''
        self.fields['para'].help_text = ''