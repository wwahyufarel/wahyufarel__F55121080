# wahyufarel__F55121080

ANALISIS NOMOR 2 
Algoritma TSP (Traveling Salesman Problem):

Worst Case: Algoritma TSP memiliki kompleksitas waktu O(n!), di mana n adalah jumlah node dalam grafik. Ini karena algoritma TSP melibatkan perhitungan semua kemungkinan rute yang mungkin, sehingga jumlah permutasi yang harus diperiksa tumbuh faktorial dengan penambahan node.
Best Case: Tidak ada kasus terbaik dalam algoritma TSP. Karena algoritma ini memeriksa semua kemungkinan rute, waktu yang dibutuhkan tidak akan berkurang terlepas dari keadaan grafik.
Average Case: Algoritma TSP memiliki kompleksitas waktu yang sangat tinggi dan sulit untuk ditentukan secara pasti. Namun, secara umum, dapat dianggap sebagai O(n!) dalam kasus rata-rata.
Algoritma Dijkstra:

Worst Case: Algoritma Dijkstra memiliki kompleksitas waktu O((V + E) log V), di mana V adalah jumlah node (vertice) dalam grafik dan E adalah jumlah tepi (edges). Dalam kasus terburuk, algoritma ini perlu mempertimbangkan semua node dan tepi dalam grafik untuk mencari jalur terpendek.
Best Case: Kasus terbaik dalam algoritma Dijkstra terjadi ketika sumber node dan tujuan node berdekatan secara langsung, atau ketika hanya ada sedikit edge dalam grafik. Dalam kasus ini, kompleksitas waktu dapat mendekati O(V), di mana V adalah jumlah node dalam grafik.
Average Case: Kompleksitas waktu rata-rata algoritma Dijkstra adalah O((V + E) log V), di mana V adalah jumlah node dan E adalah jumlah tepi dalam grafik. Algoritma ini memiliki kinerja yang baik untuk sebagian besar kasus grafik dengan jumlah node dan tepi yang moderat



ANALISIS NOMOR 1


Worst Case: O(n^2). Terjadi ketika elemen-elemen dalam daftar terurut terbalik atau secara terbalik berurutan. Setiap iterasi memerlukan perbandingan dan penukaran elemen, dan dalam kasus terburuk, semua elemen harus dipindahkan ke posisi yang tepat dalam setiap iterasi.
Best Case: O(n). Terjadi ketika elemen-elemen dalam daftar sudah terurut secara ascending. Dalam kasus ini, tidak ada penukaran yang diperlukan karena setiap elemen berada di posisi yang benar.
Average Case: O(n^2). Rata-rata kasus Bubble Sort serupa dengan kasus terburuk, karena pada setiap iterasi, penukaran masih dilakukan meskipun ada beberapa elemen yang sudah terurut dengan benar.
Insertion Sort:

Worst Case: O(n^2). Terjadi ketika elemen-elemen dalam daftar terurut terbalik atau secara terbalik berurutan. Dalam kasus ini, setiap elemen memerlukan perbandingan dengan setiap elemen sebelumnya dan kemungkinan adanya pergeseran untuk menyisipkan elemen di posisi yang tepat.
Best Case: O(n). Terjadi ketika elemen-elemen dalam daftar sudah terurut secara ascending. Dalam kasus ini, setiap elemen hanya memerlukan sedikit perbandingan dengan elemen sebelumnya, sehingga kompleksitas waktu menjadi linier.
Average Case: O(n^2). Rata-rata kasus Insertion Sort serupa dengan kasus terburuk, karena pada setiap iterasi, elemen masih harus dibandingkan dengan elemen-elemen sebelumnya untuk menentukan posisinya.
