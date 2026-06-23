from pathlib import Path
import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FileVault",
    page_icon="🗂️",
    layout="centered",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

/* Background */
.stApp {
    background: #0d0f14;
    color: #e8eaf0;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2.5rem; padding-bottom: 3rem; max-width: 680px; }

/* ── Hero ── */
.hero {
    text-align: center;
    padding: 2.8rem 1rem 2rem;
}
.hero-icon {
    font-size: 2.8rem;
    margin-bottom: .5rem;
}
.hero h1 {
    font-size: 2.6rem;
    font-weight: 700;
    letter-spacing: -1.5px;
    background: linear-gradient(135deg, #7c9cff 0%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 0 .4rem;
}
.hero p {
    color: #6b7280;
    font-size: .95rem;
    margin: 0;
}

/* ── Card ── */
.card {
    background: #161921;
    border: 1px solid #252934;
    border-radius: 16px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.2rem;
}

/* ── Section label ── */
.section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem;
    font-weight: 500;
    color: #7c9cff;
    letter-spacing: .12em;
    text-transform: uppercase;
    margin-bottom: .9rem;
}

/* ── Inputs ── */
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    background: #0d0f14 !important;
    border: 1px solid #2a2f3e !important;
    border-radius: 10px !important;
    color: #e8eaf0 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: .88rem !important;
}
div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus {
    border-color: #7c9cff !important;
    box-shadow: 0 0 0 3px rgba(124, 156, 255, .12) !important;
}

/* ── Selectbox ── */
div[data-testid="stSelectbox"] > div > div {
    background: #0d0f14 !important;
    border: 1px solid #2a2f3e !important;
    border-radius: 10px !important;
    color: #e8eaf0 !important;
}

