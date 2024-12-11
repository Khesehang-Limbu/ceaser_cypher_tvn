from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {

    }
    return render(request, "pages/home.html", context)

def about(request):
    context = {}
    return render(request, "pages/about.html", context)

def game_start(request):
    context = {}
    if request.POST:
        form_type = request.POST.get('form_type')
        if form_type == "cipher_form":
            text = request.POST['text_to_cipher']
            shift = int(request.POST['cipher_key'])

            ciphered_text = ceaser_cipher(text, shift, "encode")

            context = {
                "text": text,
                "shift": shift,
                "ciphered_text" : ciphered_text
            }
        else:
            guess = request.POST['guess']
            shift = int(request.POST['shift'])

            ciphered_text = ceaser_cipher(guess, shift, "encode")
            deciphered_text = ceaser_cipher(ciphered_text, shift, "decode")

            context = {
                "text": guess,
                "shift": shift,
                "deciphered_text": deciphered_text
            }

        return JsonResponse(context, safe=False)
    return render(request, "pages/game_start.html", context)

def ceaser_cipher(text, shift, method):
    if method == "decode":
        shift = shift * -1

    result = []
    shift = shift % 26

    for char in text:
        if char.isupper():
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            result.append(new_char)
        elif char.islower():
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)
