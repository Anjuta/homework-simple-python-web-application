__author__ = 'SONY'

from bottle import route, run, template, request, redirect, error, static_file
import Classes
import os


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=os.path.dirname(__file__) + '/static')


@route('/')
def index():
    return template('index')


@route('/reviews/:site_name/add', method='GET')
def reviews_on_site(site_name):
    review = request.GET.get('review')
    data_base.add_review(site_name, review)
    redirect('/reviews/' + site_name + '/0')


@route('/reviews/<site_name>/<num>')
def reviews_on_page(site_name, num):
    reviews = data_base.get_reviews_on_site(site_name)
    if reviews is None:
        reviews = ['No reviews yet']
    return template('reviews', header=site_name, reviews=reviews, num_page=num)


@route('/reviews', method='GET')
def reviews():
    site_name = request.GET.get('site_name').lower()
    redirect('/reviews/' + site_name + '/0')


@error(404)
@error(500)
def error(error):
    return 'Error'


data_base = Classes.DataBase()
run(host='localhost', port=8080)