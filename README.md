Latar Belakang: 
Casemiro adalah salah satu gelandang bertahan terbaik yang pernah bermain untuk Manchester United, tampil luar biasa di musim 2022/2023. Namun, performanya menurun di musim 2023/2024. Mengingat pentingnya peran ini dalam tim, proyek ini bertujuan untuk menemukan gelandang bertahan baru yang dapat menggantikan Casemiro.

Tujuan Proyek: 
Mengidentifikasi pemain yang memiliki karakteristik dan performa yang mirip dengan Casemiro di musim 2022/2023 dengan menggunakan teknik clustering.

Ada tiga file:
- [Web_Scraping_FBRef]_CDM_For_Manchester_United.ipynb adalah file yang digunakan untuk mengambil data statistik pemain sepakbola dari platform FBRef dan menyimpannya ke dalam bentuk file excel.
- [Clustering]_CDM_For_Manchester_United.ipynb adalah file yang digunakan untuk melakukan clustering terhadap data statistik pemain bola untuk menemukan pemain yang berpotensi menjadi pengganti Casemiro sebagai gelandang bertahan Manchester United. Pemain-pemain yang memiliki kemiripan berdasarkan hasil clustering akan ditampilkan dalam bentuk tabel.
- app.py adalah file untuk melakukan clustering (kode clustering-nya sama dengan yang ada di file [Clustering]_CDM_For_Manchester_United.ipynb), namun hasil clusteringnya ditampilkan menggunakan spiderplot untuk memudahkan dalam membandingkan statistik pemain-pemain yang memiliki kemiripan dengan statistik Casemiro. Implementasi visualisasi menggunakan streamlit. Untuk menjalankan streamlit bisa dengan menyimpan file app.py, lalu menjalankan perintah "streamlit run app.py" di command prompt.
