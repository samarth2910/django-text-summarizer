from django.shortcuts import render
from .utils import summarize

def home(request):
    return render(request, 'summarizer/home.html')

def summarize_text(request):
    if request.method == 'POST':
        raw_text = request.POST.get('text')
        
        if not raw_text or raw_text.strip() == "":
            return render(request, 'summarizer/home.html', {'error': 'Please enter some text to summarize.'})
        
        summary, doc, og_len, sum_len = summarize(raw_text)
        context = {
            'summary': summary,
            'original_text': raw_text,
            'original_len': og_len,
            'summary_len': sum_len,
        }
        return render(request, 'summarizer/result.html', context)

    return render(request, 'summarizer/home.html')
