import streamlit as st
import pandas as pd

# =============================================================================
# App Title and Header
# =============================================================================
st.title("Radiology Pocket Guide")
st.markdown("<p style='font-size:12px'>Created by Michailidis A. for free use</p>", unsafe_allow_html=True)
st.markdown("**Disclaimer:** This guide is for educational purposes only and is not a substitute for professional clinical judgment.")

# =============================================================================
# Sidebar: Input Parameters
# =============================================================================
st.sidebar.header("Diagnostic Parameters")

# 1. Select Imaging Modality
modality = st.sidebar.selectbox(
    "Select Imaging Modality:",
    ["X-Ray", "CT", "MRI", "Ultrasound", "Nuclear Medicine"]
)

# 2. Select Organ/System based on Modality
organ_options = []
if modality == "X-Ray":
    organ_options = ["Chest", "Skeletal", "Abdomen", "Head/Neck", "Spine"]
elif modality == "CT":
    organ_options = ["Brain", "Chest", "Abdomen/Pelvis", "Musculoskeletal", "Vascular"]
elif modality == "MRI":
    organ_options = ["Brain", "Spine", "Musculoskeletal", "Abdomen", "Pelvis"]
elif modality == "Ultrasound":
    organ_options = ["Abdomen", "Pelvis", "Thyroid", "Musculoskeletal"]
elif modality == "Nuclear Medicine":
    organ_options = ["Bone", "Cardiac", "Oncology"]
organ = st.sidebar.selectbox("Select Organ/System:", organ_options)

# 3. Select Type of Lesion
lesion_type = st.sidebar.selectbox(
    "Select Lesion Type:",
    ["Mass", "Cystic Lesion", "Calcification", "Hemorrhage", "Inflammatory", "Vascular Malformation", "Degenerative"]
)

# 4. Additional Lesion Characteristics
st.sidebar.header("Lesion Characteristics")
lesion_size = st.sidebar.text_input("Lesion Size (cm):", "e.g., 2.5")
lesion_margin = st.sidebar.selectbox("Lesion Margin:", ["Well-circumscribed", "Ill-defined", "Spiculated", "Infiltrative"])
lesion_appearance = st.sidebar.selectbox(
    "Lesion Appearance (Density/Signal):", 
    ["Hyperdense/Hyperattenuating", "Hypodense/Hypoattenuating", "Isodense/Isoattenuating", "Mixed", "T2 Hyperintense", "T1 Hypointense"]
)
lesion_enhancement = st.sidebar.selectbox(
    "Enhancement Pattern (if applicable):", 
    ["None", "Homogeneous", "Heterogeneous", "Ring-enhancing", "Peripheral enhancement", "Progressive", "Washout"]
)

