from pathlib import Path
from random import Random

import pandas as pd
import plotly.express as px
import streamlit as st


# =========================================================
# KONFIGURASI PROFIL
# =========================================================

PROFILE = {
    "name": "Andhika Rizqi Rizaldy",
    "role": "Data Analyst",
    "summary": (
        "Portofolio pembelajaran analisis data, "
        "visualisasi, dan penyusunan rekomendasi bisnis."
    ),
    "about": (
        "Saya lulusan Sistem Informasi Universitas Komputer Indonesia "
        "yang sedang mengembangkan kemampuan analisis data "
        "melalui proyek portofolio."
    ),
    "education": (
        "Lulusan Sistem Informasi, Universitas Komputer Indonesia"
    ),
    "experience": "Sertifikasi BNSP - Associate Data Analyst Februari 2026.",
    "email": "andhikarr28@gmail.com",
    "linkedin": "https://www.linkedin.com/in/andhikarr28/",
    "github": "https://github.com/andhikarr28",
}

BASE_DIR = Path(__file__).resolve().parent
CV_PATH = Path(__file__).resolve().parent / "CV_Data_Analyst.pdf"

st.set_page_config(
    page_title="Portofolio Data Analyst",
    page_icon="📊",
    layout="wide",
)

# =========================================================
# PROYEK, SERTIFIKASI, DAN MAGANG
# Isi detail yang belum tersedia setelah bukti pekerjaannya ada.
# Semua paths berkas bersifat relatif terhadap folder app.py.
# =========================================================

ACTIVITIES = [
    {
        "id": "web-shopee",
        "title": "Aplikasi Penjualan dan Pembelian Terintegrasi Shopee",
        "category": "Proyek Aplikasi",
        "status": "Detail proyek belum dilengkapi",
        "description": "Proyek aplikasi berbasis web untuk penjualan dan pembelian dengan integrasi Shopee.",
        "details": {
            "Bentuk karya": "Aplikasi berbasis web",
            "Peran pribadi": "Web Developer dan Integrasi API Shopee",
            "Periode pengerjaan": "Mei - September 2026",
            "Teknologi": "Laravel, MySQL, API Shopee",
            "Mekanisme integrasi Shopee": "",
        },
        "section_title": "Ruang lingkup proyek",
        "items": [
            "Penjualan dan pembelian berbasis web.",
            "Integrasi Shopee; mekanisme dan cakupan data perlu dilengkapi.",
        ],
        "note": "Nama teknologi, fitur rinci, status penyelesaian, dan hasil pengujian belum ditambahkan. Lengkapi berdasarkan aplikasi yang benar-benar dikerjakan.",
        "outcome": "",
        "github_url": "",
        "demo_url": "",
        "report_url": "",
        "evidence": [],
    },
    {
        "id": "bnsp-data-analyst",
        "title": "Sertifikasi Kompetensi Analis Data Madya",
        "category": "Sertifikasi Kompetensi",
        "status": "Kompeten sesuai sertifikat",
        "description": "Analis Data Madya (Associate Data Analyst) pada bidang Data Analitik, melalui LSP Informatika atas nama BNSP.",
        "details": {
            "Nama pemegang": "Andhika Rizqi Rizaldy",
            "Kualifikasi": "Analis Data Madya (Associate Data Analyst)",
            "Bidang": "Data Analitik (Data Analytics)",
            "Lembaga sertifikasi": "Lembaga Sertifikasi Profesi Informatika",
            "Atas nama": "Badan Nasional Sertifikasi Profesi (BNSP)",
            "Tanggal penerbitan": "9 Februari 2026",
            "Masa berlaku tertulis": "3 tahun",
        },
        "section_title": "Unit kompetensi pada lampiran sertifikat",
        "items": [
            "Mengumpulkan Data.",
            "Menelaah Data.",
            "Memvalidasi Data.",
            "Menentukan Objek Data.",
            "Menerapkan Akses Basis Data.",
        ],
        "note": "Informasi disalin dari sertifikat dan lampirannya. Contoh pekerjaan asesmen serta perangkat lunak yang digunakan belum dilampirkan.",
        "outcome": "Sertifikat menyatakan kompeten pada kualifikasi Analis Data Madya.",
        "github_url": "",
        "demo_url": "",
        "report_url": "",
        "evidence": [
            {"label": "Unduh sertifikat BNSP", "path": "assets/certificates/bnsp_data_analyst.pdf", "mime": "application/pdf"},
            {"label": "Unduh lampiran unit kompetensi", "path": "assets/certificates/bnsp_units.jpeg", "mime": "image/jpeg"},
        ],
    },
    {
        "id": "vsga-data-scientist",
        "title": "Pelatihan Associate Data Scientist VSGA",
        "category": "Pelatihan",
        "status": "Pelatihan selesai sesuai sertifikat",
        "description": "Pelatihan Associate Data Scientist, VSGA Digital Talent Scholarship 2025, diselenggarakan oleh BPSDMP Bandung selama 24 JP.",
        "details": {
            "Nama peserta": "Andhika Rizqi Rizaldy",
            "Program": "Vocational School Graduate Academy (VSGA)",
            "Payung program": "Digital Talent Scholarship 2025",
            "Judul pelatihan": "Associate Data Scientist",
            "Penyelenggara": "BPSDMP Bandung",
            "Periode": "18–20 Agustus 2025",
            "Durasi": "24 Jam Pelatihan (JP)",
            "Tanggal sertifikat": "30 Agustus 2025",
        },
        "section_title": "Materi pelatihan pada sertifikat",
        "items": [
            "Menguasai konsep dasar Data Science (2 JP).",
            "Menggunakan tools Data Science (2 JP).",
            "Mengumpulkan Data (2 JP).",
            "Menelaah Data (2 JP).",
            "Memvalidasi Data (2 JP).",
            "Menentukan Objek Data (2 JP).",
            "Membersihkan Data (2 JP).",
            "Mengkonstruksi Data (2 JP).",
            "Menentukan Label Data (2 JP).",
            "Membangun Model (4 JP).",
            "Mengevaluasi Hasil Pemodelan (2 JP).",
        ],
        "note": "Dokumen ini adalah sertifikat pelatihan. Tidak dicantumkan sebagai sertifikat kompetensi BNSP. Alat, dataset, proyek akhir, dan hasil evaluasi model perlu dilengkapi berdasarkan pekerjaan peserta.",
        "outcome": "Telah menyelesaikan pelatihan Associate Data Scientist selama 24 JP.",
        "github_url": "",
        "demo_url": "",
        "report_url": "",
        "evidence": [
            {"label": "Unduh sertifikat pelatihan VSGA", "path": "assets/certificates/vsga_associate_data_scientist.pdf", "mime": "application/pdf"},
        ],
    },
    {
        "id": "remote-internship",
        "title": "Magang Remote: Applied AI & Information Systems",
        "category": "Magang",
        "status": "Program selesai sesuai sertifikat",
        "description": "Lensetek International Internship Program, divisi Applied AI & Information Systems, periode Oktober–Desember 2025.",
        "details": {
            "Nama pada sertifikat": "Andhika Rizqi",
            "Penyelenggara": "Lensetek International, LLC",
            "Program": "Lensetek International Internship Program",
            "Divisi": "Applied AI & Information Systems Division",
            "Periode": "Oktober–Desember 2025",
            "Pelaksanaan": "Remote (berdasarkan keterangan peserta)",
            "Nama aplikasi": "",
            "Teknologi aplikasi": "",
            "Kontribusi pribadi": "",
        },
        "section_title": "Cakupan peran divisi menurut lampiran sertifikat",
        "items": [
            "Mendukung persiapan dan analisis data.",
            "Mendukung pengembangan serta pengujian model AI atau machine learning.",
            "Mendukung integrasi sistem dan pengembangan dashboard.",
            "Mendokumentasikan hasil proyek.",
        ],
        "note": "Lampiran menjelaskan cakupan umum peran peserta pada divisi, bukan rincian kontribusi individu. Output aplikasi disebutkan oleh peserta; nama, fitur, teknologi, dan kontribusi pribadinya belum didokumentasikan di portofolio.",
        "outcome": "Sertifikat penyelesaian magang tersedia. Detail aplikasi dan bukti hasil kerja akan ditambahkan setelah dilengkapi.",
        "github_url": "",
        "demo_url": "",
        "report_url": "",
        "evidence": [
            {"label": "Unduh sertifikat magang", "path": "assets/certificates/internship_lensetek.pdf", "mime": "application/pdf"},
        ],
    },
]


