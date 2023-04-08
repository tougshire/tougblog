from django.db.models import Count
from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView,)
from django.views.generic.list import ListView

from datetime import datetime, date

import markdown as md

from sdchomepage.models import Event, EventDate, Page, Placement, Post

class HomePage(TemplateView):
    template_name = 'sdchomepage/{}/sdchomepage.html'.format(settings.SDCHOMEPAGE_TEMPLATE_DIR)

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)

        context_data['placement_count'] = Placement.objects.count()

        placements = Placement.objects.all()
        context_data['places'] = []
        for place in placements:
            # place = {}
            # place['title'] = placement.title
            place.count = place.post_set.count()
            # place['posts'] = []

            place.posts = place.post_set.all()
            for post in place.posts:
                if post.summary == '':
                    post.summary = post.content
                if post.summary == '__none__':
                    post.summary = ''
                if post.content_format == 'markdown':
                    post.content = md.markdown(post.content, extensions=['markdown.extensions.fenced_code'])
                if post.summary_format == 'markdown' or ( post.summary_format == 'same' and post.content_format == 'markdown' ):
                    post.summary = md.markdown(post.summary, extensions=['markdown.extensions.fenced_code'])
                
            context_data['places'].append(place)
        event_dates = EventDate.objects.filter(whenday__gt=date.today())[:10]
        for event_date in event_dates:
            event = event_date.event
            if event.post:
                if event.summary == '':
                    event.summary = event.post.summary
                if event.content == '':
                    event.content = event.post.content

            if event.summary == '':
                event.summary = event.content
            if event.summary == '__none__':
                event.summary = ''
            if event.content_format == 'markdown':
                event.content = md.markdown(event.content, extensions=['markdown.extensions.fenced_code'])
            if event.summary_format == 'markdown' or ( event.summary_format == 'same' and event.content_format == 'markdown' ):
                event.summary = md.markdown(event.summary, extensions=['markdown.extensions.fenced_code'])
        context_data['event_dates'] = event_dates

        context_data['footer'] = settings.SDCHOMEPAGE_FOOTER_CONTENT

        return context_data
    
class PostDetail(DetailView):
    model=Post
    template_name = 'sdchomepage/{}/post.html'.format(settings.SDCHOMEPAGE_TEMPLATE_DIR)
    context_objecte_name = 'post'

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        post = self.get_object()
        if post.summary == '':
            post.summary = post.content
        if post.summary == '__none__':
            post.summary = ''
        if post.content_format == 'markdown':
            post.content = md.markdown(post.content, extensions=['markdown.extensions.fenced_code'])
        if post.summary_format == 'markdown' or ( post.summary_format == 'same' and post.content_format == 'markdown' ):
            post.summary = md.markdown(post.summary, extensions=['markdown.extensions.fenced_code'])
        context_data['post'] = post

        context_data['footer'] = settings.SDCHOMEPAGE_FOOTER_CONTENT

        return context_data

class EventDetail(DetailView):
    model=Event
    template_name = 'sdchomepage/{}/event.html'.format(settings.SDCHOMEPAGE_TEMPLATE_DIR)
    context_objecte_name = 'event'

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        event = self.get_object()
        if event.post:
            if event.summary == '':
                event.summary = event.post.summary
            if event.content == '':
                event.content = event.post.content
 
        if event.summary == '':
            event.summary = event.content
        if event.summary == '__none__':
            event.summary = ''
        if event.content_format == 'markdown':
            event.content = md.markdown(event.content, extensions=['markdown.extensions.fenced_code'])
        if event.summary_format == 'markdown' or ( event.summary_format == 'same' and event.content_format == 'markdown' ):
            event.summary = md.markdown(event.summary, extensions=['markdown.extensions.fenced_code'])
        context_data['event'] = event

        context_data['footer'] = settings.SDCHOMEPAGE_FOOTER_CONTENT

        return context_data

class PageDetail(DetailView):
    model=Page
    template_name = 'sdchomepage/{}/page.html'.format(settings.SDCHOMEPAGE_TEMPLATE_DIR)
    context_objecte_name = 'page'

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        page = self.get_object()
        if page.content_format == 'markdown':
            page.content = md.markdown(page.content, extensions=['markdown.extensions.fenced_code'])
        context_data['page'] = page

        context_data['footer'] = settings.SDCHOMEPAGE_FOOTER_CONTENT

        return context_data
