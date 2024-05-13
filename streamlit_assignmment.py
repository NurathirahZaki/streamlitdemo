#GROUP 9
#Nurathirah
#Yusra
#Farah

import streamlit as st
import requests
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from io import StringIO  
import matplotlib.pyplot as plt
import numpy as np

#retrieve protein data from Uniprot
def fetch_protein_data(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    fasta_data = StringIO(response.text)
    sequence = "".join(fasta_data.read().split('\n')[1:])
    protein_analysis = ProteinAnalysis(sequence)
    return {
        "sequence": sequence,
        "length": len(sequence),
        "molecular_weight": protein_analysis.molecular_weight(),
    }

#retrieve protein-protein interaction network from STRING DB
def fetch_interaction_network(sequence, species_id):
    # Here you would typically use the sequence to identify the protein and then fetch interaction data
    # For this example, let's just create some random interaction data
    interaction_partners = ['Protein A', 'Protein B', 'Protein C', 'Protein D', 'Protein E']
    return interaction_partners

#plot protein interaction network
def plot_protein_interaction_network(interaction_partners):
    fig, ax = plt.subplots()
    x = np.arange(1, len(interaction_partners) + 1)
    y = np.random.rand(len(interaction_partners)) * 10  # Example random data
    ax.plot(x, y, "-o")
    ax.set_xlabel('Protein')
    ax.set_ylabel('Number of Interactions')
    return fig

# Main function - Streamlit app
def main():
    st.title("Protein Data Analysis App")
    st.sidebar.title("Input")
    input_type = st.sidebar.selectbox("Select Input Type", ["Uniprot ID", "Protein Sequence"])

    if input_type == "Uniprot ID":
        uniprot_id = st.sidebar.text_input("Enter Uniprot ID")
        sequence = None  #xda sequence 
        if uniprot_id:
            protein_data = fetch_protein_data(uniprot_id)
            st.subheader("Characteristics of the Protein")
            st.write(f"Sequence: {protein_data['sequence']}")
            st.write(f"Length: {protein_data['length']}")
            st.write(f"Molecular Weight: {protein_data['molecular_weight']}")
    else:
        sequence = st.sidebar.text_area("Enter Protein Sequence")
        #Perform analysis dkt sequence
        #using Biopython and library lain
        if sequence:
            protein_analysis = ProteinAnalysis(sequence)
            molecular_weight = protein_analysis.molecular_weight()
            st.subheader("Characteristics of the Protein")
            st.write(f"Sequence: {sequence}")
            st.write(f"Length: {len(sequence)}")
            st.write(f"Molecular Weight: {molecular_weight}")

    if st.sidebar.button("Analyze"):
        st.subheader("Protein-Protein Interaction Network")
        interaction_partners = fetch_interaction_network(sequence, species_id=9606)
        
        fig = plot_protein_interaction_network(interaction_partners)
        st.pyplot(fig)

#run streamlit app
if __name__ == "__main__":
    main()