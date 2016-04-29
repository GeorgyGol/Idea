from django.test import TestCase
from models import Question, Choice

print("TEST")
q=Question.objects.get(pk=1)
print(q)
# Create your tests here.
