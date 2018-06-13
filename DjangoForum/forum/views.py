from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.template import loader

from .models import (
    Topic,
    Post,
    Tag,
    DOMAINS
)

from .forms import (
    TopicForm,
    PostForm,
    TagForm
)


def index(request, tag_id=None):
    template = loader.get_template('forum/index.html')
    if tag_id is None:
        topics = Topic.objects.all()
    else:
        topics = Topic.objects.filter(tags__pk=tag_id)
    tags = Tag.objects.all()

    users = User.objects.all();

    context = {
        'topics': topics,
        'tags': tags,
        'domains': DOMAINS,
        'users': users
    }
    return HttpResponse(template.render(context, request))


def topis(request, topic_id):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = Post.objects.create(
                text=form.cleaned_data['text'],
                author=request.user,
                topic=Topic.objects.get(pk=topic_id),
            )
            return HttpResponseRedirect('/forum/topic/' + topic_id)
    else:
        form = PostForm()

    topic = Topic.objects.get(pk=topic_id)

    posts = topic.posts.all()
    tags = Tag.objects.all()
    context = {
        'topic': topic,
        'posts': posts,
        'tags': tags,
        'form': form
    }
    return render(request, 'forum/topic.html', context)


def add_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)

        if form.is_valid():
            topic = Topic.objects.create(
                title=form.cleaned_data['title'],
                domain=form.cleaned_data['domain'],
                created_by=request.user
            )
            print(form.cleaned_data['tags'].first())

            for tag in form.cleaned_data['tags']:
                topic.tags.add(tag)

            return HttpResponseRedirect('/forum/')

    else:
        form = TopicForm()
        formtag = TagForm()

    context = {
        'form': form,
        'formtag': formtag,
    }
    return render(request, 'forum/add-topic.html', context)


def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)

        if form.is_valid():
            tag = Tag.objects.create(
                name=form.cleaned_data['name'],
            )

    return HttpResponseRedirect('/forum/topic/add/')
