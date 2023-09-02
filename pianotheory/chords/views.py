from django.shortcuts import render
from django.views import View
from .chords_logic import generate_random_chord

def home(request):
    return render(request, 'chords/home.html')

class ChordGenerateView(View):
    template_name = 'chords/chords_generate.html'
    
    def get(self, request, level):
        chord, chord_type = generate_random_chord(level)
        return render(request, self.template_name, {
            "level": level,
            "chord": chord,
            "chord_type": chord_type
        })


# check this place later cause the return type in render is not correct