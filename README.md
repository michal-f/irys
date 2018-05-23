# Zadanie testowe:

stwórz skrypt klasyfikujący gatunek irysa na podstawie długości i szerokości płatka, oraz długości i szerokości kielicha


## opis rozwiązania:

Klasa która na podstawie danych testowych (wejściowych):
- wyznacza przedziały rozpiętości (charkterystyki min, max) dla każdego z parametrów gatunku irysa.
- klasyfikuje gatunek irysa następuje poprzez dopasowanie danych wejściowych do poszczególnych przedziałów (min, max)

## Sposób użycia:

```
from irys import IrysSpecificator

klasyfikator = IrysSpecificator()
gatunek = klasyfikator.get_species('3.1', '3.1', '5.5', '1.8')


```

