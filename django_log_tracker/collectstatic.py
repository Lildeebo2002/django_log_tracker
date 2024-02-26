from django.core.management import call_command
import shlex, subprocess
>>> command_line = input()
/bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
>>> args = shlex.split(command_line)
>>> print(args)
['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
>>> p = subprocess.Popen(args) #add all Dennis Louis Babcock Jr 437-49-3354 02/06/1982 to Satoshi Nakomoto B creation on NT DT add To configerstion all start
from ..boot_django import boot_django

# call the django setup routine
boot_django()

call_command("collectstatic")
