
import streamlit as st
import tempfile
import os
import textwrap
import html

from gemini_service import analyze_meeting_audio

from rag_service import (
    store_meeting_report,
    ask_meeting
)

from database_service import (
    initialize_database,
    save_meeting,
    get_all_meetings,
    get_meeting,
    delete_meeting
)


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="MeetMind AI",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# DATABASE INITIALIZATION
# =====================================================

initialize_database()


# =====================================================
# SESSION STATE
# =====================================================

defaults = {
    "theme": "Dark",
    "meeting_report": None,
    "meeting_name": None,
    "current_meeting_id": None,
    "selected_meeting_id": None,
    "rag_ready": False,
    "chat_history": {}
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value


# =====================================================
# THEME CONFIGURATION
# =====================================================

is_dark = st.session_state["theme"] == "Dark"

if is_dark:

    BG_COLOR = "#090909"
    CARD_COLOR = "#151515"
    SECONDARY_CARD = "#201419"
    TEXT_COLOR = "#FFFFFF"
    MUTED_TEXT = "#B8AEB2"
    BORDER_COLOR = "#49212F"
    ACCENT_COLOR = "#A71947"
    ACCENT_HOVER = "#C72A59"
    INPUT_COLOR = "#1A1A1A"

else:

    BG_COLOR = "#FFFFFF"
    CARD_COLOR = "#FFFFFF"
    SECONDARY_CARD = "#FFFDF5"
    TEXT_COLOR = "#191919"
    MUTED_TEXT = "#6D6D6D"
    BORDER_COLOR = "#E6D39A"
    ACCENT_COLOR = "#B8860B"
    ACCENT_HOVER = "#94700A"
    INPUT_COLOR = "#FFFFFF"


# =====================================================
# HTML RENDER HELPER
# =====================================================

def render_html(content):
    """
    Render HTML directly using Streamlit's HTML renderer.
    """

    st.html(
        textwrap.dedent(content).strip()
    )


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {BG_COLOR};
        color: {TEXT_COLOR};
    }}

    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }}

    section[data-testid="stSidebar"] {{
        background-color: {CARD_COLOR};
        border-right: 1px solid {BORDER_COLOR};
    }}

    section[data-testid="stSidebar"] * {{
        color: {TEXT_COLOR};
    }}

    h1, h2, h3, h4 {{
        color: {TEXT_COLOR} !important;
    }}

    p, label {{
        color: {TEXT_COLOR};
    }}

    .hero-container {{
        padding: 1.5rem 0 2rem 0;
    }}

    .section-label {{
        color: {ACCENT_COLOR};
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }}

    .hero-title {{
        font-size: 46px;
        font-weight: 800;
        line-height: 1.15;
        letter-spacing: -1px;
        color: {TEXT_COLOR};
    }}

    .hero-title span {{
        color: {ACCENT_COLOR};
    }}

    .hero-subtitle {{
        font-size: 17px;
        line-height: 1.7;
        color: {MUTED_TEXT};
        max-width: 800px;
        margin-top: 16px;
    }}

    .metric-card {{
        background: {CARD_COLOR};
        border: 1px solid {BORDER_COLOR};
        border-radius: 18px;
        padding: 24px;
        min-height: 145px;
        box-shadow: 0 4px 18px rgba(0, 0, 0, 0.08);
    }}

    .metric-label {{
        color: {MUTED_TEXT};
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 12px;
    }}

    .metric-value {{
        color: {ACCENT_COLOR};
        font-size: 29px;
        font-weight: 800;
        word-break: break-word;
    }}

    .metric-description {{
        color: {MUTED_TEXT};
        font-size: 12px;
        margin-top: 8px;
    }}

    .feature-card {{
        background: {SECONDARY_CARD};
        border: 1px solid {BORDER_COLOR};
        border-radius: 18px;
        padding: 25px;
        min-height: 200px;
    }}

    .feature-icon {{
        font-size: 30px;
        margin-bottom: 15px;
    }}

    .feature-title {{
        color: {TEXT_COLOR};
        font-size: 19px;
        font-weight: 750;
        margin-bottom: 10px;
    }}

    .feature-text {{
        color: {MUTED_TEXT};
        font-size: 14px;
        line-height: 1.7;
    }}

    .meeting-banner {{
        background: {SECONDARY_CARD};
        border: 1px solid {BORDER_COLOR};
        border-left: 5px solid {ACCENT_COLOR};
        border-radius: 12px;
        padding: 16px 20px;
        margin: 15px 0;
    }}

    .meeting-banner-title {{
        color: {TEXT_COLOR};
        font-weight: 700;
        font-size: 16px;
    }}

    .meeting-banner-text {{
        color: {MUTED_TEXT};
        font-size: 13px;
        margin-top: 5px;
    }}

    .stButton > button {{
        border-radius: 10px;
        font-weight: 650;
        border: 1px solid {BORDER_COLOR};
    }}

    [data-testid="stFileUploader"] {{
        border: 1px dashed {ACCENT_COLOR};
        border-radius: 15px;
        padding: 12px;
    }}

    hr {{
        border-color: {BORDER_COLOR};
    }}

    [data-testid="stChatMessage"] {{
        border-radius: 14px;
    }}
        /* SELECTBOX HOVER FIX */

    div[data-baseweb="select"] > div {{
        background-color: {CARD_COLOR} !important;
        border: 1px solid {BORDER_COLOR} !important;
        color: {TEXT_COLOR} !important;
        border-radius: 10px !important;
    }}

    div[data-baseweb="select"] span {{
        color: {TEXT_COLOR} !important;
    }}

    div[role="option"] {{
        background-color: {CARD_COLOR} !important;
        color: {TEXT_COLOR} !important;
    }}

    div[role="option"]:hover {{
        background-color: {ACCENT_COLOR} !important;
        color: #FFFFFF !important;
    }}

    div[role="option"] * {{
        color: inherit !important;
    }}

    .stButton > button:hover {{
        background-color: {ACCENT_COLOR} !important;
        border-color: {ACCENT_COLOR} !important;
        color: #FFFFFF !important;
    }} 
    </style>
    """,
    unsafe_allow_html=True
)


# =====================================================
# HELPER FUNCTIONS
# =====================================================

def load_selected_meeting(meeting_id):

    meeting = get_meeting(meeting_id)

    if meeting:

        st.session_state["current_meeting_id"] = meeting["id"]

        st.session_state["selected_meeting_id"] = meeting["id"]

        st.session_state["meeting_name"] = meeting["meeting_name"]

        st.session_state["meeting_report"] = meeting["report"]

        st.session_state["rag_ready"] = True


def get_current_chat_history():

    meeting_id = st.session_state.get("current_meeting_id")

    if meeting_id is None:
        return []

    if meeting_id not in st.session_state["chat_history"]:

        st.session_state["chat_history"][meeting_id] = []

    return st.session_state["chat_history"][meeting_id]


def clear_current_meeting():

    st.session_state["meeting_report"] = None

    st.session_state["meeting_name"] = None

    st.session_state["current_meeting_id"] = None

    st.session_state["selected_meeting_id"] = None

    st.session_state["rag_ready"] = False


# =====================================================
# SIDEBAR
# =====================================================

meetings = get_all_meetings()

with st.sidebar:

    render_html(
        f"""
        <div style="
            font-size: 25px;
            font-weight: 800;
            color: {ACCENT_COLOR};
            margin-bottom: 5px;
        ">
            🎙️ MeetMind AI
        </div>

        <div style="
            color: {MUTED_TEXT};
            font-size: 13px;
            margin-bottom: 20px;
        ">
            Your Intelligent Meeting Workspace
        </div>
        """
    )

    st.divider()

    st.subheader("🎨 Appearance")

    selected_theme = st.radio(
        "Choose theme",
        ["Dark", "Light"],
        index=0 if is_dark else 1,
        horizontal=True
    )

    if selected_theme != st.session_state["theme"]:

        st.session_state["theme"] = selected_theme

        st.rerun()

    st.divider()

    st.subheader("🧭 Navigation")

    page = st.radio(
        "Go to",
        [
            "🏠 Home",
            "📊 Meeting Analysis",
            "💬 Ask Your Meeting"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.subheader("📚 Meeting History")

    if meetings:

        meeting_options = {
            f"{meeting['meeting_name']} | {meeting['created_at']}":
                meeting["id"]
            for meeting in meetings
        }

        option_labels = list(meeting_options.keys())

        current_id = st.session_state.get("current_meeting_id")

        default_index = 0

        for index, meeting in enumerate(meetings):

            if meeting["id"] == current_id:

                default_index = index

                break

        selected_label = st.selectbox(
            "Select meeting",
            option_labels,
            index=default_index
        )

        selected_id = meeting_options[selected_label]

        if selected_id != current_id:

            load_selected_meeting(selected_id)

            st.rerun()

        st.caption(f"Total meetings: {len(meetings)}")

    else:

        st.info("No meetings saved yet.")

    st.divider()

    st.caption("AI Meeting Intelligence")
    st.caption("Version 2.0")


# =====================================================
# HOME PAGE
# =====================================================

if page == "🏠 Home":

    total_meetings = len(meetings)

    latest_name = (
        meetings[0]["meeting_name"]
        if meetings
        else "No meetings yet"
    )

    latest_name = html.escape(str(latest_name))

    rag_status = (
        "Ready"
        if st.session_state.get("rag_ready")
        else "Waiting"
    )

    render_html(
        f"""
        <div class="hero-container">

            <div class="section-label">
                AI-POWERED PRODUCTIVITY
            </div>

            <div class="hero-title">
                Turn conversations into
                <span>intelligence.</span>
            </div>

            <div class="hero-subtitle">
                Analyze meetings, extract important decisions,
                track action items, and ask questions using
                AI-powered meeting intelligence.
            </div>

        </div>
        """
    )

    render_html(
        """
        <div class="section-label">
            WORKSPACE OVERVIEW
        </div>
        """
    )

    metric_col1, metric_col2, metric_col3 = st.columns(3)

    with metric_col1:

        render_html(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    📚 Total Meetings
                </div>

                <div class="metric-value">
                    {total_meetings}
                </div>

                <div class="metric-description">
                    Meetings saved in your workspace
                </div>

            </div>
            """
        )

    with metric_col2:

        render_html(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    🕒 Latest Meeting
                </div>

                <div class="metric-value"
                     style="font-size: 18px;">
                    {latest_name}
                </div>

                <div class="metric-description">
                    Most recently saved meeting
                </div>

            </div>
            """
        )

    with metric_col3:

        render_html(
            f"""
            <div class="metric-card">

                <div class="metric-label">
                    🧠 RAG Assistant
                </div>

                <div class="metric-value"
                     style="font-size: 25px;">
                    {rag_status}
                </div>

                <div class="metric-description">
                    Selected meeting knowledge status
                </div>

            </div>
            """
        )

    st.write("")
    st.write("")

    render_html(
        """
        <div class="section-label">
            NEW MEETING
        </div>
        """
    )

    st.header("🎙️ Analyze a New Meeting")

    st.write(
        "Upload an audio recording to generate an AI-powered "
        "meeting report."
    )

    uploaded_audio = st.file_uploader(
        "Upload your meeting audio",
        type=["mp3", "wav", "m4a", "ogg", "mp4"]
    )

    if uploaded_audio:

        st.audio(uploaded_audio)

        st.success(f"Uploaded: {uploaded_audio.name}")

        analyze_button = st.button(
            "🚀 Analyze & Save Meeting",
            type="primary",
            use_container_width=True
        )

        if analyze_button:

            file_extension = os.path.splitext(
                uploaded_audio.name
            )[1]

            temp_path = None

            try:

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=file_extension
                ) as temp_file:

                    temp_file.write(
                        uploaded_audio.getvalue()
                    )

                    temp_path = temp_file.name

                with st.spinner(
                    "🎧 Gemini is analyzing your meeting..."
                ):

                    report = analyze_meeting_audio(
                        temp_path
                    )

                with st.spinner(
                    "💾 Saving meeting in database..."
                ):

                    meeting_id = save_meeting(
                        meeting_name=uploaded_audio.name,
                        report=report
                    )

                with st.spinner(
                    "🧠 Building your meeting knowledge base..."
                ):

                    chunks_stored = store_meeting_report(
                        report=report,
                        meeting_id=meeting_id
                    )

                st.session_state["meeting_report"] = report

                st.session_state["meeting_name"] = uploaded_audio.name

                st.session_state["current_meeting_id"] = meeting_id

                st.session_state["selected_meeting_id"] = meeting_id

                st.session_state["rag_ready"] = True

                st.session_state["chat_history"][meeting_id] = []

                st.success(
                    "✅ Meeting analyzed and saved successfully!"
                )

                st.info(
                    f"📚 {chunks_stored} knowledge chunks stored."
                )

                st.info(
                    f"🆔 Meeting ID: {meeting_id}"
                )

                st.header("📋 Meeting Intelligence Report")

                st.markdown(report)

            except Exception as error:

                st.error(
                    f"An error occurred: {error}"
                )

            finally:

                if temp_path and os.path.exists(temp_path):

                    os.remove(temp_path)

    else:

        st.info(
            "Upload an audio file to start analyzing."
        )

    st.divider()

    render_html(
        """
        <div class="section-label">
            CAPABILITIES
        </div>
        """
    )

    st.header("✨ What MeetMind AI Can Do")

    col1, col2, col3 = st.columns(3)

    with col1:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">📝</div>

                <div class="feature-title">
                    Smart Summaries
                </div>

                <div class="feature-text">
                    Generate concise summaries containing
                    important discussions, decisions,
                    and key takeaways.
                </div>

            </div>
            """
        )

    with col2:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">👥</div>

                <div class="feature-title">
                    Action Items
                </div>

                <div class="feature-text">
                    Identify assigned tasks, responsible
                    team members, and mentioned deadlines
                    from meeting conversations.
                </div>

            </div>
            """
        )

    with col3:

        render_html(
            """
            <div class="feature-card">

                <div class="feature-icon">💬</div>

                <div class="feature-title">
                    Meeting RAG
                </div>

                <div class="feature-text">
                    Ask natural-language questions about
                    a selected meeting and retrieve
                    context-based answers.
                </div>

            </div>
            """
        )


# =====================================================
# MEETING ANALYSIS PAGE
# =====================================================

elif page == "📊 Meeting Analysis":

    st.header("📊 Meeting Analysis")

    report = st.session_state.get("meeting_report")

    meeting_name = st.session_state.get("meeting_name")

    meeting_id = st.session_state.get("current_meeting_id")

    if report and meeting_id is not None:

        safe_meeting_name = html.escape(str(meeting_name))

        render_html(
            f"""
            <div class="meeting-banner">

                <div class="meeting-banner-title">
                    📌 {safe_meeting_name}
                </div>

                <div class="meeting-banner-text">
                    Meeting ID: {meeting_id}
                </div>

            </div>
            """
        )

        st.subheader("📋 Meeting Intelligence Report")

        st.markdown(report)

        st.download_button(
            label="📥 Download Meeting Report",
            data=report,
            file_name=f"meeting_{meeting_id}_report.txt",
            mime="text/plain"
        )

        st.divider()

        st.subheader("🗑️ Meeting Management")

        delete_confirmation = st.checkbox(
            "I want to delete this meeting"
        )

        if delete_confirmation:

            if st.button(
                "Delete Selected Meeting",
                type="secondary"
            ):

                delete_meeting(meeting_id)

                clear_current_meeting()

                st.success(
                    "Meeting deleted from the database."
                )

                st.rerun()

    else:

        st.info(
            "No meeting selected. Select a meeting from the sidebar "
            "or upload a new meeting from Home."
        )


# =====================================================
# ASK YOUR MEETING PAGE
# =====================================================

elif page == "💬 Ask Your Meeting":

    st.header("💬 Ask Your Meeting")

    st.caption(
        "Ask questions about your selected meeting."
    )

    meeting_id = st.session_state.get("current_meeting_id")

    meeting_name = st.session_state.get("meeting_name")

    report = st.session_state.get("meeting_report")

    if not report or meeting_id is None:

        st.warning(
            "Please upload and analyze a meeting, "
            "or select a meeting from the sidebar."
        )

    else:

        safe_meeting_name = html.escape(str(meeting_name))

        render_html(
            f"""
            <div class="meeting-banner">

                <div class="meeting-banner-title">
                    💬 {safe_meeting_name}
                </div>

                <div class="meeting-banner-text">
                    Questions will use this meeting's knowledge only.
                </div>

            </div>
            """
        )

        current_chat = get_current_chat_history()

        st.subheader("💡 Suggested Questions")

        suggestion_col1, suggestion_col2, suggestion_col3 = st.columns(3)

        with suggestion_col1:
            st.caption("What was discussed?")

        with suggestion_col2:
            st.caption("What tasks were assigned?")

        with suggestion_col3:
            st.caption("What are the deadlines?")

        st.divider()

        if st.button("🗑️ Clear Chat"):

            st.session_state["chat_history"][meeting_id] = []

            st.rerun()

        for chat in current_chat:

            with st.chat_message("user"):

                st.write(chat["question"])

            with st.chat_message("assistant"):

                st.markdown(chat["answer"])

        question = st.chat_input(
            "Ask something about this meeting..."
        )

        if question:

            with st.chat_message("user"):

                st.write(question)

            with st.chat_message("assistant"):

                with st.spinner(
                    "🤖 Searching selected meeting knowledge..."
                ):

                    try:

                        answer = ask_meeting(
                            question=question,
                            meeting_id=meeting_id
                        )

                        st.markdown(answer)

                        st.session_state[
                            "chat_history"
                        ][meeting_id].append({

                            "question": question,

                            "answer": answer

                        })

                    except Exception as error:

                        st.error(
                            f"An error occurred: {error}"
                        )