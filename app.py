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
    "experience": "Proyek pembelajaran mandiri analisis data.",
    "email": "andhikarr28@gmail.com",
    "linkedin": "https://www.linkedin.com/in/andhikarr28/",
    "github": "https://github.com/andhikarr28",
}

BASE_DIR = Path(__file__).resolve().parent
CV_PATH = BASE_DIR / "assets" / "cv.pdf"

PROJECTS = [
    {
        "title": "Analisis Penjualan",
        "field": "Penjualan",
        "tools": ["Python", "Pandas", "Plotly"],
        "status": "Demonstrasi tersedia",
        "description": (
            "Menganalisis omzet, laba kotor, tren bulanan, "
            "dan kontribusi produk."
        ),
        "github": "",
        "report": "",
    },
    {
        "title": "Analisis Retensi Pelanggan",
        "field": "Pelanggan",
        "tools": ["SQL", "Python"],
        "status": "Rancangan proyek",
        "description": (
            "Rencana studi cohort untuk mempelajari "
            "pembelian berulang pelanggan."
        ),
        "github": "",
        "report": "",
    },
    {
        "title": "Analisis Kinerja Operasional",
        "field": "Operasional",
        "tools": ["Excel", "Power BI"],
        "status": "Rancangan proyek",
        "description": (
            "Rencana analisis ketepatan waktu dan "
            "durasi penyelesaian pesanan."
        ),
        "github": "",
        "report": "",
    },
]


# =========================================================
# PENGATURAN APLIKASI
# =========================================================

st.set_page_config(
    page_title="Portofolio Data Analyst",
    page_icon="📊",
    layout="wide",
)

CHART_COLOR = "#0D9488"


def rupiah(value):
    return "Rp" + f"{value:,.0f}".replace(",", ".")


