from .forms import *

def mainform(request): 
    return {'form_main' : ContactForm()}