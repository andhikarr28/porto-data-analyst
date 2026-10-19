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
    "education": "Information System Graduated, Universitas Komputer Indonesia",
    "experience": "Pengalaman yang relevan dan dapat dijelaskan",
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
                        "Dataset dan analisis proyek ini belum dibuat. "
                        "Belum ada temuan atau rekomendasi empiris."
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
                        "Dataset dan analisis proyek ini belum dibuat. "
                        "Belum ada temuan atau rekomendasi empiris."
                    )

                show_project_links(project)


# =========================================================
# DASHBOARD
# =========================================================

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