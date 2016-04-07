from django import forms

from .models import Post

class PostForm(forms.ModelForm): 

    class Meta:
        model = Post   # 어떤 모델이 쓰이는지 장고에게 알려줌
        fields = ('title', 'text',)    # title과 text만 보여줌
        

        