@st.dialog("Detail Kegiatan", width="large")
def show_activity(activity):
    st.subheader(activity["title"])
    st.caption(f"{activity['category']} · {activity['status']}")
    st.write(activity["description"])

    st.markdown("#### Informasi kegiatan")
    for label, value in activity["details"].items():
        if value:
            st.write(f"**{label}:** {value}")
        else:
            st.caption(f"{label}: belum ditambahkan.")

    st.markdown("#### " + activity["section_title"])
    for item in activity["items"]:
        st.write(f"• {item}")

    st.markdown("#### Hasil dan bukti")
    if activity["outcome"]:
        st.write(activity["outcome"])
    else:
        st.caption("Hasil proyek belum ditambahkan.")

    st.info(activity["note"])

    for field, label in [
        ("github_url", "Lihat kode"),
        ("demo_url", "Buka demo aplikasi"),
        ("report_url", "Baca laporan"),
    ]:
        if activity.get(field):
            st.link_button(label, activity[field])

    for index, evidence in enumerate(activity["evidence"]):
        file_path = BASE_DIR / evidence["path"]
        if file_path.is_file():
            st.download_button(
                evidence["label"],
                data=file_path.read_bytes(),
                file_name=file_path.name,
                mime=evidence["mime"],
                key=f"evidence_{activity['id']}_{index}",
            )
        else:
            st.caption(f"{evidence['label']}: berkas belum tersedia pada aplikasi.")

    if st.button("Tutup", key=f"close_activity_{activity['id']}"):
        st.rerun()


