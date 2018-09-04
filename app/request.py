import urllib.request, json
from .models import Sources,Articles


api_key = None
sources_url = None
articles_url = None
topheadlines_url = None

def configure_request(app):
    global api_key, sources_url, articles_url, topheadlines_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['ARTICLES_API_BASE_URL']
    


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(category,api_key)
    print(get_sources_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        print(get_sources_response)
        sources_results = None
        
        if get_sources_response['sources']:
           
            x = get_sources_response['sources']
            sources_results = process_results(x)
           
    
    return sources_results

def process_results(sources_list):
    '''
    Function that processes the json results
    '''
    sources_results = []

    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')

        if url:
            source_object = Sources(id,name,description,url,category,country)
            sources_results.append(source_object)
    
    return sources_results
    
def get_articles(source_id):
    '''
    Function that gets articles based on the source id
    '''
    print('dk')
    get_article_location_url = articles_url.format(source_id,api_key)
    print(get_article_location_url)
    with urllib.request.urlopen(get_article_location_url) as url:
        articles_location_data = url.read()
        articles_location_response = json.loads(articles_location_data)

        articles_location_results = None

        if articles_location_response['articles']:
            articles_location_results = process_articles(articles_location_response['articles'])
        
    return articles_location_results

def process_articles(my_articles):
    '''
    Function that processes the json results for the articles
    '''
    article_location_list = []
    
    for article in my_articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
       
        
        if urlToImage:
            article_source_object = Articles(author,title,description,url,urlToImage)
            article_location_list.append(article_source_object)
        
    return article_location_list

def topheadlines(limit):
    '''
    Function that gets articles based on the source id
    '''
    get_topheadlines_url = topheadlines_url.format(limit,api_key)

    with urllib.request.urlopen(get_topheadlines_url) as url:
        topheadlines_data = url.read()
        topheadlines_response = json.loads(topheadlines_data)

        topheadlines_results = None

        if topheadlines_response['articles']:
            topheadlines_results = process_articles(topheadlines_response['articles'])
    
    return topheadlines_results
 