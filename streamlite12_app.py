import streamlit as st
import pandas as pd

# =============================================================================
# App Title and Header
# =============================================================================
st.title("Radiology Pocket Guide")
st.markdown("<p style='font-size:12px'>Created by Michailidis A. for free use</p>", unsafe_allow_html=True)
st.markdown("**Disclaimer:** This guide is for educational purposes only. It is not a substitute for professional clinical judgment.")

# =============================================================================
# Top-Level Guide Mode Selection
# =============================================================================
guide_mode = st.sidebar.radio("Select Guide Mode:", options=["Lesion Analysis", "Radiology Topics"])

# =============================================================================
# SECTION 1: LESION ANALYSIS
# =============================================================================
if guide_mode == "Lesion Analysis":
    st.sidebar.header("Lesion Analysis Parameters")
    # Imaging modality, organ, lesion type
    modality = st.sidebar.selectbox(
        "Select Imaging Modality:",
        ["X-Ray", "CT", "MRI", "Ultrasound", "Nuclear Medicine"]
    )
    # Organ/System options based on modality
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
    
    lesion_type = st.sidebar.selectbox(
        "Select Lesion Type:",
        ["Mass", "Cystic Lesion", "Calcification", "Hemorrhage", "Inflammatory", "Vascular Malformation", "Degenerative"]
    )
    
    # Expanded lesion characteristics – additional fields for detailed analysis
    st.sidebar.header("Lesion Characteristics")
    lesion_size = st.sidebar.text_input("Lesion Size (cm):", "e.g., 2.5")
    lesion_margin = st.sidebar.selectbox("Lesion Margin:", 
                                         ["Well-circumscribed", "Ill-defined", "Spiculated", "Infiltrative", "Lobulated"])
    lesion_shape = st.sidebar.selectbox("Lesion Shape:", 
                                        ["Round/Oval", "Irregular", "Angular", "Multilobulated"])
    lesion_internal = st.sidebar.selectbox("Internal Architecture:",
                                           ["Homogeneous", "Heterogeneous", "Necrotic", "Cystic areas", "Solid"])
    lesion_calcification = st.sidebar.selectbox("Calcification Pattern:",
                                                ["None", "Central", "Diffuse", "Punctate", "Stippled", "Popcorn"])
    lesion_vascularity = st.sidebar.selectbox("Vascularity:",
                                               ["None", "Low", "Moderate", "High", "Flow voids on MRI"])
    lesion_signal = st.sidebar.selectbox("Signal / Density Characteristics:",
                                          ["Hyperdense/Hyperattenuating", "Hypodense/Hypoattenuating", "Isodense/Isoattenuating", 
                                           "T1 Hyperintense", "T1 Hypointense", "T2 Hyperintense", "T2 Hypointense", "Mixed"])
    lesion_enhancement = st.sidebar.selectbox(
        "Enhancement Pattern (if applicable):", 
        ["None", "Homogeneous", "Heterogeneous", "Ring-enhancing", "Peripheral enhancement", "Progressive", "Washout", "Centripetal"]
    )
    additional_features = st.sidebar.text_area("Additional Features (optional):", "e.g., diffusion restriction, hemorrhagic components, edema, etc.")

    # =============================================================================
    # Function: Comprehensive Lesion Analysis Guide
    # =============================================================================
    def get_complete_lesion_guide(modality, organ, lesion_type, lesion_size, lesion_margin, lesion_shape,
                                  lesion_internal, lesion_calcification, lesion_vascularity, lesion_signal,
                                  lesion_enhancement, additional_features):
        guide = f"## Lesion Analysis Guide\n\n"
        guide += f"**Modality:** {modality}\n\n"
        guide += f"**Organ/System:** {organ}\n\n"
        guide += f"**Lesion Type:** {lesion_type}\n\n"
        guide += "**Provided Characteristics:**\n"
        guide += f"- **Size:** {lesion_size} cm\n"
        guide += f"- **Margin:** {lesion_margin}\n"
        guide += f"- **Shape:** {lesion_shape}\n"
        guide += f"- **Internal Architecture:** {lesion_internal}\n"
        guide += f"- **Calcification:** {lesion_calcification}\n"
        guide += f"- **Vascularity:** {lesion_vascularity}\n"
        guide += f"- **Signal/Density:** {lesion_signal}\n"
        guide += f"- **Enhancement:** {lesion_enhancement}\n"
        guide += f"- **Additional Features:** {additional_features}\n\n"
        guide += "---\n\n"
        
        # (For brevity, we add only a few exemplary branches here. In a full app, you would include many combinations.)
        if modality == "CT" and organ == "Brain" and lesion_type == "Mass":
            guide += "### CT Brain Mass\n\n"
            guide += "**Differential Diagnosis:**\n"
            guide += "- Glioma (including glioblastoma multiforme), astrocytoma, oligodendroglioma\n"
            guide += "- Metastasis (consider multiple lesions if known primary)\n"
            guide += "- Meningioma (if extra-axial with dural tail)\n"
            guide += "- Brain abscess (if ring-enhancing with surrounding edema)\n\n"
            
            guide += "**Key Imaging Features:**\n"
            guide += "- Compare lesion density with normal gray and white matter.\n"
            guide += "- Infiltrative margins and heterogeneous signal suggest high-grade gliomas.\n"
            guide += "- Homogeneous enhancement is often seen in metastases; ring-enhancement may indicate necrosis or abscess.\n"
            guide += "- Check for calcifications (common in oligodendrogliomas) using bone windows.\n\n"
            
            guide += "**Anatomical Considerations:**\n"
            guide += "- Evaluate the lesion’s location relative to the ventricles and midline structures.\n"
            guide += "- Assess perilesional edema and mass effect.\n"
            guide += "- Review vascular supply (e.g., deep perforators).\n\n"
            guide += "For more details, please refer to [Radiopaedia – Brain Tumour](https://radiopaedia.org/articles/brain-tumour).\n\n"
        
        elif modality == "Ultrasound" and organ == "Thyroid" and lesion_type == "Mass":
            guide += "### Ultrasound Thyroid Nodule\n\n"
            guide += "**Differential Diagnosis:**\n"
            guide += "- Benign: Colloid nodule, thyroid adenoma, cystic degeneration\n"
            guide += "- Malignant: Papillary thyroid carcinoma (most common), follicular carcinoma, medullary carcinoma\n\n"
            
            guide += "**Key Imaging Features:**\n"
            guide += "- Hypoechoic nodules with irregular margins are more suspicious.\n"
            guide += "- Microcalcifications and increased intranodular vascularity raise concern for malignancy.\n"
            guide += "- TI-RADS criteria may be applied for risk stratification.\n\n"
            
            guide += "**Anatomical Considerations:**\n"
            guide += "- Note the nodule’s relationship to the thyroid capsule and adjacent structures such as the recurrent laryngeal nerve.\n\n"
            guide += "For further guidance, visit [Radiopaedia – Thyroid Nodule](https://radiopaedia.org/articles/thyroid-nodule).\n\n"
        
        else:
            guide += "### General Lesion Analysis\n\n"
            guide += "Review the lesion's morphology, internal architecture, enhancement, and additional imaging features.\n"
            guide += "Always correlate with clinical history and prior imaging studies.\n"
            guide += "If uncertain, consider additional imaging modalities (e.g., MRI, PET-CT) or image-guided biopsy.\n"
            guide += "Refer to [Radiopaedia](https://radiopaedia.org/) for extensive case examples and discussions.\n\n"
        
        guide += "---\n"
        guide += "**Remember:** This analysis is intended as an educational aid. Always integrate imaging with clinical findings and expert consultation.\n"
        return guide

    # Display the lesion analysis guide output
    lesion_output = get_complete_lesion_guide(modality, organ, lesion_type, lesion_size, lesion_margin, 
                                              lesion_shape, lesion_internal, lesion_calcification,
                                              lesion_vascularity, lesion_signal, lesion_enhancement,
                                              additional_features)
    st.header("Lesion Analysis Output")
    st.text_area("Detailed Lesion Analysis", value=lesion_output, height=600)
    
    # Optionally display a relevant image (if available)
    def get_lesion_image(modality, organ, lesion_type):
        if modality == "CT" and organ == "Brain" and lesion_type == "Mass":
            return ("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/CT_scan_of_brain_tumour.jpg/640px-CT_scan_of_brain_tumour.jpg", "CT Brain Mass Example")
        elif modality == "Ultrasound" and organ == "Thyroid" and lesion_type == "Mass":
            return ("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Thyroid_ultrasound.jpg/640px-Thyroid_ultrasound.jpg", "Ultrasound Thyroid Nodule Example")
        # ... add additional image mappings as needed ...
        return (None, None)
    
    img_url, img_caption = get_lesion_image(modality, organ, lesion_type)
    if img_url:
        st.image(img_url, caption=img_caption, use_container_width=True)