def render_activities():
    st.title("Proyek dan Sertifikasi")
    st.write("Proyek aplikasi, sertifikasi kompetensi, pelatihan, dan pengalaman magang.")
    st.caption("Klik judul kartu untuk membuka detail serta mengunduh bukti yang tersedia.")

    left, right = st.columns(2)
    with left:
        category = st.selectbox(
            "Jenis kegiatan",
            ["Semua"] + sorted({item["category"] for item in ACTIVITIES}),
            key="activity_category",
        )
    with right:
        search = st.text_input(
            "Cari kegiatan",
            placeholder="Contoh: BNSP, VSGA, Shopee, magang",
            key="activity_search",
        ).strip().casefold()

    matches = [item for item in ACTIVITIES
               if (category == "Semua" or item["category"] == category)
               and search in " ".join([
                   item["title"], item["description"], item["category"]
               ]).casefold()]

    if not matches:
        st.info("Tidak ada kegiatan yang sesuai pencarian.")
        return

    for start in range(0, len(matches), 2):
        columns = st.columns(2)
        for column, item in zip(columns, matches[start:start + 2]):
            with column:
                with st.container(border=True):
                    st.caption(item["category"])
                    if st.button(
                        item["title"],
                        key=f"open_activity_{item['id']}",
                        use_container_width=True,
                    ):
                        show_activity(item)
                    st.write(item["description"])
                    st.caption(item["status"])




# =========================================================
# PENGATURAN APLIKASI
# =========================================================



CHART_COLOR = "#0D9488"


def rupiah(value):
    return "Rp" + f"{value:,.0f}".replace(",", ".")


# =========================================================
# DATA SINTETIS
# Satu baris adalah satu pesanan berisi satu jenis produk.
# =========================================================

@st.cache_data
def make_sales_data():
    rng = Random(42)

    products = [
        ("Keyboard", "Aksesori", 350_000, 220_000),
        ("Mouse", "Aksesori", 180_000, 100_000),
        ("Headset", "Audio", 450_000, 290_000),
        ("Speaker", "Audio", 600_000, 390_000),
        ("Monitor", "Display", 2_000_000, 1_550_000),
    ]

    regions = ["Barat", "Tengah", "Timur"]
    rows = []

    for number in range(1, 1201):
        product, category, price, cost = rng.choice(products)
        quantity = rng.randint(1, 4)

        rows.append(
            {
                "order_id": f"ORD-{number:04d}",
                "date": (
                    pd.Timestamp("2025-01-01")
                    + pd.Timedelta(days=rng.randrange(365))
                ),
                "product": product,
                "category": category,
                "region": rng.choice(regions),
                "quantity": quantity,
                "unit_price": price,
                "unit_cost": cost,
            }
        )

    data = pd.DataFrame(rows)

    data["revenue"] = data["quantity"] * data["unit_price"]
    data["cogs"] = data["quantity"] * data["unit_cost"]
    data["gross_profit"] = data["revenue"] - data["cogs"]

    return data.sort_values("date").reset_index(drop=True)


df = make_sales_data()


def filter_sales(data, start, end, categories, regions):
    mask = (
        data["date"].between(
            pd.Timestamp(start),
            pd.Timestamp(end),
        )
        & data["category"].isin(categories)
        & data["region"].isin(regions)
    )
    return data.loc[mask].copy()


# =========================================================
# PROYEK MATA KULIAH
# Nilai dan SKS mengikuti transkrip yang diberikan.
# Uraian tugas adalah rencana pengembangan mandiri, bukan
# klaim tentang tugas kuliah asli atau pekerjaan selesai.
# =========================================================

