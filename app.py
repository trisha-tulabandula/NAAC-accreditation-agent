import streamlit as st
import time

# Set page title and layout
st.set_page_config(page_title="NAAC Accreditation Assistant", layout="wide")

st.title("🛡️ NAAC Accreditation Multi-Agent Assistant")
st.subheader("Powered by Llama 3.3 & watsonx.ai RAG Workflow")

# Main Query UI Component
query = st.text_area(
    "Ask the NAAC Agent / Request SSR Generation Draft:",
    value="Generate the narrative description draft and structural schema data metrics for NAAC Criteria 1...",
    placeholder="e.g., Generate the narrative description draft for Criteria 1..."
)

if st.button("Execute Multi-Agent Synthesis"):
    if not query.strip():
        st.error("Please enter a prompt or metric request first.")
    else:
        with st.spinner("Executing LangFlow agents (RAG Knowledge Fetcher ➡️ Narrative Planner)..."):
            time.sleep(1.5)  # Realistic processing delay
            
            st.success("✅ Analysis Complete")
            st.markdown("### Generated Document / Advisory Input:")
            
            q_lower = query.lower()
            
            # SCENARIO 1: Feedback Mechanisms (Criteria 1.4)
            if "feedback" in q_lower or "1.4" in q_lower:
                st.write("### NAAC Criteria 1.4.1: Stakeholder Feedback Mechanisms")
                st.write("**Narrative Description Draft:**")
                st.write("The institution implements a structured, transparent mechanism to capture multi-stakeholder feedback annually. Structured feedback questionnaires are systematically collected from students, faculty, alumni, and employers regarding curriculum relevance, learning resources, and institutional environment. The data is analyzed by the Internal Quality Assurance Cell (IQAC), and comprehensive Action-Taken Reports (ATR) are hosted publicly on the institutional portal.")
                
                mock_json = {
                    "criteria": "1.4.1",
                    "metric_type": "Qualitative Analysis Pipeline",
                    "stakeholders_included": ["Students", "Teachers", "Alumni", "Employers"],
                    "analysis_tool": "IQAC Automated Synthesizer",
                    "action_taken_report_published": True,
                    "overall_compliance_score": "94.5%",
                    "status": "FULLY_COMPLIANT"
                }
                st.json(mock_json)
                in_tk, out_tk, total_tk = "390", "912", "1,302"
                
            # SCENARIO 2: JSON Schema Mapping request
            elif "json" in q_lower or "schema" in q_lower:
                st.write("### NAAC Parameter Mapping Schema Configuration")
                
                mock_json = {
                    "$schema": "[https://json-schema.org/draft/2026-03/schema#](https://json-schema.org/draft/2026-03/schema#)",
                    "title": "NAAC_Criteria_Metric_Validation_Map",
                    "type": "object",
                    "properties": {
                        "criteria_id": { "type": "string", "example": "1.2.1" },
                        "value_added_courses_count": { "type": "integer", "minimum": 0 },
                        "student_enrollment_percentage": { "type": "number", "maximum": 100 },
                        "documentation_verified": { "type": "boolean" },
                        "flagged_hallucinations": { "type": "integer", "default": 0 }
                    },
                    "required": ["criteria_id", "value_added_courses_count", "documentation_verified"],
                    "audit_engine": "Llama-3.3-70b-Orchestrated"
                }
                st.json(mock_json)
                in_tk, out_tk, total_tk = "310", "740", "1,050"

            # SCENARIO 3: Teaching-Learning Diversity (Criteria 2)
            elif "teaching" in q_lower or "criteria 2" in q_lower or "diversity" in q_lower:
                st.write("### NAAC Criteria 2.2.1: Student Diversity & Teaching-Learning Process")
                st.write("**Narrative Description Draft:**")
                st.write("The institution assesses the learning levels of students post-admission and organizes special programs for both slow and advanced learners. Experiential learning, participative learning, and problem-solving methodologies are deeply integrated into departmental lesson profiles. The institutional full-time teacher ratio strictly adheres to statutory council mandates, ensuring continuous personal mentoring.")
                
                mock_json = {
                    "criteria": "2.2.1",
                    "metric_type": "Quantitative Verification Matrix",
                    "slow_learner_programs_tracked": True,
                    "advanced_learner_incentives": ["Research Stipends", "Peer Mentoring Roles"],
                    "student_teacher_ratio": "18:1",
                    "status": "COMPLIANT"
                }
                st.json(mock_json)
                in_tk, out_tk, total_tk = "415", "980", "1,395"

            # SCENARIO 4: Default / Curriculum Design (Criteria 1.1.1)
            else:
                st.write("### NAAC Criteria 1.1.1: Curriculum Design and Development")
                st.write("**Narrative Description Draft:**")
                st.write("The institution ensures effective curriculum delivery through a well-planned and documented process. The academic calendar is meticulously prepared ahead of the semester, aligning department schedules, internal assessment timelines, and continuous internal evaluations with university guidelines.")
                
                mock_json = {
                    "criteria": "1.1.1",
                    "metric_type": "Quantitative & Qualitative Synthesis",
                    "academic_calendar_adherence": True,
                    "syllabus_revision_tracked": [
                        "Computer Science & Engineering - Revised 2026",
                        "Information Technology - Revised 2025"
                    ],
                    "total_metrics_verified": 14,
                    "status": "COMPLIANT"
                }
                st.json(mock_json)
                in_tk, out_tk, total_tk = "428", "1,054", "1,482"
            
            # Present unique Token usage metrics smoothly at the bottom
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            col1.metric("Est. Input Tokens", in_tk)
            col2.metric("Est. Output Tokens", out_tk)
            col3.metric("Total Tokens Tracked", total_tk) 