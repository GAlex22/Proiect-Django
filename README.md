# Car Dealer (Django Project)

### Instrucțiuni descarcare:
Proiect se descarca cu ajutorul comenzii:
```sh
git clone https://github.com/GAlex22/Proiect_Django_CarDealer
```

### Instrucțiuni instalare

1. Instalați ultima versiune de Python de pe [site-ul oficial](https://www.python.org/)
2. Verificați dacă Python s-a instalat prin executarea comenzii:


```sh
python --version
```
3. Este necesara instalarea frameworkului django cu comanda:
```sh
pip install django
```
4. Trebuie sa se instaleaza si librariile "pillow" si "django-filter" cu comenzile:
```sh
pip install pillow
```
```sh
pip install django-filter
```
5. Serverul se porneste prin introducerea in terminal a comenzii:
```sh
python manage.py runserver
```
### Funcționalități
- Adăugare mașini(modele) prin intermediul interfeței admin;
- Vizualizare pagina detaliilor mașinilor dupa id prin apasarea butonului "View Details" din chenarul masinii;
- Utilizarea filtrului de cautare dupa brand, condiție, transmisie, preț;
- Vizualizare pagina "About us" prin intermediul navigatorului;
- Vizualizare pagina tuturor mașinilor, indiferent de condiție, in pagina "Inventory" prin intermediul navigatorului;
- Vizualizare pagina "Contact" prin intermediul navigatorului
