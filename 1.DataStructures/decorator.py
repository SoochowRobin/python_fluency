# The simplest and fastest way to distinguish junior and senior Python
# programmers in a technical interview is letting him write a decorator

# level 0: understand basic concepts and usage
from functools import wraps


def add_author(func):
	print('Robin Chen')
	return func

@add_author
def get_title():
	return '7 levels of using python decorator'

# print(get_title())



def add_things(func):
	def wrapper():
		title = func()
		new_title = title + ' !!!'
		return new_title
	return wrapper   # receive a callable and return a callable, that's why return wrapper

def add_publication(func):
	def wrapper():
		pub = 'Nano' 
		return pub + '\n' + func()
	return wrapper

@add_publication
@add_things
def get_titles():
	return '7 levels of using python decorator'

print(get_titles())



# level 3: we could wrap a function that receive arguments
def add_author(func):
    def wrapper(*args, **kwargs):
        author = 'Yang Zhou'
        return author + '\n' + func(*args, **kwargs)
    return wrapper

@add_author
def get_title(title):
    return title

print(get_title('Harry Potter'))
# Yang Zhou
# Harry Potter

@add_author
def get_many_title(t1, t2):
    return t1+'\n'+t2

print(get_many_title('Harry Potter 1','Harry Potter 2'))
# Yang Zhou
# Harry Potter 1
# Harry Potter 2


# level 5: keep the Metadata of original functions
def add_author(func):
	# modify here to protect Metadata
	@wraps(func)
	def wrapper(*args, **kwargs):
		author = 'Robin Chen'
		return author + '\n' + func(*args, **kwargs)
	return wrapper

@add_author
def get_title(title):
	'''
	A func that receives and returns a title.
	'''
	return title

print(get_title.__name__)
# wrapper
print(get_title.__doc__)
# None
