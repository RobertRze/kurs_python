list = ['mail@a.pl', 'rob@test.pl', 'john@vp.pl']

def search_mail(mail, list):
   return True if mail in list else False

print(search_mail('rob@test.pl', list))