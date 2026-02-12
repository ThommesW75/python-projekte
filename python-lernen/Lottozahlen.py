# Wir definieren Mengen (Sets) mit geschweiften Klammern
lottozahlen = {7,4,23,49,12,33}
getippt = {23, 42, 1, 12, 32, 7}

# Schnittmenge (Intersection) - Das mathematische Symbol ist ∩
# In Python nutzt man das '&' Zeichen
richtige = lottozahlen & getippt

print(richtige)
