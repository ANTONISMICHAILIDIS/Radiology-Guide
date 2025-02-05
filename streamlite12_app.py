import streamlit as st
import pandas as pd

# =============================================================================
# App Title and Header
# =============================================================================
st.title("Radiology Pocket Guide")
st.markdown("<p style='font-size:12px'>Created by Michailidis A. for free use</p>", unsafe_allow_html=True)
st.markdown("**Disclaimer:** This guide is for educational purposes only. It is not a substitute for professional clinical judgment.")

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
lesion_margin = st.sidebar.selectbox("Lesion Margin:", 
                                     ["Well-circumscribed", "Ill-defined", "Spiculated", "Infiltrative"])
lesion_appearance = st.sidebar.selectbox(
    "Lesion Appearance (Density/Signal):", 
    ["Hyperdense/Hyperattenuating", "Hypodense/Hypoattenuating", "Isodense/Isoattenuating", 
     "Mixed", "T2 Hyperintense", "T1 Hypointense"]
)
lesion_enhancement = st.sidebar.selectbox(
    "Enhancement Pattern (if applicable):", 
    ["None", "Homogeneous", "Heterogeneous", "Ring-enhancing", "Peripheral enhancement", "Progressive", "Washout"]
)

# =============================================================================
# Comprehensive Diagnostic Guide Generator
# =============================================================================
def get_complete_guide(modality, organ, lesion_type, lesion_size, lesion_margin, lesion_appearance, lesion_enhancement):
    guide = f"## Radiology Pocket Guide Output\n\n"
    guide += f"**Modality:** {modality}\n\n"
    guide += f"**Organ/System:** {organ}\n\n"
    guide += f"**Lesion Type:** {lesion_type}\n\n"
    guide += f"**Provided Characteristics:**\n"
    guide += f"- **Size:** {lesion_size} cm\n"
    guide += f"- **Margin:** {lesion_margin}\n"
    guide += f"- **Appearance:** {lesion_appearance}\n"
    guide += f"- **Enhancement:** {lesion_enhancement}\n\n"
    
    guide += "---\n\n"
    
    # ===================== CT Brain =====================
    if modality == "CT" and organ == "Brain" and lesion_type == "Mass":
        guide += "### CT Brain Mass Guide\n\n"
        guide += "**Differential Diagnosis:**\n"
        guide += "- **Primary Brain Tumors:** Glioma (including glioblastoma multiforme), astrocytoma, oligodendroglioma\n"
        guide += "- **Metastatic Lesions:** Especially in patients with a known primary tumor\n"
        guide += "- **Extra-Axial Lesions:** Meningioma (look for a dural tail) and schwannoma\n"
        guide += "- **Infectious/Inflammatory:** Brain abscess, tuberculoma, or tumefactive demyelination\n\n"
        
        guide += "**Imaging Features:**\n"
        guide += "- **Attenuation:** Compare lesion density with gray/white matter; necrosis or hemorrhage may cause heterogeneous attenuation.\n"
        guide += "- **Margins:** Sharp margins may suggest metastases or meningioma; infiltrative margins are common in high-grade gliomas.\n"
        guide += "- **Enhancement:** Homogeneous enhancement is seen in metastases and low-grade tumors, whereas ring enhancement is suggestive of abscess or necrotic high-grade lesions.\n"
        guide += "- **Calcifications:** Present in oligodendrogliomas and some metastases; use bone windows to assess subtle calcifications.\n\n"
        
        guide += "**Anatomical Considerations:**\n"
        guide += "- **Location:** Intra-axial vs. extra-axial; relation to the ventricular system and midline shift.\n"
        guide += "- **Edema:** Perilesional edema may indicate tumor aggressiveness.\n"
        guide += "- **Vascular Supply:** Evaluate the involvement of deep perforators or cortical branches.\n\n"
        
        guide += "**Additional Tips:**\n"
        guide += "- Consider advanced imaging (MRI with diffusion, perfusion, and spectroscopy) for further characterization.\n"
        guide += "- Correlate with clinical findings (e.g., age, immunocompromise, prior malignancies).\n"
        guide += "- Refer to [Radiopaedia – Brain Tumour](https://radiopaedia.org/articles/brain-tumour) for comprehensive imaging examples.\n\n"
    
    # ===================== CT Brain Hemorrhage =====================
    elif modality == "CT" and organ == "Brain" and lesion_type == "Hemorrhage":
        guide += "### CT Brain Hemorrhage Guide\n\n"
        guide += "**Differential Diagnosis:**\n"
        guide += "- **Intraparenchymal Hemorrhage:** Hypertensive hemorrhage, cerebral amyloid angiopathy\n"
        guide += "- **Subarachnoid Hemorrhage:** Aneurysmal rupture, arteriovenous malformation (AVM)\n"
        guide += "- **Extradural/Subdural Hematoma:** Trauma-related bleeding\n\n"
        
        guide += "**Imaging Features:**\n"
        guide += "- **Density:** Acute blood is hyperdense; subacute/chronic blood evolves to isodense or hypodense over time.\n"
        guide += "- **Location:** Typical locations include the basal ganglia (hypertensive) or convexities (traumatic).\n"
        guide += "- **Associated Findings:** Look for midline shift, intraventricular extension, and skull fractures.\n\n"
        
        guide += "**Anatomical Considerations:**\n"
        guide += "- **Vessel Anatomy:** Consider aneurysms in the circle of Willis for subarachnoid hemorrhage.\n"
        guide += "- **Cortical Involvement:** Assess sulcal effacement and surrounding edema.\n\n"
        
        guide += "**Additional Tips:**\n"
        guide += "- Immediate noncontrast CT is critical in the evaluation of suspected hemorrhage.\n"
        guide += "- For further details, see [Radiopaedia – Intracranial Hemorrhage](https://radiopaedia.org/articles/intracranial-hemorrhage).\n\n"
    
    # ===================== CT Chest Mass =====================
    elif modality == "CT" and organ == "Chest" and lesion_type == "Mass":
        guide += "### CT Chest Mass Guide\n\n"
        guide += "**Differential Diagnosis:**\n"
        guide += "- **Primary Lung Carcinoma:** Adenocarcinoma, squamous cell carcinoma, small cell carcinoma\n"
        guide += "- **Metastases:** Secondary deposits from extrapulmonary primaries\n"
        guide += "- **Benign Lesions:** Hamartoma (often with popcorn calcifications), granuloma\n"
        guide += "- **Lymphoma:** Mediastinal or pulmonary involvement\n\n"
        
        guide += "**Imaging Features:**\n"
        guide += "- **Margins:** Spiculated or irregular margins are concerning for malignancy; smooth borders suggest benignity.\n"
        guide += "- **Calcification:** Patterns (central, diffuse, eccentric) can help differentiate benign from malignant lesions.\n"
        guide += "- **Cavitation:** Cavitary lesions may be seen in squamous cell carcinoma or infectious etiologies.\n"
        guide += "- **Associated Findings:** Look for lymphadenopathy, pleural effusion, and signs of atelectasis.\n\n"
        
        guide += "**Anatomical Considerations:**\n"
        guide += "- **Lobar Distribution:** Identify whether the lesion is central (hilar) or peripheral.\n"
        guide += "- **Vascular Structures:** Consider proximity to major vessels and bronchi.\n\n"
        
        guide += "**Additional Tips:**\n"
        guide += "- Compare with prior imaging to assess growth rate.\n"
        guide += "- Correlate with patient history (smoking, occupational exposures).\n"
        guide += "- For more details, refer to [Radiopaedia – Lung Mass](https://radiopaedia.org/articles/lung-mass).\n\n"
    
    # ===================== MRI Brain Mass =====================
    elif modality == "MRI" and organ == "Brain" and lesion_type == "Mass":
        guide += "### MRI Brain Mass Guide\n\n"
        guide += "**Differential Diagnosis:**\n"
        guide += "- **Primary Tumors:** Gliomas (low-grade vs. high-grade), meningioma, lymphoma\n"
        guide += "- **Metastases:** Multiple lesions in a patient with a known malignancy\n"
        guide += "- **Inflammatory/Granulomatous:** Demyelinating lesions, sarcoidosis\n\n"
        
        guide += "**Imaging Features:**\n"
        guide += "- **Signal Characteristics:** Evaluate T1, T2, FLAIR, and diffusion sequences. Gliomas often have heterogeneous signal intensity with necrotic areas.\n"
        guide += "- **Enhancement Patterns:** Homogeneous enhancement in meningioma; ring-enhancement in high-grade tumors or abscesses.\n"
        guide += "- **Edema:** The extent of vasogenic edema can help differentiate high-grade lesions from low-grade ones.\n\n"
        
        guide += "**Anatomical Considerations:**\n"
        guide += "- **Location:** Determine if the lesion is intra-axial versus extra-axial.\n"
        guide += "- **Relationships:** Assess the involvement of adjacent structures, including the ventricles and cisterns.\n\n"
        
        guide += "**Additional Tips:**\n"
        guide += "- Use advanced MRI techniques (MR spectroscopy, perfusion imaging) to further characterize the lesion.\n"
        guide += "- Consult [Radiopaedia – MRI Brain Tumour](https://radiopaedia.org/articles/mri-brain-tumour) for an in-depth discussion.\n\n"
    
    # ===================== Ultrasound Thyroid Nodule =====================
    elif modality == "Ultrasound" and organ == "Thyroid" and lesion_type == "Mass":
        guide += "### Ultrasound Thyroid Nodule Guide\n\n"
        guide += "**Differential Diagnosis:**\n"
        guide += "- **Benign:** Colloid nodule, thyroid adenoma, cystic degeneration\n"
        guide += "- **Malignant:** Papillary thyroid carcinoma (most common), follicular carcinoma, medullary thyroid carcinoma\n\n"
        
        guide += "**Imaging Features:**\n"
        guide += "- **Echogenicity:** Hypoechoic nodules are more suspicious; heterogeneous echo texture raises concern.\n"
        guide += "- **Margins:** Irregular, microlobulated, or spiculated margins are worrisome; smooth margins suggest benignity.\n"
        guide += "- **Calcifications:** Presence of microcalcifications is highly suggestive of papillary carcinoma.\n"
        guide += "- **Vascularity:** Increased central vascularity on Doppler imaging may be seen in malignant lesions.\n\n"
        
        guide += "**Anatomical Considerations:**\n"
        guide += "- **Location:** Note the nodule’s position relative to the thyroid capsule and its proximity to critical structures (e.g., recurrent laryngeal nerve).\n"
        guide += "- **Size Criteria:** Use standardized systems such as TI-RADS for risk stratification.\n\n"
        
        guide += "**Additional Tips:**\n"
        guide += "- Consider fine-needle aspiration (FNA) biopsy if the nodule meets suspicious criteria.\n"
        guide += "- For more comprehensive guidelines, visit [Radiopaedia – Thyroid Nodule](https://radiopaedia.org/articles/thyroid-nodule).\n\n"
    
    # ===================== MRI Musculoskeletal Cystic Lesion =====================
    elif modality == "MRI" and organ == "Musculoskeletal" and lesion_type == "Cystic Lesion":
        guide += "### MRI Musculoskeletal Cystic Lesion Guide\n\n"
        guide += "**Differential Diagnosis:**\n"
        guide += "- **Benign:** Simple bone cyst, ganglion cyst, synovial cyst\n"
        guide += "- **Aneurysmal Bone Cyst (ABC):** Characterized by fluid–fluid levels\n"
        guide += "- **Infectious:** Abscess formation in osteomyelitis\n\n"
        
        guide += "**Imaging Features:**\n"
        guide += "- **Signal Characteristics:** Typically low signal on T1 and high signal on T2; fluid–fluid levels are characteristic of ABCs.\n"
        guide += "- **Enhancement:** Minimal or peripheral enhancement in simple cysts; irregular enhancement suggests abscess or neoplasm.\n\n"
        
        guide += "**Anatomical Considerations:**\n"
        guide += "- **Location in Bone:** Diaphyseal versus metaphyseal location may alter the differential.\n"
        guide += "- **Cortical Involvement:** Evaluate for cortical thinning or expansion.\n\n"
        
        guide += "**Additional Tips:**\n"
        guide += "- Compare with plain radiographs to assess for any periosteal reaction or matrix mineralization.\n"
        guide += "- See [Radiopaedia – Aneurysmal Bone Cyst](https://radiopaedia.org/articles/aneurysmal-bone-cyst) for detailed imaging examples.\n\n"
    
    # ===================== Nuclear Medicine Bone Scan Lesion =====================
    elif modality == "Nuclear Medicine" and organ == "Bone":
        guide += "### Nuclear Medicine Bone Scan Guide\n\n"
        guide += "**Differential Diagnosis:**\n"
        guide += "- **Metastatic Disease:** Focal areas of increased uptake in patients with known malignancy\n"
        guide += "- **Trauma:** Fractures or stress injuries often show focal tracer accumulation\n"
        guide += "- **Inflammatory/Arthritic Changes:** Diffuse uptake in inflammatory arthropathies\n\n"
        
        guide += "**Imaging Features:**\n"
        guide += "- **Uptake Pattern:** Focal, multifocal, or diffuse increased tracer uptake; correlate with known anatomic structures.\n"
        guide += "- **Comparison:** Always compare with previous studies if available.\n\n"
        
        guide += "**Additional Tips:**\n"
        guide += "- Consider SPECT/CT for improved anatomical localization when necessary.\n"
        guide += "- Refer to [Radiopaedia – Bone Scan](https://radiopaedia.org/articles/bone-scan) for further information.\n\n"
    
    # ===================== Default / General Guidance =====================
    else:
        guide += "### Comprehensive Diagnostic Approach\n\n"
        guide += "**General Recommendations:**\n"
        guide += "- Carefully review the lesion’s morphology, signal/density characteristics, and enhancement patterns.\n"
        guide += "- Always correlate imaging findings with the patient’s clinical history, laboratory values, and prior imaging studies.\n"
        guide += "- Consider using standardized reporting systems such as BI-RADS (breast), LI-RADS (liver), or TI-RADS (thyroid) when applicable.\n"
        guide += "- For ambiguous cases, advanced imaging (MRI, PET-CT) or image-guided biopsy may be warranted.\n\n"
        
        guide += "**Anatomical and Vascular Considerations:**\n"
        guide += "- Familiarize yourself with normal regional anatomy and its variations. For example:\n"
        guide += "  - **Brain:** Variations in circle of Willis configuration.\n"
        guide += "  - **Chest:** Variations in bronchial artery origin (e.g., arising from intercostal arteries).\n"
        guide += "  - **Abdomen/Pelvis:** Hepatic arterial variants (replaced right or left hepatic arteries), renal arterial accessory branches.\n\n"
        
        guide += "**Additional Resources:**\n"
        guide += "For in-depth information on less common scenarios, please refer to Radiopaedia and other peer-reviewed resources:\n"
        guide += "- [Radiopaedia Home](https://radiopaedia.org/)\n"
        guide += "- [PubMed](https://pubmed.ncbi.nlm.nih.gov/)\n\n"
    
    guide += "---\n\n"
    guide += "**Remember:** Always integrate imaging findings with clinical data and consult subspecialty experts as needed. This guide is intended as an educational tool and not a definitive diagnostic resource.\n"
    return guide

# =============================================================================
# Display the Comprehensive Diagnostic Guide Output
# =============================================================================
st.header("Diagnostic Pocket Guide Output")
output_text = get_complete_guide(modality, organ, lesion_type, lesion_size, lesion_margin, lesion_appearance, lesion_enhancement)
st.text_area("Complete Diagnostic Guide", value=output_text, height=800)
