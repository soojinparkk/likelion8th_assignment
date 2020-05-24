from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text= request.GET['fulltext']       #result 페이지에 입력한 글 전체
    words= text.split()        #공백을 기준으로 list로 저장해주는 함수
    word_dictionary= {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1


    return render(request, 'result.html', {'full' : text, 'total': len(words), 'dictionary' : word_dictionary.items})   #result.html로 전달해주기, 사전형객체