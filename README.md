# Gopall Cookies
![Game title artwork](/pics/title-artwork.png)

## Description
**Gopal-Cookies** adalah game menembak monster yang terinspirasi dari kartun **Boboiboy**. Pemain akan berperan sebagai Gopal, pahlawan super dengan kekuatan super untuk mengubah benda menjadi makanan. Tugas pemain adalah menembakkan cookies pada monster bernama Koko Jumbo, Multi Monster, Prob, dan Adudu.

## Libraries
- **Pygame**
- **Moderngl**
- **NumPy**
- **Pillow**

## Installation
1. Download file di GitHub sebagai zip.
2. Ekstrak zip lalu jalankan:
    ```bash
    pip install -r requirements.txt
    ```
3. Lalu jalankan:
    ```bash
    python main.py
    ```

## Mekanisme
### Pemain mengontrol Gopal
Pemain menggerakan kursor maka karakter Gopal akan bergerak sesuai arah kursor.

### Gopal menembak Cookie
Ketika pemain menekan tombol **space**, Gopal akan menembakkan cookies ke arah musuh.

![Screenshot from game](/pics/screenshot1.png)

### Cookie mengenai musuh
Ketika objek Cookies bertabrakan dengan objek Enemy, musuh akan terhapuskan dan pemain akan mendapatkan skor. 

**KHUSUS UNTUK BOSS ENEMY**:
- Ketika cookies mengenai Adudu, Adudu akan berubah menjadi slime.
- Jika slime mengenai pemain, skor akan berkurang.

### Musuh bergerak dan menembak
Musuh akan terus datang dan bergerak secara **RANDOM**. 

**UNTUK ENEMY KOKO JUMBO**:
- Ia bisa menembakkan laser yang bisa mengurangi skor pemain.

### Laser mengenai pemain
Ketika objek Laser bertabrakan dengan objek Gopal, pemain akan kehilangan **HEALTH**. Game akan berakhir jika **HEALTH** mencapai 0.

![Screenshot from game](/pics/screenshot2.png)

## UML Diagram
![UML diagram](/pics/uml-diagram.png)