COURSE_PROJECTS = [
    {
        "code": "05025",
        "course": "Sistem Basis Data",
        "credits": 3,
        "grade": "A",
        "category": "Database",
        "title": "Analisis Penjualan Menggunakan SQL",
        "tools": ["SQLite", "SQL", "Python"],
        "related_project": "Analisis Penjualan",
        "objective": "Menganalisis omzet, laba kotor, serta kontribusi produk dan wilayah dari transaksi sintetis.",
        "tasks": [
            "Memeriksa struktur tabel, nilai kosong, dan keunikan ID pesanan.",
            "Menghitung omzet, laba kotor, jumlah pesanan, dan rata-rata nilai pesanan.",
            "Membuat query agregasi bulanan, produk, dan wilayah.",
            "Mencocokkan total hasil query dengan dashboard.",
        ],
        "deliverables": ["Dataset CSV", "Database SQLite", "Query SQL", "Laporan interpretasi"],
        "data_note": "Dapat memakai dataset penjualan sintetis pada menu Dashboard. Satu baris merupakan satu pesanan dengan satu jenis produk.",
    },
    {
        "code": "05033",
        "course": "Perancangan Basis Data",
        "credits": 3,
        "grade": "A",
        "category": "Database",
        "title": "Perancangan Database Toko Elektronik",
        "tools": ["ERD", "SQL", "SQLite"],
        "related_project": "Analisis Penjualan",
        "objective": "Merancang hubungan pelanggan, produk, pesanan, dan detail pesanan untuk database toko elektronik.",
        "tasks": [
            "Mengidentifikasi kebutuhan informasi dan aturan bisnis toko.",
            "Menentukan entitas, atribut, primary key, dan foreign key.",
            "Membuat ERD dan memeriksa normalisasi.",
            "Membuat tabel serta menguji integritas relasinya.",
        ],
        "deliverables": ["ERD", "Kamus data", "Dokumentasi normalisasi", "Skrip pembuatan tabel"],
        "data_note": "Memerlukan rancangan tabel tambahan. Dataset penjualan satu tabel perlu dikembangkan menjadi struktur relasional.",
    },
    {
        "code": "05149",
        "course": "Lab. Basis Data",
        "credits": 2,
        "grade": "A",
        "category": "Database",
        "title": "Analisis Pembelian Berulang Pelanggan",
        "tools": ["SQLite", "SQL", "Python"],
        "related_project": "Analisis Retensi Pelanggan",
        "objective": "Menggabungkan data pelanggan dan pesanan untuk menghitung pembelian berulang.",
        "tasks": [
            "Memeriksa relasi customer_id pada tabel customers dan orders.",
            "Menggunakan JOIN serta menyaring pesanan selesai.",
            "Menghitung jumlah pesanan setiap pelanggan.",
            "Menghitung repeat purchase rate dan menjelaskan periode pengamatan.",
        ],
        "deliverables": ["Dataset pelanggan dan pesanan", "Query JOIN", "Tabel pembelian berulang", "Catatan analisis"],
        "data_note": "Memerlukan dataset pelanggan dan pesanan sintetis, seperti pada paket proyek retensi. Data penjualan dashboard belum memiliki customer_id.",
    },
    {
        "code": "05142",
        "course": "Probabilitas dan Statistik",
        "credits": 3,
        "grade": "A",
        "category": "Statistik",
        "title": "Analisis Distribusi Nilai Transaksi",
        "tools": ["Python", "Pandas", "Plotly"],
        "related_project": "Analisis Penjualan",
        "objective": "Memahami pemusatan, variasi, dan distribusi nilai transaksi.",
        "tasks": [
            "Memeriksa tipe data dan nilai kosong.",
            "Menghitung mean, median, kuartil, dan standar deviasi.",
            "Membuat histogram serta boxplot.",
            "Menafsirkan nilai ekstrem tanpa menghapusnya secara otomatis.",
        ],
        "deliverables": ["Kode analisis", "Tabel statistik deskriptif", "Histogram dan boxplot", "Interpretasi distribusi"],
        "data_note": "Dapat memakai kolom revenue dari dataset penjualan sintetis. Nilai ekstrem dapat berasal dari perbedaan harga produk.",
    },
    {
        "code": "05187",
        "course": "Laboratorium Probabilitas dan Statistik",
        "credits": 2,
        "grade": "A",
        "category": "Statistik",
        "title": "Analisis Perbandingan Transaksi Antarwilayah dengan SPSS",
        "tools": ["IBM SPSS Statistics"],
        "related_project": "Analisis Penjualan",
        "objective": "Menggunakan SPSS untuk membandingkan distribusi nilai transaksi antarwilayah dengan memperhatikan ukuran sampel dan komposisi produk.",
        "tasks": [
            "Mengimpor dataset CSV ke SPSS dan memeriksa tipe, label, serta tingkat pengukuran variabel.",
            "Memeriksa nilai hilang dan konsistensi kategori wilayah sebelum analisis.",
            "Menghasilkan statistik deskriptif per wilayah, termasuk jumlah observasi, mean, median, dan standar deviasi.",
            "Membuat histogram dan boxplot untuk memeriksa distribusi serta nilai ekstrem.",
            "Meninjau ukuran sampel dan komposisi produk sebelum menafsirkan perbedaan antarwilayah.",
            "Menyimpan syntax SPSS, dataset, dan output agar langkah analisis dapat diperiksa kembali.",
        ],
        "deliverables": ["Dataset SPSS (.sav)", "Syntax analisis (.sps)", "Output SPSS (.spv)", "Tabel perbandingan dan grafik distribusi", "Laporan interpretasi"],
        "data_note": "Dapat memakai dataset penjualan sintetis. Perbandingan deskriptif tidak membuktikan hubungan sebab akibat. Jika ditambahkan uji inferensial, pemilihan uji perlu didasarkan pada pertanyaan, desain, serta asumsi analisis; hasil data sintetis tidak dapat digeneralisasi ke populasi nyata.",
    },
    {
        "code": "05082",
        "course": "Data Mining",
        "credits": 3,
        "grade": "A",
        "category": "Analisis Pelanggan",
        "title": "Segmentasi Pelanggan RFM dengan RapidMiner",
        "tools": ["RapidMiner"],
        "related_project": "Analisis Retensi Pelanggan",
        "objective": "Membangun proses segmentasi pelanggan berbasis recency, frequency, dan monetary menggunakan RapidMiner pada transaksi sintetis.",
        "tasks": [
            "Mengimpor data pelanggan dan pesanan ke RapidMiner serta memeriksa tipe atribut dan format tanggal.",
            "Memeriksa nilai hilang, duplikasi ID pesanan, dan konsistensi customer_id.",
            "Menyaring pesanan selesai dan menetapkan tanggal evaluasi tetap.",
            "Menyusun alur agregasi untuk menghitung recency, frequency, dan monetary setiap pelanggan.",
            "Menentukan aturan skor RFM, termasuk arah skor recency serta penanganan nilai yang sama.",
            "Membentuk segmen, membandingkan profilnya, dan membahas sensitivitas aturan segmentasi.",
            "Menyimpan proses RapidMiner dan mengekspor tabel hasil untuk dokumentasi.",
        ],
        "deliverables": ["Proses RapidMiner (.rmp)", "Tabel RFM dan segmen (.csv)", "Dokumentasi aturan skor", "Tangkapan layar alur proses dan visualisasi", "Laporan interpretasi dan rekomendasi bersyarat"],
        "data_note": "Memerlukan transaksi dengan customer_id, misalnya dataset pada paket proyek retensi. Recency dihitung sebagai selisih hari dari pembelian terakhir ke tanggal evaluasi; frequency menghitung pesanan selesai unik; monetary menjumlahkan nilai pembelian selesai. RFM di sini berbasis aturan dan belum mencakup clustering atau model prediksi.",
    },
    {
        "code": "05071",
        "course": "Analisis Proses Bisnis",
        "credits": 3,
        "grade": "A",
        "category": "Operasional",
        "title": "Analisis Keterlambatan Pengiriman",
        "tools": ["Excel", "SQL", "Power BI"],
        "related_project": "Analisis Kinerja Operasional",
        "objective": "Mengidentifikasi pola keterlambatan pada tahap persiapan dan pengiriman pesanan.",
        "tasks": [
            "Menggambarkan alur pemrosesan pesanan.",
            "Memeriksa urutan tanggal dan menghitung durasi proses.",
            "Membedakan pengiriman selesai, belum selesai, dan dibatalkan.",
            "Menghitung ketepatan waktu dan membandingkan gudang serta wilayah.",
        ],
        "deliverables": ["Diagram proses", "KPI operasional", "Dashboard pengiriman", "Usulan pemeriksaan lanjutan"],
        "data_note": "Memerlukan dataset pengiriman seperti pada paket proyek operasional. Definisi tenggat dan tanggal evaluasi harus dicantumkan.",
    },
    {
        "code": "05148",
        "course": "Operasional Riset",
        "credits": 3,
        "grade": "A",
        "category": "Operasional",
        "title": "Simulasi Optimasi Alokasi Pengiriman",
        "tools": ["Excel Solver"],
        "related_project": "Analisis Kinerja Operasional",
        "objective": "Mencari alokasi pengiriman dengan biaya minimum berdasarkan kapasitas dan permintaan simulasi.",
        "tasks": [
            "Menyusun matriks biaya, kapasitas gudang, dan permintaan wilayah.",
            "Menentukan variabel keputusan dan fungsi tujuan.",
            "Menambahkan batasan kapasitas, permintaan, dan nonnegativitas.",
            "Menyelesaikan model, memeriksa kelayakan, dan membandingkan skenario.",
        ],
        "deliverables": ["Data asumsi simulasi", "Model Excel Solver", "Alokasi hasil optimasi", "Pemeriksaan batasan"],
        "data_note": "Matriks biaya, kapasitas, dan permintaan perlu dibuat terpisah. Dataset pengiriman saja belum cukup untuk optimasi.",
    },
    {
        "code": "05170",
        "course": "Komputer Aplikasi Sistem Informasi",
        "credits": 3,
        "grade": "A",
        "category": "Visualisasi",
        "title": "Dashboard Penjualan Menggunakan Excel",
        "tools": ["Excel", "Pivot Table"],
        "related_project": "Analisis Penjualan",
        "objective": "Menyajikan indikator penjualan pada dashboard spreadsheet dengan filter yang konsisten.",
        "tasks": [
            "Mengimpor CSV dan memeriksa tipe tanggal serta angka.",
            "Membuat tabel Excel dan pivot penjualan.",
            "Menambahkan grafik serta filter yang terhubung.",
            "Mencocokkan angka dashboard dengan data sumber.",
        ],
        "deliverables": ["Workbook Excel", "Pivot table", "Dashboard dan filter", "Panduan singkat"],
        "data_note": "Dapat memakai CSV dari Dashboard. Workbook Excel perlu dibuat sebagai luaran tersendiri.",
    },
    {
        "code": "05189",
        "course": "Konsep Sistem Informasi Geografis",
        "credits": 2,
        "grade": "A",
        "category": "Visualisasi",
        "title": "Pemetaan Penjualan Antarprovinsi",
        "tools": ["QGIS", "Python"],
        "related_project": "Analisis Penjualan",
        "objective": "Memetakan distribusi penjualan menggunakan kode provinsi dan batas administrasi yang sesuai.",
        "tasks": [
            "Menyiapkan data penjualan sintetis per provinsi.",
            "Mencatat sumber dan lisensi batas administrasi.",
            "Menggabungkan data menggunakan kode provinsi yang cocok.",
            "Memeriksa wilayah yang tidak cocok dan membuat peta berlegenda.",
        ],
        "deliverables": ["Data provinsi", "Proyek peta", "Peta penjualan", "Dokumentasi sumber dan penggabungan"],
        "data_note": "Label Barat, Tengah, dan Timur pada dashboard tidak cukup untuk pemetaan provinsi. Diperlukan data provinsi serta geometri yang sesuai.",
    },
]

