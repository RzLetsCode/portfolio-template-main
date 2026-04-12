import streamlit as st
import base64
from src.services.llm_service import AzureAIEngine
from src.services.claim_logic import draft_response_email

# ==========================================
# PAGE SETUP & CUSTOM CSS
# ==========================================
st.set_page_config(
    page_title="Insurance Claim Processor | code2career_ai",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Injecting custom CSS to clean up the UI (hide default Streamlit headers/footers)
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stButton>button {
            width: 100%;
            border-radius: 4px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE INITIALIZATION
# ==========================================
# This ensures results remain on screen even if the app reruns
if 'processing_complete' not in st.session_state:
    st.session_state.processing_complete = False
if 'claim_data' not in st.session_state:
    st.session_state.claim_data = None
if 'damage_info' not in st.session_state:
    st.session_state.damage_info = None
if 'draft_email' not in st.session_state:
    st.session_state.draft_email = None

def reset_state():
    """Resets the output state if new inputs are provided."""
    st.session_state.processing_complete = False

def main():
    # --- HEADER ---
    col_header, col_logo = st.columns([4, 1])
    with col_header:
        st.title("🛡️ Automated Claims Triage Portal")
        st.markdown("**Enterprise Multimodal AI:** Ingest unstructured emails, assess damage via Computer Vision, and auto-draft deterministic responses.")
    with col_logo:
        # Placeholder for your brand logo if you want to add it later
        st.markdown("<h3 style='text-align: right; color: #E74C3C;'>&lt; / &gt;</h3>", unsafe_allow_html=True)
    
    st.markdown("---")

    # --- SIDEBAR (CONFIG) ---
    with st.sidebar:
        st.header("⚙️ System Configuration")
        st.markdown("Provide Azure credentials to activate the engine:")
        api_key = st.text_input("Azure OPENAI API Key", type="password", help="Found in Azure Portal")
        endpoint = st.text_input("Azure OPENAI Endpoint URL", placeholder="https://your-resource.openai.azure.com/")
        
        st.markdown("---")
        st.markdown("### 📋 Standard Operating Procedure")
        st.info(
            "1. Paste the raw client email.\n"
            "2. Upload the incident evidence (photo).\n"
            "3. Click **Execute Triage**."
        )

    # --- MAIN LAYOUT ---
    col_input, col_output = st.columns([1, 1.2], gap="large")

    with col_input:
        st.subheader("📥 Data Ingestion")
        st.markdown("Submit claim details below for automated processing.")
        
        email_input = st.text_area(
            "Raw Client Email", 
            height=280, 
            placeholder="Dear agent...\n\nMy name is Linda Smith and I am writing this letter in regards with the insurance claim...",
            on_change=reset_state
        )
        
        uploaded_file = st.file_uploader(
            "Incident Evidence (JPG/PNG)", 
            type=['jpg', 'jpeg', 'png'],
            on_change=reset_state
        )

        if st.button("🚀 Execute Triage", type="primary"):
            if not email_input:
                st.warning("⚠️ Data Ingestion Error: Please provide the raw email text.")
            else:
                try:
                    # Use st.status for a professional loading indicator
                    with st.status("Initializing AI Pipeline...", expanded=True) as status:
                        st.write("Connecting to Azure API...")
                        ai_engine = AzureAIEngine(api_key=api_key, endpoint=endpoint)
                        
                        st.write("Extracting structured entities from text...")
                        st.session_state.claim_data = ai_engine.extract_text_data(email_input)
                        
                        if uploaded_file is not None:
                            st.write("Performing Computer Vision analysis...")
                            bytes_data = uploaded_file.getvalue()
                            base64_img = base64.b64encode(bytes_data).decode('utf-8')
                            st.session_state.damage_info = ai_engine.analyze_image(base64_img)
                        else:
                            st.write("No image detected. Bypassing Vision analysis...")
                            from src.models import DamageAssessment
                            st.session_state.damage_info = DamageAssessment(description="No image provided for assessment.", severity="Unknown")

                        st.write("Drafting deterministic response...")
                        st.session_state.draft_email = draft_response_email(st.session_state.claim_data, st.session_state.damage_info)
                        
                        status.update(label="Triage Complete!", state="complete", expanded=False)
                        st.session_state.processing_complete = True
                
                except Exception as e:
                    st.error(f"Pipeline Execution Failed: {str(e)}")

    # --- OUTPUT SECTION ---
    with col_output:
        st.subheader("📊 Analytical Output")
        
        if not st.session_state.processing_complete:
            st.info("Awaiting data ingestion. Output will render here upon successful execution.")
        else:
            # Using Tabs for a clean, dashboard-like presentation
            tab1, tab2, tab3 = st.tabs(["📑 Extracted Entities", "👁️ Vision Analysis", "✉️ Communications"])
            
            with tab1:
                st.markdown("### Structured Claim Data")
                # Visualizing missing fields dynamically
                missing = st.session_state.claim_data.missing_fields
                if missing:
                    st.error(f"**Missing Required Fields:** {', '.join(missing)}")
                else:
                    st.success("**All Required Fields Present**")
                
                # Displaying JSON as a clean dictionary
                st.json(st.session_state.claim_data.model_dump())

            with tab2:
                st.markdown("### Damage Severity Assessment")
                severity = st.session_state.damage_info.severity
                
                # Dynamic Metric Color based on severity
                if severity.lower() == 'high':
                    st.error(f"Assessed Severity: **{severity.upper()}**")
                elif severity.lower() == 'medium':
                    st.warning(f"Assessed Severity: **{severity.upper()}**")
                else:
                    st.success(f"Assessed Severity: **{severity.upper()}**")
                    
                st.write("**Technical Description:**")
                st.info(st.session_state.damage_info.description)
                
                if uploaded_file is not None:
                    st.image(uploaded_file, caption="Processed Image", use_container_width=True)

            with tab3:
                st.markdown("### Auto-Generated Response Draft")
                st.markdown("Review the deterministic draft below. Edits can be made before sending.")
                st.text_area("Final Output Draft", value=st.session_state.draft_email, height=300, label_visibility="collapsed")
                
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    st.button("✉️ Send to Client", disabled=True, help="Mock button for UI purposes")
                with col_btn2:
                    st.button("💾 Save to CRM", disabled=True, help="Mock button for UI purposes")

    # --- FOOTER ---
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: grey; font-size: 0.9em;'>© 2026 code2career_ai • Enterprise Architecture Demo</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()