def show_project_links(project):
    if project["github"]:
        st.link_button("Lihat kode", project["github"])

    if project["report"]:
        st.link_button("Baca laporan", project["report"])


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
        "title": "Perbandingan Nilai Transaksi Antarwilayah",
        "tools": ["Excel", "Python"],
        "related_project": "Analisis Penjualan",
        "objective": "Membandingkan distribusi nilai transaksi dengan memperhatikan ukuran sampel dan komposisi produk.",
        "tasks": [
            "Mengelompokkan transaksi berdasarkan wilayah.",
            "Menghitung ukuran sampel, median, dan variasi nilai transaksi.",
            "Membuat visualisasi distribusi antarwilayah.",
            "Meninjau komposisi produk sebelum menafsirkan perbedaan.",
        ],
        "deliverables": ["Tabel perbandingan", "Grafik distribusi", "Kode atau lembar kerja", "Ringkasan interpretasi"],
        "data_note": "Dapat memakai dataset penjualan sintetis. Perbandingan deskriptif tidak membuktikan hubungan sebab akibat.",
    },
    {
        "code": "05082",
        "course": "Data Mining",
        "credits": 3,
        "grade": "A",
        "category": "Analisis Pelanggan",
        "title": "Segmentasi Pelanggan Menggunakan RFM",
        "tools": ["Python", "Pandas"],
        "related_project": "Analisis Retensi Pelanggan",
        "objective": "Mengelompokkan pelanggan berdasarkan recency, frequency, dan monetary dari transaksi sintetis.",
        "tasks": [
            "Menentukan tanggal evaluasi tetap dan menyaring transaksi selesai.",
            "Menghitung recency, frequency, dan monetary setiap pelanggan.",
            "Menentukan aturan skor, termasuk penanganan nilai yang sama.",
            "Membuat profil segmen dan membahas sensitivitas aturan segmentasi.",
        ],
        "deliverables": ["Tabel RFM", "Aturan skor", "Visualisasi segmen", "Rekomendasi bersyarat"],
        "data_note": "Memerlukan transaksi dengan customer_id. RFM merupakan segmentasi berbasis aturan; proyek ini belum mencakup model clustering.",
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
            "Galeri Proyek",
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
        "Gunakan menu Galeri Proyek untuk melihat studi kasus, "
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
    st.subheader("Proyek unggulan")
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

elif page == "Galeri Proyek":
    st.title("Galeri Proyek")

    st.caption(
        "Analisis penjualan tersedia sebagai demonstrasi. "
        "Dua proyek lainnya masih berupa rancangan."
    )

    col1, col2 = st.columns(2)

    all_tools = sorted(
        {tool for project in PROJECTS for tool in project["tools"]}
    )

    with col1:
        tool_filter = st.selectbox(
            "Filter alat",
            ["Semua"] + all_tools,
        )

    with col2:
        field_filter = st.selectbox(
            "Filter bidang",
            ["Semua", "Penjualan", "Pelanggan", "Operasional"],
        )

    selected_projects = [
        project
        for project in PROJECTS
        if (
            tool_filter == "Semua"
            or tool_filter in project["tools"]
        )
        and (
            field_filter == "Semua"
            or field_filter == project["field"]
        )
    ]

    if not selected_projects:
        st.info("Tidak ada proyek yang sesuai dengan filter.")

    for project in selected_projects:
        with st.container(border=True):
            st.subheader(project["title"])
            st.caption(project["status"])
            st.write(project["description"])
            st.write("**Alat:** " + ", ".join(project["tools"]))

            with st.expander("Lihat detail studi kasus"):
                if project["field"] == "Penjualan":
                    st.markdown(
                        """
**Masalah bisnis**

Bagaimana distribusi omzet dan laba kotor menurut
produk, wilayah, dan waktu?

**Sumber dan struktur data**

Data sintetis dibangkitkan dengan seed tetap.
Satu baris merepresentasikan satu pesanan yang
berisi satu jenis produk.

**Pemeriksaan kualitas**

Periksa keunikan ID pesanan, nilai kosong,
kuantitas positif, dan konsistensi perhitungan
omzet serta laba kotor. Dataset ini sudah terstruktur,
sehingga belum menunjukkan penanganan data mentah
yang kompleks.

**Metode**

Agregasi deskriptif, tren bulanan, peringkat produk,
dan perbandingan wilayah.
                        """
                    )

                    product_revenue = (
                        df.groupby("product")["revenue"]
                        .sum()
                        .sort_values(ascending=False)
                    )

                    top_product = product_revenue.index[0]
                    top_share = (
                        product_revenue.iloc[0]
                        / df["revenue"].sum()
                        * 100
                    )

                    st.write(
                        f"**Temuan dari seluruh dataset:** "
                        f"{top_product} memiliki omzet terbesar, "
                        f"dengan kontribusi {top_share:.1f}%."
                    )

                    st.write(
                        "**Rekomendasi:** periksa jumlah unit dan "
                        "margin sebelum memprioritaskan produk. "
                        "Omzet tinggi dapat dipengaruhi harga satuan."
                    )

                    st.write(
                        "**Keterbatasan:** data sintetis ini tidak "
                        "membuktikan pola permintaan pasar. Laba kotor "
                        "belum memperhitungkan biaya operasional, "
                        "pajak, retur, atau diskon."
                    )

                elif project["field"] == "Pelanggan":
                    st.write(
                        "**Pertanyaan:** bagaimana proporsi pelanggan "
                        "yang kembali membeli pada bulan berikutnya?"
                    )
                    st.write(
                        "**Rencana data sintetis:** customer_id, "
                        "order_id, tanggal, dan nilai transaksi."
                    )
                    st.write(
                        "**Rencana metode:** kelompokkan pelanggan "
                        "menurut bulan pembelian pertama, lalu hitung "
                        "retensi bulanan setiap cohort."
                    )
                    st.warning(
                        "Analisis proyek ini belum ditampilkan di aplikasi. "
                        "Tambahkan hasil setelah pengerjaan dan pemeriksaan selesai."
                    )

                else:
                    st.write(
                        "**Pertanyaan:** pada tahapan mana "
                        "keterlambatan penyelesaian paling sering terjadi?"
                    )
                    st.write(
                        "**Rencana data sintetis:** order_id, waktu "
                        "masuk, tenggat, waktu selesai, dan unit kerja."
                    )
                    st.write(
                        "**Rencana metode:** hitung durasi proses, "
                        "persentase tepat waktu, dan distribusi "
                        "keterlambatan."
                    )
                    st.warning(
                        "Analisis proyek ini belum ditampilkan di aplikasi. "
                        "Tambahkan hasil setelah pengerjaan dan pemeriksaan selesai."
                    )

                show_project_links(project)


# =========================================================
# DASHBOARD
# =========================================================

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