# Ubah atribut ini pada objek mata kuliah terkait setelah mulai dikerjakan.
# Contoh: "status": "Dalam pengerjaan", "github_url": "https://..."
for course in COURSE_PROJECTS:
    course.setdefault("status", "Rencana")
    course.setdefault("work_type", "Pengembangan mandiri berbasis mata kuliah")
    course.setdefault("findings", "")
    course.setdefault("github_url", "")
    course.setdefault("report_url", "")


@st.dialog("Detail Proyek Mata Kuliah", width="large")
def show_course_project(course):
    st.subheader(course["course"])
    st.caption(
        f"Kode {course['code']} · {course['credits']} SKS · Nilai {course['grade']}"
    )
    st.write(f"**Judul proyek:** {course['title']}")
    st.write(f"**Status:** {course['status']}")
    st.write(f"**Jenis karya:** {course['work_type']}")
    st.write(f"**Proyek terkait:** {course['related_project']}")

    if course["status"] == "Rencana":
        st.info("Tugas berikut merupakan rencana pengembangan portofolio dan belum dinyatakan selesai.")

    st.markdown("#### Tujuan")
    st.write(course["objective"])

    st.markdown("#### Tugas yang dikerjakan")
    for number, task in enumerate(course["tasks"], start=1):
        st.write(f"{number}. {task}")

    st.markdown("#### Data dan batasan")
    st.write(course["data_note"])

    st.markdown("#### Alat")
    st.write(", ".join(course["tools"]))

    st.markdown("#### Luaran")
    for item in course["deliverables"]:
        st.write(f"• {item}")

    st.markdown("#### Hasil dan interpretasi")
    if course["findings"]:
        st.write(course["findings"])
    else:
        st.caption("Hasil belum ditambahkan. Isi setelah analisis dan pemeriksaan selesai.")

    st.divider()
    if course["github_url"]:
        st.link_button("Lihat kode dan dataset", course["github_url"])
    if course["report_url"]:
        st.link_button("Lihat laporan", course["report_url"])
    if not course["github_url"] and not course["report_url"]:
        st.caption("Berkas dan tautan proyek belum ditambahkan.")

    if st.button("Tutup", key=f"close_course_{course['code']}"):
        st.rerun()


