# TDRCB (Tudor’s Discord Remote Control Bot)

TDRCB este un program creat pentru a facilita controlul de la distanță a calculatorului personal. Programul se folosește de o aplicație deja utilizată de mulți dintre noi, Discord.

Programul, în sine, este un bot de Discord, adică un utilizator automat, programat să execute comenzi la trimiterea unor mesaje specifice. Acesta rulează în fundalul sistemului de operare Windows și se pornește simultan cu acesta. Pentru a rula programul în fundal, nu sunt necesare specificații foarte avansate. Avem nevoie doar de Windows 10, 1GB de RAM și 200MB de spațiu liber.

L-am creat inițial pentru a afla care era progresul unei descărcări atunci când îmi lăsam calculatorul pornit și plecam de acasă. Acum programul a primit mai multe funcții pe lângă ce i-am propus inițial. Puteam folosi un program precum TeamViewer, dar printr-un program scris de mine puteam ajunge la rezultatul dorit de la un asemenea soft.

## Funcționalități ale programului:

* Închidere și repornire a calculatorului;
* Trimitere a capturilor de ecran sau a ferestrelor individuale;
* Închidere, minimizare și maximizare a aplicațiilor din fundal;
* Executare a comenzilor MS-DOS;
* Interfață ușor de utilizat;
* Sistem ușor de instalare și actualizare a programului.

## Tehnologii / librării folosite:
* Discord.py - o librărie ce permite conectarea la un utilizator automat în Discord. Odată conectat, cu ajutorul unui cod (token) primit, utilizatorul automat va lua viață.
* PyAutoGUI, PyGetWindow - două librării ce permit capturarea imaginilor de pe ecran și operarea ferestrelor (minimizare, maximizare etc.) 
* psutil - ajută la luarea a diferite statistici ale sistemului de operare (memorie RAM utilizată, utilizarea procesorului etc.)

## Scurt ghid de instalare:
Se descarcă zip-ul de aici, se extrage și se va rula setup.exe. În fereastra ce a apărut, se introduce token-ul primit din pagina de unde s-a creat botul. În final, se apasă pe butonul „Install!” (pentru a actualiza aplicația, doar apăsați pe butonul „Update!” fără a mai introduce un token). 
Un mesaj va apărea care va indica că instalarea s-a terminat. Programul va porni după următorul restart al sistemului. Fișierul care memorează token-ul și softul sunt copiate în folderul utilizatorului. Un alt program care va lansa programul în sine, va fi copiat în folderul de Startup. În Task Manager, programul va apărea ca și launcher.exe.
Launcher.exe este un executabil care va lansa programul în sine. Acest lucru a fost făcut pentru a nu scrie date temporare în folderul protejat (Startup).

## Gânduri de viitor:
Doresc să implementez mai multe limbi in program, posibilitatea de a putea apăsa taste prin intermediul bot-ului și de a primi notificări la finalul unei descărcări.

	
