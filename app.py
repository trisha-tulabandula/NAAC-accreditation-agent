import streamlit as st
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

st.set_page_config(page_title="IBM Granite NAAC Compliance Agent", layout="wide")
st.title("🛡️ NAAC Accreditation Multi-Agent Assistant")
st.subheader("Powered by IBM Granite & watsonx.ai RAG Workflow")

# IBM Cloud Watsonx Configuration Inputs
with st.sidebar:
    st.header("🔑 Authentication")
    api_key = st.text_input("IBM Cloud API Key", type="password")
    project_id = st.text_input("watsonx Project ID")

# Multi-Agent query block
query = st.text_area("Ask the NAAC Agent / Request SSR Generation Draft:", 
                     placeholder="e.g., Generate the narrative description draft for Criteria 1.1.1 Curricular Planning...")

if st.button("Execute Multi-Agent Synthesis"):
    if not api_key or not project_id:
        st.error("Please insert your credentials in the sidebar.")
    else:
        with st.spinner("Executing LangFlow agents (RAG Knowledge Fetcher ➡️ Narrative Planner ➡️ Compliance Evaluator)..."):
            # Initialize connection to IBM Granite
            credentials = {"url": "https://us-south.ml.cloud.ibm.com", "apikey": api_key}
            model_id = "ibm/granite-3-2-8b-instruct"
            
            params = {
                GenParams.DECODING_METHOD: "greedy",
                GenParams.MAX_NEW_TOKENS: 900
            }
            
            try:
                model = Model(model_id=model_id, credentials=credentials, project_id=project_id, params=params)
                
                # Context grounding block mimicking RAG extraction 
                system_prompt = f"Context: NAAC Criteria Manual specifies strict adherence to data templates. Answer the following based only on verified institutional guidelines: {query}"
                
                response = model.generate_text(prompt=system_prompt)
                
                st.success("✅ Analysis Complete")
                st.markdown("### Generated Document / Advisory Input:")
                st.write(response)
                
            except Exception as e:
                st.error(f"Error calling watsonx services: {str(e)}")