def render_course_projects():
    st.title("Proyek Mata Kuliah")
    st.write("Penerapan pembelajaran akademik dalam pengembangan kemampuan analisis data.")
    st.caption("Klik nama mata kuliah untuk melihat detail tugas. Nilai mengikuti transkrip; uraian tugas merupakan usulan pengembangan mandiri.")

    filter_col, search_col = st.columns(2)
    categories = sorted({course["category"] for course in COURSE_PROJECTS})
    with filter_col:
        selected_category = st.selectbox("Bidang", ["Semua"] + categories, key="course_category")
    with search_col:
        search = st.text_input(
            "Cari mata kuliah atau proyek",
            placeholder="Contoh: SQL, statistik, pengiriman",
            key="course_search",
        ).strip().casefold()

    filtered_courses = []
    for course in COURSE_PROJECTS:
        searchable = " ".join([
            course["code"], course["course"], course["title"], *course["tools"]
        ]).casefold()
        if (selected_category == "Semua" or course["category"] == selected_category) and search in searchable:
            filtered_courses.append(course)

    st.caption(f"Menampilkan {len(filtered_courses)} mata kuliah.")
    if not filtered_courses:
        st.info("Tidak ada mata kuliah yang sesuai pencarian.")
        return

    for start in range(0, len(filtered_courses), 2):
        columns = st.columns(2)
        for column, course in zip(columns, filtered_courses[start:start + 2]):
            with column:
                with st.container(border=True):
                    st.caption(f"{course['category']} · {course['status']}")
                    if st.button(
                        course["course"],
                        key=f"open_course_{course['code']}",
                        use_container_width=True,
                    ):
                        show_course_project(course)
                    st.write(f"**{course['title']}**")
                    st.caption(f"{course['credits']} SKS · Nilai {course['grade']}")
                    st.write("Alat: " + ", ".join(course["tools"]))



# =========================================================
# NAVIGASI
# =========================================================

with st.sidebar:
    st.title("DATA / PORTFOLIO")
    st.caption(PROFILE["name"])

    page = st.radio(
        "Navigasi",
        [
            "Beranda",
            "Tentang Saya",
            "Proyek dan Sertifikasi",
            "Proyek Mata Kuliah",
            "Dashboard",
            "CV dan Kontak",
        ],
    )

    st.divider()
    st.caption(
        "Data demonstrasi bersifat sintetis. "
        "Bukan data perusahaan atau hasil kerja klien."
    )


