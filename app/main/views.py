from flask import render_template,redirect,url_for,request
from . import main
from ..models import Sources
from ..request import get_sources, get_articles

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    news_general = get_sources('general')
    news_business = get_sources('business')
    news_entertainment = get_sources('entertainment')
    news_sports = get_sources('sports')
    news_tech = get_sources('technology')
    news_science = get_sources('science')
   

    title = 'Home | Best News Update Site'
    
    return render_template('index.html',title=title, general=news_general, business = news_business, entertainment = news_entertainment, 
    sports = news_sports, tech = news_tech, science = news_science,)

@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    Function that returns articles based on their sources
    '''
    
    news_source = get_articles(source_id)
    title = 'Articles | All Articles'
    return render_template('articles.html', title = title, news_source=news_source)