# =============================================================================
# Generate Comprehensive Diagnostic Guide
# =============================================================================
def get_complete_guide(modality, organ, lesion_type, lesion_size, lesion_margin, lesion_appearance, lesion_enhancement):
    guide = f"## Radiology Pocket Guide Output\n\n"
    guide += f"**Modality:** {modality}\n\n"
    guide += f"**Organ/System:** {organ}\n\n"
    guide += f"**Lesion Type:** {lesion_type}\n\n"
    guide += f"**Provided Characteristics:**\n"
    guide += f"- Size: {lesion_size} cm\n"
    guide += f"- Margin: {lesion_margin}\n"
    guide += f"- Appearance: {lesion_appearance}\n"
    guide += f"- Enhancement: {lesion_enhancement}\n\n"
    
    guide += "---\n\n"
    
    # Example for CT Brain Mass (expand as a prototype)
    if modality == "CT" and organ == "Brain" and lesion_type == "Mass":
        guide += "### CT Brain Mass Guide\n\n"
        guide += "**Differential Diagnosis:**\n"
        guide += "- **Primary Brain Tumors:** Glioma (including glioblastoma multiforme), astrocytoma, oligodendroglioma\n"
        guide += "- **Metastatic Lesions:** Consider if there is a known primary malignancy elsewhere\n"
        guide += "- **Extra-Axial Tumors:** Meningioma (especially if a dural tail is present)\n"
        guide += "- **Infectious/Inflammatory:** Brain abscess or tumefactive demyelination, particularly if clinical signs of infection are present\n\n"
        
        guide += "**Imaging Features to Evaluate:**\n"
        guide += "- **Attenuation:** Compare lesion density relative to gray and white matter. Areas of necrosis or hemorrhage will have mixed densities.\n"
        guide += "- **Margins:** A well-circumscribed lesion may suggest a metastasis or meningioma, whereas an infiltrative margin favors high-grade gliomas.\n"
        guide += "- **Enhancement Patterns:** Homogeneous enhancement is common in metastases and low-grade tumors, while ring-enhancement may be seen in abscesses and high-grade malignancies.\n"
        guide += "- **Calcifications:** Present in oligodendrogliomas and some metastases; use bone window settings to identify subtle calcifications.\n\n"
        
        guide += "**Anatomical Considerations:**\n"
        guide += "- **Location:** Assess if the lesion is intra-axial (within the brain parenchyma) or extra-axial (meningeal-based).\n"
        guide += "- **Relationship to Ventricular System:** Note if there is any ventricular compression or midline shift.\n"
        guide += "- **Perilesional Edema:** The extent of surrounding edema can provide clues to the aggressiveness of the lesion.\n\n"
        
        guide += "**Additional Tips:**\n"
        guide += "- Correlate with clinical history (age, symptoms, known primary tumors, immune status).\n"
        guide += "- Consider advanced imaging with MRI for better tissue characterization if CT findings are inconclusive.\n"
        guide += "- Look for secondary signs such as hemorrhage, cystic degeneration, or calcifications.\n\n"
        guide += "For further detailed reading, please visit [Radiopaedia - Brain Tumor](https://radiopaedia.org/articles/brain-tumour).\n\n"
    
    # Example for X-Ray Chest Mass
    elif modality == "X-Ray" and organ == "Chest" and lesion_type == "Mass":
        guide += "### X-Ray Chest Mass Guide\n\n"
        guide += "**Differential Diagnosis:**\n"
        guide += "- **Primary Lung Carcinoma:** Often seen in older patients with a smoking history\n"
        guide += "- **Metastatic Disease:** Multiple nodules may suggest hematogenous spread\n"
        guide += "- **Benign Lesions:** Hamartoma (often with popcorn calcifications), granuloma (calcified in healed infections)\n\n"
        
        guide += "**Imaging Features to Evaluate:**\n"
        guide += "- **Margins:** Spiculated margins raise concern for malignancy; well-circumscribed lesions may be benign.\n"
        guide += "- **Calcification Patterns:** Stippled, eccentric, or central calcifications can help differentiate benign from malignant lesions.\n"
        guide += "- **Cavitation:** Evaluate for cavitary lesions which might represent squamous cell carcinoma or post-infectious changes.\n"
        guide += "- **Associated Findings:** Look for mediastinal lymphadenopathy, pleural effusion, or signs of atelectasis.\n\n"
        
        guide += "**Anatomical Considerations:**\n"
        guide += "- **Lobar Anatomy:** Identify which lobe is involved; central versus peripheral location may guide diagnosis.\n"
        guide += "- **Airway Involvement:** Assess for endobronchial lesions that may cause obstructive pneumonia.\n\n"
        
        guide += "**Additional Tips:**\n"
        guide += "- Compare with prior imaging to assess growth rate.\n"
        guide += "- Correlate with clinical symptoms such as cough, hemoptysis, or weight loss.\n\n"
        guide += "For additional details, please see [Radiopaedia - Lung Mass](https://radiopaedia.org/articles/lung-mass).\n\n"
    
    # Example for MRI Musculoskeletal Cystic Lesion
    elif modality == "MRI" and organ == "Musculoskeletal" and lesion_type == "Cystic Lesion":
        guide += "### MRI Musculoskeletal Cystic Lesion Guide\n\n"
        guide += "**Differential Diagnosis:**\n"
        guide += "- **Simple Bone Cyst:** Common in children and adolescents, usually asymptomatic and discovered incidentally.\n"
        guide += "- **Aneurysmal Bone Cyst (ABC):** Typically eccentric and expansile with fluid–fluid levels.\n"
        guide += "- **Abscess:** If clinical signs of infection are present, consider septic arthritis or osteomyelitis with abscess formation.\n\n"
        
        guide += "**Imaging Features to Evaluate:**\n"
        guide += "- **Signal Characteristics:** On T1-weighted images, cysts are usually low signal; on T2, high signal intensity is typical.\n"
        guide += "- **Fluid–Fluid Levels:** Highly suggestive of an ABC or hemorrhagic cyst.\n"
        guide += "- **Enhancement:** Minimal enhancement in simple cysts; irregular or rim enhancement may indicate abscess or neoplasm.\n\n"
        
        guide += "**Anatomical Considerations:**\n"
        guide += "- **Location within Bone:** Diaphyseal versus metaphyseal location can influence the differential.\n"
        guide += "- **Cortical Integrity:** Look for cortical thinning or expansion, which may suggest a more aggressive process.\n\n"
        
        guide += "**Additional Tips:**\n"
        guide += "- Compare with radiographs to look for any evidence of matrix mineralization or periosteal reaction.\n"
        guide += "- Always correlate with clinical findings such as pain, fever, or a history of trauma.\n\n"
        guide += "For further reading, refer to [Radiopaedia - Aneurysmal Bone Cyst](https://radiopaedia.org/articles/aneurysmal-bone-cyst).\n\n"
    
    # Example for Ultrasound Thyroid Lesion
    elif modality == "Ultrasound" and organ == "Thyroid" and lesion_type == "Mass":
        guide += "### Ultrasound Thyroid Nodule Guide\n\n"
        guide += "**Differential Diagnosis:**\n"
        guide += "- **Benign Nodules:** Colloid nodules, thyroid adenomas\n"
        guide += "- **Malignant Nodules:** Papillary thyroid carcinoma (most common), follicular carcinoma\n\n"
        
        guide += "**Imaging Features to Evaluate:**\n"
        guide += "- **Echogenicity:** Hypoechoic nodules are more suspicious; isoechoic or hyperechoic nodules are usually benign.\n"
        guide += "- **Margins:** Irregular, microlobulated, or spiculated margins raise suspicion for malignancy.\n"
        guide += "- **Calcifications:** Microcalcifications are concerning for papillary carcinoma.\n"
        guide += "- **Vascularity:** Increased intranodular blood flow may be seen in malignant lesions.\n\n"
        
        guide += "**Anatomical Considerations:**\n"
        guide += "- **Lobular Location:** Assess whether the nodule is in the right or left lobe, isthmus, or near critical structures such as the recurrent laryngeal nerve.\n\n"
        
        guide += "**Additional Tips:**\n"
        guide += "- Use standardized reporting systems such as the TI-RADS for risk stratification.\n"
        guide += "- Consider fine-needle aspiration (FNA) biopsy if the nodule meets size or suspicious criteria.\n\n"
        guide += "For more detailed criteria, visit [Radiopaedia - Thyroid Nodule](https://radiopaedia.org/articles/thyroid-nodule).\n\n"
    
    # Default message for combinations not explicitly expanded:
    else:
        guide += "### Comprehensive Guide\n\n"
        guide += "The combination of parameters selected is not among the most commonly encountered scenarios in this guide. Please refer to the following general recommendations:\n\n"
        guide += "**General Differential Diagnosis and Approach:**\n"
        guide += "- Review the lesion’s size, shape, margin, internal characteristics, and enhancement pattern.\n"
        guide += "- Compare with prior imaging if available to assess for stability or change.\n"
        guide += "- Correlate imaging findings with the patient’s clinical history, laboratory results, and risk factors.\n"
        guide += "- Consider advanced imaging modalities (e.g., MRI, PET-CT) or image-guided biopsy for definitive diagnosis.\n\n"
        guide += "**Anatomical and Vascular Considerations:**\n"
        guide += "- Familiarize yourself with the relevant regional anatomy and any known anatomical variations.\n"
        guide += "- Use standardized reporting systems (e.g., BI-RADS, LI-RADS, TI-RADS) when applicable.\n\n"
        guide += "For additional examples and in-depth discussions, please consult [Radiopaedia](https://radiopaedia.org/).\n\n"
    
    guide += "---\n"
    guide += "\n**Remember:** This guide is intended as an educational aid. Always integrate imaging findings with clinical data and consult subspecialty experts as needed.\n"
    return guide

# =============================================================================
# Display the Pocket Guide Output
# =============================================================================
st.header("Diagnostic Pocket Guide Output")
output_text = get_complete_guide(modality, organ, lesion_type, lesion_size, lesion_margin, lesion_appearance, lesion_enhancement)
st.text_area("Complete Diagnostic Guide", value=output_text, height=700)