# =========================================================
# BERANDA
# =========================================================

if page == "Beranda":
    st.caption("PORTOFOLIO ANALISIS DATA")
    st.title(PROFILE["name"])
    st.subheader(PROFILE["role"])
    st.write(PROFILE["summary"])

    st.info(
        "Gunakan menu Proyek dan Sertifikasi untuk melihat kegiatan, "
        "Dashboard untuk mencoba analisis, dan CV dan Kontak "
        "untuk informasi lebih lanjut."
    )

    st.divider()

    left, middle, right = st.columns(3)

    with left:
        st.subheader("01 / Masalah")
        st.write(
            "Memulai analisis dari pertanyaan bisnis "
            "yang memiliki tujuan jelas."
        )

    with middle:
        st.subheader("02 / Analisis")
        st.write(
            "Memeriksa kualitas data dan menghitung "
            "metrik dengan definisi yang konsisten."
        )

    with right:
        st.subheader("03 / Keputusan")
        st.write(
            "Menghubungkan temuan dengan rekomendasi "
            "serta menjelaskan batas interpretasinya."
        )

    st.divider()
    st.subheader("Demonstrasi analisis")
    st.write("**Analisis Penjualan dengan Dashboard Interaktif**")
    st.write(
        "Eksplorasi 1.200 pesanan sintetis selama tahun 2025 "
        "berdasarkan periode, kategori produk, dan wilayah."
    )


# =========================================================
# TENTANG SAYA
# =========================================================

elif page == "Tentang Saya":
    st.title("Tentang Saya")
    st.write(PROFILE["about"])

    st.subheader("Peta keterampilan")
    st.caption(
        "Daftar berikut adalah cakupan belajar. "
        "Sesuaikan dengan kemampuan yang dapat Anda demonstrasikan."
    )

    skills = pd.DataFrame(
        {
            "Alat / kemampuan": [
                "Excel",
                "SQL",
                "Python dan Pandas",
                "Power BI",
                "Visualisasi data",
            ],
            "Contoh penerapan": [
                "Pembersihan data dan pivot table",
                "JOIN, agregasi, dan analisis cohort",
                "Transformasi dan analisis eksploratif",
                "Pemodelan data dan dashboard",
                "Pemilihan grafik dan komunikasi temuan",
            ],
        }
    )

    st.dataframe(skills, hide_index=True, use_container_width=True)

    st.subheader("Pendidikan")
    st.write(PROFILE["education"])

    st.subheader("Pengalaman")
    st.write(PROFILE["experience"])


# =========================================================
# GALERI DAN DETAIL PROYEK
# =========================================================

elif page == "Proyek dan Sertifikasi":
    render_activities()


elif page == "Proyek Mata Kuliah":
    render_course_projects()