/* ── Buttons ── */
div[data-testid="stButton"] > button {
    width: 100%;
    background: linear-gradient(135deg, #7c9cff, #c084fc) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: .92rem !important;
    padding: .65rem 1.2rem !important;
    letter-spacing: .02em;
    transition: opacity .2s;
}
div[data-testid="stButton"] > button:hover {
    opacity: .85;
}

/* ── Alerts ── */
div[data-testid="stAlert"] {
    border-radius: 10px !important;
    font-size: .88rem !important;
}

/* ── File content box ── */
.file-content {
    background: #0d0f14;
    border: 1px solid #2a2f3e;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: .82rem;
    color: #a5b4fc;
    white-space: pre-wrap;
    word-break: break-word;
    line-height: 1.65;
}

/* ── Tab strip ── */
div[data-testid="stTabs"] [role="tablist"] {
    gap: 6px;
    border-bottom: 1px solid #252934 !important;
}
div[data-testid="stTabs"] [role="tab"] {
    background: transparent !important;
    border: none !important;
    color: #6b7280 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: .88rem !important;
    font-weight: 500 !important;
    padding: .5rem .9rem !important;
    border-radius: 0 !important;
}
div[data-testid="stTabs"] [aria-selected="true"] {
    color: #e8eaf0 !important;
    border-bottom: 2px solid #7c9cff !important;
}

/* ── Divider ── */
hr { border-color: #252934 !important; }

/* ── Footer ── */
.footer {
    text-align: center;
    margin-top: 2.5rem;
    color: #374151;
    font-size: .78rem;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: .05em;
}
</style>
""", unsafe_allow_html=True)


# ── Helpers ──────────────────────────────────────────────────────────────────
def show_success(msg): st.success(f"✓  {msg}")
def show_error(msg):   st.error(f"✗  {msg}")


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-icon">🗂️</div>
    <h1>FileVault</h1>
    <p>Create · Read · Update · Delete — all in one place</p>
</div>
""", unsafe_allow_html=True)

# ── Tab layout ────────────────────────────────────────────────────────────────
tab_create, tab_read, tab_update, tab_delete = st.tabs([
    "＋  Create", "◎  Read", "✎  Update", "⌫  Delete"
])


# ── CREATE ────────────────────────────────────────────────────────────────────
with tab_create:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">New File</p>', unsafe_allow_html=True)

    c_name = st.text_input("File name", placeholder="notes.txt", key="c_name", label_visibility="collapsed")
    st.caption("File name")
    c_content = st.text_area("Content", placeholder="Start writing here…", height=160,
                             key="c_content", label_visibility="collapsed")
    st.caption("Content")

    if st.button("Create File", key="btn_create"):
        if not c_name.strip():
            show_error("Please enter a file name.")
        else:
            path = Path(c_name.strip())
            if path.exists():
                show_error(f'"{path}" already exists.')
            else:
                try:
                    path.write_text(c_content)
                    show_success(f'"{path}" created successfully.')
                except Exception as e:
                    show_error(str(e))

    st.markdown('</div>', unsafe_allow_html=True)


# ── READ ──────────────────────────────────────────────────────────────────────
with tab_read:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Read File</p>', unsafe_allow_html=True)

    r_name = st.text_input("File name", placeholder="notes.txt", key="r_name", label_visibility="collapsed")
    st.caption("File name")

    if st.button("Read File", key="btn_read"):
        if not r_name.strip():
            show_error("Please enter a file name.")
        else:
            path = Path(r_name.strip())
            if not path.exists():
                show_error(f'"{path}" does not exist.')
            else:
                try:
                    content = path.read_text()
                    st.markdown(f'<div class="file-content">{content if content else "(empty file)"}</div>',
                                unsafe_allow_html=True)
                    st.caption(f"{len(content)} characters · {path.stat().st_size} bytes")
                except Exception as e:
                    show_error(str(e))

    st.markdown('</div>', unsafe_allow_html=True)


# ── UPDATE ────────────────────────────────────────────────────────────────────
with tab_update:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Update File</p>', unsafe_allow_html=True)

    u_name = st.text_input("File name", placeholder="notes.txt", key="u_name", label_visibility="collapsed")
    st.caption("File name")

    operation = st.selectbox(
        "Operation",
        ["Rename", "Append content", "Overwrite content"],
        key="u_op",
        label_visibility="collapsed"
    )
    st.caption("Operation")

    if operation == "Rename":
        u_newname = st.text_input("New file name", placeholder="renamed.txt", key="u_newname",
                                  label_visibility="collapsed")
        st.caption("New file name")
        if st.button("Rename", key="btn_rename"):
            if not u_name.strip() or not u_newname.strip():
                show_error("Fill in both file names.")
            else:
                path = Path(u_name.strip())
                new_path = Path(u_newname.strip())
                if not path.exists():
                    show_error(f'"{path}" does not exist.')
                elif new_path.exists():
                    show_error(f'"{new_path}" already exists.')
                else:
                    try:
                        path.rename(new_path)
                        show_success(f'Renamed to "{new_path}".')
                    except Exception as e:
                        show_error(str(e))

    elif operation == "Append content":
        u_append = st.text_area("Text to append", height=130, key="u_append", label_visibility="collapsed")
        st.caption("Text to append")
        if st.button("Append", key="btn_append"):
            if not u_name.strip():
                show_error("Please enter a file name.")
            else:
                path = Path(u_name.strip())
                if not path.exists():
                    show_error(f'"{path}" does not exist.')
                else:
                    try:
                        with open(path, 'a') as f:
                            f.write("\n" + u_append)
                        show_success("Content appended.")
                    except Exception as e:
                        show_error(str(e))

    else:  # Overwrite
        u_overwrite = st.text_area("New content", height=130, key="u_overwrite", label_visibility="collapsed")
        st.caption("New content")
        if st.button("Overwrite", key="btn_overwrite"):
            if not u_name.strip():
                show_error("Please enter a file name.")
            else:
                path = Path(u_name.strip())
                if not path.exists():
                    show_error(f'"{path}" does not exist.')
                else:
                    try:
                        path.write_text(u_overwrite)
                        show_success("File overwritten.")
                    except Exception as e:
                        show_error(str(e))

    st.markdown('</div>', unsafe_allow_html=True)


# ── DELETE ────────────────────────────────────────────────────────────────────
with tab_delete:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Delete File</p>', unsafe_allow_html=True)

    d_name = st.text_input("File name", placeholder="notes.txt", key="d_name", label_visibility="collapsed")
    st.caption("File name")

    confirm = st.checkbox("I understand this action is permanent", key="d_confirm")

    if st.button("Delete File", key="btn_delete"):
        if not d_name.strip():
            show_error("Please enter a file name.")
        elif not confirm:
            show_error("Check the confirmation box first.")
        else:
            path = Path(d_name.strip())
            if not path.exists():
                show_error(f'"{path}" does not exist.')
            else:
                try:
                    path.unlink()
                    show_success(f'"{path}" deleted.')
                except Exception as e:
                    show_error(str(e))

    st.markdown('</div>', unsafe_allow_html=True)


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown('<div class="footer">built with Python · Streamlit · pathlib</div>', unsafe_allow_html=True)