# =============================================================================
# SECTION 2: RADIOLOGY TOPICS
# =============================================================================
elif guide_mode == "Radiology Topics":
    st.sidebar.header("Radiology Topics Parameters")
    topic_mode = st.sidebar.radio("Select Topic Mode:", options=["By Section", "By System", "Cases"])
    
    if topic_mode == "By Section":
        section_options = [
            "Anatomy", "Approach", "Artificial Intelligence", "Classifications", "Gamuts",
            "Imaging Technology", "Interventional Radiology", "Mnemonics", "Pathology",
            "Radiography", "Signs", "Staging", "Syndromes"
        ]
        section = st.sidebar.selectbox("Select Section:", section_options)
    elif topic_mode == "By System":
        system_options = [
            "Breast", "Cardiac", "Central Nervous System", "Chest", "Forensic", "Gastrointestinal",
            "Gynaecology", "Haematology", "Head & Neck", "Hepatobiliary", "Interventional", 
            "Musculoskeletal", "Obstetrics", "Oncology", "Paediatrics", "Spine", "Trauma", 
            "Urogenital", "Vascular"
        ]
        system = st.sidebar.selectbox("Select System:", system_options)
    else:  # Cases
        case_options = [
            "Breast", "Cardiac", "Central Nervous System", "Chest", "Forensic", "Gastrointestinal",
            "Gynaecology", "Haematology", "Head & Neck", "Hepatobiliary", "Interventional", 
            "Musculoskeletal", "Obstetrics", "Oncology", "Paediatrics", "Spine", "Trauma", 
            "Urogenital", "Vascular"
        ]
        case = st.sidebar.selectbox("Select Case Type:", case_options)
    
    # =============================================================================
    # Function: Radiology Topic Guide Generator
    # =============================================================================
    def get_topic_guide(topic_mode, selection):
        guide = f"## Radiology Topics Guide\n\n"
        if topic_mode == "By Section":
            guide += f"### Section: {selection}\n\n"
            if selection == "Anatomy":
                guide += "**Anatomy in Radiology:**\n"
                guide += "- Detailed anatomical descriptions including normal variants and vascular supply.\n"
                guide += "- Example: Anatomy of the Circle of Willis, bronchial arterial variations, hepatic arterial variants, etc.\n"
                guide += "- [Radiopaedia – Anatomy](https://radiopaedia.org/articles/anatomy)\n\n"
            elif selection == "Approach":
                guide += "**Approaches in Radiology:**\n"
                guide += "- Discussion of imaging protocols, patient positioning, and interventional approaches.\n"
                guide += "- Examples include CT-guided biopsies, ultrasound-guided drainage, and fluoroscopy-guided procedures.\n\n"
            elif selection == "Artificial Intelligence":
                guide += "**Artificial Intelligence in Radiology:**\n"
                guide += "- AI applications for image analysis, segmentation, and computer-aided diagnosis.\n"
                guide += "- Future trends and current research in deep learning for radiology.\n\n"
            elif selection == "Classifications":
                guide += "**Radiologic Classifications:**\n"
                guide += "- Standardized systems (e.g., BI-RADS, LI-RADS, TI-RADS) used to categorize lesions.\n\n"
            elif selection == "Gamuts":
                guide += "**Radiology Gamuts:**\n"
                guide += "- Comprehensive lists of disease processes for a given finding (e.g., differential diagnosis of a pulmonary nodule).\n\n"
            elif selection == "Imaging Technology":
                guide += "**Imaging Technology:**\n"
                guide += "- Advances in imaging modalities, such as high-resolution CT, functional MRI, and digital radiography.\n\n"
            elif selection == "Interventional Radiology":
                guide += "**Interventional Radiology:**\n"
                guide += "- Techniques, devices, and protocols for image-guided interventions.\n"
                guide += "- Examples include embolization, ablation, and vascular stenting.\n\n"
            elif selection == "Mnemonics":
                guide += "**Radiology Mnemonics:**\n"
                guide += "- Memory aids to recall imaging findings and differential diagnoses.\n"
                guide += "- Example: " + '"VINDICATE" (Vascular, Infectious, Neoplastic, Degenerative, Iatrogenic, Congenital, Autoimmune, Traumatic, Endocrine).\n\n'
            elif selection == "Pathology":
                guide += "**Pathology:**\n"
                guide += "- Radiologic-pathologic correlation for various disease entities.\n\n"
            elif selection == "Radiography":
                guide += "**Radiography:**\n"
                guide += "- Principles and techniques of plain film imaging.\n\n"
            elif selection == "Signs":
                guide += "**Radiologic Signs:**\n"
                guide += "- Named signs (e.g., “thumbprint sign”, “air crescent sign”) and their diagnostic implications.\n\n"
            elif selection == "Staging":
                guide += "**Staging in Radiology:**\n"
                guide += "- Imaging criteria for cancer staging and response assessment.\n\n"
            elif selection == "Syndromes":
                guide += "**Radiologic Syndromes:**\n"
                guide += "- Descriptions of syndromes as seen on imaging (e.g., “Pancoast syndrome”, “Stafne bone cavity”).\n\n"
            else:
                guide += "Detailed information on this section is not available yet.\n\n"
        elif topic_mode == "By System":
            guide += f"### System: {selection}\n\n"
            if selection == "Breast":
                guide += "**Breast Imaging:**\n"
                guide += "- Techniques: Mammography, ultrasound, MRI.\n"
                guide += "- Common findings: masses, calcifications, architectural distortions.\n"
                guide += "- Standardized reporting: BI-RADS.\n\n"
            elif selection == "Cardiac":
                guide += "**Cardiac Imaging:**\n"
                guide += "- Modalities: Cardiac CT, MRI, and nuclear imaging.\n"
                guide += "- Topics: Coronary artery disease, cardiomyopathies, congenital heart disease.\n\n"
            elif selection == "Central Nervous System":
                guide += "**CNS Imaging:**\n"
                guide += "- Modalities: CT, MRI, PET.\n"
                guide += "- Topics: Brain tumors, stroke, demyelinating disease.\n\n"
            elif selection == "Chest":
                guide += "**Chest Imaging:**\n"
                guide += "- Modalities: Chest X-ray, CT, MRI, PET-CT.\n"
                guide += "- Topics: Lung nodules, interstitial lung disease, mediastinal masses.\n\n"
            elif selection == "Forensic":
                guide += "**Forensic Radiology:**\n"
                guide += "- Applications: Post-mortem imaging, trauma assessment, identification.\n\n"
            elif selection == "Gastrointestinal":
                guide += "**Gastrointestinal Imaging:**\n"
                guide += "- Modalities: CT, MRI, ultrasound.\n"
                guide += "- Topics: Abdominal masses, inflammatory bowel disease, pancreatitis.\n\n"
            elif selection == "Gynaecology":
                guide += "**Gynaecologic Imaging:**\n"
                guide += "- Modalities: Ultrasound, MRI, CT.\n"
                guide += "- Topics: Ovarian masses, uterine fibroids, endometrial pathology.\n\n"
            elif selection == "Haematology":
                guide += "**Haematologic Imaging:**\n"
                guide += "- Topics: Lymphadenopathy, splenomegaly, marrow disorders.\n\n"
            elif selection == "Head & Neck":
                guide += "**Head & Neck Imaging:**\n"
                guide += "- Modalities: CT, MRI, ultrasound.\n"
                guide += "- Topics: Thyroid nodules, salivary gland tumors, lymph node evaluation.\n\n"
            elif selection == "Hepatobiliary":
                guide += "**Hepatobiliary Imaging:**\n"
                guide += "- Modalities: Ultrasound, CT, MRI, nuclear medicine.\n"
                guide += "- Topics: Liver lesions, biliary obstruction, cirrhosis.\n\n"
            elif selection == "Interventional":
                guide += "**Interventional Radiology:**\n"
                guide += "- Topics: Embolization, ablation, vascular interventions.\n\n"
            elif selection == "Musculoskeletal":
                guide += "**Musculoskeletal Imaging:**\n"
                guide += "- Modalities: X-ray, CT, MRI, ultrasound.\n"
                guide += "- Topics: Fractures, tumors, inflammatory arthropathies.\n\n"
            elif selection == "Obstetrics":
                guide += "**Obstetric Imaging:**\n"
                guide += "- Modalities: Ultrasound, MRI.\n"
                guide += "- Topics: Fetal anatomy, placental disorders, congenital anomalies.\n\n"
            elif selection == "Oncology":
                guide += "**Oncologic Imaging:**\n"
                guide += "- Modalities: CT, MRI, PET-CT.\n"
                guide += "- Topics: Tumor staging, treatment response, metastases.\n\n"
            elif selection == "Paediatrics":
                guide += "**Paediatric Imaging:**\n"
                guide += "- Special considerations in radiation dose and imaging protocols.\n"
                guide += "- Topics: Congenital anomalies, pediatric tumors, trauma.\n\n"
            elif selection == "Spine":
                guide += "**Spine Imaging:**\n"
                guide += "- Modalities: X-ray, CT, MRI.\n"
                guide += "- Topics: Disc herniations, tumors, degenerative changes.\n\n"
            elif selection == "Trauma":
                guide += "**Trauma Imaging:**\n"
                guide += "- Modalities: X-ray, CT, MRI.\n"
                guide += "- Topics: Fractures, hemorrhage, organ lacerations.\n\n"
            elif selection == "Urogenital":
                guide += "**Urogenital Imaging:**\n"
                guide += "- Modalities: Ultrasound, CT, MRI.\n"
                guide += "- Topics: Renal masses, bladder pathology, prostate evaluation.\n\n"
            elif selection == "Vascular":
                guide += "**Vascular Imaging:**\n"
                guide += "- Modalities: CT angiography, MR angiography, ultrasound.\n"
                guide += "- Topics: Aneurysms, dissections, occlusive disease.\n\n"
            else:
                guide += "Detailed system-specific guidance is under development.\n\n"
        elif topic_mode == "Cases":
            guide += f"### Radiology Cases: {selection}\n\n"
            guide += "A collection of interesting and educational cases in this system:\n"
            guide += "- Review rare and common pathologies\n"
            guide += "- See examples of atypical presentations\n"
            guide += "- Detailed discussion of imaging findings and clinical correlation\n\n"
            guide += "For more cases, please visit [Radiopaedia Cases](https://radiopaedia.org/cases).\n\n"
        else:
            guide += "Topic not recognized. Please select a valid option.\n\n"
        
        guide += "---\n"
        guide += "**Note:** This section is an evolving repository of radiology knowledge. For the most up-to-date information, always consult primary resources and Radiopaedia directly.\n"
        return guide
    
    # Display the Radiology Topics guide output
    if topic_mode == "By Section":
        topic_output = get_topic_guide(topic_mode, section)
    elif topic_mode == "By System":
        topic_output = get_topic_guide(topic_mode, system)
    else:
        topic_output = get_topic_guide(topic_mode, case)
    
    st.header("Radiology Topics Output")
    st.text_area("Detailed Radiology Guide", value=topic_output, height=600)
    
    # Optionally display a generic image for topics (if desired)
    def get_topic_image(topic_mode, selection):
        # Here you can define image URLs for various topics
        if topic_mode == "By Section" and selection == "Anatomy":
            return ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Gray1124.png/640px-Gray1124.png", "Human Anatomy Example")
        elif topic_mode == "By System" and selection == "Breast":
            return ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Mammogram_2.jpg/640px-Mammogram_2.jpg", "Breast Imaging Example")
        # Add more mappings as needed...
        return (None, None)
    
    topic_img_url, topic_img_caption = get_topic_image(topic_mode, section if topic_mode=="By Section" else (system if topic_mode=="By System" else case))
    if topic_img_url:
        st.image(topic_img_url, caption=topic_img_caption, use_container_width=True)

# =============================================================================
# End of App
# =============================================================================
st.markdown("For further study, please visit [Radiopaedia](https://radiopaedia.org/) and other peer-reviewed resources.")