elif page == "Dashboard":
    st.title("Dashboard Penjualan")
    st.caption(
        "DEMONSTRASI • Data sintetis tahun 2025 • Mata uang IDR"
    )

    min_date = df["date"].min().date()
    max_date = df["date"].max().date()
    categories = sorted(df["category"].unique().tolist())
    regions = sorted(df["region"].unique().tolist())

    defaults = {
        "sales_start": min_date,
        "sales_end": max_date,
        "sales_categories": categories,
        "sales_regions": regions,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    def reset_filters():
        for key, value in defaults.items():
            st.session_state[key] = value

    st.button("Reset filter", on_click=reset_filters)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        start = st.date_input(
            "Tanggal mulai",
            min_value=min_date,
            max_value=max_date,
            key="sales_start",
        )

    with col2:
        end = st.date_input(
            "Tanggal akhir",
            min_value=min_date,
            max_value=max_date,
            key="sales_end",
        )

    with col3:
        selected_categories = st.multiselect(
            "Kategori",
            options=categories,
            key="sales_categories",
        )

    with col4:
        selected_regions = st.multiselect(
            "Wilayah",
            options=regions,
            key="sales_regions",
        )

    if start > end:
        st.error("Tanggal mulai harus sebelum atau sama dengan tanggal akhir.")
        st.stop()

    filtered = filter_sales(
        df,
        start,
        end,
        selected_categories,
        selected_regions,
    )

    if filtered.empty:
        st.info(
            "Tidak ada data untuk kombinasi filter ini. "
            "Pilih kategori dan wilayah, atau klik Reset filter."
        )
        st.stop()

    revenue = filtered["revenue"].sum()
    gross_profit = filtered["gross_profit"].sum()
    orders = filtered["order_id"].nunique()
    average_order = revenue / orders

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Omzet", rupiah(revenue))
    col2.metric("Laba kotor", rupiah(gross_profit))
    col3.metric("Jumlah pesanan", f"{orders:,}".replace(",", "."))
    col4.metric("Rata-rata pesanan", rupiah(average_order))

    with st.expander("Definisi metrik"):
        st.markdown(
            """
- **Omzet:** jumlah kuantitas × harga jual.
- **Harga pokok penjualan:** jumlah kuantitas × biaya per unit.
- **Laba kotor:** omzet dikurangi harga pokok penjualan.
- **Jumlah pesanan:** jumlah ID pesanan unik.
- **Rata-rata pesanan:** omzet dibagi jumlah pesanan.
- Satu pesanan hanya memuat satu jenis produk pada dataset ini.
- Semua nilai uang ditampilkan dalam rupiah.
            """
        )

    monthly = (
        filtered.set_index("date")
        .resample("MS")["revenue"]
        .sum()
    )

    # Isi bulan tanpa transaksi dengan nol pada periode terpilih.
    months = pd.date_range(
        pd.Timestamp(start).replace(day=1),
        pd.Timestamp(end).replace(day=1),
        freq="MS",
    )

    monthly = (
        monthly.reindex(months, fill_value=0)
        .rename_axis("date")
        .reset_index()
    )

    ranking = (
        filtered.groupby("product", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
    )

    region_summary = (
        filtered.groupby("region", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
    )

    left, right = st.columns(2)

    with left:
        fig = px.line(
            monthly,
            x="date",
            y="revenue",
            markers=True,
            title="Tren omzet bulanan",
            labels={"date": "Bulan", "revenue": "Omzet (Rp)"},
        )
        fig.update_traces(line_color=CHART_COLOR)
        st.plotly_chart(fig, use_container_width=True)

    with right:
        fig = px.bar(
            ranking.sort_values("revenue"),
            x="revenue",
            y="product",
            orientation="h",
            title="Peringkat produk berdasarkan omzet",
            labels={"product": "Produk", "revenue": "Omzet (Rp)"},
        )
        fig.update_traces(marker_color=CHART_COLOR)
        st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(
        region_summary,
        x="region",
        y="revenue",
        title="Omzet menurut wilayah",
        labels={"region": "Wilayah", "revenue": "Omzet (Rp)"},
    )
    fig.update_traces(marker_color=CHART_COLOR)
    st.plotly_chart(fig, use_container_width=True)

    top = ranking.iloc[0]
    share = top["revenue"] / revenue * 100

    st.subheader("Catatan analisis")
    st.write(
        f"Pada filter aktif, {top['product']} memberikan "
        f"omzet terbesar sebesar {rupiah(top['revenue'])}, "
        f"atau {share:.1f}% dari omzet terpilih."
    )
    st.write(
        "Peringkat omzet tidak otomatis menunjukkan produk "
        "paling menguntungkan. Periksa laba kotor dan jumlah "
        "unit sebelum menyusun keputusan persediaan."
    )
    st.caption(
        "Jika periode dimulai atau berakhir di tengah bulan, "
        "nilai bulan tersebut hanya mencakup tanggal terpilih."
    )

    st.subheader("Data hasil filter")
    st.dataframe(
        filtered,
        hide_index=True,
        use_container_width=True,
    )

    st.download_button(
        "Unduh CSV hasil filter",
        data=filtered.to_csv(index=False).encode("utf-8-sig"),
        file_name="penjualan_hasil_filter.csv",
        mime="text/csv",
    )

    with st.expander("Pemeriksaan konsistensi data"):
        checks = {
            "ID pesanan unik": df["order_id"].is_unique,
            "Tidak ada nilai kosong": not df.isna().any().any(),
            "Kuantitas positif": bool((df["quantity"] > 0).all()),
            "Omzet konsisten": bool(
                (
                    df["revenue"]
                    == df["quantity"] * df["unit_price"]
                ).all()
            ),
            "Laba kotor konsisten": bool(
                (
                    df["gross_profit"]
                    == df["revenue"] - df["cogs"]
                ).all()
            ),
            "Jumlah omzet produk sama dengan KPI": (
                ranking["revenue"].sum() == revenue
            ),
            "Jumlah omzet bulanan sama dengan KPI": (
                monthly["revenue"].sum() == revenue
            ),
        }

        for label, passed in checks.items():
            st.write(f"{'✅' if passed else '❌'} {label}")


# =========================================================
# CV DAN KONTAK
# =========================================================

elif page == "CV dan Kontak":
    st.title("CV dan Kontak")

    st.subheader("Pendidikan")
    st.write(PROFILE["education"])

    st.subheader("Pengalaman")
    st.write(PROFILE["experience"])

    if CV_PATH.is_file():
        st.download_button(
            "Unduh CV",
            data=CV_PATH.read_bytes(),
            file_name="CV_Data_Analyst.pdf",
            mime="application/pdf",
        )
    else:
        st.button("CV belum tersedia", disabled=True)

    st.subheader("Hubungi saya")

    if PROFILE["email"]:
        st.link_button(
            "Kirim surel",
            f"mailto:{PROFILE['email']}",
        )

    if PROFILE["linkedin"]:
        st.link_button("LinkedIn", PROFILE["linkedin"])

    if PROFILE["github"]:
        st.link_button("GitHub", PROFILE["github"])

    if not any(
        PROFILE[key]
        for key in ["email", "linkedin", "github"]
    ):
        st.info(
            "Kontak belum diisi. Perbarui bagian PROFILE "
            "pada awal berkas app.py."
        )
