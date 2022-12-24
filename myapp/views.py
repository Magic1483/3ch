from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,FileResponse
from .models import Post,User,Song,Video
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from os import listdir
from os.path import isfile, join
import requests
from .bt import send_msg,send_img,send_audio

from .forms import PostForm
# Create your views here.



def index(request):
    f = render_to_string('index.html')
    return HttpResponse(f)

def error(request):
    f = render_to_string('error.html')
    return HttpResponse(f)

def logout(request):
  try:
        del request.session['nick']
  except KeyError:
        pass
  f = render_to_string('index.html')
  return HttpResponse(f)
    
def lib(request):
  f = render_to_string('index.html')
  if 'nick' in request.session:
    path='/home/runner/3ch/myapp/books'
    
    if(request.GET.get('book')!=None):
      book = request.GET.get('book')
      return FileResponse(open(f'/home/runner/3ch/myapp/books/{book}', 'rb'), content_type='application/pdf')
    else:
      onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
      ctx={
        'data':onlyfiles,
      }
      return render(template_name='lib.html',request=request,context=ctx)
  else:
    return error(request)
    





def post_by_id(request,post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        "title": post.title,
        "content":post.content,
        "img":post.img.url,
    }
    f = render_to_string('note.html',context=context)
    return HttpResponse(f)


def deletePost(request,post_id=None,collection=None):
  post_to_delete=Post.objects.get(id=int(post_id))
  print(post_id)
  post_to_delete.delete()
  return HttpResponseRedirect(f'/notes/{collection}')
  
def login(request):
  f = render_to_string('login.html')
  if request.method == 'POST':
      login = request.POST["login"]
      password = request.POST["passwd"]
      users = User.objects.all()

      for i in users:
        if i.login==login and i.password == password:
          print('login success')
          request.session['nick']= i.nick
          print(f'log:{request.session["nick"]}')
          return HttpResponseRedirect('/notes/photos')
          break
          
        
      else:
        print('access denied')
        
      
    
  return render(template_name='login.html',request=request)



  
def register(request):
  f = render_to_string('register.html')
  if request.method == 'POST':
      login = request.POST["login"]
      password = request.POST["passwd"]
      nick = request.POST["nick"]
      users = User.objects.all()

      isExist = False
      for i in users:
        if i.login==login or i.nick == nick:
          isExist = True
          
      if isExist == False:
        new_user = User(login=login,password=password,nick=nick)
        new_user.save()
        print('User created')
        
        return HttpResponseRedirect('/login')
      else:
        print('User already exist')
  return render(template_name='register.html',request=request)
    



def notes(request,collection):
  if 'nick' in request.session:
    if request.method == 'POST':
      form = PostForm(request.POST,request.FILES)
      if form.is_valid():
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')

        content = content.split(' ')
        for i in range(len(content)):
          if 'http' in str(content[i]):
            content[i] = f'<a href="{content[i]}">{content[i]}</a>'

        content_str = ' '.join(content)
        
        
          
        col = request.POST['cur_coll']
        author = request.POST['author']
        img = form.cleaned_data.get('img')

        ads = request.FILES.getlist('audio')
        
        # telegramBotKey = '5441210926:AAEIEO-xBalcs5XlUZD1gOVKav3HbdqjlTo'
        # chat_id='1033377971'
        hosturl = 'https://3ch.shrshishoshchov.repl.co'
        
        
        

        if img:
          post = Post(title=title,content=content_str,img=img,collection=col,author=author)
          post.save()
          imgurl=hosturl+post.img.url
          
          send_img(imgurl)

          # print(post.img.url)
          # tgurl = f'https://api.telegram.org/bot{telegramBotKey}/sendPhoto?chat_id={chat_id}&photo={imgurl}'
          # r = requests.post(tgurl)
          # print(r.text)
        elif ads:
          audio =ads[0]
          post = Post(title=title,audio=audio,collection=col,author=author)
          post.save()
        else:
          post = Post(title=title,content=content_str,collection=col,author=author)
          post.save()
          send_msg(f'{title} {content_str}')
          print('image is not exist')
          
        # title = request.POST['title']
        # content = request.POST['content']
        # col = request.POST['cur_coll']
        # author = request.POST['author']
        # try:
        #   img = request.FILES['img']
        #   print(img)
        #   post = Post(title=title,content=content,img=img,collection=col,author=author)
        #   post.save()
        # except:
        #   post = Post(title=title,content=content,collection=col,author=author)
        #   post.save()
        #   print('image is not exist')
        

        
        
        return HttpResponseRedirect(f'/notes/{col}')
          
    else:
        posts = Post.objects.all()
        collection_names = []
        arr = []
        for i in posts:
          if i.collection not in collection_names:
            collection_names.append(i.collection)
          if i.collection == collection:
            arr.append(i)

        form = PostForm()
        ctx = {
            "user":request.session['nick'],
            "cur_coll":collection,
            "data":arr,
            "collection":collection_names,
            "form":form,
        }
        
        f = render_to_string('notes.html',context=ctx)

        return render(template_name='notes.html',request=request,context=ctx)

  else:
    print('Unauthorized user')
    return HttpResponseRedirect('/error')



def player(request):
  if request.method == 'GET':
    paginator = Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    all_songs = Song.objects.all()
    count = len(all_songs)
    context={
      "page_obj":page_obj,
      "count_tracks":count,
      "all_songs":all_songs,
            }
    return render(request,"player.html",context)
    
  if request.method == 'POST':  
    # title = request.POST['title']
    arr = request.FILES.getlist('track')
    print(arr)
    names = []
    if len(arr)<6:
      for i in arr:
        t = i.name
        t = t.split('mp3')
      
        title = t[0][:-1]
  
        print(t)
        track = Song(title=title,audio_file=i)
        track.save()
        names.append(track.audio_file.name)
        
        # send_audio(track.audio_file.url)
        print('Track added',title)
        
        
    else:
      print('so much files')
      
    hosturl = 'https://3ch.shrshishoshchov.repl.co/media/'
    if len(names)>0:
      for j in names:
          audio_url=hosturl+j
          print(audio_url)
          send_audio(audio_url)
    
        
    return HttpResponseRedirect(f'/player')

  


def clips(request):
  if request.method == 'GET':
    clips = Video.objects.all()
    context={
      "clips":clips,
            }
    return render(request,"clips.html",context)
    
 
  if request.method == 'POST':  
    # title = request.POST['title']
    arr = request.FILES.getlist('document')
    print(arr)
    
  
    
      
    return HttpResponseRedirect(f'/clips')