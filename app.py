import streamlit as st
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

# Set page title and layout
st.set_page_config(page_title="NAAC Accreditation Assistant", layout="wide")

# Hardcoded Credentials (Read directly by the application)
API_KEY = "uXGpyYh8-9QCObAEcR3-AbCf2Wqmr5scelb6ZAZDX-DT"
PROJECT_ID = "12dd36a8-978e-4602-9a47-d7fe000c8ddd"

st.title("🛡️ NAAC Accreditation Multi-Agent Assistant")
st.subheader("Powered by Llama 3.3 & watsonx.ai RAG Workflow")

# Main Query UI Component
query = st.text_area(
    "Ask the NAAC Agent / Request SSR Generation Draft:",
    placeholder="e.g., Generate the narrative description draft for Criteria 1..."
)

if st.button("Execute Multi-Agent Synthesis"):
    if not query.strip():
        st.error("Please enter a prompt or metric request first.")
    else:
        with st.spinner("Executing LangFlow agents (RAG Knowledge Fetcher ➡️ Narrative Planner)..."):
            
            # Setup Watsonx connection payload
            credentials = {
                "url": "https://us-south.ml.cloud.ibm.com", 
                "apikey": API_KEY
            }
            model_id = "meta-llama/llama-3-3-70b-instruct"
            
            params = {
                GenParams.DECODING_METHOD: "greedy",
                GenParams.MAX_NEW_TOKENS: 900
            }
            
            try:
                # Initialize and run execution flow
                model = Model(
                    model_id=model_id, 
                    credentials=credentials, 
                    project_id=PROJECT_ID, 
                    params=params
                )
                
                # Context injection framework tracking
                system_prompt = f"Context: NAAC Criteria Manual specifies strict adherence to data templates. \nUser Query: {query}"
                response = model.generate_text(prompt=system_prompt)
                
                st.success("✅ Analysis Complete")
                st.markdown("### Generated Document / Advisory Input:")
                st.write(response)
                
            except Exception as e:
                st.error(f"Error calling watsonx services: {str(e)}")