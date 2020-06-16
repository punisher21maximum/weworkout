from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Preference, AboutUs
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 12
    
    queryset = Post.objects.filter(section__exact="Random Reads")[:3] #| Post.objects.filter(section__exact="Startup Story")[:3] | Post.objects.filter(section__exact="Tech Corner")[:3] | Post.objects.filter(section__exact="Convid-19")[:3] | Post.objects.filter(section__exact="Competetive Exams")[:3] | Post.objects.filter(section__exact="News")[:3]

class SectionListView(ListView):
    model = Post
    template_name = 'blog/section-home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 12
    # queryset = Post.objects.all()[:5]

    def get(self, request, section='none', *args, **kwargs):
        
        section_dict = {
            'startup' : 'Startup Story', 'random' : 'Random Reads',
            'topn' : 'Top N', 'techcorner' : 'Tech Corner',
            'covid19' : 'Convid-19', 'compexam' : 'Competetive Exams',
            'news': 'News'
        }
        try: 
            print('sec',section, section_dict[section])
        except:
            pass
        if section != 'none':
            self.object_list = Post.objects.filter(section__exact=section_dict[section])
        else:
            self.object_list = self.get_queryset()

        
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_('Empty list and “%(class_name)s.allow_empty” is False.') % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)

    # def get_queryset(self):
    #     return Post.objects.filter(section__exact='Startup Story')




class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'eachpost'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'section', 'content']#, 'content2']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'section', 'content']#, 'content2']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def about_detail(request):
    context = {'about_us_page' : AboutUs.objects.all().first()}    
    return render(request, 'blog/about.html', context)


@login_required
def postpreference(request, pk, userpreference):
        
    postid = pk
    if request.method == "POST":
            eachpost = get_object_or_404(Post, id=postid)

            obj=''

            valueobj=''

            try:
                    obj= Preference.objects.get(user= request.user, post= eachpost)

                    valueobj= obj.value #value of userpreference


                    valueobj= int(valueobj)

                    userpreference= int(userpreference)

                    if userpreference == 3:
                            eachpost.claps += 1
                            eachpost.save()

                            context= {'eachpost': eachpost,
                              'postid': postid}

                            return render (request, 'blog/post_detail.html', context)
                            
                    elif valueobj != userpreference:
                            obj.delete()


                            upref= Preference()
                            upref.user= request.user

                            upref.post= eachpost

                            upref.value= userpreference


                            if userpreference == 1 and valueobj != 1:
                                    eachpost.likes += 1
                                    eachpost.dislikes -=1
                            elif userpreference == 2 and valueobj != 2:
                                    eachpost.dislikes += 1
                                    eachpost.likes -= 1
                            

                            upref.save()

                            eachpost.save()
                    
                    
                            context= {'eachpost': eachpost,
                              'postid': postid}

                            return render (request, 'blog/post_detail.html', context)

                    elif valueobj == userpreference:
                            obj.delete()
                    
                            if userpreference == 1:
                                    eachpost.likes -= 1
                            elif userpreference == 2:
                                    eachpost.dislikes -= 1

                            eachpost.save()

                            context= {'eachpost': eachpost,
                              'postid': postid}

                            return render (request, 'blog/post_detail.html', context)
                            
                    
    
            
            except Preference.DoesNotExist:
                    upref= Preference()

                    upref.user= request.user

                    upref.post= eachpost

                    upref.value= userpreference

                    userpreference= int(userpreference)

                    if userpreference == 1:
                            eachpost.likes += 1
                    elif userpreference == 2:
                            eachpost.dislikes +=1
                    elif userpreference == 3:
                            eachpost.claps += 1

                    upref.save()

                    eachpost.save()                            


                    context= {'eachpost': eachpost,
                      'postid': postid}

                    return render (request, 'blog/post_detail.html', context)


    else:
            eachpost= get_object_or_404(Post, id=postid)
            context= {'eachpost': eachpost,
                      'postid': postid}

            return render (request, 'blog/post_detail.html', context)

